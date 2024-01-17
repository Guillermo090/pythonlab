import matplotlib.pyplot as plt

def generate_bar_chart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.show()
    
def generate_second_pie_chart():
    labels = ['A', 'B', 'C']
    values = [200, 34, 120]
    
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('.pie.png')
    plt.close()

if __name__ == '__main__':
    labels = ['a','b','c']
    values = [10, 40, 80]
    # generate_bar_chart(labels, values)
    # generate_pie_chart(labels, values)
    generate_second_pie_chart()