# :snake:Python:snake: wifi Sniffer for Windows
In this sample we are using GCP Geoloc API to locate our self computer.
 
## Recomendations before start: 

We strongly recomment to use Virtual environments to avoid incompatibility issues betwen dependencies.

1) Install virtual enviroments with: 

      `pip install virtualenv`
  
2) Create your own virtual environment: 
  
      `virtualenv .pyenv`

3) Activate your environment (on **Windows**):

      `.pyenv\Scripts\activate`
  
## To use this sniffer:

1) Install dependencies:

      `pip install -r requirements.txt`

2) Set your API key on a .env file:

      `echo GEOLOC_KEY=USE_YOUR_OWN_KEY> .env`

3) Run the main.py file:

      `python main.py`


4) :warning: **For some reason, winwifi needs to be runned at least once to properly work** :warning: The following command needs to be runned on every new terminal:
      
      `wifi scan`
      
5) run the main.py file:

      `python main.py`


6) Enjoy
