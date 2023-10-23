# David Loewy CIS345 TTH 1030 Final Project

import csv
from tkinter import *
from PIL import Image, ImageTk
import time
import os


# Order Class
class Order:
    def __init__(self, name, ordered_items):
        total = 0
        self.customer_name = name
        self.item_list = ordered_items
        for item in ordered_items:
            total = item_dict[item] + total
        self.order_total = total
        self.order_num = self.set_order_num()
        self.order_time = time.ctime()

    @classmethod
    def set_order_num(cls):
        global order_count
        order_count += 1
        return order_count

    @property
    def customer_name(self):
        return self._customer_name

    @customer_name.setter
    def customer_name(self, name):
        self._customer_name = name.capitalize()

    def __str__(self):
        return f'Order #{self.order_num}: {self.customer_name} | {self.item_list} | Total: ${self.order_total:.2f}'


# Function for when button is pressed on welcome screen
def menu_submit_button_pressed():
    c1.deselect()
    c2.deselect()
    c3.deselect()
    c4.deselect()
    c5.deselect()
    c6.deselect()

    # Create order
    if int(order_var.get()) == 1:
        welcome_box1.grid_forget()
        welcome_box2.grid_forget()
        add_box1.grid(columnspan=3)
        order_add_label.config(text='Enter orders:')
        add_box2.grid(columnspan=3, pady=20)
        add_box3.grid(columnspan=3, pady=20)
        add_box4.grid(columnspan=3, pady=20)

    # Edit order
    elif int(order_var.get()) == 2:
        welcome_box1.grid_forget()
        welcome_box2.grid_forget()
        add_box1.grid(columnspan=3)
        order_add_label.config(text='Edit orders:')
        edit_box2.grid(columnspan=3, pady=20)
        edit_box1.grid(columnspan=3, pady=20)
        edit_box3.grid(columnspan=3, pady=20)

    # Delete order
    elif int(order_var.get()) == 3:
        welcome_box1.grid_forget()
        welcome_box2.grid_forget()
        delete_box1.grid(columnspan=3, pady=20)
        delete_box2.grid(columnspan=3, pady=20)
        delete_box3.grid(columnspan=3, pady=20)

    # View orders
    elif int(order_var.get()) == 4:
        welcome_box1.grid_forget()
        welcome_box2.grid_forget()
        print_box1.grid(columnspan=3, pady=20)
        view_orders_label.config(text=print_orders())


def order_submit_button_pressed():
    global orders, cust_name
    orders_str = [menu_item1.get(), menu_item2.get(), menu_item3.get(),
                  menu_item4.get(), menu_item5.get(), menu_item6.get()]
    temp_orders = []
    for item in orders_str:
        if item == '':
            temp_orders.append(None)
        else:
            temp_orders.append(item)
    final_orders = list(filter(None, temp_orders))
    new_order = Order(cust_name.get(), final_orders)
    orders.append(new_order)
    order_confirmed.config(text=f'Order #{new_order.order_num}: Thank you {cust_name.get()}. '
                                f'Total is: ${new_order.order_total:.2f}')
    c1.deselect()
    c2.deselect()
    c3.deselect()
    c4.deselect()
    c5.deselect()
    c6.deselect()
    cust_name.set('')


def edit_submit_button_pressed():
    global orders, cust_name
    for order in orders:
        if order_edit.get() == order.order_num:
            orders_str = [menu_item1.get(), menu_item2.get(), menu_item3.get(),
                          menu_item4.get(), menu_item5.get(), menu_item6.get()]
            temp_orders = []
            for item in orders_str:
                if item == '':
                    temp_orders.append(None)
                else:
                    temp_orders.append(item)
            final_orders = list(filter(None, temp_orders))
            order.item_list = final_orders
            total = 0
            for item in final_orders:
                total = item_dict[item] + total
            order.order_total = total
            order.order_time = time.ctime()
            edit_confirmed.config(text='Order changed successfully.')
            c1_edit.deselect()
            c2_edit.deselect()
            c3_edit.deselect()
            c4_edit.deselect()
            c5_edit.deselect()
            c6_edit.deselect()
            order_edit.set(0)
            return
    edit_confirmed.config(text='No order found with this number.')


def delete_submit_button_pressed():
    global orders, cust_name
    for order in orders:
        if order_delete.get() == order.order_num:
            orders.remove(order)
            delete_confirmed.config(text='Order deleted successfully.')
            order_delete.set(0)
            return
    delete_confirmed.config(text='No order found with this number.')


def print_orders():
    global orders
    view_order_str = ''
    for item in orders:
        view_order_str = view_order_str + str(item) + '\n'
    return view_order_str


def return_menu():
    welcome_box1.grid(columnspan=3)
    welcome_box2.grid(columnspan=3)
    add_box1.grid_forget()
    add_box2.grid_forget()
    add_box3.grid_forget()
    add_box4.grid_forget()
    edit_box1.grid_forget()
    edit_box2.grid_forget()
    edit_box3.grid_forget()
    delete_box1.grid_forget()
    delete_box2.grid_forget()
    delete_box3.grid_forget()
    print_box1.grid_forget()


def exit_program():
    global orders
    if not os.path.isfile('orders.csv'):
        with open('orders.csv', 'w', newline='') as fp:
            data = csv.writer(fp)
            data.writerow(['Name', 'Items', 'Total Price', 'Order number', 'Order Time'])

    with open('orders.csv', 'a', newline='') as fp:
        data = csv.writer(fp)
        for order in orders:
            data.writerow([order.customer_name, order.item_list, order.order_total, order.order_num, order.order_time])

    win.destroy()


# Variable declarations
order_count = 0
item_dict = {'Krabby Patty': 6.25, 'Krabby Junior Patty': 3.25, 'Krabby Dog': 2.25,
             'Kelp Shake': 3.00, 'Krabby Fries': 3.50, 'Krusty Krab Pizza': 8.50}

# Tkinter creation
win = Tk()
win.title('Krusty Krab Ordering System')
win.geometry('400x600')
win.config(bg='#33B3FF')

orders = []
cust_name = StringVar()
menu_item1 = StringVar()
menu_item2 = StringVar()
menu_item3 = StringVar()
menu_item4 = StringVar()
menu_item5 = StringVar()
menu_item6 = StringVar()

# Image and icon for screens
logo = Image.open('Krusty_Krab.png')
logo = ImageTk.PhotoImage(logo)
logo_label = Label(image=logo)
logo_label.grid(columnspan=3, column=0, row=0, pady=5, padx=3)
win.iconbitmap('krabbypatty.ico')

# Welcome_box1 for welcome screen
welcome_box1 = Frame(win, bg='cornsilk', width=200, height=30,
                     borderwidth=5, relief=RIDGE)
welcome_box1.grid(columnspan=3, row=1, column=0, pady=(20, 20))
welcome_box1.grid_propagate(False)

welcome_label = Label(welcome_box1, text='Welcome to the Krusty Krab!', width=30, font=('Arial', 8),
                      bg='cornsilk')
welcome_label.grid(row=1, columnspan=3, pady=(0, 10))

# Welcome_box2, radio buttons, and submit button for welcome screen
welcome_box2 = Frame(win, bg='cornsilk', width=200, height=190,
                     borderwidth=5, relief=RIDGE)
welcome_box2.grid(columnspan=3, row=2, column=0)
welcome_box2.grid_propagate(False)

order_var = IntVar()

r1 = Radiobutton(welcome_box2, text='Add an order', variable=order_var, value=1, bg='cornsilk')
r1.grid(row=1, column=1, sticky=W)
r2 = Radiobutton(welcome_box2, text='Edit an order', variable=order_var, value=2, bg='cornsilk')
r2.grid(row=2, column=1, sticky=W)
r3 = Radiobutton(welcome_box2, text='Delete an order', variable=order_var, value=3, bg='cornsilk')
r3.grid(row=3, column=1, sticky=W)
r4 = Radiobutton(welcome_box2, text='View orders', variable=order_var, value=4, bg='cornsilk')
r4.grid(row=4, column=1, sticky=W)

welcome_b1 = Button(welcome_box2, text='Submit', command=menu_submit_button_pressed, bg='white', width=20)
welcome_b1.grid(row=5, column=1, padx=20, pady=5, sticky=W)

exit_button = Button(welcome_box2, text='Exit & Save to file', command=exit_program, bg='white', width=20)
exit_button.grid(row=6, column=1, padx=20, pady=5, sticky=W)

# Add_box1's 'Add order:' label
add_box1 = Frame(win, bg='cornsilk', width=200, height=30,
                 borderwidth=5, relief=RIDGE)
add_box1.grid_propagate(False)

order_add_label = Label(add_box1, text='', width=30, font=('Arial', 8),
                        bg='cornsilk')
order_add_label.grid(row=1, columnspan=3, pady=(0, 10))

# Add_box 2 for name entry for add order screen
add_box2 = Frame(win, bg='cornsilk', width=200, height=30,
                 borderwidth=5, relief=RIDGE)
name_entry_label = Label(add_box2, text='Enter your name:', bg='cornsilk')
name_entry_label.grid(row=0, column=0)
name_entry = Entry(add_box2, textvariable=cust_name)
name_entry.grid(row=1, column=0)

# Add_box3 and submit/menu buttons for add order screen
add_box3 = Frame(win, bg='cornsilk', width=200, height=190,
                 borderwidth=5, relief=RIDGE)
c1 = Checkbutton(add_box3, text='Krabby Patty: $6.25', bg='cornsilk', font=('Arial', 8),
                 variable=menu_item1, onvalue='Krabby Patty', offvalue='')
c1.grid(row=0, column=0, pady=2, sticky=W)
c2 = Checkbutton(add_box3, text='Krabby Junior Patty: $3.25', bg='cornsilk', font=('Arial', 8),
                 variable=menu_item2, onvalue='Krabby Junior Patty', offvalue='')
c2.grid(row=1, column=0, pady=2, sticky=W)
c3 = Checkbutton(add_box3, text='Krabby Dog: $2.25', bg='cornsilk', font=('Arial', 8),
                 variable=menu_item3, onvalue='Krabby Dog', offvalue='')
c3.grid(row=2, column=0, pady=2, sticky=W)
c4 = Checkbutton(add_box3, text='Kelp Shake: $3.00', bg='cornsilk', font=('Arial', 8),
                 variable=menu_item4, onvalue='Kelp Shake', offvalue='')
c4.grid(row=0, column=1, pady=2, sticky=W)
c5 = Checkbutton(add_box3, text='Krabby Fries: $3.50', bg='cornsilk', font=('Arial', 8),
                 variable=menu_item5, onvalue='Krabby Fries', offvalue='')
c5.grid(row=1, column=1, pady=2, sticky=W)
c6 = Checkbutton(add_box3, text='Krusty Krab Pizza: $8.50', bg='cornsilk', font=('Arial', 8),
                 variable=menu_item6, onvalue='Krusty Krab Pizza', offvalue='')
c6.grid(row=2, column=1, pady=2, sticky=W)

add_b1 = Button(add_box3, text='Submit', command=order_submit_button_pressed, bg='white', width=20)
add_b1.grid(row=5, column=0, pady=5, sticky=W)
add_b2 = Button(add_box3, text='Menu', command=return_menu, bg='white', width=20)
add_b2.grid(row=5, column=1, pady=5, sticky=W)

# Add_box 4 for order confirmation print out
add_box4 = Frame(win, bg='cornsilk', width=200, height=30,
                 borderwidth=5, relief=RIDGE)
order_confirmed = Label(add_box4, text='Order Confirmation', width=40, bg='cornsilk')
order_confirmed.grid(columnspan=3)

# Edit_box1 for checkboxes and submit/menu buttons
edit_box1 = Frame(win, bg='cornsilk', width=200, height=190,
                  borderwidth=5, relief=RIDGE)
c1_edit = Checkbutton(edit_box1, text='Krabby Patty: $6.25', bg='cornsilk', font=('Arial', 8),
                      variable=menu_item1, onvalue='Krabby Patty', offvalue='')
c1_edit.grid(row=0, column=0, pady=2, sticky=W)
c2_edit = Checkbutton(edit_box1, text='Krabby Junior Patty: $3.25', bg='cornsilk', font=('Arial', 8),
                      variable=menu_item2, onvalue='Krabby Junior Patty', offvalue='')
c2_edit.grid(row=1, column=0, pady=2, sticky=W)
c3_edit = Checkbutton(edit_box1, text='Krabby Dog: $2.25', bg='cornsilk', font=('Arial', 8),
                      variable=menu_item3, onvalue='Krabby Dog', offvalue='')
c3_edit.grid(row=2, column=0, pady=2, sticky=W)
c4_edit = Checkbutton(edit_box1, text='Kelp Shake: $3.00', bg='cornsilk', font=('Arial', 8),
                      variable=menu_item4, onvalue='Kelp Shake', offvalue='')
c4_edit.grid(row=0, column=1, pady=2, sticky=W)
c5_edit = Checkbutton(edit_box1, text='Krabby Fries: $3.50', bg='cornsilk', font=('Arial', 8),
                      variable=menu_item5, onvalue='Krabby Fries', offvalue='')
c5_edit.grid(row=1, column=1, pady=2, sticky=W)
c6_edit = Checkbutton(edit_box1, text='Krusty Krab Pizza: $8.50', bg='cornsilk', font=('Arial', 8),
                      variable=menu_item6, onvalue='Krusty Krab Pizza', offvalue='')
c6_edit.grid(row=2, column=1, pady=2, sticky=W)

submit_edit = Button(edit_box1, text='Submit', command=edit_submit_button_pressed, bg='white', width=20)
submit_edit.grid(row=5, column=0, pady=5, sticky=W)
menu_button2 = Button(edit_box1, text='Menu', command=return_menu, bg='white', width=20)
menu_button2.grid(row=5, column=1, pady=5, sticky=W)

order_edit = IntVar()

# Edit_box2 for order number label and text entry box
edit_box2 = Frame(win, bg='cornsilk', width=200, height=30,
                  borderwidth=5, relief=RIDGE)
order_entry_label = Label(edit_box2, text='Enter the order number you are editing:', bg='cornsilk')
order_entry_label.grid(row=0, column=0)
order_entry = Entry(edit_box2, textvariable=order_edit)
order_entry.grid(row=1, column=0)

# Edit_box3 for edit confirmation window
edit_box3 = Frame(win, bg='cornsilk', width=200, height=30,
                  borderwidth=5, relief=RIDGE)
edit_confirmed = Label(edit_box3, text='Edit Confirmation', width=30, bg='cornsilk')
edit_confirmed.grid(columnspan=3)

# Delete_box1 for order number label and text entry box
order_delete = IntVar()

delete_box1 = Frame(win, bg='cornsilk', width=200, height=30,
                    borderwidth=5, relief=RIDGE)
delete_entry_label = Label(delete_box1, text='Enter the order number you are deleting:', bg='cornsilk')
delete_entry_label.grid(row=0, column=0)
delete_entry = Entry(delete_box1, textvariable=order_delete)
delete_entry.grid(row=1, column=0)

# Delete_box2 for submit/menu buttons
delete_box2 = Frame(win, bg='cornsilk', width=200, height=30,
                    borderwidth=5, relief=RIDGE)
submit_edit = Button(delete_box2, text='Submit', command=delete_submit_button_pressed, bg='white', width=20)
submit_edit.grid(row=5, column=0, pady=5, sticky=W)
menu_button3 = Button(delete_box2, text='Menu', command=return_menu, bg='white', width=20)
menu_button3.grid(row=5, column=1, pady=5, sticky=W)

# Delete_box3 for delete confirmation
delete_box3 = Frame(win, bg='cornsilk', width=200, height=30,
                    borderwidth=5, relief=RIDGE)
delete_confirmed = Label(delete_box3, text='Delete Confirmation', width=30, bg='cornsilk')
delete_confirmed.grid(columnspan=3)

# Print_box1 for frame that will show all orders
print_box1 = Frame(win, bg='cornsilk', width=200, height=300,
                   borderwidth=5, relief=RIDGE)
view_orders_label = Label(print_box1, text='', bg='cornsilk', font=('Arial', 7), justify=LEFT)
view_orders_label.grid(row=0, column=0)
menu_button4 = Button(print_box1, text='Menu', command=return_menu, bg='white', width=20)
menu_button4.grid(row=1, column=0, pady=5, sticky=W)

win.mainloop()
