import mysql.connector

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  port='3336',
  password='12345',
  database='jira'
)
try:
   mycursor = mydb.cursor()
   mycursor.execute("select table_name from information_schema.tables where table_schema = 'jira'")
   myresult = mycursor.fetchall()

   list_new = []
   for i in myresult:
       y = str(i).replace(',', '').replace('(','').replace(')','').replace('\'','')
       list_new.append(y)
#print(list_new)


   for i in list_new:
       #print(i)
       query = 'ALTER TABLE'+ ' ' + '`jira`'+ '.' + '`' + i + '`' + ' ' +'CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci'
       #mycursor.execute("ALTER TABLE `votehistory` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
       mycursor.execute(query)
       print(query)

except mysql.connector.Error as err:
  print("Something went wrong: {}".format(err))
