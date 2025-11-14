import streamlit as st
from typing import List

st.title("Bus and Queue Tracker")

# Sidebar controls: search box and buses selection
st.sidebar.header("Controls")

search_route = st.sidebar.text_input("Search bus route", value="")

# Try to fetch available buses from the backend; fall back to an empty list
def _fetch_bus_routes() -> List[str]:
	try:
		import requests

		resp = requests.get("http://127.0.0.1:8000/bus", timeout=2)
		resp.raise_for_status()
		data = resp.json()
		# Expecting a list of bus objects with a `route` field
		routes = [str(item.get("route") ) for item in data]
		return sorted(set(routes))
	except Exception:
		return []

bus_options = _fetch_bus_routes()

selected_buses = st.sidebar.multiselect("Buses", options=bus_options, default=None)

# Main area: reflect the selection and search
st.markdown("### Current filters")
st.write("Search route:", search_route or "(none)")
st.write("Selected buses:", selected_buses or "(none)")

if not bus_options:
	st.info("No buses were fetched from the backend. Make sure the FastAPI server is running at http://127.0.0.1:8000")
