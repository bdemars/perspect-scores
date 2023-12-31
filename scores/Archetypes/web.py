import os
from flask import Flask, jsonify, request
from web_app import predict_archetype

app = Flask(__name__)

@app.route("/archetype-api/health", methods=["GET"])
def health_check():
    return jsonify({"msg": "GH Archetypes API"})

@app.route("/archetype-api/calculate", methods=["GET"])
def get_design_patterns():
    args = request.args
    github_repo = args['github_repo']
    dev_key = args.get('gh_key', '')
    print(args)
    return predict_archetype(dev_key, github_repo)

if __name__ == "__main__":
    debug = os.environ.get("DEBUG", False)
    port = os.environ.get("PORT", 5050)
    app.run(host="0.0.0.0", port=port, debug=debug)