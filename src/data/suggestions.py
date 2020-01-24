import pandas as pd

 

def load_data():

    People = pd.read_csv("datasrc/People.csv")
    People = People.where((pd.notnull(People)), None)
    Attendance = pd.read_csv("datasrc/Attendance.csv")
    Desks = pd.read_csv("datasrc/Desks.csv")
    return People, Attendance, Desks

 

def suggest_seat( user: int,Todays_Date:str) -> str:
    """
    Suggest a seat for an employee.
    Args:
        user (int): Employee number
    Returns:
        seat (str): Suggested seat range
        caveats (str): Does this seat exactly fit requirements?
    """
   

    People, Attendance, Desks = load_data()   
    Special_Feature = People.loc[People["Username"] == user, "Special_Feature"].values[-1]
    Employee_Team = People.loc[People["Username"] == user, "Team"].values[-1]

    

    # Ideally the Attendance data would be realtime
    Todays_Attendance = Attendance[Attendance["Date"] == Todays_Date]

    # Ratio of occupancy/desks to assess if a seat is available:
    Team_Capacity = Todays_Attendance["Team"].value_counts() / Desks["Team"].value_counts()   
    Available_Desks_By_Team = (Desks["Team"].value_counts()) - Attendance.loc[Attendance["Date"]==Todays_Date ,"Team"].value_counts().sort_values(ascending=False)
    Available_Desks_By_Team = Available_Desks_By_Team.where((pd.notnull(Available_Desks_By_Team)), 0).map(int)
   

    # Less than 1 means a seat is available
    if Team_Capacity[Employee_Team] < 1:    
        # So sit on your team's allocated desks

        if Special_Feature is None:
            Team_Seats = Desks.loc[Desks["Team"] == Employee_Team, "Desk"]
            return {

                "Team" : Employee_Team,
                "Feature" : None,
                "Seats" : Team_Seats.tolist(),
                "DesksAvailable" : Available_Desks_By_Team[Employee_Team],
                "FirstChoice" : True
            }
       

        # If you need a special feature sit on a particular desk

        if Special_Feature is not None:
            Team_Seats = Desks.loc[Desks["Team"] == Employee_Team]
            Feature_Seats = Team_Seats.loc[Team_Seats["Special Requirements"] == Special_Feature, "Desk"]
            return {

                "Team" : Employee_Team,
                "Feature" : Special_Feature,
                "Seats" : Feature_Seats.tolist(),
                "DesksAvailable" : Available_Desks_By_Team[Employee_Team],
                "FirstChoice" : True,

            }
 

    # More than 1 means a seat isn't available

    if Available_Desks_By_Team[Employee_Team] > 1: 
        # Suggest they sit with a low occupancy team
        if Special_Feature is None:

            Surrogate_Team = Team_Capacity.sort_values().index[2]
            Team_Seats = Desks.loc[Desks["Team"] == Surrogate_Team, "Desk"]
            return {

                "Team" : Surrogate_Team,
                "Feature" : None,
                "Seats" : Team_Seats.tolist(),
                "DesksAvailable" : Available_Desks_By_Team[Employee_Team],
                "FirstChoice" : False

            }