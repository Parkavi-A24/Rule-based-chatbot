from flask import Flask, render_template, request, jsonify

app = Flask(_name_)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def chatbot():
    msg = request.args.get("msg").lower()

    if msg in ["hi", "hello", "hey"]:
        reply = "Hello! How can I help you?"
    elif msg == "how are you":
        reply = "I am fine. Thanks for asking!"
    elif msg == "what is your name":
      reply = "I am CodSoft Chatbot."
    elif msg == "bye":
        reply = "Goodbye! Have a nice day."
    else:
        reply = "Sorry, I don't understand."

    return jsonify(reply)

if _name_ == "_main_":
    app.run(debug=True)
