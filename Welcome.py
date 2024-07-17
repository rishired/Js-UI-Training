# friend = "rishi"
# friends = ['pavan',"rishi",'vaishnav','ritwik']
# if friend in friends:
#     print("yes he is available")
# else:
#     print("hes is not available")
#
#
# message="welcome to python class"
# def demomessage(message):
#     print(message)
# demomessage(message)
#
# def demomessage(message):
#     return message;
# print(demomessage(message))
#
#
# class Friend:
#     since = 3
# def gettotalfriendshipdays(since):
#     print(since)
# gettotalfriendshipdays('since')

# print(3+3)

# 3+1
#
# 3*3
#
# 2**3
#
# "Hello, world!"  # only the last line is printed

# print(3+1)
#
# print(3*3)
#
# print(2**3)
#
# print("Hello, world!")

# i=((5/3), (5%3), (5.0/3), (5/3.0), (5.2%3))
# for j in i:
#     print(int(j))


# i=((2000.3**200), (1.0 + 1.0 - 1.0), (1.0 + 1.0e20 - 1.0e20))  # 2000.3**200 (This operation results in a number
#                                                                # that is too large to be represented as a
#                                                          # standard floating-point number in Python, hence the overflow.)
# for j in i:
#     print(float(j))


# i=((1.0 + 1.0 - 1.0), (1.0 + 1.0e20 - 1.0e20))
# for j in i:
#     print(float(j))

# x = 'Rishi'
# print (f'hello, my name is {x}')


# i= (float(123), float('123'), float('123.23'), int(123), int('123'), int(float('123.23')), str(12), str(12.2), bool('a'), bool(0), bool(0.1))
# for j in i:
#     print(j)


# range(5)
#
# for i in range(5):
#     print(i)
#
# type(range(5))
#
#
# for i in range(0,101):
#     print(i)
#
#
# for i in range(0,101,15):
#    print(i)
#
# for i in range(0,101):
#     if i % 5 == 0 and i % 3 !=0:
#         print(i)
#
#
# x=5
#
#
# if x == 2:
#     print('prime number')
# else:
#     if x % 2 != 0:
#         for i in range(1,x):
#             if (i % 1 == 0 and i % x == 0):
#                 print(1,i)
#     else:
#           print('Not a prime')
#
#
#
# for x in range(2,21):
#     for i in range(2,21):
#         if x % i == 0:
#             if x != i:
#                 print (i)
#     print ('-------')
#
#
#
# x = 4
# if x <= 1:
#   print('not a prime')
# elif x == 2:
#     print('PRIME')
# elif x == 3:
#     print('PRIME')
# else:
#   if x % 2 != 0 and x % 3 != 0:
#     for i in range(4,x+1):
#       if (i % 1 == 0 and x % i == 0):
#         print(f'{x} is a PRIME NUMBER')
#   else:
#         print ('Not Prime')
#
#
# i = 0
# while i in range(0,101):
#   print(i)
#   if (i == 100):
#     break
#   i+=1
#
#
# i = 7
# while i in range (0,110):
#   if i % 7 == 0:
#     print(i)
#   if ( i == 106):
#       break
#   i+=1
#
#
# i = 10000
# while i in range(0,10000):
#   if i % 5 == 0 and i % 7 == 0 and i % 11 == 0:
#     print (i)
#
# count = 0
# number = 1
# results = []
#
# # Loop until we find 20 numbers divisible by 5, 7, and 11
# while count < 20:
#     if number % 5 == 0 and number % 7 == 0 and number % 11 == 0:
#         results.append(number)
#         count += 1
#     number += 1
#
# # Print the results
# print("The first 20 numbers divisible by 5, 7, and 11 are:")
# for num in results:
#     print(num)