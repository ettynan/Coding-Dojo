# # Part 1


# def draw_stars(list):

#     for idx, val in enumerate(list):
#         print "*" * val

# draw_stars([4,6,1,3,5,7,25])

 #Part 2


def draw_stars(list):

    for idx, val in enumerate(list):
        if(val>=0 and val <=9):
            print "*" * val
        else:
            print val[0].lower() * len(val)

draw_stars([4,"Tom",1,"Michael",5,7,"Jimmy Smith"])
