# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line
#Part 1
#1 Variable leek_price integer value of 2
leek_price = 2
#2 Cast into a string with price
print('Leek is '+str(leek_price) + ' euro per kilo.')

#Part 2
#1 Order
leek_order = 'leek 4'
#2 en 3 Find, slicing and extract
leek_number = int(leek_order[leek_order.find('4')])
#3 Cast int

#4 Sum total 
sum_total = leek_number * leek_price
print(sum_total)

#Part 3
#1 Variable broccoli price and order
broccoli_price = 2.34
broccoli_order = 'broccoli 1.6'
#2 Total price order
broccoli_kgs =  float(broccoli_order[broccoli_order.find(    '1'):broccoli_order.find('6')+1])
#3 Assemble and broccoli_order.find('broccoli')
broccoli_total = round(broccoli_kgs* broccoli_price, 2)
print(str(broccoli_kgs) + 'kg broccoli costs ' + str(broccoli_total) + 'e')