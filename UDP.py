import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox, Button

num1 = 0B0110011001100000
num2 = 0B0101010101010101
num3 = 0B1000111100001100


def add(x, y):
    result = x + y
    if result > 0B1111111111111111:
        result = (result % 0B10000000000000000) + (result >> 16)

    return result

def result_process(n):
    
    number = n[2:]
    if len(number) < 16:
        number = '0' + number
    return number


sum = add(add(num1, num2), num3)
UDPsum = add(add(add(num1, num2), num3), ~sum + 0B10000000000000000)

textbox2 = TextBox(plt.axes([0.3, 0.7, 0.5, 0.075]), 'sum', initial=result_process(bin(sum)))
textbox3 = TextBox(plt.axes([0.3, 0.6, 0.5, 0.075]), 'check', initial=result_process(bin(UDPsum)))
button = Button(plt.axes([0.3, 0.5, 0.5, 0.075]), "check")


def button_click(event):
    textbox2.text = result_process(bin(sum))
    textbox3.text = result_process(bin(UDPsum))
    plt.show()


button.on_clicked(button_click)
plt.show()
