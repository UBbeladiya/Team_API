#python -m pip install firebase_admin


import firebase_admin
from firebase_admin import credentials, firestore
import random

def firebase_data(addrress,date,gamename):
    try:
        # initialize Firebase Admin SDK credentials
        path = "/home/utsav23/Team_API/khelmahakumbh-91709-firebase-adminsdk-zcf2z-8cb59227c0.json"
        cred = credentials.Certificate(path)
        firebase_admin.initialize_app(cred)

        # create Firestore client
        db = firestore.client()

        # retrieve teams collection from Firestore
        teams_ref = db.collection('Player')
        teams = teams_ref.stream()

        # create a list of team names
        team_names = [team.to_dict()['p_Name'] for team in teams]

        # randomly shuffle the list of team names
        random.shuffle(team_names)

        # create a schedule list
        schedule = []

        # loop through the shuffled list of team names and generate match schedule
        for i in range(0, len(team_names), 2):
            match = {
                'home_team': team_names[i],
                'away_team': team_names[i+1],
                'date': date, # set a default date for the match
                'addrress': addrress,
                'gamename': gamename
            }
            schedule.append(match)

        # write the match schedule to Firestore
        schedule_ref = db.collection('matches')
        for match in schedule:
            schedule_ref.add(match)

        return True

    except Exception as e :
        
        print(e)
        return False