from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load("model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def prediction():
    Gender = request.form.get("gender")
    Married = request.form.get("married")
    Education = request.form.get("education")
    Self_Employed = request.form.get("employed")
    ApplicantIncome = request.form.get("app_income")
    CoapplicantIncome = request.form.get("self_co_income")
    LoanAmount = request.form.get("loan_amount")
    Loan_Amount_Term = request.form.get("loan_term")
    Credit_History = request.form.get("credit_history")
    Property_Area = request.form.get("property_area")

    # Check if any field is empty
    if not all([
        Gender, Married, Education, Self_Employed,
        ApplicantIncome, CoapplicantIncome,
        LoanAmount, Loan_Amount_Term,
        Credit_History, Property_Area
    ]):
        return render_template(
            "index.html",
            pred="----Please fill in all fields----"
        )

    try:
        # Convert inputs to numeric values
        final = [
            int(Gender),
            int(Married),
            int(Education),
            int(Self_Employed),
            float(ApplicantIncome),
            float(CoapplicantIncome),
            float(LoanAmount),
            float(Loan_Amount_Term),
            float(Credit_History),
            int(Property_Area),
        ]

        # Predict
        prediction = model.predict([final])

        if prediction[0] == 1:
            result = "----Your Loan is Approved----"
        else:
            result = "----Your Loan is Not Approved----"

        return render_template("index.html", pred=result)

    except ValueError:
        return render_template(
            "index.html",
            pred="----Invalid input. Please enter valid numbers----"
        )

    except Exception as e:
        return render_template(
            "index.html",
            pred=f"Error: {str(e)}"
        )


if __name__ == "__main__":
    app.run(debug=True)
