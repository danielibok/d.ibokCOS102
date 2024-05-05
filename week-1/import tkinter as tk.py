import tkinter as tk
from tkinter import messagebox
def tmenu():
    messagebox.showinfo('Info', 'Welcome to PAU cafeteria')
    global root
    root = tk.Tk()
    root.title("Menu")
    root.geometry('700x800')
    label_1 = tk.Label(root, text = 'MENU', font = ('times','15','bold'))
    label_1.pack()
    label_2 = tk.Label(root, text = 'RICE/PASTA     ',font = ('times','13','bold'))
    label_2.pack(anchor='w')
    label_3 = tk.Label(root, text = 'Jollof Rice                  350\nCoconut Fried Rice   350\nJollof Spaghetti          350\n')
    label_3.pack(anchor='w')
    label_4 = tk.Label(root, text = ' PROTEINS       ',font = ('times','13','bold'))
    label_4.pack(anchor='e')
    label_5 = tk.Label(root, text = 'Sweet Chili Chicken      1100\nGrilled Chicken Wings    400\nFried Beef                          400\nFried Fish                         500\nBoiled Egg                       200\nSauteed Sausages           200\n')
    label_5.pack(anchor='e')
    label_6= tk.Label(root, text = '   SIDE DISHES',font = ('times','13','bold'))
    label_6.pack(anchor='w')  
    label_7 = tk.Label(root, text = 'Savory Beans                     350\nRoasted Sweet Potatoes    300\nFried Plantain                    150\nMixed Vegetable Salad   150\nBoiled yam                       150')
    label_7.pack(anchor='w')
    label_8 = tk.Label(root, text = 'BEVERAGES',font = ('times','13','bold'))
    label_8.pack(anchor='e')
    label_9 = tk.Label(root, text = 'Water                       200\nGlass Drink(35cl)      150\nPET Drink(35cl)        300\nPET Drink(50cl)        350\nGlass/Canned Malt   500\nFresh Yo                      600\nPineapple Juice         350\nMango Juice               350\nZobo Drink                 350')
    label_9.pack(anchor='e')
    label_10 = tk.Label(root, text = 'SOUPS & SWALLOWS',font = ('times','13','bold'))
    label_10.pack(anchor='w')
    label_11 = tk.Label(root, text = 'Eba                  100\nPoundo Yam  100\nSemo               100\nAtama Soup   450\nEgusi Soup     480')
    label_11.pack(anchor='w')
    label_12 = tk.Label(root, text = 'ENJOY', font = ('times','14','bold'))
    label_12.pack()
    #add a button widget
    button = tk.Button(root, text='tap to order!', command=root.destroy)
    button.pack()
tmenu()
root.mainloop()

menu_items = {
    "RICE/PASTA": ["jollof rice", "coconut rice", "jollof spaghetti"],
    "PROTEINS": ["sweet chilichicken", "grilled chicken wings", "fried beef", "fried fish", "boiled egg", "sauteed sausages"],
    "SIDE DISHES": ["savoury beans", "roasted sweet potatoes", "fried plantains", "mixed vegetable salad", "boiled yam"],
    "BEVERAGES": ["water", "glass drink(35cl)", "pet drink(35cl)", "pet drink(50cl)", "glass/canned malt", "fresh yo", "pinneaple juice", "mango juice", "zobo drink"],
    "SOUPS & SWALLOWS": ["eba", "poundo yam", "semo", "atama soup", "egusi"]
    }
menu_prices = {
    "jollof rice": 350.00,
    "coconut rice": 350.00,
    "jollof spaghetti": 350.00,
    "sweet chilichicken": 1100.00,
    "grilled chicken wings": 400.00,
    "fried beef": 400.00,
    "fried fish": 500.00,
    "boiled egg": 200.00,
    "sauteed sausages": 200.00,
    "savoury beans": 350.00,
    "roasted sweet potatoes": 300.00,
    "fried plantains": 150.00,
    "mixed vegetable salad": 150.00,
    "boiled yam": 150.00,
    "water": 200.00,
    "glass drink(35cl)": 150.00,
    "pet drink(35cl)": 300.00,
    "pet drink(50cl)": 350.00,
    "glass/canned malt": 500.00,
    "fresh yo": 600.00,
    "pinneaple juice": 350.00,
    "mango juice": 350.00,
    "zobo drink": 350.00,
    "eba": 100.00,
    "poundo yam": 100.00,
    "semo": 100.00,
    "atama soup": 450.00,
    "egusi": 480.00,
}

def cost(root,username_entry,spinbox_items):
    total_cost = 0
    discount = 0
    order={}
    for category, items in menu_items.items():
        for item in items:
            quantity = int(spinbox_items[item].get())  # Use spinbox_item instead of entry
            if quantity > 0:
                order[item] = quantity
                total_cost += quantity * menu_prices[item]  # Use menu_prices instead of menu
    
    if total_cost >= 5000:
        discount = total_cost * 0.25  # 25% discount 
    elif total_cost >= 2500 and total_cost<=5000:
        discount = total_cost * 0.15  # 15% discount 
    elif total_cost >= 1000 and total_cost<2500:
        discount = total_cost * 0.1   # 10% discount  
    else:
        discount = total_cost * 0     # 0% discount 
    total_with_discount = total_cost - discount

    cost_window = tk.Toplevel(root)
    cost_window.title("Bill")
    username = username_entry.get()
    order_text = f"{username}'s Order:\n"
    for item, quantity in order.items():
        order_text += f"{item}: {quantity}\n"
    order_text += f"\nTotal Price before discount: N{total_cost:.2f}\n"
    order_text += f"Discount applied: N{discount:.2f}\n"
    order_text += f"Total Price after discount: N{total_with_discount:.2f}\n"
    cost_label = tk.Label(cost_window, text=order_text)
    cost_label.pack()
    root.mainloop()

root = tk.Tk()
root.title("Order Application")
root.geometry('700x800')
#create username label and entry
username_label = tk.Label(root, text = 'Username')
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

left_frame = tk.Frame(root)
left_frame.pack(side=tk.LEFT,fill=tk.BOTH)
    
right_frame = tk.Frame(root)
right_frame.pack(side=tk.RIGHT,fill=tk.BOTH)
spinbox_items ={}
for category, items in menu_items.items():
    if category in ["RICE/PASTA", "PROTEINS", "SIDE DISHES"]:
        frame = left_frame
        side = tk.LEFT
    else:
        frame = right_frame
        side = tk.RIGHT
        
    label_category = tk.Label(frame, text=f'{category.upper()}', font=('times', '11', 'bold'))
    label_category.pack(side=tk.TOP, anchor='w')
        
    for item in items:
        label_item = tk.Label(frame, text=f'{item}: {menu_prices[item]} N', anchor='w')
        label_item.pack(side=tk.TOP, anchor='w')
        spinbox_item = tk.Spinbox(frame, from_=0, to=15, increment=1)
        spinbox_item.pack(side=tk.TOP, anchor='w')
        spinbox_items[item]=spinbox_item
        
# Finish Button
finish_button = tk.Button(root, text="Finish", command=lambda:cost(root,username_entry,spinbox_items))
finish_button.pack()
root.mainloop()