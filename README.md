## COUNTDOWN IN TWITTER DISPLAYNAME
- python 3.8
- docker 20.10
- docker-compose 1.29

## How to use
- clone this repo.
- install python package dependencies using `pip install -r requirements.txt`.
- put your twitter API token credentials in **.env** file.
- define the specified **end_date** countdown in **end_date** parameter of `CountDown` class in the `countdown.py` file.
- run the program with `docker-compose up -d`
- or just run `python3 countdown.py` if you want to run the program without docker