import requests
import numpy as np
import matplotlib.pyplot as plt

response = requests.get("http://localhost:8080/v1/reports/analysis/price/avg?code=IGAR")
res = response.json()
current_year = res['current_year']
three_year = res['three_year']
five_year = res['five_year']

labels = ['Current year', 'Three year', 'Five year']
asset_price = [current_year['asset_price'], three_year['asset_price'], five_year['asset_price']]
eps = [current_year['eps'], three_year['eps'], five_year['eps']]
price_limit = [current_year['price_limit'], three_year['price_limit'], five_year['price_limit']]
safety_price_limit = current_year['safety_price_limit'], three_year['safety_price_limit'], five_year['safety_price_limit']

x = np.arange(len(labels))  # the label locations
width = 0.20  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - 0.2, asset_price, width, label='Asset Price')
rects2 = ax.bar(x, eps, width, label='EPS')
rects3 = ax.bar(x + 0.2, price_limit, width, label='Price Limit')
rects4 = ax.bar(x + 0.4, safety_price_limit, width, label='Safety Price limit')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Price')
ax.set_title('Average Price IGAR')
ax.set_xticks(x, labels)
ax.legend()

ax.bar_label(rects1, padding=1)
ax.bar_label(rects2, padding=1)
ax.bar_label(rects3, padding=1)
ax.bar_label(rects4, padding=1)

fig.tight_layout()

plt.show()

# labels = ['G1', 'G2', 'G3', 'G4', 'G5']
# men_means = [20, 34, 30, 35, 27]
# women_means = [25, 32, 34, 20, 25]
# any_means = [22, 30, 34, 27, 21]

# x = np.arange(len(labels))  # the label locations
# width = 0.20  # the width of the bars


# print(x)
# print(x + 0.1)
# print(x + width/2)
# print(x - width)

# fig, ax = plt.subplots()
# rects1 = ax.bar(x - 0.2, men_means, width, label='Men')
# rects2 = ax.bar(x, women_means, width, label='Women')
# rects3 = ax.bar(x + 0.2, any_means, width, label='Any')
# rects4 = ax.bar(x + 0.4, any_means, width, label='Any')

# # Add some text for labels, title and custom x-axis tick labels, etc.
# ax.set_ylabel('Scores')
# ax.set_title('Scores by group and gender')
# ax.set_xticks(x, labels)
# ax.legend()

# ax.bar_label(rects1, padding=2)
# ax.bar_label(rects2, padding=2)
# ax.bar_label(rects3, padding=2)
# ax.bar_label(rects4, padding=2)

# fig.tight_layout()

# plt.show()