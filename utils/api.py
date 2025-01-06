from flask import Flask, jsonify
import utils.sys_stat as ss

app = Flask(__name__)

# API Route
@app.route('/api/sys_stat', methods=['GET'])
def api_system_usage():
    data = ss.GetSysStat()
    return jsonify(data)

# TEST
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)