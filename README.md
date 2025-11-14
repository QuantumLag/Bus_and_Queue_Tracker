# Bus_Queue_Tracker
🚌 Bus & Queue Tracker

A real-time bus tracking system built using FastAPI, Streamlit Dashboard, and a Python simulator that updates bus locations continuously.

🚀 Features (Current Progress)

✔ Add new buses with route, latitude, longitude

✔ Fetch all buses

✔ Fetch buses by route

✔ Update bus location using a PATCH API (used by the simulator)

✔ Basic Streamlit dashboard

✔ Python location simulator sending updates every 3 seconds

🛠 Tech Stack
Component	Technology
Backend	FastAPI
Database	SQLite + SQLAlchemy
Frontend	Streamlit
Scripts	Python Requests
Server	Uvicorn
📁 Project Structure
bus-queue-tracker/
│── main.py              # FastAPI backend APIs
│── models.py            # SQLAlchemy ORM models
│── schemas.py           # Pydantic request/response schemas
│── database.py          # DB engine + session creation
│── simulator.py         # Bus location update simulator
│── dashboard.py         # Streamlit UI for viewing data
│── data.db              # SQLite database file
│── README.md            # Project documentation

⚙️ How to Run the Backend

Open a terminal and run:

uvicorn main:app --reload


This starts your API server at:

📌 http://127.0.0.1:8000

📌 Swagger Docs: http://127.0.0.1:8000/docs

📡 How to Run the Bus Simulator
python simulator.py


This script automatically sends a PATCH request to your FastAPI backend every 3 seconds to update the bus location.

📊 How to Run the Streamlit Dashboard
streamlit run dashboard.py


This launches a simple UI where users can search or view buses.

🔮 Upcoming Features

These will be added in future updates:

⏳ Bus stop management

👥 Queue length tracking

⏱ Arrival time prediction

🗺 Interactive live map

🧭 Better UI & navigation

👤 Author

Satchit K
