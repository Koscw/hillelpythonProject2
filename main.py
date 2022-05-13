from flask import Flask

app = Flask(__name__)

all_users = [
	{
		'name': 'Ivan',
		'age': 25,
        'email':'superivan@gmail.com',
        'id':132323432322
	},
	{
		'name': 'Oleg',
		'age': 27,
        'email':'superoleg@gmail.com',
        'id':234829348923
	},
	{
		'name': 'Alex',
		'age': 21,
        'email':'superalex@gmail.com',
        'id':348924892483
	},
{
		'name': 'Joshua',
		'age': 18,
        'email':'superjoshua@gmail.com',
        'id':93024902029
	}
]


@app.route('/users')
def id_list_outup():
	id_list = []
	for i in all_users:
		id_list.append([i['id'],i['name'],i['age'],i['email']])
    	return id_list

@app.route("/user/<id>")
def userid(user_id):
    return(next((x for x in all_users if x["id"] == user_id), None))
app.run('localhost',8000)