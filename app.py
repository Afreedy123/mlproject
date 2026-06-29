from flask import Flask, request, render_template
import traceback

from src.pipeline.predict_pipeline import CustomData, PredictPipeline

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():

    if request.method == 'GET':
        return render_template("home.html")

    try:
        print("\n================ REQUEST RECEIVED ================")

        gender = request.form.get("gender")
        race = request.form.get("ethnicity")
        parent = request.form.get("parental_level_of_education")
        lunch = request.form.get("lunch")
        course = request.form.get("test_preparation_course")
        reading = request.form.get("reading_score")
        writing = request.form.get("writing_score")

        print("Gender :", gender)
        print("Race :", race)
        print("Parent :", parent)
        print("Lunch :", lunch)
        print("Course :", course)
        print("Reading :", reading)
        print("Writing :", writing)

        data = CustomData(
            gender=gender,
            race_ethnicity=race,
            parental_level_of_education=parent,
            lunch=lunch,
            test_preparation_course=course,
            reading_score=float(reading),
            writing_score=float(writing)
        )

        print("\nCreating DataFrame...")

        pred_df = data.get_data_as_data_frame()

        print(pred_df)

        print("\nLoading Prediction Pipeline...")

        predict_pipeline = PredictPipeline()

        print("Calling predict()...")

        prediction = predict_pipeline.predict(pred_df)

        print("Prediction Completed")
        print(prediction)

        return render_template(
            "home.html",
            results=prediction[0]
        )

    except Exception:

        print("\n================ ERROR OCCURRED ================")
        traceback.print_exc()
        print("================================================")

        return f"""
        <h1>Prediction Failed</h1>
        <pre>{traceback.format_exc()}</pre>
        """


if __name__ == "__main__":
    app.run(debug=True)