from flask import Flask, jsonify, request, render_template
import requests
import country_lookup 

app = Flask(__name__)

# Flask route to call the country lookup service
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/health', methods=['GET'])
def health():
    return jsonify(status='ok')

@app.route('/diag', methods=['GET'])
def diag():
    api_url = 'https://www.travel-advisory.info/api'
    response = requests.get(api_url)

    if response.status_code == 200:
        api_status = {"code": 200, "status": "ok"}
    else:
        api_status = {"code": response.status_code, "status": "error"}

    return jsonify(api_status=api_status)

@app.route('/convert', methods=['POST'])
def convert():
    data = country_lookup.load_data_from_api()
    country_name = request.form['country_name']

    if data:
        country_code = country_lookup.lookup_country_name(country_name, data)
        return render_template('result.html',country_code=country_code)
    else:
        return jsonify(error="Data not available. Use '/diag' to check the API status.")


if __name__ == '__main__':
    app.run(port=5001)
    app.run(debug=True)

