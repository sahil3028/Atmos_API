from flask import Flask, render_template
import pandas as pd
app= Flask(__name__)

stations=pd.read_csv("data/stations.txt",skiprows=17)
stations=stations[["STAID","STANAME                                 "]]

@app.route("/")
def home():
    return render_template("home.html",data=stations.to_html())

@app.route("/about/")
def anything_name():
    return render_template("about.html")
@app.route("/api/v1/<s>/<date>")
def temp(s,date):
    filename="data/TG_STAID"+ str(s).zfill(6)+".txt"
    df=pd.read_csv(filename,skiprows=20,parse_dates=["    DATE"])

    row = df.loc[df['    DATE'] == date, '   TG']

    if not row.empty:
        temperature = row.iloc[0] / 10
        return {
            "station": s,
            "temperature": temperature
        }

    else:
        return "No data found"

if __name__=="__main__":
    app.run(debug=True, port=6969)