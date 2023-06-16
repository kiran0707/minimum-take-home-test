# minimum-take-home-test

Basic UI in flask and data manipulation in pandas.


## Setup

It is recommended to run python in a virtual environment. Spin up virtual environment then run the following commands

Install requirements from requirements.txt
```
pip install -r requirements.txt
```

## How to use this app

Run the flask app
```
python app.py
```

Flask app will run at localhost, port 5000 
This app takes 2 csv input,
1. emission factor
2. activity data

Then, click Upload

There are few options to see the final data
1. See the merged data, here you need to give the lookup field, example "Spend"
2. See the merged data with grouped data, here you need to give the lookup field and group by field , example "Spend" and "Lookup identifiers"
3. See the merged data, sorted by a field, here you need to give the lookup field and sort by field, example "Spend" and "co2e value"
4. See the merged data, filterd by a field and field value. here you need to give look up field, filter by field and filter value, example "Spend", "Lookup identifiers" and "Real estate activities"


