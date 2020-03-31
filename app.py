from flask import Flask, request, render_template
from twilio.rest import Client
import config

app = Flask(__name__)

@app.route("/")
def home():
  return render_template('home.html')

@app.route('/send_sms', methods=['POST'])
def send_sms():

    if request.method == 'POST':
     #  store form data
      phone_number = request.form['phone']
      message = request.form['message']
     # Create account for api
      account_sid = config.ACCOUNT_SID
      auth_tok = config.AUTH_TOK
     # Create connection to twilio and send message
      client = Client(account_sid, auth_tok)
      message = client.messages \
                     .create(
                         body = f"{message}",
                         from_="+12029522229",
                         to= f"+1{phone_number}"
                     )
      return render_template('message_sent.html')
    return home()
    


if __name__ == "__main__": 
  app.run(debug=True)