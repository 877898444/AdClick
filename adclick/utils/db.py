from db import DB
from db import list_profiles,remove_profile

#Connecting to a Database
db = DB(username="root", password="root", hostname="localhost",
            dbtype="mysql")


#Saving a profile
#db.save_credentials()
db.save_credentials(profile="local_pg")

#Connecting from a profile
db = DB()
db = DB(profile="local_pg")


list_profiles()
remove_profile('demo')

#Executing Queries
df1 = db.query("select * from Artist;")

#Find Database
results = db.find_table("A*")
db.find_column("*Address*")

