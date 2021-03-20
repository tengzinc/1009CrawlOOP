import mysql.connector
from mysql.connector import Error

class Database:
    """
    A class used to represent Database
    '''
    Attributes
    ----------
    self._db : Object
        Database connection object to access database
    '''
    :Methods
    _connection():
        private method to set up connection to database.
    createTable():
        Create Table in the database, if table exist it will truncate table to clear data previously
    disconnect():
        Disconnect from database
    insert(type, user, text,likes,datecreate,commented):
        inserting data into MYSQL database
    search(keyword):
        search keyword to look for news
    truncatetable():
         remove item from table that was saved previously
    printnews(category):
        Printing news base on social media (reddit or twitter)
    """

    def __init__(self,host,user,password,database):
        """
         Construct all the necessary attributes for Database and initialize the logins
        :param host: str. server of the database
        :param user: str. username of the database
        :param password: str. password of the database
        :param database: str. Schema of the database
        """
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.charset = "utf8mb4"
<<<<<<< HEAD
        self._connection() #call _connection function

    def _connection(self): #private method
=======
        self.__connection()  # call _connection function

    def __connection(self):  # private method
>>>>>>> 7b7f613bd8be56c2d56d6dd569edab469e88faf7
        """
            Create connection between python and mysql
            ----------
        """
        try:
            conn = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.database,
                charset = self.charset
            )
            self._db = conn
            print("\ndatabase connected")
        except Error as err:
            print("error while connecting to database",err)

<<<<<<< HEAD
    def createTable(self): #not required anymore as the database is inside .sql script
=======
    def createTable(self):
>>>>>>> 7b7f613bd8be56c2d56d6dd569edab469e88faf7
        """
        Create Table in the database, if table exist it will truncate table to clear data previously
        :return:
        None
        """
        cursor = self._db.cursor()
        sql = "CREATE TABLE crawleddata (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, type VARCHAR(20) COLLATE utf8mb4_unicode_ci NOT NULL,user VARCHAR(100) COLLATE utf8mb4_unicode_ci NOT NULL,"\
<<<<<<< HEAD
              "text VARCHA  R(10000) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL NULL,"\
              "likes INT , dates DATETIME , commented INT )"
        #cursor.execute("CREATE TABLE IF NOT EXISTS crawleddata (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, type VARCHAR(20) COLLATE utf8mb4_unicode_ci NOT NULL,user VARCHAR(100) COLLATE utf8mb4_unicode_ci NOT NULL,"
                       #"text VARCHAR(10000) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL NULL,"
                       #"likes INT , dates DATETIME , commented INT )")
=======
              "text VARCHAR(10000) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL NULL,"\
              "likes INT , dates DATETIME , commented INT )"
>>>>>>> 7b7f613bd8be56c2d56d6dd569edab469e88faf7
        try:
            cursor.execute(sql)
            self._db.commit() #to update database
        except Error as err:
            print("error creating table,",err)
            self.truncatetable()
            print("table truncated")
        cursor.close()

<<<<<<< HEAD
    def disconnect(self): # put _ to make it private
=======
    def disconnect(self):  # _ to make it private
>>>>>>> 7b7f613bd8be56c2d56d6dd569edab469e88faf7
        """
        Disconnect from database
        :return:
        None
        """
        self._db.close()
        print("connection close")

<<<<<<< HEAD
    def insert(self, type, user, text,likes,datecreate,commented): # TAKES IN 6 PARAMETER
=======
    def insert(self, type, user, text, likes, datecreate, commented):
>>>>>>> 7b7f613bd8be56c2d56d6dd569edab469e88faf7
        """
        inserting data into MYSQL database
        :param type: str. type of post (reddit or twitter)
        :param user: str. user that created the post
        :param text: str. content of the post
        :param likes: str. the amount of likes for the post
        :param datecreate: str. the date and time of the post that was created
        :param commented: str. number of comments for the post
        :return:
        None
        """
<<<<<<< HEAD
        #enter whatever or grab whatever put inside here to insert
        cursor = self._db.cursor() #access sql
        val = (type, user,text,likes,datecreate,commented)
=======
        cursor = self._db.cursor()  # access sql
        val = (type, user, text, likes, datecreate, commented)
>>>>>>> 7b7f613bd8be56c2d56d6dd569edab469e88faf7
        try:
            cursor.execute("INSERT INTO crawleddata (type,user,text,likes,dates,commented) VALUES (%s, %s,%s, %s, %s,%s)", val)
            self._db.commit() #update database
        except Error as err:
            print("error inserting data into database.",err)
        cursor.close() #close cursor everytime after use for security purposes

    def read(self,limit):
        """
        Read top few data from table using limits
        :param limit: int
        :return:
         result: str
        """
        cursor = self._db.cursor()
        try:
            cursor.execute("SELECT * FROM crawleddata LIMIT "+(str(limit))) #select all from table(comment)
            result = cursor.fetchall()
        except Error as err:
            print("error reading data",err)
        #for x in result:
         #  print(x)
        cursor.close()
        return result

    def search(self,keyword):
        """
        search keyword to find news
        :param keyword: str
        :return:
         result: str
        """
        cursor = self._db.cursor()
        sql = "SELECT * FROM crawleddata WHERE text LIKE \"%"+keyword+"%\""
<<<<<<< HEAD
        #ALTER TABLE crawleddata ADD FULLTEXT (text);
        #sql =  "SELECT * FROM crawleddata WHERE MATCH(text) AGAINST ('" +keyword +"')"
=======
>>>>>>> 7b7f613bd8be56c2d56d6dd569edab469e88faf7
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
        except Error as err:
<<<<<<< HEAD
            print("error searching for keyword. ",err)
        result = cursor.fetchall()
        #for result in x:
         #   print(result) #print result here
=======
            print("error searching for keyword. ", err)
>>>>>>> 7b7f613bd8be56c2d56d6dd569edab469e88faf7
        cursor.close()
        return result

    def truncatetable(self):
        """
        to remove item from table(crawleddata) that was saved previously
        :return:
        None
        """
        cursor = self._db.cursor()
        try:
            # THIS IS TO REMOVE ITEM FROM THE TABLE SAVED PREVIOUSLY
            cursor.execute("TRUNCATE TABLE crawleddata")
        except Error as err:
<<<<<<< HEAD
            print("error deleteing table",err)
        # updating code here
=======
            print("error deleteing table", err)
>>>>>>> 7b7f613bd8be56c2d56d6dd569edab469e88faf7
        cursor.close()

    def printnews(self,category): #print specific news
        """
        Printing news base on social media (reddit or twitter)
        :param category: str
        :return:
        result: str
        """
        cursor = self._db.cursor()
<<<<<<< HEAD
        if(category == "twitter"):
            type = "tweet"
        elif(category == "reddit"):
            type = "post"
        else:
            print("type only twitter or reddit")
            exit()
        sql = "SELECT * FROM crawleddata WHERE type = '"+type+"'"
        try:
            cursor.execute(sql)   # select all from table(comment)
        except Error as err:
            print("error printing news",err)
        result = cursor.fetchall()
        #for x in result:
         #   print(x)
=======
        if(category.lower() == "twitter"):
            type = "tweet"
        elif(category.lower() == "reddit"):
            type = "post"
        else:
            print("no such news, type only twitter or reddit")
            type = category
        try:
            sql = "SELECT * FROM crawleddata WHERE type = '" + type + "'"
            cursor.execute(sql)   # select all from table(comment)
            result = cursor.fetchall()
        except Error as err:
            print("error printing news", err)
            result = None
>>>>>>> 7b7f613bd8be56c2d56d6dd569edab469e88faf7
        cursor.close()
        return result
