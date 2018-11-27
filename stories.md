## happy path 1
* greet
  - utter_greet
* insurance_status
  - utter_policy_search
* policy
  - utter_searched_policy
  - action_check_status
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_goodbye
  - action_restart
  
## happy path 2
* greet
  - utter_greet
* insurance_status+policy
  - utter_searched_policy
  - action_check_status
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_goodbye
  - action_restart

## happy path 3
* greet
  - utter_greet
* insurance_search
  - utter_policy_search
* policy
  - utter_searched_policy
  - action_check_status
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_goodbye
  - action_restart
  
## happy path 4
* greet
  - utter_greet
* insurance_search+policy
  - utter_searched_policy
  - action_check_status
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_goodbye
  - action_restart

