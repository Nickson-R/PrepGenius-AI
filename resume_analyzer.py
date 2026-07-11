import PyPDF2


def extract_text(pdf_path):

    text = ""

    with open(pdf_path, "rb") as file:

        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text

    return text.lower()


def extract_skills(text):

    possible_skills = [

        "python",
        "sql",
        "java",
        "api",
        "git",
        "cloud",
        "aws",
        "azure",
        "gcp",
        "javascript",
        "react",
        "excel",
        "data analysis",
        "communication",
        "oop",
        "networking",
        "n8n",
        "arduino",
        "esp32",
        "tensorflow",
        "opencv"
    ]

    found_skills = []

    for skill in possible_skills:

        if skill in text:
            found_skills.append(skill)

    return found_skills