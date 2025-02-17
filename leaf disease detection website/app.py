from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Define chatbot responses for plant diseases
responses = {
    "greeting": [
        "Hello! I'm here to help you with plant diseases. How can I assist you today?",
        "Hi there! Ask me anything about plant diseases.",
        "Greetings! Let's talk about plant health."
    ],
    "goodbye": [
        "Goodbye! Take care of your plants!",
        "Farewell! Feel free to ask more questions later.",
        "See you later! Happy gardening!"
    ],
    "default": [
        "I'm not sure I understand. Could you please rephrase that?",
        "I don't have an answer for that. Can you ask something else?",
        "I'm still learning about plant diseases. Please ask another question."
    ],
    "tomato_blight": [
        "Tomato blight is a common disease caused by fungi. It leads to dark spots on leaves and fruits.",
        "**Solution**: Remove affected plants, avoid overhead watering, and use fungicides. Rotate crops and ensure good air circulation."
    ],
    "powdery_mildew": [
        "Powdery mildew appears as white powdery spots on leaves.",
        "**Solution**: Reduce humidity, improve air circulation, and apply fungicides. Avoid overcrowding plants and water them at the base."
    ],
    "root_rot": [
        "Root rot is caused by overwatering and poor drainage. Symptoms include yellowing leaves and wilting.",
        "**Solution**: Improve soil drainage and avoid overwatering. Remove affected plants and let the soil dry out before replanting."
    ],
    "leaf_spot": [
        "Leaf spot diseases cause dark or brown spots on leaves.",
        "**Solution**: Remove infected leaves and avoid wetting the foliage when watering. Use fungicides and ensure proper spacing between plants."
    ],
    "rust": [
        "Rust appears as orange or brown pustules on leaves.",
        "**Solution**: Remove infected leaves and apply fungicides. Avoid overhead watering and ensure plants are well-spaced."
    ],
    "aphids": [
        "Aphids are small insects that suck sap from plants.",
        "**Solution**: Use insecticidal soap or neem oil. Encourage natural predators like ladybugs to control aphid populations."
    ],
    "wilting": [
        "Wilting can be caused by underwatering, overwatering, or diseases like fusarium wilt.",
        "**Solution**: Check soil moisture and inspect roots for signs of disease. Ensure proper watering practices and remove affected plants."
    ],
    "nutrient_deficiency": [
        "Yellowing leaves can indicate nutrient deficiencies.",
        "**Solution**: Perform a soil test to identify missing nutrients. Fertilize plants with a balanced fertilizer to address deficiencies."
    ],
    "leaf_mold": [
        "Leaf mold is a fungal disease that causes yellow spots on leaves, which later turn brown.",
        "**Solution**: Improve air circulation and avoid overhead watering. Remove infected leaves and apply fungicides."
    ],
    "late_blight": [
        "Late blight is a serious disease that affects tomatoes and potatoes. It causes dark, water-soaked spots on leaves and fruits.",
        "**Solution**: Remove and destroy infected plants immediately. Avoid overhead watering and apply fungicides preventively."
    ],
    "spider_mites": [
        "Spider mites are tiny pests that suck sap from plants, causing yellowing and stippling on leaves.",
        "**Solution**: Use insecticidal soap or neem oil. Increase humidity around plants and regularly spray them with water to deter spider mites."
    ]
}

# Basic chatbot function
def chatbot_response(message):
    message = message.lower()

    if any(word in message for word in ["hello", "hi", "greetings"]):
        return random.choice(responses["greeting"])
    elif any(word in message for word in ["goodbye", "bye", "see you"]):
        return random.choice(responses["goodbye"])
    elif "blight" in message:
        return random.choice(responses["tomato_blight"])
    elif "powdery mildew" in message:
        return random.choice(responses["powdery_mildew"])
    elif "root rot" in message:
        return random.choice(responses["root_rot"])
    elif "leaf spot" in message:
        return random.choice(responses["leaf_spot"])
    elif "rust" in message:
        return random.choice(responses["rust"])
    elif "aphids" in message:
        return random.choice(responses["aphids"])
    elif "wilting" in message:
        return random.choice(responses["wilting"])
    elif "nutrient deficiency" in message or "yellow leaves" in message:
        return random.choice(responses["nutrient_deficiency"])
    elif "leaf mold" in message:
        return random.choice(responses["leaf_mold"])
    elif "late blight" in message:
        return random.choice(responses["late_blight"])
    elif "spider mites" in message:
        return random.choice(responses["spider_mites"])
    else:
        return random.choice(responses["default"])

# Route to serve the frontend
@app.route("/")
def index():
    return render_template("website.html")

# Route to handle chatbot requests
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    bot_response = chatbot_response(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
