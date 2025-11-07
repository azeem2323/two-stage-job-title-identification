# 🧠 Two-Stage Job Title Identification System

A machine learning and web-based system that identifies and classifies job titles from online job advertisements using a **two-stage model** combining **BERT embeddings** and **unsupervised similarity measures**.  

Built as a **major project** for the **Department of Computer Science (Data Science)**, Lords Institute of Engineering and Technology, affiliated to Osmania University.

---

## 🚀 Features

- **Stage 1**: Classifies job advertisements by sector using BERT.
- **Stage 2**: Matches the closest job title within that sector using similarity metrics.
- **ML Models Used**: BERT, SVM, Naïve Bayes, CNN, Logistic Regression.
- **Web Interface**: Simple HTML frontend built with Django.
- **Dataset**: Custom dataset of online job advertisements.

---

## 🏗️ Tech Stack

| Component | Technology |
|------------|-------------|
| Language | Python 3.7+ |
| Framework | Django |
| Machine Learning | scikit-learn, TensorFlow, Transformers |
| Visualization | Matplotlib, Pandas |
| Frontend | HTML (Tkinter used for local GUI experiments) |

---

## ⚙️ Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/azeem2323/Jobtitleprediction.git
   cd Jobtitleprediction
