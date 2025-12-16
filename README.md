COVID‑19 Data Visualization Dashboard
A Python mini‑project that analyses city‑wise COVID‑19 case statistics and visualizes them using Matplotlib.
The dashboard reads data from a CSV file, calculates key health metrics, highlights critical cities, and displays a multi‑bar chart with a trend line.

Features
Load COVID‑19 data for multiple cities from csv_data.csv.

Object‑oriented design with separate classes for city data, analysis, and reporting.

Calculates for each city:

Recovery rate

Mortality rate

Growth rate (based on previous confirmed cases, if provided)

Severity level (High / Medium / Low) based on active cases

Identifies critical cities using an active‑case threshold.

Console dashboard with neatly formatted statistics.

Matplotlib visualization:

Stacked bars for Confirmed, Recovered, Active cases

Red trend line showing growth rate (%) on a secondary axis

Automation features:

Decorator for dashboard header

Lambda function for percentage formatting

Project Structure
text
covid_19/
├── analyzer.py        # DataAnalyzer class – file handling & calculations
├── city_class.py      # City class – stores stats & computes metrics
├── dashboard_main.py  # Main dashboard script – printing & plotting
└── csv_data.csv       # Input dataset for multiple cities
Installation
Clone the repository

bash
git clone <your-repo-url>
cd covid_19
(Optional) Create and activate a virtual environment

bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
Install dependencies

Only Matplotlib is required (rest are from the Python standard library):

bash
pip install matplotlib
Usage
From inside the covid_19 folder:

bash
python dashboard_main.py
The script will:

Print a header: ====== COVID-19 DASHBOARD ======.

Load data from csv_data.csv.

For each city, print:

Confirmed and active cases

Recovery, mortality, and growth rates

Severity level

Print the list of critical cities (above the active threshold).

Display a Matplotlib window with:

Stacked bars (Confirmed, Recovered, Active)

Growth‑rate trend line (%)

To change the analysis, edit csv_data.csv (add/remove cities, update numbers, optionally add a PrevConfirmed column for growth rate).

Core Components
City class (city_class.py)
Represents a single city and its COVID‑19 data.

Attributes: name, confirmed, recovered, deaths, active, prev_confirmed.

Methods:

recovery_rate() – returns recovery percentage.

mortality_rate() – returns mortality percentage.

growth_rate() – returns growth rate based on previous confirmed.

severity_level() – returns "High", "Medium", or "Low".

__str__() – nicely formatted string for printing.

DataAnalyzer class (analyzer.py)
Handles file I/O and aggregated analysis.

Builds a safe path to csv_data.csv relative to the script.

load_data() – reads the CSV and creates a list of City objects.

critical_cities(threshold=20000) – returns names of cities with high active cases.

average_recovery_rate(), average_mortality_rate(), average_growth_rate() – dataset‑level summary metrics.

Report class & Dashboard (dashboard_main.py)
dashboard_header decorator prints the dashboard title automatically.

run_dashboard() coordinates analysis, printing, and visualization.

Report prints a summary:

Average recovery rate

Average mortality rate

Average growth rate

Uses a lambda function, e.g. fmt_percent = lambda x: f"{x:.2f}%", for consistent percentage formatting.

Data Format (csv_data.csv)
Example columns:

text
City,Confirmed,Recovered,Deaths,Active,PrevConfirmed
Mumbai,1200000,1150000,20000,20000,1180000
Delhi,900000,870000,15000,15000,890000
Pune,600000,570000,9000,21000,590000
Bengaluru,750000,720000,10000,20000,740000
PrevConfirmed is optional; if missing or zero, growth rate is treated as 0.

Possible Extensions
Use pandas for more advanced data manipulation.

Export summary reports to CSV or PDF.

Add a simple GUI (Tkinter / web dashboard).

Fetch live COVID‑19 data from an API instead of a static CSV.

License
Add your preferred license here (e.g. MIT License), or keep “All rights reserved” if you don’t want to open‑source it fully.

Acknowledgements
Python community and official documentation

Matplotlib library for visualization

Public COVID‑19 data sources (or your course dataset)
