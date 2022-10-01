# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line
#1 Write a function farm_action that takes the seven factors as arguments in the order they are listed above, and returns a single string containing the action(s) the farmer should take. 
#2 Under some combination of conditions the function needs to return multiple actions. This happens when cows can be milked, the land can be fertilized or the grass can be mown.
#3 The format for returning multiple actions is to return a string with each action on its own line, in order. The last line should not end on a newline.

def main():
    weather = ["rainy", "sunny", "windy", "neutral"]
    time_of_the_day = ["day", "night"]
    cow_milking_status = [True, False]
    location_of_the_cows = ["pasture", "cowshed"]
    season = ["winter", "spring", "summer", "fall"]
    slurry_tank = [True, False]
    grass_status = [True, False]

def farm_action(
    weather,
    time_of_day,
    cow_milking_status,
    location_of_the_cows,
    season,
    slurry_tank,
    grass_status,
):
    if (
        time_of_day == "night"
        and location_of_the_cows == "pasture"
        or location_of_the_cows == "pasture"
        and weather == "rainy"
    ):
        return "take cows to cowshed"
    if cow_milking_status == True and location_of_the_cows == "cowshed":
        return "milk cows"
    if cow_milking_status == True and location_of_the_cows == "pasture":
        return "take cows to cowshed\nmilk cows\ntake cows back to pasture"
    if (
        slurry_tank == True
        and location_of_the_cows == "cowshed"
        and (weather != "sunny" or "windy")
    ):
        return "fertilize pasture"
    if (
        slurry_tank == True
        and location_of_the_cows == "pasture"
        and (weather != "sunny" or "windy")
    ):
        return "take cows to cowshed\nfertilize pasture\ntake cows back to pasture"
    if (
        grass_status == True
        and season == "spring"
        and weather == "sunny"
        and location_of_the_cows != "pasture"
        and time_of_day != "night"
    ):
        return "mow grass"
    if (
        grass_status == True
        and season == "spring"
        and weather == "sunny"
        and location_of_the_cows == "pasture"
        and time_of_day != "night"
    ):
        return "take cows to cowshed\nmow grass\ntake cows back to pasture"
    else:
        return "wait"