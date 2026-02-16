# 🌍 Air Quality Index (AQI) Prediction System

A full-stack Machine Learning web application that predicts **Air Quality Index (AQI)** using key air pollutant parameters:

* **PM2.5**
* **NO₂**
* **O₃**
* **CO**

The system provides real-time AQI predictions along with health-based recommendations and visual AQI indicators.

---

## 🚀 Features

* 🔹 Machine Learning-based AQI prediction
* 🔹 Feature scaling using `StandardScaler`
* 🔹 Flask REST API backend
* 🔹 Interactive frontend with AQI meter visualization
* 🔹 Health suggestions based on AQI category
* 🔹 Production-ready configuration with Gunicorn

---

## 🧠 Tech Stack

**Backend**

* Python
* Flask
* Scikit-learn
* NumPy
* Gunicorn

**Frontend**

* HTML
* Tailwind CSS
* JavaScript

---

## 📂 Project Structure

```
├── backend.py
├── air_quality_prediction.pkl
├── requirements.txt
├── static/
│   ├── index.html
│   └── predict.html
└── README.md
```

* Backend logic: 
* Project dependencies: 

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/aqi-prediction.git
cd aqi-prediction
```

### 2️⃣ Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
python backend.py
```

App runs at:

```
http://127.0.0.1:8081/
```

---

## 🔮 How It Works

1. User inputs pollutant values (PM2.5, NO₂, O₃, CO).
2. Features are scaled using `StandardScaler`.
3. The trained ML model predicts AQI.
4. AQI category and health recommendations are displayed dynamically.

---

## 📊 AQI Categories

| AQI Range | Category                       |
| --------- | ------------------------------ |
| 0–50      | Good                           |
| 51–100    | Moderate                       |
| 101–150   | Unhealthy for Sensitive Groups |
| 151–200   | Unhealthy                      |
| 201–300   | Very Unhealthy                 |
| 301–500   | Hazardous                      |

---

## ⚠️ Disclaimer

Predictions are for educational and informational purposes only. For accurate air quality information, consult official environmental monitoring sources.

---

## 📌 Future Improvements

* Deploy to cloud (AWS / Azure / Render)
* Add live AQI API integration
* Improve model accuracy with larger datasets
* Add historical AQI trend analysis

---

### 👨‍💻 Author

**Chaitanya Korada**
Machine Learning & Web Development Project

