"""
This program aims to help identify children and people who are tagged missing on
social media

The process by which it works is to crawl popular social media sites that use
compatible api looking for posts with the phrases "missing" or "help find" among
other related statements. Then it cross references to see if the person has been
found.If not, the program runs through all "missing" people that have been found
by orphanages, policing institutions and media houses that use the service.
Once a match has been established, the contact details of the phone number either
included in the text post or image is sent to the party that currently has the
missing person.

Then the program replies all the posts it was able to find and use, indicating that
the person's relatives or family member has been contacted in order to create awareness
and get other agencies to implement the system


potential problems::
    Because the system can be manipulated by people who want to find others they are
    stalking and such, measures should be implemented to ensure that the program
    is used rightly

    Also, not all missing people will be found by responsible agencies thus finding
    such people might prove difficult

    Privacy converns and legal complications might arise


process breakdown::
                    process one
    program scrubs the internet for posts about missing people
    - program checks the recency and number of reposts as a check for authenticity
    - program sends a ping to agencies with a picture of the person
    - if the first ever post includes a last seen, the program includes this in
    the ping to help narrow the search
    - once the person is found(confirmation by reputable agency), a reply is sent
    to all posts to ensure that the post is no longer circulated unnecessarily



                        process two
    - agencies that sign on to the platform send a picture of the missing person
    to our database
    - the program then scrubs the internet looking for the very first post about
    the person being missing
    - the program contacts the sender of the post and then forwards the agency's
    contacts to that person
    - after confirmation of the person no longer being missing, the case file is
    marked as solved



potential expansions::
    - connections to national databases in order to match pictures of victims with
    registration pictures and then informing next of kin or parent of them being found
    - connection to cctv cameras in order to expand search for kidnapping victims
    - find social media accounts of people who have committed crime to help in
    crime fighting


components the program  will need:
    - crawler to search for relevant posts
    - AI to compare images to ensure that the pictures match the person
    - interraction bot to reply posts and messages of agencies (infomring them the
    person's relatives have been found) and people( informing them missing person
    has been located)
    - database to keep track of demography of missing people, time taken to find
    them among others
    - hardware to hold the computational power

features:
    - search for tweets in vicitiny

"""










"""
    rather than taking one picture and then searching the entirity of social media
    for a match and then moving on to the next picture, put a collection of pictures
    in a list and check for matches for each of them.
    This will save bandwidth and processing time


    drawbacks:
        will take longer to find matches for all the pictures depending on the
        number of images to be searched
"""

