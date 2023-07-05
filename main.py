from socketify import App
from model import Users

from config import Database

db = Database()

database = db.connect()

app = App()

def home(res, req):
    users = Users.select(Users.name).dicts().limit(1000)
    users = [user for user in users]

    res.end(users)

def execute(res, req):
    query = Users.select().dicts().limit(100)
    users = database.execute(query)
    
    users = [user for user in query]

    res.end(users)


app.get('/', execute)
app.get('/home', home)


app.listen(5000)
app.run()