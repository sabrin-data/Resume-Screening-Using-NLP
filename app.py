import streamlit as st
import joblib
from pypdf import PdfReader

# =====================================
# Page Configuration
# =====================================

st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =====================================
# Load Trained Model
# =====================================

model = joblib.load("best_resume_classifier_model.pkl")

# =====================================
# Extract Text From PDF
# =====================================

def extract_text_from_pdf(uploaded_file):

    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:

            text += page_text + " "

    return " ".join(text.split())

# =====================================
# Skills Dictionary 
# =====================================

skills = [

# Programming Languages

"python",
"java",
"c",
"c++",
"c#",
"r",
"go",
"swift",
"kotlin",
"scala",
"perl",
"php",
"ruby",
"matlab",
"typescript",
"javascript",

# Web

"html",
"css",
"bootstrap",
"tailwind",
"react",
"angular",
"vue",
"next.js",
"node.js",
"express",
"flask",
"django",
"fastapi",

# Databases

"sql",
"mysql",
"postgresql",
"sqlite",
"oracle",
"mongodb",
"redis",
"firebase",
"mariadb",
"cassandra",

# Data Analysis

"pandas",
"numpy",
"matplotlib",
"seaborn",
"plotly",
"scipy",
"statistics",
"power bi",
"tableau",
"excel",
"google sheets",

# Machine Learning

"machine learning",
"deep learning",
"artificial intelligence",
"ai",
"supervised learning",
"unsupervised learning",
"reinforcement learning",
"classification",
"regression",
"clustering",
"feature engineering",
"model evaluation",

# Libraries

"scikit-learn",
"tensorflow",
"keras",
"pytorch",
"xgboost",
"lightgbm",
"catboost",
"opencv",
"nltk",
"spacy",
"transformers",

# NLP

"natural language processing",
"nlp",
"bert",
"gpt",
"llm",
"tokenization",
"stemming",
"lemmatization",
"sentiment analysis",
"text classification",

# Computer Vision

"cnn",
"yolo",
"image processing",
"object detection",
"face recognition",

# Cloud

"aws",
"azure",
"google cloud",
"gcp",
"cloud computing",

# DevOps

"docker",
"kubernetes",
"github",
"git",
"gitlab",
"jenkins",
"ci/cd",

# Big Data

"hadoop",
"spark",
"hive",
"kafka",
"airflow",

# Data Engineering

"etl",
"data warehouse",
"data lake",
"snowflake",

# BI

"dashboard",
"business intelligence",
"data visualization",

# Office

"word",
"powerpoint",
"outlook",
"access",
"visio",
"office",

# HR

"recruitment",
"human resources",
"payroll",
"peoplesoft",
"data entry",

# Soft Skills

"leadership",
"communication",
"problem solving",
"teamwork",
"time management",
"critical thinking",
"presentation",
"negotiation",
"project management",
"decision making"

]

# =====================================
# Extract Skills
# =====================================

def extract_skills(text, skills_list):

    text = text.lower()

    found_skills = []

    for skill in skills_list:

        if skill.lower() in text:

            found_skills.append(skill)

    return sorted(list(set(found_skills)))

# =====================================
# Professional CSS
# =====================================

st.markdown("""

<style>

.stApp{

background:linear-gradient(
135deg,
#FFF5FA 0%,
#FFEAF4 35%,
#FDE2F3 70%,
#FFF8FB 100%
);

}

.main-title{

font-size:52px;

font-weight:800;

text-align:center;

color:#C2185B;

margin-top:10px;

margin-bottom:5px;

}

.sub-title{

text-align:center;

font-size:20px;

color:#6A1B4D;

margin-bottom:40px;

}

.block{

background:white;

padding:25px;

border-radius:18px;

box-shadow:0 10px 25px rgba(0,0,0,.08);

margin-bottom:25px;

}

div[data-testid="stFileUploader"]{

background:white;

padding:20px;

border-radius:18px;

border:2px dashed #E91E63;

}

.stButton>button{

background:#E91E63;

color:white;

border:none;

border-radius:10px;

font-weight:bold;

}

</style>

""", unsafe_allow_html=True)

# =====================================
# Header
# =====================================

st.markdown(
"""
<div class='main-title'>
🤖 AI Resume Screening System
</div>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<div class='sub-title'>
Upload your Resume and let AI predict the job category and extract your professional skills.
</div>
""",
unsafe_allow_html=True
)

# =====================================
# Upload PDF
# =====================================

uploaded_file = st.file_uploader(

"📄 Upload Resume (PDF)",

type=["pdf"]

)

# =====================================
# Complete Skills Dictionary 
# =====================================

skills.extend([

# Data Science
"data analysis",
"data mining",
"data science",
"predictive analytics",
"data cleaning",
"data preprocessing",
"exploratory data analysis",
"eda",
"feature selection",
"cross validation",
"hyperparameter tuning",
"confusion matrix",
"accuracy",
"precision",
"recall",
"f1 score",
"roc curve",
"auc",

# Python Libraries
"joblib",
"pickle",
"beautifulsoup",
"requests",
"selenium",
"streamlit",
"gradio",
"dash",
"openai",
"langchain",
"faiss",
"chromadb",

# Databases
"sql server",
"pl/sql",
"database design",
"database administration",

# Cloud
"amazon web services",
"ec2",
"s3",
"lambda",
"azure ml",
"azure devops",
"google colab",

# Linux
"linux",
"ubuntu",
"bash",
"shell scripting",

# Networking
"tcp/ip",
"dns",
"dhcp",
"vpn",
"firewall",

# Software
"jira",
"trello",
"notion",
"slack",
"figma",

# Engineering
"autocad",
"solidworks",
"ansys",
"matlab simulink",

# Accounting
"quickbooks",
"sap",
"erp",

# HR
"employee relations",
"onboarding",
"performance management",
"training",
"interviewing",

# Marketing
"digital marketing",
"seo",
"sem",
"google analytics",
"social media",

# Finance
"financial analysis",
"budgeting",
"forecasting",

# Office
"microsoft office",
"excel advanced",
"vlookup",
"pivot table",
"xlookup",

# Soft Skills
"adaptability",
"multitasking",
"creativity",
"analytical thinking",
"attention to detail",
"organization",
"customer service",
"public speaking",
"mentoring",
"coaching"

])

# =====================================
# After Upload
# =====================================

if uploaded_file is not None:

    st.success("✅ Resume uploaded successfully!")

    # Extract text
    text = extract_text_from_pdf(uploaded_file)

    # Predict category
    prediction = model.predict([text])[0]

    # Confidence Score
    confidence = None

    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba([text])[0]
        confidence = probabilities.max() * 100

    # Extract skills
    found_skills = extract_skills(text, skills)

    # =====================================
    # Result Cards
    # =====================================

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### 🎯 Predicted Category")

        st.success(prediction)

    with col2:

        st.markdown("### 📊 Confidence Score")

        if confidence is not None:

            st.metric(
                label="Prediction Confidence",
                value=f"{confidence:.2f}%"
            )

        else:

            st.info("Confidence score is not available for this model.")

    st.markdown("---")

    st.markdown("### 💡 Extracted Skills")

    st.write(f"**Total Skills Found:** {len(found_skills)}")

    # =====================================
    st.markdown("---")

    st.markdown("### 💡 Extracted Skills")
    st.write(f"**Total Skills Found:** {len(found_skills)}")

    if found_skills:

        tags_html = ""

        for skill in found_skills:
            tags_html += f"""
            <span style="
                display:inline-block;
                background:#F8BBD0;
                color:#880E4F;
                padding:10px 18px;
                margin:6px;
                border-radius:25px;
                font-weight:bold;
                font-size:16px;
            ">
                {skill}
            </span>
            """

        st.markdown(tags_html, unsafe_allow_html=True)

    else:
        st.warning("No skills were detected in this resume.")

    # =====================================
    # Download Results
    # =====================================

    if confidence is not None:
        result_text = f"""
AI Resume Screening Result

Predicted Category:
{prediction}

Confidence Score:
{confidence:.2f}%

Extracted Skills:
"""
    else:
        result_text = f"""
AI Resume Screening Result

Predicted Category:
{prediction}

Confidence Score:
Not Available

Extracted Skills:
"""

    for skill in found_skills:
        result_text += f"\n- {skill}"

    st.download_button(
        "📥 Download Results",
        result_text,
        "resume_screening_result.txt",
        "text/plain"
    )

    with st.expander("📄 Show Extracted Resume Text"):
        st.text_area(
            "",
            text,
            height=350
        )

# =====================================
# Footer
# =====================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""

<hr>

<div style="text-align:center;
color:#9E9E9E;
font-size:15px;">

🤖 AI Resume Screening System

<br>

Built with ❤️ using Python, NLP, Scikit-learn and Streamlit

</div>

""", unsafe_allow_html=True)