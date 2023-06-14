# This file was generated by the Tkinter Designer by Parth Jadhav
#
# Generated by the above dude, but updated by the man, the myth, the legend, you know who - Jash Karangiya

# ====================# Importing useful libraries - like Miss Anya##=============================================== #

import io
import threading
import time
import webbrowser
from pathlib import Path

from tkinter.ttk import Treeview

import pandas as pd

# from tkinter import *


# Declaring global variables:
csv_exists = ''
image_1= None
image_2= None
image_3= None
image_4= None
image_5= None
image_6= None
image_7= None
image_8= None

entry_bg_1 = None
entry_bg_2 = None
entry_bg_3 = None
entry_bg_4 = None

# Explicit imports to satisfy Flake8
from tkinter import (Button, Canvas, Entry, Frame, PhotoImage, Scrollbar, Text,
                     Tk, filedialog, font, messagebox)

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame0")


# ==================================================================================================================== #

# ====================================# Function declaration and definition #==================== #


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# Function to convert Excel file to CSV data
def convert_to_csv(filepath):
    try:
        # Read the Excel file into a pandas DataFrame
        df = pd.read_excel(filepath)

        # Convert the DataFrame to CSV format
        csv_data = df.to_csv(index=False)

        return csv_data
    except Exception as e:
        print(f"Failed to convert to CSV: {str(e)}")
        return None


# Function to handle file selection and conversion
def open_excel_file():
    global entry_3
    filetypes = [('Excel Files', '*.xlsx *.xls')]
    filepath = filedialog.askopenfilename(filetypes=filetypes)
    if filepath:
        print("Selected Excel file:", filepath)
        # Convert Excel file to CSV data
        csv_data = convert_to_csv(filepath)
        if csv_data:
            print("Converted CSV data:")
            print(csv_data)
            df = pd.read_csv(io.StringIO(csv_data))
            # this is ther code to call the second page UI

            callin(df)
            # Create the table frame
        else:
            print("Failed to convert to CSV.")
    else:
        # Show error message if no file is selected
        messagebox.showerror("Error", "No file selected")


# this will be used in the API
def print_text():
    global entry_4  # Use the global entry_3 variable
    text = entry_4.get()
    text = text.strip()  # Remove leading/trailing whitespace
    print("Text:", text)


# this is the code to display item
def display_table(df):
    table_frame = Frame(window, bg="#FFFFFF")
    table_frame.place(x=26, y=135, width=440, height=440)
    # Clear previous table, if any

    if table_frame.winfo_children():
        for child in table_frame.winfo_children():
            child.destroy()

    # Create a Treeview widget
    table = Treeview(table_frame)

    # Create a horizontal scrollbar
    x_scrollbar = Scrollbar(table_frame, orient="horizontal")
    x_scrollbar.pack(side="bottom", fill="x")

    # Create a vertical scrollbar
    y_scrollbar = Scrollbar(table_frame)
    y_scrollbar.pack(side="right", fill="y")

    # Attach the scrollbars to the table
    table.configure(xscrollcommand=x_scrollbar.set, yscrollcommand=y_scrollbar.set)
    x_scrollbar.configure(command=table.xview)
    y_scrollbar.configure(command=table.yview)
    # Define columns
    columns = df.columns.tolist()
    table['columns'] = columns

    # Format columns
    for col in columns:
        table.column(col, anchor="center")
        table.heading(col, text=col)

    # Insert data rows
    for i, row in df.iterrows():
        values = row.values.tolist()
        table.insert("", "end", values=values, iid=i + 1)  # Update the line

    # Display the table
    table.pack(side="left", fill="both", expand=True)


# ==================================================================================================================== #


# =============# # Below code is about the GUI and where the components should be placed #===================== #
# this is the title code
window = Tk()

window.geometry("1080x665")
window.configure(bg="#222831")

#  Aa code too phela mathi bani ne aaviyo
window.title("HYPERVECT | Excelite")
# photo = PhotoImage(file="")
# window.iconbitmap("assets/frame0/favicon.bmp")

# this is the home page code

# Alert starts:

canvas = Canvas(
    window,
    bg="#222831",
    height=665,
    width=1080,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    151.0,
    332.0,
    image=image_image_1
)

text1 = canvas.create_text(
    535.0,
    276.0,
    anchor="nw",
    text="Analyze your Excel file with the help of Excelite",
    fill="#FFFFFF",
    font=("Poppins Regular", 15 * -1)
)

text2 = canvas.create_text(
    561.0,
    301.0,
    anchor="nw",
    text="Just drop your files below!",
    fill="#FFFFFF",
    font=("Poppins Regular", 20 * -1)
)

canvas.create_text(
    54.0,
    611.0,
    anchor="nw",
    text="Copyright \n©2023 HYPERVECT PVT. LTD",
    fill="#FFFFFF",
    font=("Poppins Regular", 12 * -1)
)


canvas.create_text(
    899.0,
    629.0,
    anchor="nw",
    text="About Us",
    fill="#FFFFFF",
    font=("Poppins Regular", 12 * -1),
    underline=True
)

# canvas.tag_bind(canvas.create_text, "<Button-1>", lambda event: open_about_us())


canvas.create_text(
    977.0,
    629.0,
    anchor="nw",
    text="Contact Us",
    fill="#FFFFFF",
    font=("Poppins Regular", 12 * -1),
    underline=True
)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
button_image_2 = Button(
    window,
    image=image_image_2,
    bg="#222831",
    bd=0,
    activebackground="#222831",
    command=open_excel_file

)
button_image_2.place(x=493.0, y=349.0)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    706.0,
    65.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    151.0,
    69.0,
    image=image_image_4
)

# Alert ends:

# Na kamu button

# upload_button = Button(
#     window,
#     text="Upload Excel File",
#     command=open_excel_file,
#     font=("Poppins Regular", 12),
#     bg="#393E46",
#     fg="#FFFFFF",
#     activebackground="#00ADB5",
#     activeforeground="#FFFFFF",
#     relief="flat"
# )
# upload_button.place(x=10, y=10)

# this is the UI code
def callin(df):
    df=df
    global entry_3, image_2, entry_4, entry_bg_1, image_5, image_6, image_4, entry_bg_2, entry_bg_4,image_7,image_8
    canvas = Canvas(
        window,
        bg="#222831",
        height=665,
        width=1080,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    image_image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(
        258.0,
        332.0,
        image=image_image_6
    )
    print(image_5)

    canvas.create_text(
        54.0,
        611.0,
        anchor="nw",
        text="Copyright \nÂ©2023 HYPERVECT PVT. LTD",
        fill="#FFFFFF",
        font=("Poppins Regular", 12 * -1)
    )

    canvas.create_text(
        899.0,
        629.0,
        anchor="nw",
        text="About Us",
        fill="#FFFFFF",
        font=("Poppins Regular", 12 * -1)
    )

    canvas.create_text(
        977.0,
        629.0,
        anchor="nw",
        text="Contact Us",
        fill="#FFFFFF",
        font=("Poppins Regular", 12 * -1)
    )

    # image_image_2 = PhotoImage(
    #     file=relative_to_assets("image_2.png"))
    # image_2 = canvas.create_image(
    #     151.0,
    #     69.0,
    #     image=image_image_2
    # )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        151.0,
        69.0,
        image=image_image_4
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        695.0,
        93.0,
        image=image_image_5
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        806.0,
        246.5,
        image=entry_image_1
    )
    entry_1 = Text(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=580.0,
        y=181.0,
        width=452.0,
        height=129.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        806.0,
        528.0,
        image=entry_image_2
    )
    entry_2 = Text(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=580.0,
        y=484.0,
        width=452.0,
        height=86.0
    )

    # entry_3 = Entry(
    #     bd=0,
    #     bg="#D9D9D9",
    #     fg="#000716",
    #     highlightthickness=0
    # )
    # entry_3.place(
    #     x=34.0,
    #     y=126.0,
    #     width=440.0,
    #     height=438.0
    # )
    canvas.create_text(
        580.0,
        146.0,
        anchor="nw",
        text="Summary\n",
        fill="#FFFFFF",
        font=("Poppins Regular", 15 * -1)
    )

    canvas.create_text(
        580.0,
        353.0,
        anchor="nw",
        text="Ask any questions related to the excel sheet",
        fill="#FFFFFF",
        font=("Poppins Regular", 15 * -1)
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        806.0,
        397.0,
        image=entry_image_4
    )
    entry_4 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_4.place(
        x=580.0,
        y=383.0,
        width=452.0,
        height=26.0
    )

    canvas.create_text(
        580.0,
        445.0,
        anchor="nw",
        text="Answer from ChatGPT",
        fill="#FFFFFF",
        font=("Poppins Regular", 16 * -1)
    )


    image_image_7 = PhotoImage(
        file=relative_to_assets("image_7.png"))
    image_7 = canvas.create_image(
        977.0,
        445.0,
        image=image_image_7
    )

    image_image_8 = PhotoImage(
        file=relative_to_assets("image_8.png"))
    image_8 = canvas.create_image(
        982.0,
        601.0,
        image=image_image_8
    )
    display_table(df)

    window.resizable(False, False)
    window.mainloop()

    


window.resizable(False, False)
window.mainloop()

# ==================================================================================================================== #
