# mobile app data analysis project
 A guided project done on dataquest, mainly analyzed data for google play store and apple store by using python
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from csv import reader\n",
    "\n",
    "### The Google Play data set ###\n",
    "opened_file = open('googleplaystore.csv')\n",
    "read_file = reader(opened_file)\n",
    "android = list(read_file)\n",
    "android_header = android[0]\n",
    "android = android[1:]\n",
    "\n",
    "### The App Store data set ###\n",
    "opened_file = open('AppleStore.csv')\n",
    "read_file = reader(opened_file)\n",
    "ios = list(read_file)\n",
    "ios_header = ios[0]\n",
    "ios = ios[1:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['App', 'Category', 'Rating', 'Reviews', 'Size', 'Installs', 'Type', 'Price', 'Content Rating', 'Genres', 'Last Updated', 'Current Ver', 'Android Ver']\n",
      "\n",
      "\n",
      "['Photo Editor & Candy Camera & Grid & ScrapBook', 'ART_AND_DESIGN', '4.1', '159', '19M', '10,000+', 'Free', '0', 'Everyone', 'Art & Design', 'January 7, 2018', '1.0.0', '4.0.3 and up']\n",
      "\n",
      "\n",
      "['Coloring book moana', 'ART_AND_DESIGN', '3.9', '967', '14M', '500,000+', 'Free', '0', 'Everyone', 'Art & Design;Pretend Play', 'January 15, 2018', '2.0.0', '4.0.3 and up']\n",
      "\n",
      "\n",
      "['U Launcher Lite – FREE Live Cool Themes, Hide Apps', 'ART_AND_DESIGN', '4.7', '87510', '8.7M', '5,000,000+', 'Free', '0', 'Everyone', 'Art & Design', 'August 1, 2018', '1.2.4', '4.0.3 and up']\n",
      "\n",
      "\n",
      "Number of rows: 10841\n",
      "Number of columns: 13\n",
      "\n",
      "\n",
      "['id', 'track_name', 'size_bytes', 'currency', 'price', 'rating_count_tot', 'rating_count_ver', 'user_rating', 'user_rating_ver', 'ver', 'cont_rating', 'prime_genre', 'sup_devices.num', 'ipadSc_urls.num', 'lang.num', 'vpp_lic']\n",
      "\n",
      "\n",
      "['284882215', 'Facebook', '389879808', 'USD', '0.0', '2974676', '212', '3.5', '3.5', '95.0', '4+', 'Social Networking', '37', '1', '29', '1']\n",
      "\n",
      "\n",
      "['389801252', 'Instagram', '113954816', 'USD', '0.0', '2161558', '1289', '4.5', '4.0', '10.23', '12+', 'Photo & Video', '37', '0', '29', '1']\n",
      "\n",
      "\n",
      "['529479190', 'Clash of Clans', '116476928', 'USD', '0.0', '2130805', '579', '4.5', '4.5', '9.24.12', '9+', 'Games', '38', '5', '18', '1']\n",
      "\n",
      "\n",
      "Number of rows: 7197\n",
      "Number of columns: 16\n"
     ]
    }
   ],
   "source": [
    "def explore_data(dataset, start, end, rows_and_columns=False):\n",
    "    dataset_slice = dataset[start:end]    \n",
    "    for row in dataset_slice:\n",
    "        print(row)\n",
    "        print('\\n') # adds a new (empty) line between rows\n",
    "        \n",
    "    if rows_and_columns:\n",
    "        print('Number of rows:', len(dataset))\n",
    "        print('Number of columns:', len(dataset[0]))\n",
    "\n",
    "print(android_header)\n",
    "print('\\n')\n",
    "explore_data(android, 0, 3, True)\n",
    "print('\\n')\n",
    "print(ios_header)\n",
    "print('\\n')\n",
    "explore_data(ios, 0, 3, True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "['App', 'Category', 'Rating', 'Reviews', 'Size', 'Installs', 'Type', 'Price', 'Content Rating', 'Genres', 'Last Updated', 'Current Ver', 'Android Ver']\n",
      "['Life Made WI-Fi Touchscreen Photo Frame', '1.9', '19', '3.0M', '1,000+', 'Free', '0', 'Everyone', '', 'February 11, 2018', '1.0.19', '4.0 and up']\n"
     ]
    }
   ],
   "source": [
    "print('\\n')\n",
    "print(android_header)\n",
    "print(android[10472])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "scrolled": false
   },
   "outputs": [],
   "source": [
    "deleted = False  \n",
    "\n",
    "if not deleted and len(android) > 10840:  \n",
    "    del android[10472]\n",
    "    deleted = True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "There are multiple duplicate data in the data set, because the data\n",
      "\n",
      "\n",
      "was collected multiple times throughout the time\n"
     ]
    }
   ],
   "source": [
    "print(\"There are multiple duplicate data in the data set, because the data\")\n",
    "print('\\n')\n",
    "print(\"was collected multiple times throughout the time\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Instagram', 'SOCIAL', '4.5', '66577313', 'Varies with device', '1,000,000,000+', 'Free', '0', 'Teen', 'Social', 'July 31, 2018', 'Varies with device', 'Varies with device']\n",
      "\n",
      "\n",
      "['Instagram', 'SOCIAL', '4.5', '66577446', 'Varies with device', '1,000,000,000+', 'Free', '0', 'Teen', 'Social', 'July 31, 2018', 'Varies with device', 'Varies with device']\n",
      "\n",
      "\n",
      "['Instagram', 'SOCIAL', '4.5', '66577313', 'Varies with device', '1,000,000,000+', 'Free', '0', 'Teen', 'Social', 'July 31, 2018', 'Varies with device', 'Varies with device']\n",
      "\n",
      "\n",
      "['Instagram', 'SOCIAL', '4.5', '66509917', 'Varies with device', '1,000,000,000+', 'Free', '0', 'Teen', 'Social', 'July 31, 2018', 'Varies with device', 'Varies with device']\n",
      "\n",
      "\n"
     ]
    }
   ],
   "source": [
    "for data in android: \n",
    "    if data[0] == \"Instagram\": \n",
    "        print(data)\n",
    "        print('\\n')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "number of duplicate apps: \n",
      "1181\n"
     ]
    }
   ],
   "source": [
    "def count_duplicate (dataset): \n",
    "    unique_apps = []\n",
    "    duplicate_apps = []\n",
    "    for data in dataset: \n",
    "        name = data[0]\n",
    "        if name in unique_apps: \n",
    "            duplicate_apps.append(name)\n",
    "        else: \n",
    "            unique_apps.append(name)\n",
    "    print(\"number of duplicate apps: \")\n",
    "    print(len(duplicate_apps))\n",
    "\n",
    "count_duplicate (android)\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "we would leave the newest data by comparing the number of ratings\n",
      "meaning we leave the data with the most ratings\n"
     ]
    }
   ],
   "source": [
    "print(\"we would leave the newest data by comparing the number of ratings\")\n",
    "print(\"meaning we leave the data with the most ratings\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "reviews_max = {}\n",
    "\n",
    "for data in android:\n",
    "    name = data[0]\n",
    "    n_reviews = float(data[3])\n",
    "    \n",
    "    if name in reviews_max and reviews_max[name] < n_reviews:\n",
    "        reviews_max[name] = n_reviews\n",
    "        \n",
    "    elif name not in reviews_max:\n",
    "        reviews_max[name] = n_reviews"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "actual length:  9659\n"
     ]
    }
   ],
   "source": [
    "print (\"actual length: \", len(reviews_max))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "unique data:  9659\n"
     ]
    }
   ],
   "source": [
    "android_clean = []\n",
    "already_added = []\n",
    "\n",
    "for data in android:\n",
    "    name = data[0]\n",
    "    n_reviews = float(data[3])\n",
    "    \n",
    "    if name not in already_added and reviews_max[name] == n_reviews:\n",
    "        android_clean.append(data)\n",
    "        already_added.append(name)\n",
    "\n",
    "print(\"unique data: \", len(android_clean))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "def check_English (string): \n",
    "    count = 0\n",
    "    for c in string: \n",
    "        if ord(c) > 127:\n",
    "            count += 1\n",
    "            if count > 3: \n",
    "                return False\n",
    "    return True\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Remaining length android:  9614\n",
      "Remaining length ios:  6183\n"
     ]
    }
   ],
   "source": [
    "English_app_android = []\n",
    "English_app_ios = []\n",
    "for data in android_clean: \n",
    "    name = data[0]\n",
    "    if check_English(name): \n",
    "        English_app_android.append(data)\n",
    "\n",
    "for data in ios: \n",
    "    name = data[1]\n",
    "    if check_English(name): \n",
    "        English_app_ios.append(data)\n",
    "\n",
    "print(\"Remaining length android: \", len(English_app_android))\n",
    "print(\"Remaining length ios: \", len(English_app_ios))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "number of free apps in Google Store :  8864\n",
      "number of free apps in Apple Store:  3222\n"
     ]
    }
   ],
   "source": [
    "free_android_app = []\n",
    "free_ios_app = []\n",
    "for data in English_app_android:\n",
    "    price = data[7]\n",
    "    if price == \"0\" or price == \"0.0\" or price == \"$0.00\": \n",
    "        free_android_app.append(data)\n",
    "for data in English_app_ios: \n",
    "    price = data[4]\n",
    "    if price == \"0\" or price == \"0.0\" or price == \"$0.00\":\n",
    "        free_ios_app.append(data)\n",
    "\n",
    "print(\"number of free apps in Google Store : \", len(free_android_app))\n",
    "print(\"number of free apps in Apple Store: \", len(free_ios_app))\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Because our end goal is to add the app on both Google Play and the App Store,\n",
      "we need to find app profiles that are successful in both markets. For instance, \n",
      "a profile that works well for both markets might be a productivity app that \n",
      "makes use of gamification.\n"
     ]
    }
   ],
   "source": [
    "print(\"Because our end goal is to add the app on both Google Play and the App Store,\" )\n",
    "print(\"we need to find app profiles that are successful in both markets. For instance, \")\n",
    "print(\"a profile that works well for both markets might be a productivity app that \") \n",
    "print(\"makes use of gamification.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "def freq_table(dataset, index): \n",
    "    frequency_table = {}\n",
    "    percentage_table = {}\n",
    "    total = 0\n",
    "    \n",
    "    for app in dataset: \n",
    "        genre = app[index]\n",
    "        total+=1\n",
    "        if genre in frequency_table: \n",
    "            frequency_table[genre] += 1\n",
    "        else: \n",
    "            frequency_table[genre] = 1\n",
    "    for key in frequency_table: \n",
    "        percentage_table[key] = frequency_table[key]/total*100\n",
    "    return percentage_table\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Games : 58.16263190564867\n",
      "Entertainment : 7.883302296710118\n",
      "Photo & Video : 4.9658597144630665\n",
      "Education : 3.662321539416512\n",
      "Social Networking : 3.2898820608317814\n",
      "Shopping : 2.60707635009311\n",
      "Utilities : 2.5139664804469275\n",
      "Sports : 2.1415270018621975\n",
      "Music : 2.0484171322160147\n",
      "Health & Fitness : 2.0173805090006205\n",
      "Productivity : 1.7380509000620732\n",
      "Lifestyle : 1.5828677839851024\n",
      "News : 1.3345747982619491\n",
      "Travel : 1.2414649286157666\n",
      "Finance : 1.1173184357541899\n",
      "Weather : 0.8690254500310366\n",
      "Food & Drink : 0.8069522036002483\n",
      "Reference : 0.5586592178770949\n",
      "Business : 0.5276225946617008\n",
      "Book : 0.4345127250155183\n",
      "Navigation : 0.186219739292365\n",
      "Medical : 0.186219739292365\n",
      "Catalogs : 0.12414649286157665\n"
     ]
    }
   ],
   "source": [
    "def display_table(dataset, index):\n",
    "    table = freq_table(dataset, index)\n",
    "    table_display = []\n",
    "    for key in table:\n",
    "        key_val_as_tuple = (table[key], key)\n",
    "        table_display.append(key_val_as_tuple)\n",
    "\n",
    "    table_sorted = sorted(table_display, reverse = True)\n",
    "    for entry in table_sorted:\n",
    "        print(entry[1], ':', entry[0])\n",
    "\n",
    "\n",
    "display_table(free_ios_app, 11)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "FAMILY : 18.907942238267147\n",
      "GAME : 9.724729241877256\n",
      "TOOLS : 8.461191335740072\n",
      "BUSINESS : 4.591606498194946\n",
      "LIFESTYLE : 3.9034296028880866\n",
      "PRODUCTIVITY : 3.892148014440433\n",
      "FINANCE : 3.7003610108303246\n",
      "MEDICAL : 3.531137184115524\n",
      "SPORTS : 3.395758122743682\n",
      "PERSONALIZATION : 3.3167870036101084\n",
      "COMMUNICATION : 3.2378158844765346\n",
      "HEALTH_AND_FITNESS : 3.0798736462093865\n",
      "PHOTOGRAPHY : 2.944494584837545\n",
      "NEWS_AND_MAGAZINES : 2.7978339350180503\n",
      "SOCIAL : 2.6624548736462095\n",
      "TRAVEL_AND_LOCAL : 2.33528880866426\n",
      "SHOPPING : 2.2450361010830324\n",
      "BOOKS_AND_REFERENCE : 2.1435018050541514\n",
      "DATING : 1.861462093862816\n",
      "VIDEO_PLAYERS : 1.7937725631768955\n",
      "MAPS_AND_NAVIGATION : 1.3989169675090252\n",
      "FOOD_AND_DRINK : 1.2409747292418771\n",
      "EDUCATION : 1.1620036101083033\n",
      "ENTERTAINMENT : 0.9589350180505415\n",
      "LIBRARIES_AND_DEMO : 0.9363718411552346\n",
      "AUTO_AND_VEHICLES : 0.9250902527075812\n",
      "HOUSE_AND_HOME : 0.8235559566787004\n",
      "WEATHER : 0.8009927797833934\n",
      "EVENTS : 0.7107400722021661\n",
      "PARENTING : 0.6543321299638989\n",
      "ART_AND_DESIGN : 0.6430505415162455\n",
      "COMICS : 0.6204873646209386\n",
      "BEAUTY : 0.5979241877256317\n"
     ]
    }
   ],
   "source": [
    "display_table(free_android_app, 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Tools : 8.449909747292418\n",
      "Entertainment : 6.069494584837545\n",
      "Education : 5.347472924187725\n",
      "Business : 4.591606498194946\n",
      "Productivity : 3.892148014440433\n",
      "Lifestyle : 3.892148014440433\n",
      "Finance : 3.7003610108303246\n",
      "Medical : 3.531137184115524\n",
      "Sports : 3.463447653429603\n",
      "Personalization : 3.3167870036101084\n",
      "Communication : 3.2378158844765346\n",
      "Action : 3.1024368231046933\n",
      "Health & Fitness : 3.0798736462093865\n",
      "Photography : 2.944494584837545\n",
      "News & Magazines : 2.7978339350180503\n",
      "Social : 2.6624548736462095\n",
      "Travel & Local : 2.3240072202166067\n",
      "Shopping : 2.2450361010830324\n",
      "Books & Reference : 2.1435018050541514\n",
      "Simulation : 2.0419675090252705\n",
      "Dating : 1.861462093862816\n",
      "Arcade : 1.8501805054151623\n",
      "Video Players & Editors : 1.7712093862815883\n",
      "Casual : 1.7599277978339352\n",
      "Maps & Navigation : 1.3989169675090252\n",
      "Food & Drink : 1.2409747292418771\n",
      "Puzzle : 1.128158844765343\n",
      "Racing : 0.9927797833935018\n",
      "Role Playing : 0.9363718411552346\n",
      "Libraries & Demo : 0.9363718411552346\n",
      "Auto & Vehicles : 0.9250902527075812\n",
      "Strategy : 0.9138086642599278\n",
      "House & Home : 0.8235559566787004\n",
      "Weather : 0.8009927797833934\n",
      "Events : 0.7107400722021661\n",
      "Adventure : 0.6768953068592057\n",
      "Comics : 0.6092057761732852\n",
      "Beauty : 0.5979241877256317\n",
      "Art & Design : 0.5979241877256317\n",
      "Parenting : 0.4963898916967509\n",
      "Card : 0.45126353790613716\n",
      "Casino : 0.42870036101083037\n",
      "Trivia : 0.41741877256317694\n",
      "Educational;Education : 0.39485559566787\n",
      "Board : 0.3835740072202166\n",
      "Educational : 0.3722924187725632\n",
      "Education;Education : 0.33844765342960287\n",
      "Word : 0.2594765342960289\n",
      "Casual;Pretend Play : 0.236913357400722\n",
      "Music : 0.2030685920577617\n",
      "Racing;Action & Adventure : 0.16922382671480143\n",
      "Puzzle;Brain Games : 0.16922382671480143\n",
      "Entertainment;Music & Video : 0.16922382671480143\n",
      "Casual;Brain Games : 0.13537906137184114\n",
      "Casual;Action & Adventure : 0.13537906137184114\n",
      "Arcade;Action & Adventure : 0.12409747292418773\n",
      "Action;Action & Adventure : 0.10153429602888085\n",
      "Educational;Pretend Play : 0.09025270758122744\n",
      "Simulation;Action & Adventure : 0.078971119133574\n",
      "Parenting;Education : 0.078971119133574\n",
      "Entertainment;Brain Games : 0.078971119133574\n",
      "Board;Brain Games : 0.078971119133574\n",
      "Parenting;Music & Video : 0.06768953068592057\n",
      "Educational;Brain Games : 0.06768953068592057\n",
      "Casual;Creativity : 0.06768953068592057\n",
      "Art & Design;Creativity : 0.06768953068592057\n",
      "Education;Pretend Play : 0.056407942238267145\n",
      "Role Playing;Pretend Play : 0.04512635379061372\n",
      "Education;Creativity : 0.04512635379061372\n",
      "Role Playing;Action & Adventure : 0.033844765342960284\n",
      "Puzzle;Action & Adventure : 0.033844765342960284\n",
      "Entertainment;Creativity : 0.033844765342960284\n",
      "Entertainment;Action & Adventure : 0.033844765342960284\n",
      "Educational;Creativity : 0.033844765342960284\n",
      "Educational;Action & Adventure : 0.033844765342960284\n",
      "Education;Music & Video : 0.033844765342960284\n",
      "Education;Brain Games : 0.033844765342960284\n",
      "Education;Action & Adventure : 0.033844765342960284\n",
      "Adventure;Action & Adventure : 0.033844765342960284\n",
      "Video Players & Editors;Music & Video : 0.02256317689530686\n",
      "Sports;Action & Adventure : 0.02256317689530686\n",
      "Simulation;Pretend Play : 0.02256317689530686\n",
      "Puzzle;Creativity : 0.02256317689530686\n",
      "Music;Music & Video : 0.02256317689530686\n",
      "Entertainment;Pretend Play : 0.02256317689530686\n",
      "Casual;Education : 0.02256317689530686\n",
      "Board;Action & Adventure : 0.02256317689530686\n",
      "Video Players & Editors;Creativity : 0.01128158844765343\n",
      "Trivia;Education : 0.01128158844765343\n",
      "Travel & Local;Action & Adventure : 0.01128158844765343\n",
      "Tools;Education : 0.01128158844765343\n",
      "Strategy;Education : 0.01128158844765343\n",
      "Strategy;Creativity : 0.01128158844765343\n",
      "Strategy;Action & Adventure : 0.01128158844765343\n",
      "Simulation;Education : 0.01128158844765343\n",
      "Role Playing;Brain Games : 0.01128158844765343\n",
      "Racing;Pretend Play : 0.01128158844765343\n",
      "Puzzle;Education : 0.01128158844765343\n",
      "Parenting;Brain Games : 0.01128158844765343\n",
      "Music & Audio;Music & Video : 0.01128158844765343\n",
      "Lifestyle;Pretend Play : 0.01128158844765343\n",
      "Lifestyle;Education : 0.01128158844765343\n",
      "Health & Fitness;Education : 0.01128158844765343\n",
      "Health & Fitness;Action & Adventure : 0.01128158844765343\n",
      "Entertainment;Education : 0.01128158844765343\n",
      "Communication;Creativity : 0.01128158844765343\n",
      "Comics;Creativity : 0.01128158844765343\n",
      "Casual;Music & Video : 0.01128158844765343\n",
      "Card;Action & Adventure : 0.01128158844765343\n",
      "Books & Reference;Education : 0.01128158844765343\n",
      "Art & Design;Pretend Play : 0.01128158844765343\n",
      "Art & Design;Action & Adventure : 0.01128158844765343\n",
      "Arcade;Pretend Play : 0.01128158844765343\n",
      "Adventure;Education : 0.01128158844765343\n"
     ]
    }
   ],
   "source": [
    "display_table(free_android_app, 9)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Social Networking : 71548.34905660378\n",
      "Photo & Video : 28441.54375\n",
      "Games : 22788.6696905016\n",
      "Music : 57326.530303030304\n",
      "Reference : 74942.11111111111\n",
      "Health & Fitness : 23298.015384615384\n",
      "Weather : 52279.892857142855\n",
      "Utilities : 18684.456790123455\n",
      "Travel : 28243.8\n",
      "Shopping : 26919.690476190477\n",
      "News : 21248.023255813954\n",
      "Navigation : 86090.33333333333\n",
      "Lifestyle : 16485.764705882353\n",
      "Entertainment : 14029.830708661417\n",
      "Food & Drink : 33333.92307692308\n",
      "Sports : 23008.898550724636\n",
      "Book : 39758.5\n",
      "Finance : 31467.944444444445\n",
      "Education : 7003.983050847458\n",
      "Productivity : 21028.410714285714\n",
      "Business : 7491.117647058823\n",
      "Catalogs : 4004.0\n",
      "Medical : 612.0\n"
     ]
    }
   ],
   "source": [
    "ios_genre = freq_table(free_ios_app, 11)\n",
    "\n",
    "for genre in ios_genre: \n",
    "    total = 0\n",
    "    len_genre = 0\n",
    "    average = 0\n",
    "    for app in free_ios_app: \n",
    "        install = int(app[5])\n",
    "        if app[11] == genre: \n",
    "            len_genre += 1\n",
    "            total += install\n",
    "    average = total / len_genre\n",
    "    print(genre, \":\", average)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "on average, Navigation apps have the highest number of user reviews.\n",
      "after that is the social networking and music app\n",
      "These three, by average, is the most popular genres in app store\n"
     ]
    }
   ],
   "source": [
    "print(\"on average, Navigation apps have the highest number of user reviews.\")\n",
    "print(\"after that is the social networking and music app\")\n",
    "print(\"These three, by average, is the most popular genres in app store\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ART_AND_DESIGN : 1986335.0877192982\n",
      "AUTO_AND_VEHICLES : 647317.8170731707\n",
      "BEAUTY : 513151.88679245283\n",
      "BOOKS_AND_REFERENCE : 8767811.894736841\n",
      "BUSINESS : 1712290.1474201474\n",
      "COMICS : 817657.2727272727\n",
      "COMMUNICATION : 38456119.167247385\n",
      "DATING : 854028.8303030303\n",
      "EDUCATION : 1833495.145631068\n",
      "ENTERTAINMENT : 11640705.88235294\n",
      "EVENTS : 253542.22222222222\n",
      "FINANCE : 1387692.475609756\n",
      "FOOD_AND_DRINK : 1924897.7363636363\n",
      "HEALTH_AND_FITNESS : 4188821.9853479853\n",
      "HOUSE_AND_HOME : 1331540.5616438356\n",
      "LIBRARIES_AND_DEMO : 638503.734939759\n",
      "LIFESTYLE : 1437816.2687861272\n",
      "GAME : 15588015.603248259\n",
      "FAMILY : 3695641.8198090694\n",
      "MEDICAL : 120550.61980830671\n",
      "SOCIAL : 23253652.127118643\n",
      "SHOPPING : 7036877.311557789\n",
      "PHOTOGRAPHY : 17840110.40229885\n",
      "SPORTS : 3638640.1428571427\n",
      "TRAVEL_AND_LOCAL : 13984077.710144928\n",
      "TOOLS : 10801391.298666667\n",
      "PERSONALIZATION : 5201482.6122448975\n",
      "PRODUCTIVITY : 16787331.344927534\n",
      "PARENTING : 542603.6206896552\n",
      "WEATHER : 5074486.197183099\n",
      "VIDEO_PLAYERS : 24727872.452830188\n",
      "NEWS_AND_MAGAZINES : 9549178.467741935\n",
      "MAPS_AND_NAVIGATION : 4056941.7741935486\n"
     ]
    }
   ],
   "source": [
    "android_category = freq_table(free_android_app, 1)\n",
    "\n",
    "for category in android_category: \n",
    "    total = 0\n",
    "    len_category = 0\n",
    "    for app in free_android_app: \n",
    "        category_app = app[1]\n",
    "        if category_app == category: \n",
    "            install = app[5].replace(\"+\", \"\")\n",
    "            install = install.replace(\",\", \"\")\n",
    "            total += float(install)\n",
    "            len_category += 1\n",
    "    average = total / len_category\n",
    "    print(category, \":\", average)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Based on the data, a promising app profile for Google Play is a\n",
      "Books & Reference or Productivity app. These categories have a\n",
      "strong install base while facing less competition than gaming or\n",
      "social media apps. Books & Reference apps (8.7M installs on avg.)\n",
      "can be monetized through premium content or subscriptions, while\n",
      "Productivity apps (16.7M installs on avg.) attract both casual and\n",
      "professional users, offering potential for paid features. Both\n",
      "categories align well with trends on the App Store, making them\n",
      "ideal for cross-platform success.\n"
     ]
    }
   ],
   "source": [
    "print(\"Based on the data, a promising app profile for Google Play is a\")\n",
    "print(\"Books & Reference or Productivity app. These categories have a\")\n",
    "print(\"strong install base while facing less competition than gaming or\")\n",
    "print(\"social media apps. Books & Reference apps (8.7M installs on avg.)\")\n",
    "print(\"can be monetized through premium content or subscriptions, while\")\n",
    "print(\"Productivity apps (16.7M installs on avg.) attract both casual and\")\n",
    "print(\"professional users, offering potential for paid features. Both\")\n",
    "print(\"categories align well with trends on the App Store, making them\")\n",
    "print(\"ideal for cross-platform success.\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

