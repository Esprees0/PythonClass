import matplotlib.pyplot as plt
def main():
    sales = [25,25,30,20]
    slice_lables = ['1st Qtr','2nd Qtr','3rd Qtr','4th Qtr']
    plt.bar(sales,slice_lables,color=('r','m','g','k'))
    plt.pie(sales,labels=slice_lables)
    plt.title('Sales by Quarter')
    plt.show()
main()