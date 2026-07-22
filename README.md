# 🏦 Home Loan Approval Prediction Web Application

A machine learning web application that predicts whether a home loan application is likely to be approved based on user inputs such as gender, marital status, education, income, loan amount, credit history, and property area. The application is built using **Flask** and a **Decision Tree Classifier**, providing instant loan approval predictions through a simple and user-friendly web interface.

## 🚀 Live Demo

https://loan-approval-prediction-m5k0.onrender.com

## 📂 GitHub Repository

https://github.com/saniya331/loan-approval-prediction

## 📋 Table of Contents

- Features
- Technologies Used
- Installation
- Project Structure
- Screenshots
- How It Works
- Model Information

## ✨ Features

- User-friendly web interface
- Predicts home loan approval instantly
- Decision Tree machine learning model
- Input validation for better user experience
- Responsive design

## 🛠️ Technologies Used

- **Backend:** Flask
- **Frontend:** HTML, CSS
- **Machine Learning:** Scikit-learn, Joblib
- **Programming Language:** Python
- **Deployment:** Render

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/saniya331/loan-approval-prediction.git
```

### Move to the project directory

```bash
cd loan-approval-prediction
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

## 📁 Project Structure

```
loan-approval-prediction/
│
├── static/
├── templates/
│   └── index.html
├── app.py
├── model.pkl
├── requirements.txt
└── README.md
```

## 📸 Screenshots

_Add screenshots of your application here._

## ⚙️ How It Works

1. Enter the required loan applicant details.
2. Click the **Predict** button.
3. The trained Decision Tree model processes the inputs.
4. The application displays whether the loan is likely to be **Approved** or **Not Approved**.

## 🤖 Model Information

- **Algorithm:** Decision Tree Classifier
- **Library:** Scikit-learn
- **Model Storage:** Joblib (`model.pkl`)


  ## 🚀 Future Enhancements

- Improve prediction accuracy using advanced machine learning models.
- Add user authentication and application history.
- Store data in a MySQL database.
- Integrate document upload and verification.
- Provide AI-based explanations for prediction results.
- Develop a REST API for external integration.
- Deploy using Docker and cloud platforms.
- Integrate real-world banking APIs.

## 👩‍💻 Author

**Saniya Begum**

- GitHub: https://github.com/saniya331
- LinkedIn: www.linkedin.com/in/saniya-begum-9a89643b6
