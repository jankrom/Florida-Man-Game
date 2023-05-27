import sys
sys.path.append('../')
from cmu_112_graphics import *

def edu_appStarted(app):
    imgUrl = app.path + '/education/boatscreen.jpg'
    app.boatScreen1 = app.loadImage(imgUrl)
    app.boatScreen = app.scaleImage(app.boatScreen1, .4)
    imgUrl = app.path + '/education/FishingScreen.jpg'
    app.fishingScreen1 = app.loadImage(imgUrl)
    app.fishingScreen = app.scaleImage(app.fishingScreen1, .3)
    imgUrl = app.path + '/education/MapScreen.jpg'
    app.mapScreen1 = app.loadImage(imgUrl)
    app.mapScreen = app.scaleImage(app.mapScreen1, .4)

##########################################
# Intro to Education Screens Mode
##########################################

def eduIntroMode_redrawAll(app, canvas):
    message1 = ''' 
                Before we begin the game, take time to learn some 
                information about overfishing and how the problem can 
                impact society. This information will be very useful 
                when we start the game! Pay special attention to the 
                types of fish in Florida waters, specifically the ones 
                you should or shouldn't fish. 
                '''
    canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(app.floridaBackground))
    canvas.create_text(.9*app.width/3, 1.5*app.height/5, 
                        text='Welcome to the Rulebook!', font='Arial 28 bold')
    canvas.create_text(.8*app.width/3, 2.5*app.height/5, text= message1, font= 'Arial 14')
    canvas.create_text(.8*app.width/3, 3.5*app.height/5, text='Press any key to start learning!', font= 'Arial 20')

def eduIntroMode_keyPressed(app, event):
    app.mode = 'eduPg1Mode'

#########################################################
# Educational Mode, Page 1 of Information on Overfishing
#
# Sources for Information:
#  https://www.newsecuritybeat.org/2018/08/water-oil-fish-geostrategic-resource/
#
#  https://www.theworldcounts.com/challenges/planet-earth/oceans/overfishing-statistics/story
# 
#  http://sfmn.fiu.edu/the-impact-of-overfishing-on-the-economy-ecosystem-and-social-life/
#########################################################

def eduPg1Mode_redrawAll(app, canvas):
    message2 = ''' 
                Globally, overfishing is a massive problem 
                that has the potential to cause major harms. 
                Nearly 1 billion people rely on fish as their 
                primary food source, and 260 million people
                earn their living through marine fisheries. If 
                this sector were to collapse, all of these people 
                would be put at risk. We are too close to the 
                breaking point. Nearly 80 percent of the world's 
                fish are either fully exploited, over-exploited, 
                depleted, or in collapse. For large predatory fish,
                that number increases to 90 percent of the stock 
                being gone. If governments don't start to make 
                drastic changes, fishermen will continue to exploit 
                fish stock to meet rising demand from our growing 
                population. At the current rate, studies show that 
                we will run out of seafood by 2048. 
                '''
    message3 = '''
                This problem isn't confined to distant 
                oceans across the globe-- it's closer than 
                we realize. In Florida, overfishing risks 
                the $9.2 billion dollar annual saltwater 
                fishing industry, as well as the worth of the
                coral reefs, an additional $375 billion a year.
                On top of that, Florida is the birthplace of 
                many fish that eventually migrate throughout 
                the Atlantic, Carribean, and Gulf of Mexico. 
                Overfishing in Florida would disrupt food 
                chains across all of these oceans, cascading 
                across more species than just the exploited 
                ones.
                '''
    canvas.create_rectangle(0, 0, app.width, app.height, fill = "light blue")
    canvas.create_rectangle(app.width/50, 45.5*app.height/50, 49*app.width/50, 49.5*app.height/50, fill = "white")
    canvas.create_image(1.1*app.width/5, .65*app.height/2, image=ImageTk.PhotoImage(app.overfishing))
    canvas.create_image(3*app.width/4, 2.97*app.height/4, image=ImageTk.PhotoImage(app.OFmap))
    canvas.create_text(app.width/2, .9*app.height/10, 
                        text='Overfishing', font='Arial 30 bold underline')
    canvas.create_text(2.7*app.width/4, 1.75*app.height/5, text= message2, font= 'Arial 14')
    canvas.create_text(.85*app.width/4, 3.6*app.height/5, text= message3, font= 'Arial 14')
    canvas.create_text(app.width/2, 4.65*app.height/5, text='If at any point you want to skip to the game, press space!', font= 'Arial 20')
    canvas.create_text(app.width/2, 4.85*app.height/5, text='If at any point you want to go back, press backspace!', font= 'Arial 20')


def eduPg1Mode_keyPressed(app, event):
    if (event.key == 'Space'):
        app.mode = 'map'
    elif (event.key == 'Backspace'):
        app.mode = 'eduIntroMode'
    else:
        app.mode = 'eduPg2Mode'

#########################################################
# Educational Mode, Page 2 of Information on Good Fish
#
# Sources for Information:
#  https://www.visitflorida.com/travel-ideas/articles/florida-fishing-top-10-popular-fish-in-fl/
#
#  https://fishingbooker.com/blog/tarpon-fishing-in-florida/
#
#  https://www.hawkscay.com/experience/florida-keys-fishing-charters/tarpon-backcountry-fishing 
#
#  https://captrichknox.com/trout-fishing.html
#########################################################

def eduPg2Mode_redrawAll(app, canvas):
    message1 = ''' 
                Considering Florida has nearly 8,000 lakes, over 10,500 miles of
                rivers, and nearly 2,500 miles of shoreline, fishing is a common
                passtime of its many residents and visitors. There are a number
                of commonly caught fish in Florida, either for sport or 
                consumption. Two of such fish are the Tarpon and Trout:
                '''
    message2 = ''' 
                Tarpon is one of the most popular gamefish, valued for their
                fighting ability and acrobatics at the end of a line moreso
                than for their value as food. When hooked, they can jump 
                over 10 feet out of the water, and are known for rattling 
                their gills like a snake when upset. Such fish are found all 
                over Florida, preferring the area's mild water temperatures 
                and living in a wide range of salinities, and can reach a 
                size of 8 feet long and 280 pounds, making them an ideal 
                catch for fisherman wanting a challenge.
                '''
    message3 = '''
                Trout are found across the east coast from New York to 
                Florida, and are often between 20 and 30 inches long
                and 4 to 10 pounds. The spotted sea trout specifically 
                is considered one of Florida's most popular gamefish 
                because of how easy they are to find and how likely they 
                are to bite a lure, while still being aggressive when 
                hooked, adding to the difficulty and their appeal as a
                sport fish. 
                '''
    canvas.create_rectangle(0, 0, app.width, app.height, fill = "light blue")
    canvas.create_rectangle(app.width/50, 45.5*app.height/50, 49*app.width/50, 49.5*app.height/50, fill = "white")
    canvas.create_image(.9*app.width/5, .9*app.height/2, image=ImageTk.PhotoImage(app.tarpon))
    canvas.create_image(3.2*app.width/4, 2.9*app.height/4, image=ImageTk.PhotoImage(app.trout))
    canvas.create_text(.85*app.width/2, 1.1*app.height/5, text= message1, font= 'Arial 18')
    canvas.create_text(2.5*app.width/4, 2.3*app.height/5, text= message2, font= 'Arial 14')
    canvas.create_text(1.2*app.width/4, 3.6*app.height/5, text= message3, font= 'Arial 14')
    canvas.create_text(app.width/2, app.height/10, 
                        text='Ideal Fish to Hook', font='Arial 30 bold underline')
    canvas.create_text(app.width/2, 4.65*app.height/5, text='If at any point you want to skip to the game, press space!', font= 'Arial 20')
    canvas.create_text(app.width/2, 4.85*app.height/5, text='If at any point you want to go back, press backspace!', font= 'Arial 20')


def eduPg2Mode_keyPressed(app, event):
    if (event.key == 'Space'):
        app.mode = 'map'
    elif (event.key == 'Backspace'):
        app.mode = 'eduPg1Mode'
    else:
        app.mode = 'eduPg3Mode'


#############################################################
# Educational Mode, Page 3 of Information on Overfished Fish
#
# Sources for Information:
#  https://www.nature.org/en-us/about-us/where-we-work/united-states/florida/stories-in-florida/snapper-grouper-fisheries/
#
#  https://www.fisheries.noaa.gov/history-management-gulf-mexico-red-snapper
# 
#  https://www.nationalgeographic.com/animals/article/florida-considering-opening-a-fishery-for-endangered-goliath-grouper 
#
#########################################################

def eduPg3Mode_redrawAll(app, canvas):
    message1 = ''' 
                Of the many fish that are harvested off the coast of Florida, species 
                of snapper and grouper are the most at risk for overfishing-- up to 
                55 different species! Such fish are crucial to the biodiversity of 
                the ecosystem, and help control populations of smaller fish by acting 
                as predators.
                '''
    message2 = ''' 
                Red snapper has historically been overfished, with the 
                overuse of the resource dating back to the 1850s. Through 
                the 1970's and 80's, the population of the fish was so 
                depleted that the spawning potential hit 2%, so low that the
                population couldn't be sustained. Through government 
                intervention through the 90's and early 2000's, the stock is 
                officially recovering, but fishers should still avoid risking 
                overfishing, and the fish is still classified as "rebuilding".
                '''
    message3 = '''
                Certain species of grouper are known to weigh up to 800 
                pounds, which make them likely targets for fishers. As a 
                result, they have been on Florida's fishing ban list since 
                the 1990s, following their near extinction due to overfishing 
                in the past. As a result, certain grouper species are still 
                classified as "vulnerable", which is a step up from their 
                "critically endangered" status of 3 years ago. 
                '''
    canvas.create_rectangle(0, 0, app.width, app.height, fill = "light blue")
    canvas.create_rectangle(app.width/50, 45.5*app.height/50, 49*app.width/50, 49.5*app.height/50, fill = "white")
    canvas.create_image(.9*app.width/5, .9*app.height/2, image=ImageTk.PhotoImage(app.redSnapper))
    canvas.create_image(3.2*app.width/4, 2.9*app.height/4, image=ImageTk.PhotoImage(app.grouper))
    canvas.create_text(app.width/2, app.height/10, 
                        text='Overfished Populations', font='Arial 30 bold underline')
    canvas.create_text(.9*app.width/2, 1.2*app.height/5, text= message1, font= 'Arial 18')
    canvas.create_text(2.5*app.width/4, 2.3*app.height/5, text= message2, font= 'Arial 14')
    canvas.create_text(1.2*app.width/4, 3.6*app.height/5, text= message3, font= 'Arial 14')
    canvas.create_text(app.width/2, 4.65*app.height/5, text='If at any point you want to skip to the game, press space!', font= 'Arial 20')
    canvas.create_text(app.width/2, 4.85*app.height/5, text='If at any point you want to go back, press backspace!', font= 'Arial 20')


def eduPg3Mode_keyPressed(app, event):
    if (event.key == 'Space'):
        app.mode = 'map'
    elif (event.key == 'Backspace'):
        app.mode = 'eduPg2Mode'
    else:
        app.mode = 'eduPg4Mode'

###########################################################
# Educational Mode, Page 4 of Information on Invasive Fish
#
# Sources for Information:
#  https://www.cbsnews.com/news/florida-arapaima-new-invasive-species/ 
#  
#  https://www.wtsp.com/article/life/animals/10-foot-long-amazonian-river-monster-showed-up-in-florida/67-7fcd96d7-1f91-4743-9f63-7dec7f2d7805
#
#########################################################

def eduPg4Mode_redrawAll(app, canvas):
    message1 = ''' 
                Any area full of ports opens themselves up for invasion by invasive
                species, and Florida is no exception. From the Burmese python
                to the green iguana to the lionfish, Florida wildlife is 
                constantly at risk from invasive populations. Earlier in 2021, a
                new species is threatening Florida aquatic wildlife: the Arapaima.
                '''
    message2 = ''' 
                The Arapaima is the latest potential invasive species
                to be spotted in Florida, a massive monster fish that
                can grow up to 10 feet long and weigh up to 440 pounds.
                Such fish originate in the Amazon, namely Brazil, Peru,
                and Guyana. It is one of the world's largest predatory
                fish, with nearly impenetrable scales and the ability
                to survive 24 hours outside water. The Arapaima can be 
                compared to a Tarpon, in that they have similar jumping
                abilities and often prey on smaller mammals and other
                fish. 
                '''
    message3 = '''
                This species is considered invasive because they are a threat to
                native wildlife in Florida, especially considered their wild and
                varied appetite and quick reproductive capabilities, allowing 
                them to outcompete local wildlife easily if they reach full
                capacity. This threatens both commercially and economically
                important fish. Luckily, this invasive species is rare and hasn't
                been shown to have widescale reproduction yet, so the Florida
                ecosystem is safe for now. 
                '''
    canvas.create_rectangle(0, 0, app.width, app.height, fill = "light blue")
    canvas.create_rectangle(app.width/50, 45.5*app.height/50, 49*app.width/50, 49.5*app.height/50, fill = "white")    
    canvas.create_image(.75*app.width/4, .9*app.height/2, image=ImageTk.PhotoImage(app.arapaima))
    canvas.create_text(app.width/2, app.height/10, 
                        text='Invasive Species', font='Arial 30 bold underline')
    canvas.create_text(.85*app.width/2, 1.1*app.height/5, text= message1, font= 'Arial 18')
    canvas.create_text(2.5*app.width/4, 2.35*app.height/5, text= message2, font= 'Arial 14')
    canvas.create_text(.85*app.width/2, 3.8*app.height/5, text= message3, font= 'Arial 18')
    canvas.create_text(app.width/2, 4.65*app.height/5, text='If at any point you want to skip to the game, press space!', font= 'Arial 20')
    canvas.create_text(app.width/2, 4.85*app.height/5, text='If at any point you want to go back, press backspace!', font= 'Arial 20')


def eduPg4Mode_keyPressed(app, event):
    if (event.key == 'Space'):
        app.mode = 'map'
    elif (event.key == 'Backspace'):
        app.mode = 'eduPg3Mode'
    else:
        app.mode = 'eduPg6Mode'


#########################################################
# Educational Mode, Page 6 of Information on Game Goals
#
#########################################################

def eduPg6Mode_redrawAll(app, canvas):
    message1 = ''' 
                The object of the game is simple: be the best fisherman for the 
                environment! Try to earn as many points as possible by catching
                the right kind of fish: hook the fish with large populations and
                get a bonus for removing invasive species from the waters, but
                avoid hooking overfished populations at all costs! There are 3 
                parts to the game:
                '''
    message2 = '''
                The first part of the game is to 
                choose the section of Florida that 
                you want to go fishing in! Simply
                click in a region off the coast of
                Florida to choose your location. 
                Don't worry too much about this 
                step: it just helps us determine 
                how to set up the environment 
                you're going to fish in!
                '''
    canvas.create_rectangle(0, 0, app.width, app.height, fill = "light blue")
    canvas.create_rectangle(app.width/50, 45.5*app.height/50, 49*app.width/50, 49.5*app.height/50, fill = "white")
    canvas.create_text(app.width/2, app.height/10, 
                        text='How To Play:', font='Arial 30 bold underline')
    canvas.create_image(2.9*app.width/4, 3.2*app.height/5, image=ImageTk.PhotoImage(app.mapScreen))
    canvas.create_text(.85*app.width/2, 1.4*app.height/5, text= message1, font= 'Arial 20')
    canvas.create_text(app.width/5, 1.2*app.height/2, text= message2, font= 'Arial 14')
    canvas.create_text(app.width/2, 4.65*app.height/5, text='If at any point you want to skip to the game, press space!', font= 'Arial 20')
    canvas.create_text(app.width/2, 4.85*app.height/5, text='If at any point you want to go back, press backspace!', font= 'Arial 20')


def eduPg6Mode_keyPressed(app, event):
    if (event.key == 'Space'):
        app.mode = 'map'
    elif (event.key == 'Backspace'):
        app.mode = 'eduPg4Mode'
    else:
        app.mode = 'eduPg6_2Mode'

##############################################################
# Educational Mode, Page 6 of Information on Game Goals Part 2
#
##############################################################

def eduPg6_2Mode_redrawAll(app, canvas):
    message1 = ''' 
                The object of the game is simple: be the best fisherman for the 
                environment! Try to earn as many points as possible by catching
                the right kind of fish: hook the fish with large populations and
                get a bonus for removing invasive species from the waters, but
                avoid hooking overfished populations at all costs! There are 3 
                parts to the game:
                '''
    message2 = '''
                The second part of the game is to move the 
                boat through the water to choose the section 
                of that part of the ocean you want to stop 
                and fish in. Simply use the arrow keys and
                the specified letters to move the boat and 
                look around your surroundings:

                To move the boat:
                Up arrow = forwards
                Right arrow = turn right
                Left arrow = turn left

                To look around the boat:
                W = pan up
                S = pan down
                '''
    canvas.create_rectangle(0, 0, app.width, app.height, fill = "light blue")
    canvas.create_rectangle(app.width/50, 45.5*app.height/50, 49*app.width/50, 49.5*app.height/50, fill = "white")
    canvas.create_text(app.width/2, app.height/10, 
                        text='How To Play:', font='Arial 30 bold underline')
    canvas.create_image(2.9*app.width/4, 3.2*app.height/5, image=ImageTk.PhotoImage(app.boatScreen))
    canvas.create_text(.85*app.width/2, 1.4*app.height/5, text= message1, font= 'Arial 20')
    canvas.create_text(app.width/5, 1.3*app.height/2, text= message2, font= 'Arial 14')
    canvas.create_text(app.width/2, 4.65*app.height/5, text='If at any point you want to skip to the game, press space!', font= 'Arial 20')
    canvas.create_text(app.width/2, 4.85*app.height/5, text='If at any point you want to go back, press backspace!', font= 'Arial 20')


def eduPg6_2Mode_keyPressed(app, event):
    if (event.key == 'Space'):
        app.mode = 'map'
    elif (event.key == 'Backspace'):
        app.mode = 'eduPg6Mode'
    else:
        app.mode = 'eduPg6_3Mode'

##############################################################
# Educational Mode, Page 6 of Information on Game Goals Part 3
#
##############################################################

def eduPg6_3Mode_redrawAll(app, canvas):
    message1 = ''' 
                The object of the game is simple: be the best fisherman for the 
                environment! Try to earn as many points as possible by catching
                the right kind of fish: hook the fish with large populations and
                get a bonus for removing invasive species from the waters, but
                avoid hooking overfished populations at all costs! There are 3 
                parts to the game:
                '''
    message2 = '''
                The third part of the game is to fish! Use the up 
                and down arrow keys to move the hook up and down 
                to catch fish. Remember: a fish will only be caught
                if you bring the hook into the same region as the 
                fish's mouth, so pay attention to the direction the 
                fish is going. Once you hook a fish, bring it all 
                the way up to the boat to get your score counted and 
                to free up the hook to catch more fish-- you can only 
                hook one at a time!
                
                Remember to target only the well-populated species 
                and the invasive species, and to avoid the overfished 
                species and any alligators. There is no way to get a 
                fish off your hook, so if you accidentally hook an 
                overfished species you have no choice but to take the 
                penalty. If you hit an alligator with the hook anywhere, 
                not just on the mouth, you get kicked out of your location 
                and can no longer fish there. 
                '''
    canvas.create_rectangle(0, 0, app.width, app.height, fill = "light blue")
    canvas.create_rectangle(app.width/50, 45.5*app.height/50, 49*app.width/50, 49.5*app.height/50, fill = "white")
    canvas.create_text(app.width/2, app.height/10, 
                        text='How To Play:', font='Arial 30 bold underline')
    canvas.create_image(3.2*app.width/4, 3*app.height/5, image=ImageTk.PhotoImage(app.fishingScreen))
    canvas.create_text(.85*app.width/2, 1.4*app.height/5, text= message1, font= 'Arial 20')
    canvas.create_text(1.3*app.width/5, 1.3*app.height/2, text= message2, font= 'Arial 14')
    canvas.create_text(app.width/2, 4.65*app.height/5, text='If at any point you want to skip to the game, press space!', font= 'Arial 20')
    canvas.create_text(app.width/2, 4.85*app.height/5, text='If at any point you want to go back, press backspace!', font= 'Arial 20')


def eduPg6_3Mode_keyPressed(app, event):
    if (event.key == 'Space'):
        app.mode = 'map'
    elif (event.key == 'Backspace'):
        app.mode = 'eduPg6_2Mode'
    else:
        app.mode = 'eduPg7Mode'

#########################################################
# Educational Mode, Page 7 of Information on Points
#
#########################################################

def eduPg7Mode_redrawAll(app, canvas):
    message1 = ''' 
                Here are the points for each fish:
                '''
    message2 = ''' 
                For the fish that have ample populations 
                in Florida waters, you earn one point per 
                fish that you catch.
                Grey fish are the tarpon, and yellow fish 
                are the trout, so aim for yellow and grey 
                fish!
                '''
    message3 = ''' 
                For the fish that are overfished, you 
                lose 2 points for every fish you catch.
                Orange fish are red snapper and brown 
                fish are grouper, so avoid the red and 
                brown fish!
                '''
    message4 = ''' 
                For the fish that are invasive species, you 
                get a bonus for removing them from Florida 
                waters, and earn 3 points for every fish you catch.
                Green fish are the arapaima, so aim for the green
                fish too for the extra bonus!
                '''
    message5 = ''' 
                Watch out for alligators! They halt your fishing progress and force you to move to a different location. 
                '''
    canvas.create_rectangle(0, 0, app.width, app.height, fill = "light blue")
    canvas.create_rectangle(app.width/50, 45.5*app.height/50, 49*app.width/50, 49.5*app.height/50, fill = "white")
    canvas.create_text(app.width/2, app.height/10, 
                        text='How To Win', font='Arial 30 bold underline')
    canvas.create_image(.8*app.width/5, .95*app.height/2, image=ImageTk.PhotoImage(app.redSnapper))
    canvas.create_image(1.6*app.width/4, 2.2*app.height/4, image=ImageTk.PhotoImage(app.grouper))
    canvas.create_image(3.2*app.width/5, 1.35*app.height/5, image=ImageTk.PhotoImage(app.tarpon))
    canvas.create_image(3.2*app.width/4, 2.1*app.height/5, image=ImageTk.PhotoImage(app.trout))
    canvas.create_image(3*app.width/4, 3.7*app.height/5, image=ImageTk.PhotoImage(app.arapaima))
    canvas.create_text(.85*app.width/2, .75*app.height/5, text= message1, font= 'Arial 20')
    canvas.create_text(.8*app.width/4, 1.5*app.height/5, text= message2, font= 'Arial 14')
    canvas.create_text(2.9*app.width/4, 2.9*app.height/5, text= message3, font= 'Arial 14')
    canvas.create_text(.9*app.width/4, 3.7*app.height/5, text= message4, font= 'Arial 14')
    canvas.create_text(.9*app.width/2, 4.4*app.height/5, text= message5, font= 'Arial 13')
    canvas.create_text(app.width/2, 4.65*app.height/5, text='If at any point you want to skip to the game, press space!', font= 'Arial 20')
    canvas.create_text(app.width/2, 4.85*app.height/5, text='If at any point you want to go back, press backspace!', font= 'Arial 20')


def eduPg7Mode_keyPressed(app, event):
    if (event.key == 'Space'):
        app.mode = 'map'
    elif (event.key == 'Backspace'):
        app.mode = 'eduPg6Mode'
    else:
        app.mode = 'map'


##########################################
# Help Mode
##########################################

# put all the pictures for the fish key here
# reminders that the man is trying to go to jail so you want to target
# overfished species first, and leave invasive species
# avoid alligators at all cost

def helpMode_redrawAll(app, canvas):
    message1 = ''' 
                Here are the points for each fish:
                '''
    message2 = ''' 
                For the fish that have ample populations 
                in Florida waters, you earn one point per 
                fish that you catch.
                Grey fish are the tarpon, and yellow fish 
                are the trout, so aim for yellow and grey 
                fish!
                '''
    message3 = ''' 
                For the fish that are overfished, you 
                lose 2 points for every fish you catch.
                Orange fish are red snapper and brown 
                fish are grouper, so avoid the red and 
                brown fish!
                '''
    message4 = ''' 
                For the fish that are invasive species, you 
                get a bonus for removing them from Florida 
                waters, and earn 3 points for every fish you catch.
                Green fish are the arapaima, so aim for the green
                fish too for the extra bonus!
                '''
    message5 = ''' 
                Watch out for alligators! They halt your fishing progress and force you to move to a different location. 
                '''
    canvas.create_rectangle(0, 0, app.width, app.height, fill = "light blue")
    canvas.create_rectangle(app.width/50, 45.5*app.height/50, 49*app.width/50, 49.5*app.height/50, fill = "white")
    canvas.create_text(app.width/2, app.height/10, 
                        text='Help Desk', font='Arial 30 bold underline')
    canvas.create_image(.8*app.width/5, .95*app.height/2, image=ImageTk.PhotoImage(app.redSnapper))
    canvas.create_image(1.6*app.width/4, 2.2*app.height/4, image=ImageTk.PhotoImage(app.grouper))
    canvas.create_image(3.2*app.width/5, 1.35*app.height/5, image=ImageTk.PhotoImage(app.tarpon))
    canvas.create_image(3.2*app.width/4, 2.1*app.height/5, image=ImageTk.PhotoImage(app.trout))
    canvas.create_image(3*app.width/4, 3.7*app.height/5, image=ImageTk.PhotoImage(app.arapaima))
    canvas.create_text(.85*app.width/2, .75*app.height/5, text= message1, font= 'Arial 20')
    canvas.create_text(.8*app.width/4, 1.5*app.height/5, text= message2, font= 'Arial 14')
    canvas.create_text(2.9*app.width/4, 2.9*app.height/5, text= message3, font= 'Arial 14')
    canvas.create_text(.9*app.width/4, 3.7*app.height/5, text= message4, font= 'Arial 14')
    canvas.create_text(.9*app.width/2, 4.4*app.height/5, text= message5, font= 'Arial 13')
    canvas.create_text(app.width/2, 4.65*app.height/5, text='If at any point you want to skip to the game, press space!', font= 'Arial 20')
    canvas.create_text(app.width/2, 4.85*app.height/5, text='If at any point you want to go back, press backspace!', font= 'Arial 20')


def helpMode_keyPressed(app, event):
    app.mode = 'map'

