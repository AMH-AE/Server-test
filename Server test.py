from flask import Flask, request

app = Flask(__name__)

@app.route('/track', methods=['GET'])
def track():
    # Collect tracking parameters from the URL
    source = request.args.get('source')
    campaign = request.args.get('campaign')
    user_id = request.args.get('user_id')

    # Log or process the data
    print(f"Source: {source}, Campaign: {campaign}, User ID: {user_id}")

    # Respond to the request
    return "Thank you for clicking the link!"

if __name__ == '__main__':
    app.run(debug=True)
