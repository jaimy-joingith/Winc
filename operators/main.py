# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line
#1 Comparison between the two.
spoken_most_spain = "Spanish"
spoken_most_switz = "Switzerland"
#2 Most prevalent religion
prev_religion_spain = "Roman Catholic"
prev_religion_switz = "Roman Catholic"
#3 Name length capital
capital_name_spain = "Madrid"
capital_name_switz = "Bern"
#4 Gdp
gdp_spain = 1393351000000
gdp_switz = 7315020000000
#5 Population growth
growth_pop_spain = 0.13
growth_pop_switz = 0.65
#6 Population count
count_pop_spain = 47163418
count_pop_switz = 8508698
#7 check operators
print (spoken_most_spain is spoken_most_switz)
print (prev_religion_spain is prev_religion_switz)
print (len(capital_name_spain) == len(capital_name_spain))
print (gdp_switz <= gdp_spain)
print (growth_pop_spain <1 and growth_pop_switz <1)
print (count_pop_spain > 1000000 or count_pop_switz > 1000000)
print (count_pop_spain > 1000000 and count_pop_switz > 1000000)