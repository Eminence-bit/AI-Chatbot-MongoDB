from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb+srv://prajyothnani123:prajyothnani123@mydatabase.ndjzos2.mongodb.net/")  # Replace with your connection string if needed
db = client["Client"]
conversations = db["conversations"]

# Predefined responses
responses = {
    "hello": "Hi there! How can I assist you?",
    "how are you": "I'm just a program, but I'm functioning as expected!",
    "bye": "Goodbye! Have a great day!",
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.json.get("message", "").lower()
    response = responses.get(user_message, "I'm not sure how to respond to that.")
    
    # Save conversation to MongoDB
    conversations.insert_one({"user_message": user_message, "bot_response": response})
    
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
