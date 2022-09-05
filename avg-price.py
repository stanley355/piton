import requests
import numpy as np
import matplotlib.pyplot as plt

response = requests.get("http://localhost:8080/v1/reports/analysis/price/avg?code=CEKA")
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
ax.set_title('Average Price CEKA')
ax.set_xticks(x, labels)
ax.legend()

ax.bar_label(rects1, padding=1)
ax.bar_label(rects2, padding=1)
ax.bar_label(rects3, padding=1)
ax.bar_label(rects4, padding=1)

fig.tight_layout()

plt.show()
