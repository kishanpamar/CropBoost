from flask import Flask, jsonify, render_template, request, send_from_directory
import csv, json, os

app = Flask(__name__, static_url_path='/static', static_folder='static', template_folder='templates')
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
I18N_DIR = os.path.join(os.path.dirname(__file__), "static", "i18n")

def read_mandi():
    out = []
    with open(os.path.join(DATA_DIR, "mandi_prices.csv"), encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            for k in ["min","max","modal"]:
                row[k] = float(row[k])
            out.append(row)
    return out

def read_json(name):
    with open(os.path.join(DATA_DIR, name), encoding="utf-8") as f:
        return json.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/i18n")
def i18n():
    lang = request.args.get("lang","en")
    path = os.path.join(I18N_DIR, f"{lang}.json")
    if not os.path.exists(path):
        path = os.path.join(I18N_DIR, "en.json")
    with open(path, encoding="utf-8") as f:
        return jsonify(json.load(f))

@app.route("/api/mandi")
def api_mandi():
    data = read_mandi()
    state = request.args.get("state")
    commodity = request.args.get("commodity")
    market = request.args.get("market")
    if state: data = [d for d in data if d["state"].lower()==state.lower()]
    if commodity: data = [d for d in data if d["commodity"].lower()==commodity.lower()]
    if market: data = [d for d in data if d["market"].lower()==market.lower()]
    data.sort(key=lambda x: (x["date"], x["modal"]), reverse=True)
    return jsonify(data)

@app.route("/api/weather")
def api_weather():
    city = request.args.get("city", "Rajkot")
    weather = read_json("weather.json")
    return jsonify(weather.get(city, []))

@app.route("/api/schemes")
def api_schemes():
    return jsonify(read_json("schemes.json"))

@app.route("/api/trainings")
def api_trainings():
    return jsonify(read_json("trainings.json"))

@app.route("/api/kvk")
def api_kvk():
    state = request.args.get("state")
    data = read_json("kvk.json")
    if state:
        data = [d for d in data if d["state"].lower()==state.lower()]
    return jsonify(data)

@app.route("/api/crop-guides")
def api_guides():
    crop = request.args.get("crop")
    data = read_json("crop_guides.json")
    if crop:
        data = [d for d in data if d["crop"].lower()==crop.lower()]
    return jsonify(data)

@app.route("/api/calendar")
def api_calendar():
    return jsonify(read_json("crop_calendar.json"))

@app.route("/api/knowledge")
def api_knowledge():
    return jsonify(read_json("farming_knowledge.json"))

@app.route("/manifest.json")
def manifest():
    return send_from_directory("static", "manifest.json")

@app.route("/sw.js")
def sw():
    return send_from_directory("static", "sw.js")

@app.route("/health")
def health():
    return jsonify({"status":"ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)
