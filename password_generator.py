import  random 
import string
import pandas as pd

def randomString(stringLength=10):
    """Generate  a random string of fixed length """
    letters =string.ascii_lowercase
    res_df=pd.DataFrame(columns=['Password'])
    #685956
    for x in range(7287):
        txtpass=""        
        for  i in range(stringLength):
            txtpass=txtpass + (random.choice(letters)) 
        newrow={'Password':txtpass}
        res_df=res_df.append(newrow, ignore_index=True)    
    return res_df


df_atten=pd.read_csv("datasrc/People.csv")
df_pass=randomString(7)
df_final= df_atten.join(df_pass)
print(df_final.count())
df_final.to_csv('datasrc/People.csv',index=False)
