print('string') #single cote
print("string") #multi cote
print("mohith's phone") # coat can be used as
print(0) #int
print(7.7) #float value
print(3+9) # add,sub,mul,div=>arthemaetical operations
print(8*3)
print(8/2) #single slash returns float value
print(8//2) #double slash return int value 

#print("i have "+ 50 +"rupees") # if we run this we get an error as 50 is an int so int concatination can be possible by below 2 methods.
print("i have "+ str(50) +" rupees")
print(f"i have {50} rupess")
print(f"i have {2*100} rupess") #we can use calculations in the backets also

#python is dynamically typed as we no need to mention that int float like that
'''
int to_sec=24*3*6
string mohith="bobby" #no need to mention the datatype
'''

#nameing conversion be use u nderscore and its better to use small letters
''' to_calculate=4*6 '''


#examplecode:-
cal_to_sec=24*60*60
name_last="brother"

print(cal_to_sec)
print(f"25 days have {25*cal_to_sec} seconds")
print(f"50 days have {50*cal_to_sec} seconds {name_last}")
print(f"100 days have {100*cal_to_sec} seconds {name_last}")