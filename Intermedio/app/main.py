import utils
import read_csv as csv
import charts
# import random

# data = [
#     {
#         "country": "Peru",
#         "population": 100000
#     },
#     {
#         "country": "Bolivia",
#         "population": 200000
#     },
#     {
#         "country": "Venezuela",
#         "population": 300000
#     }
# ]C
def run ():
    data = csv.read_csv('./public/world_population.csv')
    data = list(filter(lambda x: x['Continent'] == "South America", data))
    # country = input("Dijite el pais a graficar ")
    # country_selected = utils.population_by_country(data, country)
    # print(country_selected)
    # if len(country_selected) > 0:
    #     labels, values = utils.get_population(country_selected)
    #     charts.generate_bar_charts_v1(labels, values)
    labels = list(map(lambda l: l["Country/Territory"], data))
    lista = [item["World Population Percentage"] for item in data if 'World Population Percentage' in item]
    values = list(map(float, lista))
    charts.generate_pie_charts(labels, values)
if __name__ == '__main__':
    # run()
    a = {1,2}
    b = {2,3}
    print(a | b)