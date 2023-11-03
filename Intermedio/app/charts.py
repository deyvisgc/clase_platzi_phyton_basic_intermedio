import matplotlib.pyplot as plt
def generate_bar_charts(labels, values, bar_labels, bar_colors):
   #fi => es la figura
   # ax => cordenas a grafica
#    fruits = ['apple', 'blueberry', 'cherry', 'orange']
#    counts = [40, 100, 30, 55]
#    bar_labels = ['red', 'blue', '_red', 'orange']
#    bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']
#    fig, ax = plt.subplots()
#    ax.bar(fruits, counts, label=bar_labels, color=bar_colors)
#    ax.set_ylabel('fruit supply')
#    ax.set_title('Fruit supply by kind and color')
#    ax.legend(title='Fruit color')
#    plt.show()
    fig, ax = plt.subplots()
    ax.bar(labels, values, label=bar_labels, color=bar_colors)
    plt.show()
def generate_bar_charts_v1(labels, values):
   #fi => es la figura
   # ax => cordenas a grafica
#    fruits = ['apple', 'blueberry', 'cherry', 'orange']
#    counts = [40, 100, 30, 55]
#    bar_labels = ['red', 'blue', '_red', 'orange']
#    bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']
#    fig, ax = plt.subplots()
#    ax.bar(fruits, counts, label=bar_labels, color=bar_colors)
#    ax.set_ylabel('fruit supply')
#    ax.set_title('Fruit supply by kind and color')
#    ax.legend(title='Fruit color')
#    plt.show()
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()    
def generate_pie_charts(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    # aqui organizo esta grafica y que este en forma de circulo
    ax.axis('equal')
    plt.show()
if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [100, 200, 80]
  bar_labels = ['red', 'blue', 'orange']
  bar_colors = ['tab:red', 'tab:blue', 'tab:orange']
  #generate_bar_charts(labels, values, bar_labels, bar_colors)
  generate_pie_charts(labels, values)