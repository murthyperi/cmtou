from twilio.rest import Client
import os
#16179345923


# Your Account SID from twilio.com/console
# trial account_sid = "AC94c82671c2fcfb1a43cfe8d9ab32aeaa"
# trial auth_token  ="c9bbc529bbab17d32612c6e464844a21" 


account_sid =os.getenv('TWILIO_ACCOUNT_SID')
auth_token=os.getenv('TWILIO_AUTH_TOKEN')
fromNum=os.getenv('FROMNUMBER')
toNum=os.getenv('TONUMBER')


# Your Auth Token from twilio.com/console

def sendTwilioSMS(strMsg):
  client = Client(account_sid, auth_token)

  message = client.messages.create(
      to=toNum, 
      from_=fromNum,
      body=strMsg)

