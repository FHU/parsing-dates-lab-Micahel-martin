#parse month should take in the text of the month and return the number 
#as a string
#January -> 1 (as a string)
#YOU MAY USE THIS FUNCTION IF YOU WANT TO OR YOU MAY REMOVE IT
def parse_month(month):
    dictionary= {'January': '01' ,'Feburary' : '02' ,'March': '03' ,'April': '04','May': '05', 'June': '06' ,'July': '07','August': '08' ,'September' :'09','October': '10', 'November': '11', 'December': '12'}
    return dictionary[month]

#REMOVE PASS AND FIX THIS FUNCTION
#parse_date function should return the date formated as MM/DD/YYYY
#DO NOT REMOVE THIS FUNCTION
def parse_date(user_string):
     split=user_string.split()
     list=split
     print(list[0]); '/' (list[1]); '/' (list[2])
#REMOVE PASS AND YOUR CODE GOES HERE
if __name__ == '__main__':
   def parse_month(month):
    dictionary= {'January': '01' ,'Feburary' : '02' ,'March': '03' ,'April': '04','May': '05', 'June': '06' ,'July': '07','August': '08' ,'September' :'09','October': '10', 'November': '11', 'December': '12'}
    return dictionary[month]

#REMOVE PASS AND FIX THIS FUNCTION
#parse_date function should return the date formated as MM/DD/YYYY
#DO NOT REMOVE THIS FUNCTION
def parse_date(user_string):
     split=user_string.split()
     list=split
     print(list[0]);'/'(list[1]);'/'(list[2])