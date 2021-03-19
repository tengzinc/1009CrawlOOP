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

    def __init__(self, host, user, password, database):
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
        self.__connection()  # call _connection function

    def __connection(self):  # private method
        """
            Create connection between python and mysql
            ----------
        """
        try:
            conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                charset=self.charset
            )
            self._db = conn
            print("\ndatabase connected")
        except Error as err:
            print("error while connecting to database", err)

    def createTable(self):
        """
        Create Table in the database, if table exist it will truncate table to clear data previously
        :return:
        None
        """
        cursor = self._db.cursor()
        sql = "CREATE TABLE crawleddata (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, type VARCHAR(20) COLLATE utf8mb4_unicode_ci NOT NULL,user VARCHAR(100) COLLATE utf8mb4_unicode_ci NOT NULL,"\
              "text VARCHAR(10000) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL NULL,"\
              "likes INT , dates DATETIME , commented INT )"
        try:
            cursor.execute(sql)
            self._db.commit()  # to update database
        except Error as err:
            print("error creating table,", err)
            self.truncatetable()
            print("table truncated")
        cursor.close()

    def disconnect(self):  # _ to make it private
        """
        Disconnect from database
        :return:
        None
        """
        self._db.close()
        print("connection close")

    def insert(self, type, user, text, likes, datecreate, commented):
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
        cursor = self._db.cursor()  # access sql
        val = (type, user, text, likes, datecreate, commented)
        try:
            cursor.execute(
                "INSERT INTO crawleddata (type,user,text,likes,dates,commented) VALUES (%s, %s,%s, %s, %s,%s)", val)
            self._db.commit()  # update database
        except Error as err:
            print("error inserting data into database.", err)
        cursor.close()  # close cursor everytime after use for security purposes

    def search(self, keyword):
        """
        search keyword to find news
        :param keyword: str
        :return:
         result: str
        """
        cursor = self._db.cursor()
        sql = "SELECT * FROM crawleddata WHERE text LIKE \"%"+keyword+"%\""
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
        except Error as err:
            print("error searching for keyword. ", err)
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
            print("error deleteing table", err)
        cursor.close()

    def printnews(self, category):  # print specific news
        """
        Printing news base on social media (reddit or twitter)
        :param category: str
        :return:
        result: str
        """
        cursor = self._db.cursor()
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
        cursor.close()
        return result
