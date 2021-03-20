from nltk.sentiment.vader import SentimentIntensityAnalyzer

class socialMedia:
    """
    A class to represent social media
    ...
    Attributes
    ----------
    socialMedia : Object
            Create object for different social media. Object has database type, sentiment score and crime score 
            
    Methods
    -------
    getCrimeScore():
        returns dictionary: Key = Crime type, Value = Crime Count)
    getSentimentScore():
        returns double: Score of social media's overall sentiment(range -1 to 1)
    getSentiment():
        returns str: Category of social media's sentiment based on sentiment score    
    """

    def __init__(self,database,socialMediaType):
        """
        Constructs all the necessary attributes for the social media:
            Generates Object Crime score
            Generates Object platform sentiment score


        Parameters
        ----------
            database: object
                database object containing social media
            socialMediaType: str
                "reddit"= database containing reddit, "twitter" = database containing twitter
        """
        self.__database= database                   
        self.__socialMediaType = socialMediaType
        self.__overallSentiment = 0
        self.__crimeScore= {"scam": 0,"drug": 0,"violence": 0, "sexOffence": 0}
        self.__generateCrimeScore()
        self.__readSentiment()
        

    def getCrimeScore(self):
        """
        Gets crime score for the social media

        Parameters
        ----------
        None

        Returns
        -------
            Dictionary : key = crime type, value = crime count
        """
        return self.__crimeScore

    def getSentimentScore(self):
        """
        get social media's sentiment score

        Parameters
        ----------
            None

        Returns
        -------
            double: social media's sentiment score
        """
        return self.__overallSentiment
    
    def getSentiment(self):
        """
        get social media's sentiment type

        Parameters
        ----------
            None

        Returns
        -------
            String: social media's sentiment Type
        """
        return self.__categorizeSentiment()

    def __generateCrimeScore(self):
        """
        1)Reads social media comments from database
        2)Categorize social media's comments into categories and count of crime word occurences

        Parameters
        ----------
            None

        Returns
        -------
            None 
        """
        scam = {"cheat", "cheating", "cheated","scam","scammed", 
        "scamming", "deceive","deceived","decieving","extort","extorted",
        "extortion","impersonate","imporsonation","impersonating","embezzle",
        "embezzled","embezzeling","embezze","embezzlement","bribe","bribed",
        "bribery","forge","forged","forgery"}
        drug = {"drug","drugs","smuggle","cannibis","marijuana",
        "cocaine","heroin","overdose","smuggle","narcotics","bullet","bullets",
        "trafficking"}
        violence= {"abuse","abused","abusing","attack","attacked"
        ,"attacking","attacker","assault","assaulted","assaulting","stabed",
        "stabbing","murder","murdered","kill","killed","torture",
        "torturing","tortured","man slaugter","weapon","weapons",
        "knife","sword","gun","firearm","gang","gangster"}
        sexOffence = {"rape","raped","raping","molest","molested",
        "molesting","molester","sexual","paedophile","upskirt"}
        
        #wordDict= {"scam": 0,"drug": 0,"violence": 0, "sexOffence": 0}

        for x in self.__database.printnews(self.__socialMediaType):
            words= str(x[3]).lower().split()
            for word in words:
                if word in scam:
                    self.__crimeScore["scam"]+=1                
                if word in drug:
                    self.__crimeScore["drug"]+=1  
                if word in violence:
                    self.__crimeScore["violence"]+=1
                if word in sexOffence:
                    self.__crimeScore["sexOffence"]+=1

    def __analyzeSentiment(self,text):
        """
        Takes in string and calculates sentiment score: -1(negative) to 1(postitive)
        Parameters
        ----------
            text : str
                text to generate sentiment score from

        Returns
        -------
            score : double
                score for the text's sentiment
        """
        score= SentimentIntensityAnalyzer().polarity_scores(text)
        return score['compound']

    def __readSentiment(self):
        """
        Read all comments from social media from database, 
        generate total sentiment score from all the comments and 
        update social media's object total Sentiment score

        Parameters
        ----------
            None

        Returns
        -------
            None
        """
        rowCount= 0
        for x in self.__database.printnews(self.__socialMediaType):
            self.__overallSentiment+=self.__analyzeSentiment(x[3])
            rowCount+=1
        if rowCount!=0:
            self.__overallSentiment=self.__overallSentiment/rowCount    

    def __categorizeSentiment(self):
        """
        Get object's sentiment score, categorize and return the type of sentiment 

        Parameters
        ----------
            None

        Returns
        -------
            sentimentCategory : str
                returns the type of sentiment of the object
        """
        score = self.__overallSentiment
        if score < -0.4:
            return "Worst"
        elif score < -0.3:
            return "Very Bad"
        elif score < -0.1:
            return "Bad"
        elif score < 0.1:
            return "Neutral"
        elif score < 0.3:
            return "Good"
        elif score < 0.4:
            return "Very Good"
        else:
            return "Best"
 