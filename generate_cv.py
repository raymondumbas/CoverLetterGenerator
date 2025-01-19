from datetime import datetime
from fpdf import FPDF
import google.generativeai as genai

with open("api_key.txt", "r") as file:
    api_key = file.read().strip()  # Strip removes any extra whitespace or newlines

print("Cover Letter Generator")
print("")

# Get Position Title
print("Enter position title:")
positionTitle = input()
print("")

# Get Company Name
print("Enter company name:")
companyName = input()
print("")


# Get Current Date
current_date = datetime.now()
formatted_date = current_date.strftime("%B %d, %Y")

# Get Custom Paragraph
print("What interests you about this specific company?")
initialParagraph = input()

initialPrompt = f"""This is a paragraph from a cover letter I am writing for a job application to {companyName} as a {positionTitle}.: 
I am particularly drawn to {companyName}’s commitment to {initialParagraph}.
I am eager to apply my skills and knowledge to contribute to {companyName}'s mission. 

Refine this to sound better while still keeping the same ideas and make the total length between 360 to 380 characters. Feel free to elaborate
upon what's given to make is sound professional and interesting, even if that means adding more than is given to make sure the the paragraph is not too short
and meets the 360 to 380 character count. The paragraph should be ready for me to paste into my cover letter, i.e. there should not be additional parts i needt to add or edit"""


genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(initialPrompt)
edittedParagraph = response.text.strip()


while True:
    print("Here is the current paragraph: \n")
    print(edittedParagraph) 
    print("")
    print("""
          Would you like to make any changes?
          1: Manual Change
          2: Enter a prompt
          3: Nope, looks good to me
          """)
    response = input()

    match response:
        case 1:
            print("Enter what you want to change the paragraph to.")
            edittedParagraph = input()
        case 2:
            print("Enter the prompt you want to run with the current paragraph.")
        case 3:
            print("Continuing to final output.")
            break;
        case _:
            print("Please select either 1, 2, or 3. ")


# Final Formatted Output
final_cv = f"""Raymond Umbas
(760) 717-6641
raymond.umbas@gmail.com

{formatted_date}

Dear Hiring Manager,

I am writing to express my interest in the {positionTitle} position at {companyName}. As a dedicated and motivated computer science graduate, I am eager to contribute to your innovative company while gaining valuable hands-on experience.

My passion for technology began early, driving me to pursue a degree in computer science. I have cultivated a skill set in technical languages such as Javascript, CSS, HTML, C++ and Python through coursework and personal projects. These experiences have equipped me with proficiency in software development and algorithm design.

What distinguishes me as a candidate is my ability to apply technical skills with a perspective focused on user experience. With a background in the service industry, I have honed my ability to anticipate and meet customer needs effectively. I am committed to creating software that not only meets technical requirements but also delivers a seamless and positive user experience.

{edittedParagraph}

In conclusion, I am enthusiastic about the opportunity to join {companyName} as a {positionTitle}. With my technical expertise, passion for technology, and strong work ethic, I believe I would be a valuable addition to your team. I look forward to the possibility of discussing how my dedication and eagerness to learn can contribute to your organization.

Thank you for considering my application.

Sincerely,

Raymond Umbas
"""


# Initialize the PDF object
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Write the content (handles multiline text)
pdf.multi_cell(0, 7, final_cv)

# Save the PDF
output_path = f"./outputs/RaymondUmbasCV{companyName}.pdf"
pdf.output(output_path)

print(f"PDF saved as {output_path}")


