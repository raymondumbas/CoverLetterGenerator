from datetime import datetime

print("Cover Letter Generator")
print("")

# Get Position Title
print("Enter position title:")
positionTitle = input()
print("")

# Get Company Name
print("Enter company name:")
companyName = input()


# Get Current Date
current_date = datetime.now()
formatted_date = current_date.strftime("%B %d, %Y")

finalOutput = f"""Raymond Umbas
(760) 717-6641
raymond.umbas@gmail.com

{formatted_date}

Dear Hiring Manager,

I am writing to express my interest in the {positionTitle} position at {companyName}. As a dedicated and motivated computer science graduate, I am eager to contribute to your innovative company while gaining valuable hands-on experience.

My passion for technology began early, driving me to pursue a degree in computer science. I have cultivated a skill set in technical languages such as Javascript, CSS, HTML, C++ and Python through coursework and personal projects. These experiences have equipped me with proficiency in software development and algorithm design.

What distinguishes me as a candidate is my ability to apply technical skills with a perspective focused on user experience. With a background in the service industry, I have honed my ability to anticipate and meet customer needs effectively. I am committed to creating software that not only meets technical requirements but also delivers a seamless and positive user experience.

I am particularly drawn to {companyName}'s commitment to. Your commitment …. I am eager to apply my skills and knowledge to contribute to {companyName} mission.

In conclusion, I am enthusiastic about the opportunity to join {companyName} as a {positionTitle}. With my technical expertise, passion for technology, and strong work ethic, I believe I would be a valuable addition to your team. I look forward to the possibility of discussing how my dedication and eagerness to learn can contribute to your organization.

Thank you for considering my application.

Sincerely,

Raymond Umbas
"""

print(finalOutput)

