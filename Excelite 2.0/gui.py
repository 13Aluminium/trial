# This file was generated by the Tkinter Designer by Parth Jadhav

# Generated by the above dude, but updated by the man, the myth, the legend, you know who - Jash Karangiya

# ====================# Importing useful libraries - like Miss Anya##=============================================== #

from pathlib import Path
import time
import threading
import pandas as pd
import webbrowser

# from tkinter import *


# Declaring global variables:
csv_exists = ''


# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog, messagebox, font, Scrollbar, Frame

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"X:/Jash/Github/hypervect/ExcelSoftware/build/build/assets/frame0")


# ==================================================================================================================== #

# ====================================# Function declaration and definition #==================== #



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# Aa function excel ne CSV ma convert kare che
def convert_to_csv(filepath):
    try:
        # Read the Excel file into a pandas DataFrame
        df = pd.read_excel(filepath)

        # Convert the DataFrame to CSV format without saving
        csv_data = df.to_csv(index=False)

        return csv_data
    except Exception as e:
        print(f"Failed to convert to CSV: {str(e)}")
        return None


# Aa function excel files j upload karva de
def open_excel_file():
    filetypes = [('Excel Files', '*.xlsx *.xls')]
    filepath = filedialog.askopenfilename(filetypes=filetypes)
    if filepath:
        print("Selected Excel file:", filepath)
        # Perform further processing with the selected file


#  Mare phela upload thava ime ee animation nakhvu hatu etle aavu name
# Aa function ma CSV ma convert thai che ane teno filepath display kare che
# Jo filepath aavi jai etle ke CSV bani gai, etle pachi badha element destroy kari ne nava element lavana


# def upload_animation():
    # Display loading animation
    # canvas.create_text(
    #     702.0,
    #     389.0,
    #     anchor="center",
    #     text="Uploading...",
    #     fill="#FFFFFF",
    #     font=("Poppins Regular", 12 * -1)
    # )
    # canvas.update()


def uploading_excel():
    # Simulate upload process (replace with your actual file upload logic)
    time.sleep(2)

    # Get the selected file path
    filetypes = [('Excel Files', '*.xlsx *.xls')]
    filepath = filedialog.askopenfilename(filetypes=filetypes)

    return filepath


# Need to rename this function:
def filepathh():
    filepath = uploading_excel()
    if filepath:
        # Display file name
        filename = Path(filepath).name
        text3 = canvas.create_text(
            702.0,
            389.0,
            anchor="center",

            text="Uploaded file: " + filename,

            fill="#FFFFFF",
            font=("Poppins Regular", 12 * -1)
        )

        # Convert Excel file to CSV
        csv_data = convert_to_csv(filepath)
        print("Ahi nathi aavtu")
        if csv_data:
            print("Converted CSV data:")
            print(csv_data)

            global csv_exists
            csv_exists = True

            # Delete the text1 element
            canvas.delete(text1)
            canvas.delete(text2)
            canvas.delete(image_3)
            canvas.delete(text3)
            # Destroy - Heh! You can destroy sh*t
            button_image_2.destroy()
            return csv_exists

        else:
            print("Failed to convert to CSV.")
    else:
        # Show error message if no file is selected
        messagebox.showerror("Error", "No file selected")


#  Mare phela upload thava ime ee animation nakhvu hatu etle aavu name
# Aa function ma CSV ma convert thai che ane teno filepath display kare che
# Jo filepath aavi jai etle ke CSV bani gai, etle pachi badha element destroy kari ne nava element lavana

# def upload_animation():
#     # Display loading animation
#     # canvas.create_text(
#     #     702.0,
#     #     389.0,
#     #     anchor="center",
#     #     text="Uploading...",
#     #     fill="#FFFFFF",
#     #     font=("Poppins Regular", 12 * -1)
#     # )
#     # canvas.update()


def open_excel_file():
    upload_thread = threading.Thread(target=filepathh)
    upload_thread.start()


# Define a callback function
# A code too chatGPT jode thi lidhi che mara phela about us ane contact us ma link nakhvi hati
def callback(url):
    webbrowser.open_new_tab(url)


def open_about_us():
    callback("https://www.youtube.com/watch?v=dQw4w9WgXcQs")

def open_contact_us():
    callback("https://www.youtube.com/")


# ===================================================================================================================== #


# =============# # Below code is about the GUI and where the components should be placed #===================== #

#  Aa code too phela mathi bani ne aaviyo
window = Tk()
window.title("HYPERVECT | Excelite")
# photo = PhotoImage(file="")
window.iconbitmap("X:/Jash/Github/hypervect/ExcelSoftware/build/build/assets/frame0/favicon.bmp")


window.geometry("1080x665")
window.configure(bg="#222831")

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

canvas.create_text(
    51.0,
    453.0,
    anchor="nw",
    text="Lorem Ipsum is simply dummy ",
    fill="#FFFFFF",
    font=("Poppins Regular", 12 * -1)
)

canvas.create_text(
    48.0,
    432.0,
    anchor="nw",
    text="Lorem Ipsum is simply dummy ",
    fill="#FFFFFF",
    font=("Poppins Regular", 12 * -1)
)

canvas.create_text(
    48.0,
    406.0,
    anchor="nw",
    text="Lorem Ipsum is simply dummy ",
    fill="#FFFFFF",
    font=("Poppins Regular", 12 * -1)
)

canvas.create_text(
    56.0,
    380.0,
    anchor="nw",
    text="Lorem Ipsum is simply dummy ",
    fill="#FFFFFF",
    font=("Poppins Regular", 12 * -1)
)

canvas.create_text(
    51.0,
    354.0,
    anchor="nw",
    text="Lorem Ipsum is simply dummy ",
    fill="#FFFFFF",
    font=("Poppins Regular", 12 * -1)
)

canvas.create_text(
    56.0,
    328.0,
    anchor="nw",
    text="Lorem Ipsum is simply dummy ",
    fill="#FFFFFF",
    font=("Poppins Regular", 12 * -1)
)

canvas.create_text(
    56.0,
    302.0,
    anchor="nw",
    text="Lorem Ipsum is simply dummy ",
    fill="#FFFFFF",
    font=("Poppins Regular", 12 * -1)
)

canvas.create_text(
    56.0,
    276.0,
    anchor="nw",
    text="Lorem Ipsum is simply dummy ",
    fill="#FFFFFF",
    font=("Poppins Regular", 12 * -1)
)

canvas.create_text(
    59.0,
    224.0,
    anchor="nw",
    text="Lorem Ipsum is simply dummy ",
    fill="#FFFFFF",
    font=("Poppins Regular", 12 * -1)
)

canvas.create_text(
    59.0,
    250.0,
    anchor="nw",
    text="Lorem Ipsum is simply dummy ",
    fill="#FFFFFF",
    font=("Poppins Regular", 12 * -1)
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

# canvas.tag_bind(canvas.create_text, "<Button-1>", lambda event: open_contact_us())



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

value = filepathh()

if value == True:
    # Chat Section: (This is section is loaded after the CSV is converted successfully)
    # Load image_5 after successful conversion

    image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        695.0,
        78.0,
        image=image_image_5
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        699.0,
        234.5,
        image=entry_image_1
    )
    entry_1 = Text(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=345.0,
        y=169.0,
        width=708.0,
        height=129.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        699.0,
        510.0,
        image=entry_image_2
    )
    entry_2 = Text(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=345.0,
        y=466.0,
        width=708.0,
        height=86.0
    )

    canvas.create_text(
        341.0,
        134.0,
        anchor="nw",
        text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut.",
        fill="#FFFFFF",
        font=("Poppins Regular", 15 * -1)
    )

    canvas.create_text(
        345.0,
        341.0,
        anchor="nw",
        text="Ask any questions related to the excel sheet",
        fill="#FFFFFF",
        font=("Poppins Regular", 15 * -1)
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        699.0,
        385.0,
        image=entry_image_3
    )
    entry_3 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_3.place(
        x=345.0,
        y=371.0,
        width=708.0,
        height=26.0
    )

    canvas.create_text(
        345.0,
        433.0,
        anchor="nw",
        text="Answer from ChatGPT",
        fill="#FFFFFF",
        font=("Poppins Regular", 16 * -1)
    )


window.resizable(False, False)
window.mainloop()

# ==================================================================================================================== #

