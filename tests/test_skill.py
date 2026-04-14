"""Tests for Unofficial Trump Insult Generator Alexa skill."""
from unittest.mock import MagicMock
import pytest
from ask_sdk_model import LaunchRequest, IntentRequest, Intent, Slot

import lambda_function as lf


def make_hi(request, session_attrs=None):
    hi = MagicMock()
    hi.request_envelope.request = request
    hi.attributes_manager.session_attributes = {} if session_attrs is None else dict(session_attrs)
    rb = MagicMock()
    for m in ("speak", "ask", "set_card", "set_should_end_session"):
        getattr(rb, m).return_value = rb
    hi.response_builder = rb
    return hi


def make_intent(name, slots=None):
    slot_objs = {k: Slot(name=k, value=str(v)) for k, v in (slots or {}).items()}
    return IntentRequest(intent=Intent(name=name, slots=slot_objs))


class TestLaunchRequest:
    def test_can_handle(self):
        assert lf.LaunchRequestHandler().can_handle(make_hi(LaunchRequest()))

    def test_speaks_welcome(self):
        hi = make_hi(LaunchRequest())
        lf.LaunchRequestHandler().handle(hi)
        speech = hi.response_builder.speak.call_args[0][0]
        assert "Trump Insult Generator" in speech

    def test_keeps_session_open(self):
        hi = make_hi(LaunchRequest())
        lf.LaunchRequestHandler().handle(hi)
        hi.response_builder.ask.assert_called_once()
        hi.response_builder.set_should_end_session.assert_not_called()


class TestGetNewTrumpInsultIntent:
    def test_can_handle(self):
        assert lf.GetNewTrumpInsultHandler().can_handle(
            make_hi(make_intent("GetNewTrumpInsult"))
        )

    def test_cannot_handle_wrong_intent(self):
        assert not lf.GetNewTrumpInsultHandler().can_handle(
            make_hi(make_intent("OtherIntent"))
        )

    def test_generates_insult_with_name(self):
        hi = make_hi(make_intent("GetNewTrumpInsult", slots={"firstname": "Brandon"}))
        lf.GetNewTrumpInsultHandler().handle(hi)
        speech = hi.response_builder.speak.call_args[0][0]
        assert len(speech) > 0
        assert speech != "I could not find a name to insult."

    def test_insult_contains_first_name(self):
        hi = make_hi(make_intent("GetNewTrumpInsult", slots={"firstname": "Brandon"}))
        lf.GetNewTrumpInsultHandler().handle(hi)
        speech = hi.response_builder.speak.call_args[0][0]
        assert "Brandon" in speech

    def test_no_name_returns_error(self):
        hi = make_hi(make_intent("GetNewTrumpInsult"))
        lf.GetNewTrumpInsultHandler().handle(hi)
        speech = hi.response_builder.speak.call_args[0][0]
        assert "could not find a name" in speech.lower()

    def test_ends_session(self):
        hi = make_hi(make_intent("GetNewTrumpInsult", slots={"firstname": "Brandon"}))
        lf.GetNewTrumpInsultHandler().handle(hi)
        hi.response_builder.set_should_end_session.assert_called_once_with(True)


class TestHelpIntent:
    def test_can_handle(self):
        assert lf.HelpIntentHandler().can_handle(make_hi(make_intent("AMAZON.HelpIntent")))

    def test_keeps_session_open(self):
        hi = make_hi(make_intent("AMAZON.HelpIntent"))
        lf.HelpIntentHandler().handle(hi)
        hi.response_builder.ask.assert_called_once()
        hi.response_builder.set_should_end_session.assert_not_called()


class TestCancelStopIntent:
    @pytest.mark.parametrize("name", ["AMAZON.CancelIntent", "AMAZON.StopIntent"])
    def test_can_handle(self, name):
        assert lf.CancelOrStopIntentHandler().can_handle(make_hi(make_intent(name)))

    def test_says_goodbye(self):
        hi = make_hi(make_intent("AMAZON.StopIntent"))
        lf.CancelOrStopIntentHandler().handle(hi)
        assert "Goodbye" in hi.response_builder.speak.call_args[0][0]
