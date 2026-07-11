# 🤖 AI Resume Screening System (NLP)

An AI-powered Resume Screening System built with **Python**, **Natural Language Processing (NLP)**, **Scikit-learn**, and **Streamlit**.

The application predicts the most suitable job category from an uploaded resume (PDF) and automatically extracts technical and professional skills.

---

# ✨ Features

✅ Upload Resume in PDF format

✅ Extract text automatically from PDF files

✅ Predict Resume Category using Machine Learning

✅ Extract 250+ Technical & Professional Skills

✅ Modern and Interactive Streamlit Interface

✅ Download Screening Results

✅ Display Extracted Resume Text

---

# 🖥️ Application Preview

### 🏠 Home Page

![Home](images/home_page.png)

---

### 📂 Upload Resume

![Upload](images/upload_resume.png)

---

### 🎯 Prediction Result

![Prediction](images/prediction_result.png)

---

### 💡 Skills Extraction

![Skills](images/skills_extraction.png)

---

# 📊 Machine Learning Workflow

1. Data Collection
2. Data Cleaning & Preprocessing
3. Text Vectorization (TF-IDF)
4. Model Training
5. Model Evaluation
6. Resume Classification
7. Skills Extraction
8. Streamlit Deployment

---

# 🛠️ Technologies Used

- 🐍 Python
- 🤖 Scikit-learn
- 📄 NLP (Natural Language Processing)
- 📊 Pandas
- 🔢 NumPy
- 📈 Matplotlib
- 🎨 Streamlit
- 📑 PyPDF
- 💾 Joblib

---

# 📂 Project Structure

```text
Resume-Screening-Using-NLP/
│
├── app.py
├── best_resume_classifier_model.pkl
├── requirements.txt
├── README.md
├── images/
│   ├── home_page.png
│   ├── upload_resume.png
│   ├── prediction_result.png
│   └── skills_extraction.png
└── notebook.ipynb
```

---

# 🧹 Data Preprocessing

The resumes were preprocessed before training the model by:

- Removing punctuation
- Removing numbers
- Converting text to lowercase
- Removing stop words
- Tokenization
- Lemmatization
- TF-IDF Vectorization

---

# 🧠 Machine Learning Model

Several classification algorithms were trained and compared.

🏆 **Best Model:** Linear Support Vector Classifier (LinearSVC)

**Performance**

- Accuracy: **71.23%**
- Macro F1 Score: **68.35%**
- Weighted F1 Score: **70.37%**

> ℹ️ **Note:** The deployed model is **LinearSVC**, which provides strong classification performance but does not support probability predictions (`predict_proba`). Therefore, confidence scores are not displayed.

---

# 🚀 How to Run

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Resume-Screening-Using-NLP.git
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```

---

# 📌 Future Improvements

- 🔹 Train a Logistic Regression model to display confidence scores
- 🔹 Support DOCX resumes
- 🔹 Improve NLP preprocessing
- 🔹 Add more resume categories
- 🔹 Enhance the user interface

---

# 👩‍💻 Author

**Sabrin Khater**

💼 Aspiring Data Analyst & Junior Data Scientist

🔗 LinkedIn: *(Add your LinkedIn profile)*

💻 GitHub: *(Add your GitHub profile)*

---

⭐ If you like this project, don't forget to give it a star!
