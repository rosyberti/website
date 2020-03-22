import pandas as pd
import matplotlib.pyplot as plt
import mpld3

test_data = pd.DataFrame(pd.read_csv('tests.csv'))
case_data = pd.DataFrame(pd.read_csv('cases.csv'))
death_data = pd.DataFrame(pd.read_csv('deaths.csv'))

plt.style.use('dark_background')
chart = plt.bar(test_data['State'],test_data['Coronavirus Tests Performed'])
mpld3.fig_to_html(chart)
