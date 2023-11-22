from flask import Flask, render_template, request
import stripe

app = Flask(__name__)

# Set your Stripe API key
stripe.api_key = 'your_stripe_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/charge', methods=['POST'])
def charge():
    # Get the payment token submitted by the form
    token = request.form['stripeToken']

    # Create a charge: this will charge the user's card
    try:
        charge = stripe.Charge.create(
            amount=1000,  # amount in cents
            currency='usd',
            description='Example charge',
            source=token,
        )
    except stripe.error.CardError as e:
        # The card has been declined
        return render_template('error.html', error=str(e))

    # Render the success page
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
