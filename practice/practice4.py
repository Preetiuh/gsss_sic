Farmer Problem Statement
Mahesh is a farmer and owns 80 acres of land. His land is equally divided into 5 segments.
He grows tomatoes in the 1st segment, potatoes in the 2nd segment, cabbage in the 3rd segment, sunflower in the 4th segment and sugarcane in the 5th segment.
He is converting his land from chemical-driven farming to chemical-free farming. Mahesh starts with the conversion of vegetables into chemical-free produce. He spends the first 6 months doing the same.
He then converts the sunflower land bank into chemical-free farming. This takes him another 4 months. Finally, he converts sugarcane into chemical-free farming over the next 4 months.
He gets a yield of the following for tomatoes. 30% of his tomato land gives him 10 tonne yield per acre.
The remaining 70% of his tomato land gives him 12 tonnes yield per acre. The selling price of tomato
is Rs. 7 per Kg.
The yield of potatoes is 10 tonnes per acre. He sells each kg at Rs. 20.
The yield of cabbage is 14 tonnes per acre. He sells each kg at Rs. 24.
The yield of sunflowers is 0.7 tonnes per acre. He sells each kg at Rs. 200.
The yield of sugarcane is 45 tonnes per acre. He sells each tonne at Rs. 4,000.
All the crops are sowed at the same time. Mahesh gets the above yield at the above-mentioned rate
in one crop cycle across his entire land of 80 acres.
What is
a. The overall sales achieved by Mahesh from the 80 acres of land.


# Each crop gets 16 acres (80 acres / 5)
acres = 16

# Sales = yield per acre × acres × price per kg 
tomato_sales = (0.3 * acres * 10 + 0.7 * acres * 12) * 1000 * 7
potato_sales = acres * 10 * 1000 * 20
cabbage_sales = acres * 14 * 1000 * 24
sunflower_sales = acres * 0.7 * 1000 * 200
sugarcane_sales = acres * 45 * 4000  # price per tonne

total = tomato_sales + potato_sales + cabbage_sales + sunflower_sales + sugarcane_sales
print("Total sales: Rs.", int(total))