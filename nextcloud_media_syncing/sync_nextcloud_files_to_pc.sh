#!/bin/bash
source .env

process_file () {
	is_success=true
	error_msg=""

    string=$1
	phone_path=$2
    separator=$3

    tmp=${string//"$separator"/$'\2'}
    IFS=$'\2' read -a arr <<< "$tmp"

	phone_path+="${arr[0]}"

	cd /home/pi/scripts/nextcloud_media_syncing 
	source /home/pi/scripts/nextcloud_media_syncing/.venv/bin/activate

	# TODO: parse out new path on windows pc hard drive for slack msg
	# TODO: embed the new image into the slack message
	cmdOutput=$(sshpass -p $WINDOWS_PASS scp -r /var/nextcloud/data/gans/files/InstantUpload/Camera/* johnr@192.168.1.11:C:/PhotoPrism/originals/Camera 2>&1)

	if [ -z "${cmdOutput}" ]; 
	then
		is_success=true
	else
		is_success=false
		error_msg=$cmdOutput
	fi

	python3 ./slack_photo_notification_manager.py $is_success $phone_path $error_msg
}

inotifywait -m -r /var/nextcloud/data/gans/files/InstantUpload -e create |
	while read path action file; do
		SEPARATOR='.ocTransferId'
		EXTENSION='jpg'

		if [[ "$file" =~ .*"$EXTENSION".* ]]; then
			sleep 5
			process_file $file $path $SEPARATOR
		fi
	done