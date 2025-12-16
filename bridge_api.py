from flask import Flask, jsonify, request
from omnibus import OmnibusEngine
import threading

app = Flask(__name__)
engine = None

@app.route('/swarm/start', methods=['POST'])
def start_swarm():
    global engine
    target = request.json.get('target')
    engine = OmnibusEngine(target)
    # Run in thread so the web UI doesn't freeze
    threading.Thread(target=engine.engage).start()
    return jsonify({"status": "Swarm Initiated", "target": target})

@app.route('/swarm/status', methods=['GET'])
def get_status():
    if not engine: return jsonify({"kills": []})
    return jsonify({
        "kills": engine.nexus.knowledge['confirmed_vulns'],
        "tech": list(engine.nexus.knowledge['technologies'])
    })

if __name__ == '__main__':
    app.run(port=5000)
