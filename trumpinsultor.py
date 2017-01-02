from ask import alexa
from generator import generateInsult

@alexa.default
def lambda_handler(request, context=None):
    """ The default handler gets invoked if no handler is set for a request type """
    return alexa.route_request(request)

@alexa.request("LaunchRequest")
def launch_request_handler(request):
    welcome = "Welcome to Trump Insult Generator.  You can generate an insult from Donald Trump's quotes by saying insult first name.  Lets get started."
    return alexa.create_response(message=welcome,reprompt_message='You can generate an insult from Donald Trumps quotes by saying insult first name',end_session=True)

@alexa.intent('AMAZON.StopIntent')
def stop_intent_handler(request):
    return alexa.create_response(message="Goodbye!")

@alexa.request("SessionEndedRequest")
def session_ended_request_handler(request):
    return alexa.create_response(message="Goodbye!",end_session=True)

@alexa.intent('GetNewTrumpInsult')
def get_new_trump_insult(request):
    firstname = request.slots["firstname"]
    if firstname is None:
        card = alexa.create_card(title="GetNewTrumpInsult",subtitle=None,content="Could not find a name to insult.")
        return alexa.create_response("I could not find a name to insult.",end_session=True)
    insult = generateInsult(firstname)
    card = alexa.create_card(title="GetNewTrumpInsult", subtitle=None,content="asked alexa to get a new Trump insult")
    return alexa.create_response(insult,end_session=Trust,card_obj=card)

@alexa.intent('AMAZON.HelpIntent')
def help_intent_handler(request):
    msg = "You can generate a Trump insult by saying insult first name.  Example:  Insult Ronnie."
    return alexa.create_response(msg,end_session=True)

