import os
import sqlite3
from datetime import datetime as dt

class Database():

	def __init__(self, db_path):
		self.db_path = db_path

		if not os.path.exists(self.db_path):
			self.create()

	def create(self):
		with sqlite3.connect(self.db_path) as con:
			cur = con.cursor()
			cur.execute('''CREATE TABLE IF NOT EXISTS Chats ( 
					             id integer PRIMARY KEY, 
					             first_name text, 
					             last_name text, 
					             username text, 
					             date_added text, 
					             assign_schedule integer, 
					             date_assigned_schedule text
					        ) WITHOUT ROWID''')
			con.commit()

	def add_chat(self, newchat):
		today = dt.now().strftime('%Y-%m-%d')
		with sqlite3.connect(self.db_path) as con:
			cur = con.cursor()
			cur.execute('INSERT OR IGNORE INTO Chats(id, first_name, last_name, username, date_added) VALUES(?,?,?,?,?)',
				        (newchat.id, newchat.first_name, newchat.last_name, newchat.username, today))
			con.commit()

	def update_assign_shedule(self, chat_id):
		today = dt.now().strftime('%Y-%m-%d')
		with sqlite3.connect(self.db_path) as con:
			cur = con.cursor()
			cur.execute('UPDATE Chats SET assign_schedule=1, date_assigned_schedule=? WHERE id=?', (today, chat_id))
			con.commit()

	def get_chats_for_schedule(self):
		today = dt.now().strftime('%Y-%m-%d')
		columns = ['id','first_name','last_name','username']
		with sqlite3.connect(self.db_path) as con:
			cur = con.cursor()
			cur.execute('SELECT id, first_name, last_name, username from Chats WHERE assign_schedule=1')
			chats = cur.fetchall()

			return [dict(zip(columns, chat)) for chat in chats]