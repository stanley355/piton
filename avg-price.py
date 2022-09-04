import requests
import json
import numpy as np
import matplotlib.pyplot as plt

response = requests.get("http://localhost:8080/v1/reports/analysis/price/avg?code=ARNA")
res = response.json()
current_year = res['current_year']
three_year = res['three_year']
five_year = res['five_year']

# set width of bar
barWidth = 0.20
fig = plt.subplots(figsize =(12, 8))

# set height of bar
asset_price = [current_year['asset_price'], three_year['asset_price'], five_year['asset_price']]
eps = [current_year['eps'], three_year['eps'], five_year['eps']]
price_limit = [current_year['price_limit'], three_year['price_limit'], five_year['price_limit']]
safety_price_limit = current_year['safety_price_limit'], three_year['safety_price_limit'], five_year['safety_price_limit']

# Set position of bar on X axis
br1 = np.arange(len(asset_price))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]
br4 = [x + barWidth for x in br3]

# Make the plot
plt.bar(br1, asset_price, color ='r', width = barWidth,
        edgecolor ='grey', label ='Asset price')
plt.bar(br2, eps, color ='g', width = barWidth,
        edgecolor ='grey', label ='EPS')
plt.bar(br3, price_limit, color ='b', width = barWidth,
        edgecolor ='grey', label ='Price Limit')
plt.bar(br4, safety_price_limit, color ='y', width = barWidth,
        edgecolor ='grey', label ='Safety Price Limit')

# Adding Xticks
plt.xlabel('ARNA', fontweight ='bold', fontsize = 14)
plt.ylabel('Avg Price', fontweight ='bold', fontsize = 14)
plt.xticks([r + barWidth for r in range(len(asset_price))],
        ['Current year', 'Three year', 'Five year'])

plt.legend()
plt.show()