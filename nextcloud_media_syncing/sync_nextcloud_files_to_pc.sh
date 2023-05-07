#!/bin/bash
source .env

main() {
	initialize_inotify
}

send_slack_message() {
	python3 ./slack_photo_notification_manager.py $1 $2 $3
}

sync_media_from_nextcloud_to_storage() {
	echo $(sshpass -p $WINDOWS_PASS scp -r /var/nextcloud/data/gans/files/InstantUpload/Camera/* johnr@192.168.1.11:C:/PhotoPrism/originals/Camera 2>&1)
}

initialize_inotify() {
	inotifywait -m -r /var/nextcloud/data/gans/files/InstantUpload -e create |
		while read path action file; do
			SEPARATOR='.ocTransferId'
			EXTENSION_JPG='jpg'
			EXTENSION_MP4='mp4'

			if [[ "$file" =~ .*"$EXTENSION_JPG".* || "$file" =~ .*"$EXTENSION_MP4".* ]]; then
				process_qualifying_file $file $path $SEPARATOR
			fi
		done
}

strip_media_name_from_part_file() {
    tmp=${1//"$2"/$'\2'}
    IFS=$'\2' read -a arr <<< "$tmp"

	echo ${arr[0]}
}

activate_python_venv() {
	cd /home/pi/scripts/nextcloud_media_syncing && source /home/pi/scripts/nextcloud_media_syncing/.venv/bin/activate
}

process_qualifying_file () {
	activate_python_venv

	nextcloud_media_path=($2$(strip_media_name_from_part_file $1 $3))

	error_msg=""
	is_success=true
	syncCmdOutput=$(sync_media_from_nextcloud_to_storage)
	if [ -z "${syncCmdOutput}" ]; 
	then
		is_success=true
	else
		is_success=false
		error_msg=$syncCmdOutput
	fi

	send_slack_message $is_success $nextcloud_media_path $error_msg
}

main "$@"; exit