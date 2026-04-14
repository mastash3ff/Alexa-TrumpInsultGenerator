from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response

from generator import generateInsult

sb = SkillBuilder()


class LaunchRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input: HandlerInput) -> bool:
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input: HandlerInput) -> Response:
        speech = (
            "Welcome to Trump Insult Generator. "
            "You can generate an insult from Donald Trump's quotes by saying insult first name. "
            "Let's get started."
        )
        reprompt = (
            "You can generate an insult from Donald Trump's quotes by saying insult first name."
        )
        return (
            handler_input.response_builder
            .speak(speech)
            .ask(reprompt)
            .response
        )


class GetNewTrumpInsultHandler(AbstractRequestHandler):
    def can_handle(self, handler_input: HandlerInput) -> bool:
        return is_intent_name("GetNewTrumpInsult")(handler_input)

    def handle(self, handler_input: HandlerInput) -> Response:
        slots = handler_input.request_envelope.request.intent.slots
        firstname_slot = slots.get("firstname") if slots else None
        firstname = (
            firstname_slot.value
            if firstname_slot and firstname_slot.value
            else None
        )

        if not firstname:
            speech = "I could not find a name to insult."
            return (
                handler_input.response_builder
                .speak(speech)
                .set_should_end_session(True)
                .response
            )

        insult = generateInsult(firstname)
        return (
            handler_input.response_builder
            .speak(insult)
            .set_should_end_session(True)
            .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input: HandlerInput) -> bool:
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input: HandlerInput) -> Response:
        speech = (
            "You can generate a Trump insult by saying insult first name. "
            "Example: Insult Ronnie."
        )
        return (
            handler_input.response_builder
            .speak(speech)
            .ask(speech)
            .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input: HandlerInput) -> bool:
        return (
            is_intent_name("AMAZON.CancelIntent")(handler_input)
            or is_intent_name("AMAZON.StopIntent")(handler_input)
        )

    def handle(self, handler_input: HandlerInput) -> Response:
        return (
            handler_input.response_builder
            .speak("Goodbye!")
            .set_should_end_session(True)
            .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input: HandlerInput) -> bool:
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input: HandlerInput) -> Response:
        return handler_input.response_builder.response


sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(GetNewTrumpInsultHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())

lambda_handler = sb.lambda_handler()
