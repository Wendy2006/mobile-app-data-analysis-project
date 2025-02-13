#!/usr/bin/env python
# coding: utf-8

# In[ ]:

print("Title: " Mobile App Data Analysis Project)
print("We're working as data analysts for a company that develops free mobile apps for Android and iOS.")
print("Since our apps make money through in-app ads, our revenue depends on how many people use them.")
print("Our goal in this project is to figure out what kinds of apps are most likely to attract a large number of users.")
print("By analyzing data from the App Store and Google Play, we can help our developers make informed decisions about")
print(which types of apps to create.")
print("As of September 2018, there were around 2 million apps on the App Store and 2.1 million on Google Play,")
print("making it essential to choose the right type of app to stand out in the competitive market.")

# In[1]:


from csv import reader

### The Google Play data set ###
opened_file = open('googleplaystore.csv')
read_file = reader(opened_file)
android = list(read_file)
android_header = android[0]
android = android[1:]

### The App Store data set ###
opened_file = open('AppleStore.csv')
read_file = reader(opened_file)
ios = list(read_file)
ios_header = ios[0]
ios = ios[1:]


# In[2]:


def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]    
    for row in dataset_slice:
        print(row)
        print('\n') # adds a new (empty) line between rows
        
    if rows_and_columns:
        print('Number of rows:', len(dataset))
        print('Number of columns:', len(dataset[0]))

print(android_header)
print('\n')
explore_data(android, 0, 3, True)
print('\n')
print(ios_header)
print('\n')
explore_data(ios, 0, 3, True)


# In[3]:


print('\n')
print(android_header)
print(android[10472])


# In[4]:


deleted = False  

if not deleted and len(android) > 10840:  
    del android[10472]
    deleted = True


# In[5]:


print("There are multiple duplicate data in the data set, because the data")
print('\n')
print("was collected multiple times throughout the time")


# In[6]:


for data in android: 
    if data[0] == "Instagram": 
        print(data)
        print('\n')


# In[7]:


def count_duplicate (dataset): 
    unique_apps = []
    duplicate_apps = []
    for data in dataset: 
        name = data[0]
        if name in unique_apps: 
            duplicate_apps.append(name)
        else: 
            unique_apps.append(name)
    print("number of duplicate apps: ")
    print(len(duplicate_apps))

count_duplicate (android)
        


# In[8]:


print("we would leave the newest data by comparing the number of ratings")
print("meaning we leave the data with the most ratings")


# In[9]:


reviews_max = {}

for data in android:
    name = data[0]
    n_reviews = float(data[3])
    
    if name in reviews_max and reviews_max[name] < n_reviews:
        reviews_max[name] = n_reviews
        
    elif name not in reviews_max:
        reviews_max[name] = n_reviews


# In[10]:


print ("actual length: ", len(reviews_max))


# In[11]:


android_clean = []
already_added = []

for data in android:
    name = data[0]
    n_reviews = float(data[3])
    
    if name not in already_added and reviews_max[name] == n_reviews:
        android_clean.append(data)
        already_added.append(name)

print("unique data: ", len(android_clean))


# In[12]:


def check_English (string): 
    count = 0
    for c in string: 
        if ord(c) > 127:
            count += 1
            if count > 3: 
                return False
    return True


# In[13]:


English_app_android = []
English_app_ios = []
for data in android_clean: 
    name = data[0]
    if check_English(name): 
        English_app_android.append(data)

for data in ios: 
    name = data[1]
    if check_English(name): 
        English_app_ios.append(data)

print("Remaining length android: ", len(English_app_android))
print("Remaining length ios: ", len(English_app_ios))


# In[14]:


free_android_app = []
free_ios_app = []
for data in English_app_android:
    price = data[7]
    if price == "0" or price == "0.0" or price == "$0.00": 
        free_android_app.append(data)
for data in English_app_ios: 
    price = data[4]
    if price == "0" or price == "0.0" or price == "$0.00":
        free_ios_app.append(data)

print("number of free apps in Google Store : ", len(free_android_app))
print("number of free apps in Apple Store: ", len(free_ios_app))
    


# In[15]:


print("Because our end goal is to add the app on both Google Play and the App Store," )
print("we need to find app profiles that are successful in both markets. For instance, ")
print("a profile that works well for both markets might be a productivity app that ") 
print("makes use of gamification.")


# In[16]:


def freq_table(dataset, index): 
    frequency_table = {}
    percentage_table = {}
    total = 0
    
    for app in dataset: 
        genre = app[index]
        total+=1
        if genre in frequency_table: 
            frequency_table[genre] += 1
        else: 
            frequency_table[genre] = 1
    for key in frequency_table: 
        percentage_table[key] = frequency_table[key]/total*100
    return percentage_table


# In[17]:


def display_table(dataset, index):
    table = freq_table(dataset, index)
    table_display = []
    for key in table:
        key_val_as_tuple = (table[key], key)
        table_display.append(key_val_as_tuple)

    table_sorted = sorted(table_display, reverse = True)
    for entry in table_sorted:
        print(entry[1], ':', entry[0])


display_table(free_ios_app, 11)


# In[18]:


display_table(free_android_app, 1)


# In[19]:


display_table(free_android_app, 9)


# In[20]:


ios_genre = freq_table(free_ios_app, 11)

for genre in ios_genre: 
    total = 0
    len_genre = 0
    average = 0
    for app in free_ios_app: 
        install = int(app[5])
        if app[11] == genre: 
            len_genre += 1
            total += install
    average = total / len_genre
    print(genre, ":", average)


# In[21]:


print("on average, Navigation apps have the highest number of user reviews.")
print("after that is the social networking and music app")
print("These three, by average, is the most popular genres in app store")


# In[22]:


android_category = freq_table(free_android_app, 1)

for category in android_category: 
    total = 0
    len_category = 0
    for app in free_android_app: 
        category_app = app[1]
        if category_app == category: 
            install = app[5].replace("+", "")
            install = install.replace(",", "")
            total += float(install)
            len_category += 1
    average = total / len_category
    print(category, ":", average)


# In[23]:


print("Based on the data, a promising app profile for Google Play is a")
print("Books & Reference or Productivity app. These categories have a")
print("strong install base while facing less competition than gaming or")
print("social media apps. Books & Reference apps (8.7M installs on avg.)")
print("can be monetized through premium content or subscriptions, while")
print("Productivity apps (16.7M installs on avg.) attract both casual and")
print("professional users, offering potential for paid features. Both")
print("categories align well with trends on the App Store, making them")
print("ideal for cross-platform success.")

