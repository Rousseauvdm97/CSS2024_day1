"""
Storing data in Python

1. Lists
2. Dictionaries
3. Data Frames - specific to Pandas
"""

import pandas as pd

file_countries = pd.read_csv("country_data.csv")

print(file_countries)

"""
    Age Gender       Country
0    39      M  South Africa
1    25      M      Botswana
2    29      F  South Africa
3    46      M  South Africa
4    22      F         Kenya
5    35      F    Mozambique
6    22      F       Lesotho
7    49      M         Kenya
8    30      M         Kenya
9    40      F         Egypt
10   30      M         Sudan
"""

#Making data from scratch

#this below is a dumb way to store info in Python
age1 = 30
age2 = 25
age3 = 29

age_list = [30, 25, 29, 46, 22]

print(age_list)

"""
[30, 25, 29, 46, 22]
"""

#Below is just an example of the data types in the list, but is not good practice
age_list_ext = [30, 25, 29, 46, 22, 3.14, "tau"]

print(age_list_ext)

"""
[30, 25, 29, 46, 22, 3.14, 'tau']
"""

#indexing examples
print(age_list_ext[0])

"""
30
"""

print(age_list_ext[6])

"""
tau
"""

#extra examples for different functions
print(min(age_list)) #cannot use for extended list error = TypeError: '<' not supported between instances of 'str' and 'float'

"""
22
"""

print(max(age_list))

"""
46
"""

print(sum(age_list))

"""
152
"""

print(len(age_list))

"""
5
"""

#calculating average
print(sum(age_list)/len(age_list))

"""
30.4
"""

#another way for average
avg = sum(age_list)/len(age_list)

print(avg)

"""
30.4
"""

#Example list

g1 = "M"
g2 = "F"
g3 = "M"

gender = ["M", "F", "M"]

#Another example list
c1 = "South Africa"
c2 = "Lesotho"

country_list = ["South Africa", "Lesotho"]



print(age_list[0:2])

"""
[30, 25]
"""

print(age_list[0:3]) #last value is the value in the list minus 1

"""
[30, 25, 29]
"""

#new functin append to use in lists
age_list.append(100) #appending a new number to the list

print(age_list)

#how to append 100 in the first position in a list using the insert method
age_list.insert(0, 100)

"""
Dictionaries - key:value pairs

cat: "a cute animal""

"""

mammals = {"cat": "a cute animal", "lion": "king of the jungle", "whale": "a large ocean-dwelling creature"}

print(mammals["whale"])

"""
Data frames
"""

fruits = ["apple", "banana", "orange", "grape", "kiwi"]

size_nm = [9.8, 10.1, 13.2, 8.7, 20.5]

fruit_sizes = {
    'fruits': fruits,
    'sizes': size_nm
    }

"""
df - dataframe
"""

df = pd.DataFrame(fruit_sizes)

print(df['fruits'])

print(df["sizes"])

print(df['sizes'].mean())

print(df.describe())

print(df[df["sizes"]> 10])

print(df[1:3])

#adding column to df
prices = [10.99, 8.49, 3.99, 5.49, 30.99]

df['prices'] = prices

#dropping column from df
df.drop(columns = ["sizes"], inplace = True)

#######################################################################

"""
Revision of work from day 1
"""

import pandas as pd

file_test = pd.read_csv("country_data.csv", skiprows=3)

print(file_test.info())

print(file_test.describe())


"""
Storing data in Python revision
"""

file_store = pd.read_csv("country_data.csv")
print(file_store)


"""
lists
dictionarys
dataframes

this is useful as we do not want to generate data per variable eg

a1 = 2
a2 = 5
a3 = 7
etc...
"""

#lists

age = [30,40,30,49,22,35,22,46,29,25,39] #note that we are working with integers and therefore they are only seperated with , and not ""

print(age)

#Using lists with indixes

print(age[0]) #Remember that indixes always starts at 0
print(age[1])
print(age[10])

#Therefore the indices range from 0 to 10 in the "age" list

#Now we access basic stats from the age list

print(min(age))
print(max(age))
print(len(age))
print(sum(age))

#To calculate average

avg = sum(age)/len(age)

print(avg)

#storing text
C2 = "M"
C3 = "M"
C4 = "F" #Remember that with text it always needs to be in "" otherwise will think it is a variable which is most likely not defined

#creating a list for gender

gender = ["M","M","F","M","F","F","F","M","M","F","M"]
print(gender[0])
print(gender[1])
print(gender[2])
print(gender[-1]) #use -1 in the index to get the last value in the list

# country list
country = ["South Africa","Botswana","South Africa","South Africa","Kenya","Mozambique","Lesotho","Kenya","Kenya","Egypt","Sudan"]

print(country)
print(country[0])
print(country[5])

# Data Storage With Lists
my_list = [42, -2021, 6.283,"tau", "node"] #Note that list can contain differnt data types ie int, float and string/text but in practice not good 
print(my_list)

#printing all the items in the list
print(my_list[:])

#appending an item in the list in the last index
my_list.append("pi")

#adding items to the list using insert
my_list.insert(0, "hello") #The first argument for insert is the index where the item is to be inserted

#Remove item from list using remove function

my_list.remove("hello") #msut type in the item that needs to be removed
my_list.remove(6.283)

#printing a range of values using [x:y]

print(my_list[0:3]) #Remember that the last entry is index number -1, if you want to print the entire list using the len function it is eg

print(my_list[0:len(my_list)]) #since the last index is 4 and the length of the list is 5, (5-1) = 4 and therefore everything is printed

#Dictionaries

dic_person = {"name": 'John Doe', 'age': 30, 'gender': 'M', 'address': '1113 Poo str'}

#to access information in the dictionary we have to look for the "key" to obtain the "value"

print(dic_person['name'])
print(dic_person['age'])
print(dic_person['address'])

#adding a new item to the dictionary

dic_person["phone"] = '999 999 9999'

print(dic_person.get("phone")) #get function to get value in key value pair

#Dataframes

#creating df

#first we create the dictionary with the lists we generated
data = {"age" : age, "gender": gender, "country": country}

df = pd.DataFrame(data)

print(df)

#Columns based acess as follows
print(df["age"])
print(df["gender"])

#basic stats of a specific column
print(min(df["age"]))
#or
print(df["age"].min())

#same usage for max and mean (mean works in dataframes and not lists)

print(df['age'].max())
print(df['age'].mean())

# Filtering data
print(df[df['age'] > 30])

# Slicing rows and columns
print(df[1:4])  # Select rows 1 to 3 and all columns

# Adding a new column
df['new_column'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] #same as with dictionary but now we add a list
print(df)

# Removing a column
df.drop(columns = ['new_column'], inplace = True)
print(df)
