# Journal

This is a journal of how I wrote this program, and what was my thought process. 

What is the problem?
Higher Lower Game in python. I will be comparing two people, things, or topics, and I would choose who is more famous. The winner topic will be compared to a new topic. When you get it right you score one point and if you make a mistake you lose a life. You have try lives, and if you run out of lives, game over. 

## Breakdown of the program.
 - The art - Done
 - data for comparison -  Done
 - asking the player to compare and vote - Done
 - if right; update the score - Done
 - if wrong; update the lives - Done
 - remember the wining topic - Done
 - compare it with a new topic - Done

## Formatting Data
The data is create in a list with each element of the list being a dictionary.   
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    }
I create a new functionn format(person). This function takes a dictionary, stores each key value pair as variable and value. Finally it returns the full string as output of the function. 

## Data comparison:
I created a new function compare(a,b). This function would compare the followers of person One with person Two. If person One followers is biggers return A otherwise return B



