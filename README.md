# 🌦️ Autonomous Riyadh Weather Monitoring & Prediction System
[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://www.python.org/)
[![AWS](https://img.shields.io/badge/AWS-EC2-orange?logo=amazon-aws)](https://aws.amazon.com/)
[![Streamlit](https://img.shields.io/badge/Dashboard-Live-FF4B4B?logo=streamlit)](http://13.62.76.150:8501)

An end-to-end data engineering pipeline that automates real-time weather collection from Riyadh, processes time-series data, and provides predictive insights through a cloud-hosted dashboard.

---

## 👥 The Engineering Team
| Role | Name | Technical Focus |
| :--- | :--- | :--- |
| **Data Engineer** | AHMED BOBANE | AWS EC2, Crontab Automation |
| **Data Scientist** | OSAMA ABDULKADIR | EDA, Jupyter Research |
| **Full-Stack Dev** | ABDALMOUMEN ZA DAHMAN | Streamlit UI, Git Version Control, API Integration |

---

## 🏗️ System Architecture & Workflow

1.  **Ingestion Layer**: A Python service connects to the OpenWeather API to fetch live metrics for Riyadh.
2.  **Cloud Layer**: Hosted on **AWS EC2 (Ubuntu)** to ensure 24/7 system availability.
3.  **Automation Layer**: A **Linux Cron Job** (`0 * * * *`) triggers the pipeline at the start of every hour.
4.  **Security**: Environment variables (`.env`) protect sensitive API credentials from exposure.
5.  **Storage**: Real-time records are appended to a time-series CSV database (`data/raw_weather_data.csv`).

---

## 🧪 Data Science & Machine Learning
We moved beyond collection into predictive analytics using two core research phases:

### 📈 Phase 1: Exploratory Data Analysis (EDA)
Located in `notebooks/01_EDA_Cleaning.ipynb`. We analyzed temperature distributions and cleaned raw data points to prepare for modeling.

### 🤖 Phase 2: Predictive Modeling
Located in `notebooks/02_Baseline_Modeling.ipynb`. We implemented a **Linear Regression** model to predict the temperature of the next hour ($T_{t+1}$) based on historical trends.

---

## 💻 How to View
* **Live Dashboard**: `http://13.62.76.150:8501`
* **Data Logs**: Found in `data/raw_weather_data.csv` (Updates hourly via AWS)

---

## 🛠️ Technology Stack
* **Backend**: Python (Pandas, Scikit-learn, Dotenv)
* **Cloud**: Amazon Web Services (EC2 Instance)
* **Automation**: Crontab (Linux Scheduler)
* **Frontend**: Streamlit (Interactive Web Dashboard)
* **Version Control**: Git & GitHub

---


## 🔮 Future Work
* **Real-time Inference**: Migrating the Jupyter Machine Learning model directly into the AWS pipeline for live "Predicted vs Actual" charts.
* **Alerting System**: Adding an automated email/SMS alert for extreme weather conditions in Riyadh.

---
> **Final Project Status**: System is currently operational and updating the dataset hourly.
