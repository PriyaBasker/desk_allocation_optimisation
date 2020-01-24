import src.helper.request as r
import pandas as pd

header = {'User-Agent': 'AverageLengthofSongs/0.0.1 (priya.basker@gmail.com)'}


def validate_login(name,password):	
	"""
    	Validates the username and password
    Parameters: 
		name: user name  of the user 
		password : password of the user
    Returns: 
    	boolen : valid or not """
	
	#Read the attendance excelsheet check if username and password matched
	df_atten=pd.read_csv("datasrc/People.csv")
	# 10006 ultbjxu
	
	if (df_atten.Username.astype(str).str.contains(name).any() and df_atten.Password.astype(str).str.contains(password).any()):		
		return True
	else: 
		return False 
	
def get_user_details_id(id):
	"""
     Get userdetails by id 
    Parameters: 
		id_tag: id of the user
		limit : number of titles to select
    Returns: 
        df : dataframe with user details """
	
	people=pd.read_csv("datasrc/People.csv")
	
	df_user=people[people['Username']==int(id)]
	df_user=df_user[['Username','Team','Age_Range','Gender','Grade','Travel_Time','Special_Feature']]
	print(df_user)
	return df_user





