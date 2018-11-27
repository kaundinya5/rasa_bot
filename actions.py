from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
import requests

class ActionCheckPolicyNumber(Action):
	def name(self):
		return "action_check_status"
	def run(self, dispatcher, tracker, domain):
		Base = automap_base()
		engine = create_engine('postgresql+psycopg2://kaundinya@testdbinstance.cjgud0fxglke.us-east-1.rds.amazonaws.com:5432/insurance_info')
		Base.prepare(engine, reflect=True)
		Insurance = Base.classes.insurances
		session = Session(engine)
		policy_number = tracker.get_slot('policy_number')
		details = session.query(Insurance).filter_by(policy_number=policy_number).first()
		dispatcher.utter_message(f"Your Policy Number is {details.policy_number}")
		dispatcher.utter_message(f"Your Account Name is {details.account_name}")
		dispatcher.utter_message(f"Your Expiration Date is {details.expiration_date}")
		dispatcher.utter_message(f"Your Premium is {details.premium}")
		return []
