# Weather Report

### A Command-Line Weather Report Tool

Enter a valid zipcode and get:

* Current weather

* Sunrise and sunset times

* 10-day forecast

* Any weather alerts for your area

* Any hurricanes known to the Weather Underground


### System Requirements

* You will need to have **Python&nbsp;3** installed on your machine or have access to a Python&nbsp;3 interpreter. See [Python's site](https://www.python.org/) for details.

* Copy this repo to your computer.

* You will need to make sure that you have a virtual environment running Python&nbsp;3 in the folder that you made in the above step. [See this site for details if you're not familiar.](http://docs.python-guide.org/en/latest/dev/virtualenvs/) **Complete this step before attempting the below.**

* Using your favorite command line program (e.g., Terminal on Mac&nbsp;OS&nbsp;X), install the requirements file in your virtual environment: `pip install -r requirements.txt`.

* **This program requires a Weather Underground API Key**, so you will need to (1) [sign up for the website](http://www.wunderground.com/weather/api) and (2) sign up for a key.

* Save your Weather Underground key as a variable in your local environment by adding the following line to the `.envrc` file in this repo's directory on your computer: `export WU_KEY=whatever-your-real-key-is`

* **TO RUN THE PROGRAM** run `python3 weather.py` on the command line.
