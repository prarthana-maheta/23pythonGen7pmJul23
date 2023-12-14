# import sqlite3
#
# sqliteConnection = sqlite3.connect('local.db')
# cursor = sqliteConnection.cursor()
#
# print(sqliteConnection)
# print(cursor)
#
# # cursor.execute( """ CREATE TABLE IF NOT EXISTS projects (
# #                                     id integer PRIMARY KEY,
# #                                     name text NOT NULL,
# #                                     begin_date text,
# #                                     end_date text
# #                                 ); """)
# #
# # cursor.execute("""CREATE TABLE IF NOT EXISTS tasks (
# #                                 id integer PRIMARY KEY,
# #                                 name text NOT NULL,
# #                                 priority integer,
# #                                 status_id integer NOT NULL,
# #                                 project_id integer NOT NULL,
# #                                 begin_date text NOT NULL,
# #                                 end_date text NOT NULL,
# #                                 FOREIGN KEY (project_id) REFERENCES projects (id)
# #                             );""")
#
# cursor.execute("""
#                                             INSERT INTO student (name, standard)
#                                             VALUES (?, ?)
#                                             ON CONFLICT (name)
#                                             DO UPDATE SET
#                                                 name = EXCLUDED.name,
#                                                 standard = EXCLUDED.standard,
#                                    (var_name,var_standard);""")
#
# sqliteConnection.commit()
#
# # sqliteConnection.close()
#
#
# cursor.execute(
#     "SELECT * FROM example")
# keywords = cursor.fetchall()


#
#
#
#
#
# cursor.execute("""
#                                             INSERT INTO presearch (keyword, top_add_link,max_stake,stakes,json_data)
#                                             VALUES (?, ?,?,?,?)
#                                             ON CONFLICT (keyword)
#                                             DO UPDATE SET
#                                                 keyword = EXCLUDED.keyword,
#                                                 top_add_link = EXCLUDED.top_add_link,
#                                                 max_stake = EXCLUDED.max_stake,
#                                                 stakes = EXCLUDED.stakes,
#                                                 json_data = EXCLUDED.json_data """,
#                                    (key_data['keyword'],
#                                     top_add_link,
#                                     max_stake,
#                                     stakes, json.dumps(key_data)))
#
#                     sqliteConnection.commit()
#
# update_query = """
#                             UPDATE keywords
#                             SET is_processed = TRUE
#                             WHERE keyword = ?
#                         """
#
#                     cursor.execute(update_query, (key_data['keyword'],))
#                     sqliteConnection.commit()

import requests

response = requests.get("https://dev.to/dendihandian/installing-sqlite3-in-windows-44eb",)
print(response)
breakpoint()
