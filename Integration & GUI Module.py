# Integration & GUI Modules Project

# Real-Time Cryptocurrency Price Tracker using Tkinter + REST API

import tkinter as tk

from tkinter import messagebox

import requests

# Function to fetch crypto price

def get_price():

    crypto = coin_entry.get().lower().strip()

    if not crypto:

        messagebox.showwarning("Input Error", "Please enter a cryptocurrency name!")

        return

    try:

        url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd"

        response = requests.get(url)

        data = response.json()

        if crypto in data:

            price = data[crypto]["usd"]

            result_label.config(

                text=f"{crypto.upper()} Price: ${price}",

                font=("Arial", 14, "bold")

            )

        else:

            messagebox.showerror("Error", "Cryptocurrency not found!")

    except Exception as e:

        messagebox.showerror("API Error", str(e))

# Create GUI Window

root = tk.Tk()

root.title("Crypto Price Tracker")

root.geometry("450x250")

root.resizable(False, False)

# Title

title_label = tk.Label(

    root,

    text="Real-Time Crypto Price Tracker",

    font=("Arial", 16, "bold")

)

title_label.pack(pady=15)

# Input Field

coin_entry = tk.Entry(root, width=25, font=("Arial", 12))

coin_entry.pack(pady=10)

coin_entry.insert(0, "bitcoin")

# Button

search_button = tk.Button(

    root,

    text="Get Price",

    command=get_price,

    font=("Arial", 12)

)

search_button.pack(pady=10)

# Result Label

result_label = tk.Label(

    root,

    text="Enter a cryptocurrency name",

    font=("Arial", 12)

)

result_label.pack(pady=20)

# Run Application

root.mainloop()
