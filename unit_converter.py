import tkinter as tk
from tkinter import ttk, messagebox

units = {
    "Length": {
        "Meter": 1,
        "Kilometer": 1000,
        "Centimeter": 0.01,
        "Millimeter": 0.001,
        "Mile": 1609.344,
        "Foot": 0.3048
    },
    "Weight": {
        "Kilogram": 1,
        "Gram": 0.001,
        "Milligram": 0.000001,
        "Pound": 0.453592
    },
    "Temperature": {
        "Celsius": "C",
        "Fahrenheit": "F",
        "Kelvin": "K"
    }
}

def update_units(event=None):
    category = category_box.get()
    available = list(units[category].keys())

    from_box["values"] = available
    to_box["values"] = available

    from_box.current(0)
    to_box.current(1 if len(available) > 1 else 0)


def convert():
    try:
        value = float(entry.get())

        category = category_box.get()
        from_unit = from_box.get()
        to_unit = to_box.get()

        if category == "Temperature":
            if from_unit == "Celsius":
                celsius = value
            elif from_unit == "Fahrenheit":
                celsius = (value - 32) * 5 / 9
            else:
                celsius = value - 273.15

            if to_unit == "Celsius":
                result = celsius
            elif to_unit == "Fahrenheit":
                result = (celsius * 9 / 5) + 32
            else:
                result = celsius + 273.15

        else:
            base_value = value * units[category][from_unit]
            result = base_value / units[category][to_unit]

        result_label.config(
            text=f"Result: {result:.4f} {to_unit}"
        )

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid number."
        )

    except Exception:
        messagebox.showerror(
            "Error",
            "Something went wrong."
        )


def clear():
    entry.delete(0, tk.END)
    result_label.config(text="Result: ")


root = tk.Tk()
root.title("Unit Converter")
root.geometry("450x550")
root.resizable(False, False)
root.configure(bg="#eaf2f8")

title = tk.Label(
    root,
    text="UNIT CONVERTER",
    font=("Arial", 22, "bold"),
    bg="#eaf2f8",
    fg="#154360"
)
title.pack(pady=20)

tk.Label(
    root,
    text="Select Category",
    font=("Arial", 12),
    bg="#eaf2f8"
).pack(pady=5)

category_box = ttk.Combobox(
    root,
    values=list(units.keys()),
    state="readonly",
    width=25
)
category_box.pack(pady=5)
category_box.current(0)
category_box.bind("<<ComboboxSelected>>", update_units)

tk.Label(
    root,
    text="Enter Value",
    font=("Arial", 12),
    bg="#eaf2f8"
).pack(pady=5)

entry = tk.Entry(root, font=("Arial", 14), width=25)
entry.pack(pady=5)

tk.Label(
    root,
    text="From Unit",
    font=("Arial", 12),
    bg="#eaf2f8"
).pack(pady=5)

from_box = ttk.Combobox(root, state="readonly", width=25)
from_box.pack(pady=5)

tk.Label(
    root,
    text="To Unit",
    font=("Arial", 12),
    bg="#eaf2f8"
).pack(pady=5)

to_box = ttk.Combobox(root, state="readonly", width=25)
to_box.pack(pady=5)

update_units()

convert_button = tk.Button(
    root,
    text="CONVERT",
    command=convert,
    font=("Arial", 12, "bold"),
    bg="#2874a6",
    fg="white",
    width=15
)
convert_button.pack(pady=15)

clear_button = tk.Button(
    root,
    text="CLEAR",
    command=clear,
    font=("Arial", 11),
    bg="#d5d8dc",
    width=15
)
clear_button.pack()

result_label = tk.Label(
    root,
    text="Result: ",
    font=("Arial", 16, "bold"),
    bg="#eaf2f8",
    fg="#154360"
)
result_label.pack(pady=10)

root.mainloop()