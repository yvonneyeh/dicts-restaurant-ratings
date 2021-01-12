"""Restaurant rating lister."""


# put your code here

def restaurant_ratings(filename):

    # open score file
    opened_file = open(filename)

    # create empty dictionary
    ratings_dict = {}

    # read ratings in file, split lines:
    for line in opened_file:
        # strip the right whitespace from the lines
        sentences = line.rstrip()
        # seperate words by splitting colon
        full_restaurant_lst = sentences.split(":")
        #restaurant, score = sentences.split(":")
        # dictionay formatting (restaurant = key, value)
        restaurant = full_restaurant_lst[0]
        score = full_restaurant_lst[1]
        # for restaurant, score in full_restaurant_lst:
        # convert score string into integer
        ratings_dict[restaurant] = int(score)

def sorted_list(ratings_dict):
    for restaurant, score in sorted(ratings_dict.items()):
        print(f"{restaurant} is rated at {score}.")

restaurant_ratings('scores.txt')

    # turn keys into list then sort alphabetically
    
    # print(ratings_review)

    # put items into dictionary
        # for restaurant, score in full_restaurant_lst.items():
            # ratings_review[restaurant] = ratings_review.get(restaurant)
           
           
           
    # convert number string into integer

    #sort the items
       
    #         print (f'{restaurant} {score}')
    # return f'{restaurant} {score}'

        




# put ratings in alphabetical order by restaurant
# print f-string "restaurant is rated, score"







# ratings_review[full_restaurant_list[::2]] = full_restaurant_list[1::2]
# restaurants == full_restaurant_list[::2]
# ratings == full_restaurant_list[1::2]