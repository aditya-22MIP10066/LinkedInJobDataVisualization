from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
df = pd.read_csv("data/linkedin_jobs.csv")

@app.route("/")
def index():
    top_companies = df['company'].value_counts().head(10)
    top_locations = df['location'].value_counts().head(10)
    jobs_by_date = df['date_posted'].value_counts().sort_index()
    source_data = df['source'].value_counts()

    return render_template("index.html",
        company_data=top_companies.to_dict(),
        location_data=top_locations.to_dict(),
        dates=jobs_by_date.index.tolist(),
        job_counts=jobs_by_date.tolist(),
        source_data=source_data.to_dict()
    )

if __name__ == "__main__":
    app.run(debug=True)
