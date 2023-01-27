from docx import Document
from docx.shared import Pt

# prompt the user for the 3 pieces of information we need, and put them into the 4 bullet points required in a .txt file
# 1 company name (Capitalized)
# 2 job location (Capitalized, may be a region, city, or state)
# 3 position name (lowercase)
# 4 company name (again Capitalized)

print("Enter company name (required)")
company_name = input()

print("\nEnter job location (Capitalized, either as a region, city, or state)")
job_location = input()

print("\nEnter position name")
position_name = input()

print("\nParams provided:")
print("Company Name: ", company_name)
print("Location: ", job_location)
print("Position Name: ", position_name)

OPENING_STATEMENT = "To the Hiring Manager at ", company_name, ","
CLOSING_STATEMENT = "I look forward to the opportunity to show you how I can benefit the ", company_name, " team."
INTRODUCTORY_STATEMENT = "I am an Utrecht-based Salesforce Developer looking for the next big opportunity to grow my technical skills and contribute meaningfully. After reviewing the description, I believe that I provide the specialized skills that you are seeking for your ", position_name, " position, and I would like to share more about the value I can contribute to ", company_name, "."

document = Document('JdeGuiseCL-General.docx')
for paragraph in document.paragraphs:
	if 'COMPANY_NAME_1' in paragraph.text:
		paragraph.text = OPENING_STATEMENT
	elif 'COMPANY_NAME_2' in paragraph.text and 'POSITION_NAME' in paragraph.text:
		paragraph.text = INTRODUCTORY_STATEMENT
	elif 'COMPANY_NAME_3' in paragraph.text:
		paragraph.text = CLOSING_STATEMENT

save_name = "JdeGuiseCL-%s.docx" % (company_name.replace(" ", ""))
document.save(save_name)

print("Done! Document saved as", save_name)