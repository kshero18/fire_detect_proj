from twilio.rest import Client

### Find these values at https://twilio.com/user/account
account_sid = "AC59c1a7238efd97b6b15b218e3d79f08f"
auth_token = "a0f0386d29f71030f11e0b7a995d7ad9"

client = Client(account_sid, auth_token)

##client.api.account.messages.create(
##    to="+91-6362101806",
##    from_="+12029294795" ,  #+1 210-762-4855"
##    body="fire Detected" )
