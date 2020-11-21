string1 = 'CarBadBoxNumKeyValRayCppSan'

n = 3
chunks = [string1[i:i+n] for i in range(0, len(string1), n)]
print(chunks)


import datetime

my_date = datetime.datetime(2020, 7, 21)
sentence = f"{my_date:%B %d, %Y} fell on a {my_date:%A} and was day {my_date:%j}"
print(sentence)