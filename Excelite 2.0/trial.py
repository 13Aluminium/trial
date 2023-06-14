from pathlib import Path
import pandas as pd
import io
from tkinter import Tk, Canvas, PhotoImage, filedialog, messagebox, Button, Frame, Scrollbar
from tkinter.ttk import Treeview

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/aluminium/inter/ExcelSoftware/build/build/assets/frame0")


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
    filetypes = [('Excel Files', '*.xlsx *.xls')]
    filepath = filedialog.askopenfilename(filetypes=filetypes)
    if filepath:
        print("Selected Excel file:", filepath)
        # Convert Excel file to CSV data
        csv_data = convert_to_csv(filepath)
        if csv_data:
            print("Converted CSV data:")
            print(csv_data)

            # Display the CSV data in a table format
            df = pd.read_csv(io.StringIO(csv_data))
            display_table(df)

            # Perform further processing with the CSV data
        else:
            print("Failed to convert to CSV.")
    else:
        # Show error message if no file is selected
        messagebox.showerror("Error", "No file selected")

def display_table(df):
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
        table.insert("", "end", values=values, iid=i+1)  # Update the line

    # Display the table
    table.pack(side="left", fill="both", expand=True)

# Below code is about the GUI and where the components should be placed
window = Tk()
window.title("HYPERVECT | Excelite")
window.geometry("800x600")
window.configure(bg="#222831")

# Create the canvas
canvas = Canvas(
    window,
    bg="#222831",
    height=600,
    width=800,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# Create the image placeholder
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(151.0, 332.0, image=image_image_1)

# Create the "Upload Excel File" button
upload_button = Button(
    window,
    text="Upload Excel File",
    command=open_excel_file,
    font=("Poppins Regular", 12),
    bg="#393E46",
    fg="#FFFFFF",
    activebackground="#00ADB5",
    activeforeground="#FFFFFF",
    relief="flat"
)
upload_button.place(x=10, y=10)

# Create the table frame
table_frame = Frame(window, bg="#FFFFFF")
table_frame.place(x=10, y=50, width=780, height=540)

# Start the main event loop
window.mainloop()
