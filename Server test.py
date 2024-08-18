from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the home page!"

@app.route('/track', methods=['GET'])
def track():
    source = request.args.get('source')
    campaign = request.args.get('campaign')
    user_id = request.args.get('user_id')
    print(f"Source: {source}, Campaign: {campaign}, User ID: {user_id}")
    return "Thank you for clicking the link!"

if __name__ == '__main__':
    app.run(debug=True)
