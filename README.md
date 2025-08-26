
# LinkedIn Job Data Visualization

## 🌟 Project Overview

The **LinkedIn Job Data Visualization** is a web application that provides interactive visual insights into job postings sourced from LinkedIn (via a CSV dataset). It allows users to explore key trends such as top hiring companies, most active job locations, and job posting activity over time — all through dynamic charts.

---

## 🎥 Demo Video

[Watch the Demo](https://drive.google.com/file/d/1T1xduaEov91vjpTAT3XLSKcLY3atyblu/view?usp=drive_link)


---

## ✨ Features

* **📊 Interactive Visualizations**  
  Explore job data via Pie Charts, Bar Charts, and Line Graphs using Chart.js.

* **🏢 Company Trends**  
  View the top 10 companies hiring the most through a vibrant pie chart.

* **📍 Location Insights**  
  See the top 10 locations with the highest number of job postings.

* **📈 Timeline of Postings**  
  Track how job postings fluctuate over time using a clean line chart.

* **🐍 Python Flask Backend**  
  Handles all data processing and chart serving using a lightweight backend.

* **🔎 Clean Data Handling**  
  Efficient CSV reading, grouping, and transformation using Pandas.

---

## 💻 Technologies Used

* **Backend**: Python 3.x, Flask  
* **Frontend**: HTML5, CSS3, JavaScript  
* **Visualization**: Chart.js  
* **Data Processing**: Pandas, NumPy  
* **Dependency Management**: `pip`, `requirements.txt`

---

## ⚙️ Setup and Installation

```bash
# Clone the repository (if applicable)
git clone https://github.com/your_username/linkedin-job-data-visualization.git
cd linkedinjob

# Create a virtual environment
python -m venv jobvenv

# Activate the environment
# Windows:
jobvenv\Scripts\activate

# macOS/Linux:
source jobvenv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🚀 Usage

```bash
# Start the Flask app
python app.py
```

- Open your browser and navigate to: http://127.0.0.1:5000/
- You’ll see visualizations of your job dataset in the form of interactive charts.

---
 
## 📁 Project Structure

```bash
linkedinjob/
├── app.py                   # Flask backend
├── data/
│   └── linkedin_jobs.csv    # CSV job dataset
├── templates/
│   └── index.html           # Main HTML page
├── requirements.txt         # Python dependencies
└── jobvenv/                 # Virtual environment (created during setup)
```

---

## 🌱 Future Enhancements

- 🔍 Advanced Filtering: Filter by company, location, date, or job title.

- 🗺️ Geographical Maps: Integrate geographical visualizations for better regional insights.

- 📊 More Metrics: Add analysis for job types, salary (if available), and keyword trends.

- 💾 Database Integration: Replace CSV with a real database for dynamic data updates.

- 📱 Responsive Design: Improve styling for mobile and tablet views.

- ☁️ Deployment: Deploy to platforms like Heroku, Render, or Vercel for public access.
