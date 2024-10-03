# Bike Sharing Dashboard 
This dashboard displays bike sharing data analysis, including rental trends by weekday, weekend, holiday, and casual versus registered users. The dashboard was created using Streamlit and visualizes the analysis data.

## Installation
To set up and run the dashboard locally, follow these steps:

1. Clone this repository to your local machine:
```
git clone https://github.com/EkaPutra0856/Belajar_Analisis_Data.git
```
2. Navigate to the project directory:
```
cd ./to/path/Belajar_Analisis_Data
```
3. Install the required packages listed in the requirements.txt file:
```
pip install -r requirements.txt
```
4. Run the dashboard using Streamlit:
```
streamlit run ./dashboard/dashboard.py
```
5. Access the dashboard using web browser at:
```
http://localhost:8501
```

## Directory Structure
```
submission/
├── dashboard/
│   └── dashboard.py  
│   └── clean_day.py 
│   └── clean_hour.py 
├── data/
│   ├── day.csv        
│   └── hour.csv       
├── README.md                
├── requirements.txt        
└── notebook.ipynb   
└── url.txt
```

## Requirements
Ensure you have Python 3.x installed, with this libraries:

- pandas
- seaborn
- streamlit
- matplotlib
- numpy
- babel

All dependencies are listed in the requirements.txt file and can be installed using the command mentioned above.

