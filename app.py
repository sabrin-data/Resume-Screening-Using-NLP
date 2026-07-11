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

# Check if the model supports probability prediction
supports_probability = hasattr(model, "predict_proba")

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

# =====================================
# Programming Languages
# =====================================

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

# =====================================
# Web Development
# =====================================

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

# =====================================
# Databases
# =====================================

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

# =====================================
# Data Analysis
# =====================================

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
"data cleaning",
"data preprocessing",
"exploratory data analysis",
"eda",
"reporting",
"dashboard",
"dashboard creation",
"data visualization",

# =====================================
# Machine Learning
# =====================================

"machine learning",
"deep learning",
"artificial intelligence",
"ai",
"classification",
"regression",
"clustering",
"supervised learning",
"unsupervised learning",
"reinforcement learning",
"feature engineering",
"feature selection",
"model evaluation",
"cross validation",
"random forest",
"decision tree",
"logistic regression",
"linear regression",
"k-means",
"svm",
"xgboost",
"lightgbm",
"catboost",

# =====================================
# Deep Learning
# =====================================

"tensorflow",
"keras",
"pytorch",
"cnn",
"lstm",
"gru",

# =====================================
# NLP
# =====================================

"natural language processing",
"nlp",
"bert",
"gpt",
"llm",
"transformers",
"tokenization",
"stemming",
"lemmatization",
"sentiment analysis",
"text classification",
"tf-idf",
"nltk",
"spacy",

# =====================================
# Computer Vision
# =====================================

"opencv",
"image processing",
"object detection",
"face recognition",
"yolo",

# =====================================
# Cloud
# =====================================

"aws",
"azure",
"google cloud",
"gcp",
"cloud computing",

# =====================================
# DevOps
# =====================================

"git",
"github",
"gitlab",
"docker",
"kubernetes",
"jenkins",
"ci/cd",

# =====================================
# Big Data
# =====================================

"hadoop",
"spark",
"hive",
"kafka",
"airflow",

# =====================================
# Data Engineering
# =====================================

"etl",
"data warehouse",
"data lake",
"snowflake",

# =====================================
# Business Intelligence
# =====================================

"business intelligence",

# =====================================
# Office
# =====================================

"word",
"excel",
"powerpoint",
"outlook",
"access",
"office",
"visio",

# =====================================
# HR
# =====================================

"recruitment",
"human resources",
"payroll",
"peoplesoft",
"data entry",

# =====================================
# Evaluation Metrics
# =====================================

"accuracy",
"precision",
"recall",
"f1 score",
"roc auc",
"confusion matrix",

# =====================================
# Soft Skills
# =====================================

"leadership",
"communication",
"problem solving",
"critical thinking",
"teamwork",
"time management",
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

    return sorted(set(found_skills))

# =====================================
# Professional CSS
# =====================================

st.markdown("""
<style>

.stApp{
background:linear-gradient(
135deg,
#FFF7FB 0%,
#FFEAF4 30%,
#FDE2F3 70%,
#FFF7FB 100%);
}

.main-title{
font-size:54px;
font-weight:800;
text-align:center;
color:#C2185B;
margin-top:15px;
margin-bottom:5px;
}

.sub-title{
text-align:center;
font-size:20px;
color:#6A1B4D;
margin-bottom:35px;
}

.block{
background:white;
padding:25px;
border-radius:18px;
box-shadow:0 8px 20px rgba(0,0,0,.08);
margin-bottom:25px;
}

div[data-testid="stFileUploader"]{
background:white;
padding:20px;
border-radius:18px;
border:2px dashed #EC407A;
box-shadow:0 6px 15px rgba(0,0,0,.05);
}

.stButton>button{
background:#E91E63;
color:white;
border:none;
border-radius:12px;
padding:10px 22px;
font-weight:bold;
font-size:16px;
transition:0.3s;
}

.stButton>button:hover{
background:#C2185B;
}

div[data-testid="metric-container"]{
background:white;
border-radius:15px;
padding:15px;
box-shadow:0 5px 15px rgba(0,0,0,.08);
}

</style>
""", unsafe_allow_html=True)

# =====================================
# Header
# =====================================

st.markdown("""
<div class='main-title'>
🤖 AI Resume Screening System
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='sub-title'>
Upload your Resume and let AI predict the most suitable job category and automatically extract your professional skills.
</div>
""", unsafe_allow_html=True)

# =====================================
# Upload PDF
# =====================================

uploaded_file = st.file_uploader(
    "📄 Upload Resume (PDF)",
    type=["pdf"]
)

# =====================================
# Extra Skills
# =====================================

extra_skills = [

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

# Python
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
"pivot table",
"vlookup",
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

]

# إزالة التكرار إن وجد
skills = list(set(skills + extra_skills))
# =====================================
# After Upload
# =====================================

if uploaded_file is not None:

    st.success("✅ Resume uploaded successfully!")

    # Extract text
    text = extract_text_from_pdf(uploaded_file)

    # Predict Category
    prediction = model.predict([text])[0]

    # Confidence Score
    confidence = None

    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba([text])[0]
        confidence = round(probabilities.max() * 100, 2)

    # Extract Skills
    found_skills = extract_skills(text, skills)

    # =====================================
    # Result Cards
    # =====================================

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("## 🎯 Predicted Category")
        st.success(prediction)

    with col2:
        st.markdown("## 📊 Confidence Score")

        if confidence is not None:
            st.metric(
                label="Prediction Confidence",
                value=f"{confidence}%"
            )
        else:
            st.warning("This model does not support confidence scores.")

    st.markdown("---")

    # =====================================
    # Extracted Skills
    # =====================================

    st.markdown("## 💡 Extracted Skills")
    st.write(f"**Total Skills Found:** {len(found_skills)}")

    if found_skills:

        tags_html = """
<div style="
display:flex;
flex-wrap:wrap;
gap:10px;
margin-top:10px;
">
"""

        for skill in found_skills:

            tags_html += f"""
<div style="
background:linear-gradient(135deg,#EC407A,#D81B60);
color:white;
padding:10px 20px;
border-radius:999px;
font-weight:600;
font-size:16px;
box-shadow:0 4px 10px rgba(0,0,0,.15);
">
✅ {skill}
</div>
"""

        tags_html += "</div>"

        st.markdown(tags_html, unsafe_allow_html=True)

    else:

        st.warning("No skills were detected in this resume.")

    st.markdown("---")

    # =====================================
    # Download Results
    # =====================================

    result_text = f"""
=========================
AI Resume Screening Report
=========================

Predicted Category:
{prediction}

Confidence Score:
"""

    if confidence is not None:
        result_text += f"{confidence}%\n"
    else:
        result_text += "Not Available\n"

    result_text += "\nExtracted Skills:\n"

    for skill in found_skills:
        result_text += f"• {skill}\n"

    st.download_button(
        "📥 Download Results",
        data=result_text,
        file_name="resume_screening_result.txt",
        mime="text/plain"
    )

    # =====================================
    # Show Resume Text
    # =====================================

    with st.expander("📄 Show Extracted Resume Text"):

        st.text_area(
            "",
            text,
            height=350
        )

# =====================================
# Footer
# =====================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""

<hr>

<div style="text-align:center;
color:#9E9E9E;
font-size:15px;">

🤖 <b>AI Resume Screening System</b>

<br><br>

Built with ❤️ using Python • NLP • Scikit-learn • Streamlit

</div>

""", unsafe_allow_html=True)