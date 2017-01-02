import json, random

#parse trump quotes from json file
with open('trump.json') as trump_file:
	quotes = json.load(trump_file)

#insult structure layout
templates = [
        ["subjectnametwice1", "user_name",  "subjectnametwice2", "user_name",  "predicate", "insult3", "kicker",],
        ["user_name", "subjectnamefirst", "predicate", "insult3", "kicker",],
        ["user_name", "subjectnamefirst", "predicate", "insult3", "kicker",],
        ["user_name", "subjectnamefirst", "predicate", "insult3", "kicker",],
        ["user_name", "subjectnamefirst", "predicate", "insult3", "kicker",],
        ["user_name", "subjectnamefirst", "predicate", "insult3", "kicker",],
        ["subjectnamesecond", "user_name",  "predicate", "insult3", "kicker",],
        ["subjectnamesecond", "user_name",  "predicate", "insult3", "kicker",],
        ["subjectnamesecond", "user_name",  "predicate", "insult3", "kicker",],
        ["subjectnamesecond", "user_name",  "predicate", "insult3", "kicker",],
        ["subjectnamesecond", "user_name",  "predicate", "insult3", "kicker",],
        ["subjectnamesecond", "user_name",  "predicate", "insult3", "kicker",],
        ["subjectnamesecond", "user_name",  "predicate", "insult3", "kicker",],
        ["subjectnamesecond", "user_name",  "predicate", "insult3", "kicker",],
        ["subjectnamesecond", "user_name",  "predicate", "insult3", "kicker",],
        ["subjectnamesecond", "user_name",  "predicate", "insult3", "kicker",],
        ]

#reserved only for Donald and Ivanka Trump
niceQuotes = [
  "What a beautiful person!",
  "That one should be our president!",
  "I know the best people. And that's one of them.",
  "Fantastic, yuge potential!"
]

def generateInsult(name):
	"""Randomly generates an insult provided a name."""
	
	#filter out the best people
	if ((name.lower().find('donald') > -1) or
      (name.lower().find('trump') > -1) or
      (name.lower().find('ivanka') > -1) ): 
		return niceQuotes[getRandomInt(len(niceQuotes))]
  
	#generate a random sentence structure
	template = templates[getRandomInt(len(templates))]

        newQuote = str()		
	for i in range(len(template)):
		word = template[i]

		#find and replace occurrence of user_name with provided name
		if (word == "user_name"):
			newQuote += name
		else:
			#else replace part of sentence with random structure
			newQuote += quotes[word][getRandomInt(len(quotes[word]))]
			
	return newQuote


def getRandomInt(n):
	return int(((random.random() * 1000000) + 1) % n)
