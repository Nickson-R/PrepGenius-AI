import os
import tempfile
import streamlit as st
#import matplotlib.pyplot as plt
import pandas as pd

from companies import companies
from resume_analyzer import (
    extract_text,
    extract_skills
)

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="PrepGenius AI",
    page_icon="🚀",
    layout="wide"
)

# ---------------- CSS ----------------

st.markdown("""
<style>

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

div[data-testid="metric-container"]{
    background:#1b1b1b;
    border:1px solid #444;
    border-radius:20px;
    padding:20px;
}

div.stButton > button{
    width:100%;
    height:55px;
    border-radius:15px;
    font-size:18px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.title("🚀 PrepGenius AI")

    st.markdown("""
### AI Placement Assistant

Upload your resume and get:

✅ ATS Score

✅ Skill Analysis

✅ Placement Score

✅ Skill Gap Analysis

✅ Personalized Roadmap

✅ Company Comparison
""")

    st.divider()

    st.metric(
        "Supported Companies",
        len(companies)
    )

    st.metric(
        "Version",
        "1.0"
    )

    st.caption(
        "Built using Python + Streamlit"
    )

# ---------------- HEADER ----------------

st.title("🚀 PrepGenius AI")

st.subheader(
    "AI Powered Placement Readiness Analyzer"
)

st.info("""
🎯 ATS Score

❌ Skill Gap Analysis

📅 Personalized Roadmap

🏢 Company Comparison
""")

# ---------------- COMPANY SELECT ----------------

company = st.selectbox(
    "🏢 Select Company",
    list(companies.keys())
)

# ---------------- LOGOS ----------------

logos = {

    "tcs":"assets/tcs.png",
    "infosys":"assets/infosys.png",
    "hcltech":"assets/hcl tech.png",
    "zoho":"assets/zoho.png",
    "surveysparrow":"assets/survey sparrow.png",
    "accenture":"assets/accenture.png",
    "cognizant":"assets/cognizant.png",
    "capgemini":"assets/capgemini.png",
    "deloitte":"assets/deloitte.png",
    "wipro":"assets/wipro.png",
    "techmahindra":"assets/tech mahindra.png",
    "renault":"assets/renault.png"
}

if company in logos:

    logo_path = logos[company]

    if os.path.exists(logo_path):

        col1, col2 = st.columns([1,5])

        with col1:
            st.image(
                logo_path,
                width=100
            )

        with col2:
            st.subheader(
                company.upper()
            )

# ---------------- FILE UPLOAD ----------------

uploaded_file = st.file_uploader(
    "📄 Upload Resume",
    type=["pdf"]
)

# ---------------- ANALYZE ----------------

if st.button("🚀 Analyze"):

    if uploaded_file is None:

        st.error(
            "Please upload a resume."
        )

    else:

        try:

            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".pdf"
            ) as tmp:

                tmp.write(
                    uploaded_file.getvalue()
                )

                pdf_path = tmp.name

            text = extract_text(
                pdf_path
            )

            user_skills = extract_skills(
                text
            )

        except Exception as e:

            st.error(
                f"PDF Error : {e}"
            )

            st.stop()

        data = companies[company]

        missing_skills = []

        for skill in data["skills_needed"]:

            if skill.lower() not in user_skills:

                missing_skills.append(
                    skill
                )

        matched_skills = (
            len(data["skills_needed"])
            - len(missing_skills)
        )

        score = (
            matched_skills
            / len(data["skills_needed"])
        ) * 100

        ats_score = min(
            40
            + len(user_skills) * 4
            + matched_skills * 6,
            100
        )

        # ---------------- METRICS ----------------

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "🎯 Placement",
            f"{score:.0f}%"
        )

        col2.metric(
            "📄 ATS",
            f"{ats_score:.0f}%"
        )

        col3.metric(
            "✅ Skills",
            len(user_skills)
        )

        col4.metric(
            "❌ Missing",
            len(missing_skills)
        )

        st.progress(
            score / 100
        )

        if score >= 80:

            st.success(
                "🟢 Highly Ready"
            )

        elif score >= 50:

            st.warning(
                "🟡 Moderately Ready"
            )

        else:

            st.error(
                "🔴 Needs Preparation"
            )

        # ---------------- TABS ----------------

        tab1, tab2, tab3, tab4 = st.tabs([
            "📄 Skills",
            "📊 Analysis",
            "📅 Roadmap",
            "🏢 Companies"
        ])

        # ---------------- SKILLS ----------------

        with tab1:

            st.subheader(
                "Skills Found"
            )

            for skill in user_skills:

                st.success(
                    skill
                )

        # ---------------- ANALYSIS ----------------

        with tab2:

            st.subheader(
                "Missing Skills"
            )

            if len(missing_skills) == 0:

                st.success(
                    "No missing skills."
                )

            else:

                for skill in missing_skills:

                    st.error(
                        skill
                    )

            st.subheader(
                "Skill Distribution"
            )

            chart_df = pd.DataFrame(
    {
        "Category": labels,
        "Count": sizes
    }
)

st.bar_chart(
    chart_df.set_index("Category")
)

        # ---------------- ROADMAP ----------------

        with tab3:

            st.subheader(
                "Personalized Roadmap"
            )

            if len(missing_skills) == 0:

                st.success(
                    "Focus on projects and interviews."
                )

            else:

                for i, skill in enumerate(
                    missing_skills,
                    start=1
                ):

                    st.write(
                        f"🚀 Week {i} → Learn {skill}"
                    )

        # ---------------- COMPANY COMPARISON ----------------

        with tab4:

            scores = {}

            for c in companies:

                needed = companies[c]["skills_needed"]

                temp_missing = []

                for skill in needed:

                    if skill.lower() not in user_skills:

                        temp_missing.append(
                            skill
                        )

                matched = (
                    len(needed)
                    - len(temp_missing)
                )

                company_score = (
                    matched
                    / len(needed)
                ) * 100

                scores[c.upper()] = company_score

            df = pd.DataFrame(
                scores.items(),
                columns=[
                    "Company",
                    "Score"
                ]
            )

            st.bar_chart(
                df.set_index(
                    "Company"
                )
            )

        # ---------------- RECOMMENDATIONS ----------------

        st.subheader(
            "💡 Company Recommendations"
        )

        for skill in missing_skills:

            st.info(
                f"Learn {skill}"
            )

        # ---------------- REPORT ----------------

        report = f"""
Company : {company}

ATS Score : {ats_score:.0f}%

Placement Score : {score:.0f}%

Skills :
{user_skills}

Missing :
{missing_skills}
"""

        st.download_button(
            "📄 Download Report",
            report,
            file_name="placement_report.txt"
        )

        # ---------------- FEATURES ----------------

        with st.expander(
            "✨ Features Used"
        ):

            st.write("✅ Resume Parsing")
            st.write("✅ ATS Score")
            st.write("✅ Skill Extraction")
            st.write("✅ Skill Gap Analysis")
            st.write("✅ Personalized Roadmap")
            st.write("✅ Company Comparison")
            st.write("✅ Report Download")

# ---------------- FOOTER ----------------

st.markdown("---")

st.caption(
    "🚀 Made by Rex Nickson | PrepGenius AI v1.0"
)