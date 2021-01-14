#This program will take an input from the user and extract information.
#It will take the age, name, and gender.
def age(paragraph_list):
    if 'years' in paragraph_list:
        index = paragraph_list.index('years')
        index = index - 1
        age_found = paragraph_list[index]
    elif 'yrs' in paragraph_list:
        index = paragraph_list.index('yrs')
        index = index - 1
        age_found = paragraph_list[index]
    else:
        age_found = 'No age found.'
    print(age_found)

def name(paragraph_list):
    name_is = "No name found."
    if 'name' in paragraph_list:
        name_index = paragraph_list.index("name")
        name_index = name_index + 2
        name_is = paragraph_list[name_index]
    print(name_is)

def location(paragraph_list):
    location_is = "No location found."
    if 'live' in paragraph_list:
        location_index = paragraph_list.index("live")
        location_index = location_index + 2
        location_is = paragraph_list[location_index]
        if location_is == 'the':
            location_index = location_index + 1
    print(location_is)





paragraph_og = input("Please introduce yourself: \n")

paragraph = paragraph_og.lower()
paragraph = paragraph.replace(".", "")
paragraph = paragraph.replace(",", "")
paragraph = paragraph.replace("!", "")
paragraph = paragraph.replace("?", "")
paragraph = paragraph.replace(";", "")
paragraph = paragraph.replace(":", "")
paragraph = paragraph.replace("(", "")
paragraph = paragraph.replace(")", "")
paragraph = paragraph.replace("'", "")

#This turns the paragraph into a list of strings with all of the words in it.
paragraph_list = paragraph.split(" ")

print(paragraph)
print(paragraph_list)

age(paragraph_list)
name(paragraph_list)
location(paragraph_list)
