from flask import Flask, render_template
import requests

app = Flask(__name__)

#@app.route("/")
#def index(): #pastebin.com/nrzVECZT
  #  fortnite_response = requests.get("https://fortnite-api.com/v2/news")
  #  corona_json = requests.get("https://api.covid19api.com/dayone/country/denmark/status/confirmed").json()
  #  motd_0 = fortnite_response.json() ["data"]["br"]["motds"][0]
  #  return render_template("index.html", motd_0 = motd_0, smittede=smittede(corona_json), smittede_siden_sidst= smittede_siden_sidst(corona_json))

@app.route("/kage")
def kage():
    dmi_requests = requests.get ("https://dmigw.govcloud.dk/v2/metObs/collections/observation/items?api-key=b275cfb6-c81b-41a2-9dd1-847d824a9b20&limit=1&parameterId=temp_dry&stationId=06186")
    data = dmi_requests.json()
    temp_value = data["features"][0]["properties"]["value"]
    return render_template("kage.html", temp = temp_value)





#def smittede(json):
 #   return json[-1]["Cases"]



#def smittede_siden_sidst(json):
 #   return json[-7]["Cases"]


if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0")


# localhost:5000 kge
#a8a72feb95ab4c639a234d9c3e6bd61e