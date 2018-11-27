# rasa_bot
## Steps to run the project
1. Install pip `sudo apt-get install python3-pip`
2. Install venv `pip install virtualenv`
3. Create a virtual env 'virtualenv rasa --python=python3.6'
4. Activate the virual env `source path_to_virtualenv/bin/activate`
4. Install the requirements file `pip install -r requirements.txt`
5. Run the rasa core with `python -m rasa_core.run -d models/dialogue -u models/current/nlu --endpoints endpoints.yml --enable_api --credentials credentials.yml`
6. Run custom actions in another tab with `python -m rasa_core_sdk.endpoint --actions actions`
7. Chat with the bot in the rasa core file. 
