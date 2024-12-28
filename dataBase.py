import sqlite3
connec = sqlite3.connect("ThirlledMagerzine.db")
cursor = connec.cursor()

# Creating table
line = '''
CREATE TABLE IF NOT EXISTS authors
    (
    id INTEGER PRIMARY KEY,
    name VARCHAR(80),
    job VARCHAR(30),
    city VARCHAR(30),
    picture VARCHAR(255)
    )
'''
cursor.execute(line)

line = '''
CREATE TABLE IF NOT EXISTS podcast
    (
    id INTEGER PRIMARY KEY,
    name VARCHAR(80),
    date VARCHAR(60),
    duration VARCHAR(50),
    picture VARCHAR(255)
    )
'''
cursor.execute(line)
line = '''
CREATE TABLE IF NOT EXISTS magerzines
    (
    id INTEGER PRIMARY KEY,
    catergory VARCHAR(80),
    author VARCHAR(60),
    title VARCHAR(80),
    duration VARCHAR(255),
    picture VARCHAR(255),
    discription VARCHAR(255)
    )
'''
cursor.execute(line)
line = '''
    INSERT INTO authors(name, job,city,picture) VALUES
    ("JK.Rowling","Artist", "London", "https://cdn.pixabay.com/photo/2019/03/18/13/22/person-4063084_960_720.jpg"),
    ("Pablo Picasso", "Painter", "Barcelona", "https://cdn.pixabay.com/photo/2020/02/22/21/20/mime-4871674_640.jpg"),
    ("Vincent van Gogh", "Painter", "Amsterdam","https://cdn.pixabay.com/photo/2019/03/17/17/43/asaxofono-4061555_640.jpg"),
    ("Frida Kahlo", "Painter", "Mexico City","https://cdn.pixabay.com/photo/2018/12/17/22/42/gian-3881445_640.jpg"),
    ("Banksy", "Street Artist", "Bristol","https://cdn.pixabay.com/photo/2016/10/22/02/37/musician-1759636_640.jpg"),
    ("Claude Monet", "Painter", "Paris","https://cdn.pixabay.com/photo/2020/03/12/15/29/beijing-or-beijing-4925388_640.jpg")
'''
cursor.execute(line)
connec.commit()

line = '''
    INSERT INTO podcast(name, date, duration,picture) VALUES
    ("The Daily", "November 23, 2024", "25 minutes","https://i.pinimg.com/236x/5e/03/8c/5e038c3f2aba00bac6d45db102f2fac9.jpg"),
    ("Serial", "October 18, 2024", "40 minutes","https://i.pinimg.com/enabled_lo_mid/236x/dd/01/fd/dd01fd9e430271d08d4766ac905a6f1e.jpg"),
    ("Stuff You Should Know", "November 22, 2024", "50 minutes","https://i.pinimg.com/474x/5a/72/67/5a7267177c3cab0c8882759acd2201b2.jpg"),
    ("How I Built This", "November 21, 2024", "45 minutes","https://i.pinimg.com/236x/d2/6d/90/d26d9061023d86dfe075a9256234027b.jpg"),
    ("The Joe Rogan Experience", "November 20, 2024", "3 hours 15 minutes","https://i.pinimg.com/236x/8c/e9/b3/8ce9b350cbdc30ea7c14f1d3bb35d1f4.jpg"),
    ("The Moth", "November 19, 2024", "1 hour","https://i.pinimg.com/enabled_lo_mid/236x/70/57/0f/70570f1396098b4db6af60587e80a9f8.jpg"),
    ("TED Talks Daily", "November 22, 2024", "10 minutes","https://i.pinimg.com/enabled_lo_mid/236x/02/e2/1f/02e21fd49920bb098f3c05703c0369fa.jpg"),
    ("Armchair Expert", "November 18, 2024", "1 hour 30 minutes","https://i.pinimg.com/enabled_lo_mid/474x/72/7e/23/727e2377ea0010abbe35773c586e8fb6.jpg"),
    ("Crime Junkie", "November 21, 2024", "1 hour 10 minutes","https://i.pinimg.com/enabled_lo_mid/236x/f1/0e/82/f10e820b22a9baa8807e4ed75ae6035a.jpg"),
    ("Call Her Daddy", "November 23, 2024", "55 minutes","https://i.pinimg.com/236x/9d/c8/8c/9dc88cb76834e92fd8388178335c93e5.jpg")

'''
cursor.execute(line)
connec.commit()

line = '''
    INSERT INTO magerzines (catergory, author, title, duration, picture, discription) VALUES
    ("Podcast Magazine", 
    "Podcast Industry", 
    "The Future of Podcasting", 
    "Monthly", 
    "https://i.pinimg.com/enabled_lo_mid/236x/3b/81/b0/3b81b0755e67dfe79049360d6f1982c1.jpg", 
    "Podcast Magazine covers the latest trends in the podcasting industry, featuring interviews with creators, industry professionals, and tips for improving podcast production."),

("Podcaster News", "Podcast News", "Top 10 Podcasts to Watch in 2024", "Monthly", "https://i.pinimg.com/enabled_lo_mid/236x/92/91/3b/92913b5fea241f670ec137b310e01cb8.jpg", 
"Podcaster News provides breaking news, reviews, and features about popular podcasts, offering insight into emerging podcast technologies and trends in the podcasting world."),
("History Hub",
"Historical Events", "Unveiling Ancient Mysteries",
"Weekly",
"https://i.pinimg.com/236x/1a/34/3a/1a343a1bb0578b8f2725084bd80d4f6d.jpg",
"A deep dive into historical events and untold stories from the past, featuring expert guests and thrilling narratives."),

("TechTalk Today",
"Technology & Innovation", "AI Revolution and Beyond",
"Bi-Weekly",
"https://i.pinimg.com/236x/e3/5e/22/e35e22805868665dd969ef6f38b39c01.jpg",
"Explore the latest advancements in technology, focusing on artificial intelligence, cybersecurity, and gadgets reshaping the future."),

("Mindful Living",
"Health & Wellness", "The Art of Meditation",
"Monthly",
"https://i.pinimg.com/236x/92/06/bf/9206bf1141552359332a309d10c2415f.jpg",
"Your guide to mental health and mindfulness practices, featuring expert advice, guided sessions, and inspiring personal stories."),

("Sports Chronicles",
"Sports", "Legends of the Game",
"Weekly",
"https://i.pinimg.com/236x/91/9b/e7/919be7c08fcba250c9c30617e9b4d690.jpg",
"Relive the greatest moments in sports history and hear from athletes and commentators about what drives their passion."),

("Business Edge",
"Entrepreneurship", "Startup Success Stories",
"Bi-Monthly",
"https://i.pinimg.com/236x/e2/5a/00/e25a00402fd34a7b5339b0e0a378c0f2.jpg",
"Get insights from successful entrepreneurs, learn innovative strategies, and stay ahead in the competitive business world."),
("Podcasting Weekly", "Podcast Reviews", "How to Grow Your Podcast Audience", "Weekly", "https://i.pinimg.com/enabled_lo_mid/236x/d2/f4/be/d2f4be3b8a8fde13de7df2ae4287fa42.jpg", 
"Podcasting Weekly is aimed at podcast creators, offering advice on marketing, growing audiences, and improving podcast quality with tips on podcast production and promotion.")
'''
cursor.execute(line)
connec.commit()
# print("----------------------")

# line = "SELECT * FROM authors WHERE name = 'JK.Rowling'"
# line = "SELECT * FROM authors LIMIT 3 "
# line =" SELECT * FROM authors ORDER BY column DESC LIMIT 3"
# cursor.execute(line)
# row = cursor.fetchall()
# print(row)

