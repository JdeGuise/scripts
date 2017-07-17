from docx import Document
from docx.shared import Pt

# prompt the user for the 3 pieces of information we need, and put them into the 4 bullet points required in a .txt file
# 1 company name (Capitalized)
# 2 job location (Capitalized, may be a region, city, or state)
# 3 position name (lowercase)
# 4 company name (again Capitalized)

print "Enter company name (required)"

company_name = raw_input()

print "Enter job location (Capitalized, either as a region, city, or state)"

job_location = raw_input()

print "Enter position name"

position_name = raw_input().lower()

print company_name
print job_location
print position_name


# lazy... boooooo
AAAA_flag = False
AAAA1 = "To the Hiring Manager at ", company_name, ","
AAAA2 = "I look forward to the opportunity to show you how I can benefit the ", company_name, " team."
BBBB_CCCC = "I am a Michigan-based computer science graduate interested in relocation to ", job_location, ".  I believe that I provide the specialized skills that you are seeking for the ", position_name, " position, and I believe that I would make a valuable addition to the company."

#
# Store these pieces of information as 4 lines with the first line as the name of the file
# Use this file to feed into update_cl.py as a with('open' -r): call
# load into variables
# iterate over our 4 regexes and replace them

document = Document('JdeGuiseCL-General.docx')

for paragraph in document.paragraphs:
	if 'AAAA' in paragraph.text:
		if AAAA_flag is True:
			paragraph.text = AAAA2
		else:
			paragraph.text = AAAA1
			AAAA_flag = True
	if 'BBBB' in paragraph.text and 'CCCC' in paragraph.text:
		paragraph.text = BBBB_CCCC

for paragraph in document.paragraphs:
	print paragraph.text

save_name = "JdeGuiseCL-%s.docx" % (company_name.replace(" ", ""))
document.save(save_name)
