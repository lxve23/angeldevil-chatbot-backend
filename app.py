from flask import Flask, request, jsonify
from flask_cors import CORS
from chat import newMessage

app = Flask(__name__)
CORS(app, origins=["https://lxve23.github.io/"])

@app.route("/chat", methods=["POST"])
def gpt_call():  
    data = request.get_data(as_text=True)
    ai_response = newMessage(data)

    try:
        angel_response, devil_response = ai_response.split("--SPLIT--", 1)
    except ValueError:
        return jsonify({"error": "Error while responding"})
    
    response = {
        "angel": angel_response.strip(),
        "devil": devil_response.strip()
    }
    return jsonify(response)


if __name__ == "__main__":
    app.run()
