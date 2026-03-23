# 🌦️ AtmosAPI

AtmosAPI is a RESTful API built using Flask that provides historical weather data (temperature) based on station ID and date.  
It uses real-world datasets processed with Pandas and exposes clean API endpoints for easy access.

---

## 🚀 Features

- Fetch temperature data by station and date
- RESTful API design
- Fast data retrieval using Pandas
- Simple web interface
- Data analysis and visualization included

---

## 🛠️ Tech Stack

- Python
- Flask
- Pandas
- HTML (Jinja Templates)

---

## 📂 Project Structure

AtmosAPI/
│
├── data/              # Weather dataset files
├── templates/         # HTML templates
│   ├── home.html
│   └── about.html
├── main.py            # Flask application
└── README.md

---

## 🔌 API Usage

### Endpoint

GET /api/v1/<station>/<date>

### Example

http://127.0.0.1:6969/api/v1/4/1860-01-01

### Response

{
  "station": 4,
  "temperature": 0.7
}

---

## 🖥️ Web Interface

- Home page shows available stations
- Example API usage included
- Clean and minimal interface

---

## 📊 Data Analysis

- Explored historical temperature trends
- Visualized seasonal variations
- Processed raw dataset using Pandas

---

## ⚙️ Installation & Setup

1. Clone the repository

git clone https://github.com/your-username/AtmosAPI.git

2. Navigate to the project

cd AtmosAPI

3. Install dependencies

pip install flask pandas

4. Run the application

python main.py

5. Open in browser

http://127.0.0.1:6969/

---

## 💡 Future Improvements

- Add more weather parameters (humidity, wind, etc.)
- Deploy API online
- Add authentication and rate limiting
- Improve frontend UI

---

## 🧠 Author

Sahil Sah