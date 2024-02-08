#parse month should take in the text of the month and return the number 
#as a string
#January -> 1 (as a string)
#YOU MAY USE THIS FUNCTION IF YOU WANT TO OR YOU MAY REMOVE IT
def parse_month(month):
    dictionary= {'January': '01' ,
                 'Feburary' : '02' ,
                 'March': '03' ,
                 'April': '04',
                 'May': '05', 
                 'June': '06' ,
                 'July': '07',
                 'August': '08' ,
                 'September' :'09',
                 'October': '10', 
                 'November': '11', 
                 'December': '12'}
    month=dictionary[month]
    return(month)

#REMOVE PASS AND FIX THIS FUNCTION
#parse_date function should return the date formated as MM/DD/YYYY
#DO NOT REMOVE THIS FUNCTION
def parse_date(user_string):
    new=user_string.split()
    month1 = new[0]
    day = new[1]
    if len(day) == 3:
        day  = day[0:2]
    else:
        day = "0" + day[0:1]
    year = new[2]
    return (f'{month1}/{day}/{year}')

#REMOVE PASS AND YOUR CODE GOES HERE
if __name__ == '__main__':
    user_string = 0
    while user_string != "-1":
        user_string = input()
        if user_string != "-1":
            date = parse_date(user_string)
            print(date)
#REMOVE PASS AND FIX THIS FUNCTION
#parse_date function should return the date formated as MM/DD/YYYY
#DO NOT REMOVE THIS FUNCTION
