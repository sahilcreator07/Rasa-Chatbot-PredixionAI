from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from datetime import datetime, timedelta

class ActionAskPayment(Action):
    def name(self):
        return "action_ask_payment"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        payment_ready = tracker.get_slot('payment_ready')
        if payment_ready:
            dispatcher.utter_message(text="Great! You can pay your loan here: [payment link]")
        else:
            dispatcher.utter_message(text="Are you ready to proceed with your loan payment today?")
        return []

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from datetime import datetime, timedelta

class ActionHandleExtensionAndExcuse(Action):
    def name(self):
        return "action_handle_extension_and_excuse"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        reason = tracker.get_slot('reason')
        
        # If the user provided a reason, acknowledge the excuse
        if reason:
            dispatcher.utter_message(text=f"We understand your '{reason}', but timely payments help avoid extra charges and maintain your loan-card score.")
        else:
            dispatcher.utter_message(text="I understand your situation.")
        
        # Extend due date by 10 days
        new_due_date = datetime.now() + timedelta(days=10)
        dispatcher.utter_message(text=f"Your new due date is {new_due_date.strftime('%Y-%m-%d')}. Please make sure to pay by this date.")
        
        return []
