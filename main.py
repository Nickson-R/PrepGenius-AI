from companies import companies
from resume_analyzer import extract_text, extract_skills


print("\n🏢 Available Companies:\n")

for company_name in companies:
    print("👉", company_name.upper())


company = input(
    "\nEnter company name: "
).lower().strip()


if company in companies:

    data = companies[company]

    print(
        "\n🚀 ===== Placement Preparation Report ===== 🚀\n"
    )

    print(f"🏢 Company : {company.upper()}")
    print(f"💰 CTC : {data['ctc']}")

    print("\n📚 Topics To Prepare:\n")

    for topic in data["topics"]:
        print("✅", topic)

    print("\n🎯 Important Interview Questions:\n")

    for question in data["questions"]:
        print("👉", question)

    print("\n🛠️ Skills Needed:\n")

    for skill in data["skills_needed"]:
        print("⭐", skill)

    print("\n🚀 Suggested Projects:\n")

    for project in data["projects_to_build"]:
        print("📌", project)

    choice = input(
        "\n📄 Upload Resume? (yes/no): "
    ).lower()

    if choice == "yes":

        pdf = input(
            "Enter PDF name: "
        )

        try:

            text = extract_text(pdf)

            user_skills = extract_skills(text)

            print(
                "\n📄 Skills Found In Resume:\n"
            )

            if len(user_skills) == 0:

                print(
                    "❌ No skills detected."
                )

            else:

                for skill in user_skills:
                    print("✅", skill)

        except FileNotFoundError:

            print(
                "❌ PDF file not found."
            )

            user_skills = []

    else:

        my_skills = input(
            "\n📝 Enter your skills (comma separated): "
        ).lower()

        user_skills = []

        for skill in my_skills.split(","):
            user_skills.append(
                skill.strip()
            )

    missing_skills = []

    for skill in data["skills_needed"]:

        if skill.lower() not in user_skills:
            missing_skills.append(skill)

    matched_skills = (
        len(data["skills_needed"])
        - len(missing_skills)
    )

    score = (
        matched_skills
        / len(data["skills_needed"])
    ) * 100

    print("\n📊 Skill Gap Analysis:\n")

    print(
        f"🎯 Placement Readiness Score : {score:.0f}%"
    )

    if score >= 80:

        status = "Highly Ready"
        print("🟢 Status : Highly Ready")

    elif score >= 50:

        status = "Moderately Ready"
        print("🟡 Status : Moderately Ready")

    else:

        status = "Needs Preparation"
        print("🔴 Status : Needs Preparation")

    print("\n✨ Features Used:\n")

    print("✅ Resume Parsing")
    print("✅ Skill Extraction")
    print("✅ Skill Gap Analysis")
    print("✅ Placement Readiness Score")
    print("✅ Personalized Roadmap")
    print("✅ Report Generation")

    print("\n💡 Company Recommendations:\n")

    if company == "accenture":

        print("👉 Focus on Cloud Fundamentals.")
        print("👉 Practice SQL queries.")
        print("👉 Build API projects.")

    elif company == "hcltech":

        print("👉 Learn PL/SQL thoroughly.")
        print("👉 Study AWS/Azure basics.")
        print("👉 Build cloud projects.")

    elif company == "surveysparrow":

        print("👉 Improve JavaScript skills.")
        print("👉 Learn Git and REST APIs.")
        print("👉 Build dashboard projects.")

    elif company == "zoho":

        print("👉 Practice DSA daily.")
        print("👉 Solve coding problems.")
        print("👉 Build full-stack projects.")

    elif company == "tcs":

        print("👉 Focus on Aptitude.")
        print("👉 Practice HR questions.")
        print("👉 Improve Python fundamentals.")

    else:

        print(
            "👉 Continue improving missing skills."
        )

    if len(missing_skills) == 0:

        print(
            "\n🎉 You already have all required skills!"
        )

    else:

        print("\n❌ Missing Skills:\n")

        for skill in missing_skills:
            print("❌", skill)

    print(
        "\n🚀 Recommended Next Steps:\n"
    )

    if len(missing_skills) == 0:

        print(
            "✅ Focus on mock interviews and projects."
        )

    else:

        for skill in missing_skills:

            print(
                f"👉 Learn {skill}"
            )

    print(
        "\n📅 Personalized Roadmap:\n"
    )

    if len(missing_skills) == 0:

        print(
            "🎉 Practice interview questions."
        )

    else:

        for i, skill in enumerate(
            missing_skills,
            start=1
        ):

            print(
                f"🚀 Week {i} → Learn {skill}"
            )

    with open(
        "placement_report.txt",
        "a",
        encoding="utf-8"
    ) as file:

        file.write(
            "\n🚀 ===== Placement Preparation Report ===== 🚀\n"
        )

        file.write(
            f"Company : {company.upper()}\n"
        )

        file.write(
            f"CTC : {data['ctc']}\n"
        )

        file.write(
            f"\nPlacement Score : {score:.0f}%\n"
        )

        file.write(
            f"Status : {status}\n"
        )

        file.write(
            "\nSkills Found:\n"
        )

        for skill in user_skills:
            file.write(
                f"✅ {skill}\n"
            )

        file.write(
            "\nMissing Skills:\n"
        )

        for skill in missing_skills:
            file.write(
                f"❌ {skill}\n"
            )

        file.write(
            "\nRecommended Projects:\n"
        )

        for project in data[
            "projects_to_build"
        ]:

            file.write(
                f"📌 {project}\n"
            )

        file.write(
            "\n" + "-" * 60 + "\n"
        )

    print(
        "\n💾 Report Saved Successfully!"
    )

else:

    print(
        "\n❌ Company not found."
    )

    print(
        "\nAvailable Companies:\n"
    )

    for company_name in companies:

        print(
            "👉",
            company_name.upper()
        )