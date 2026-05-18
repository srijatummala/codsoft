import customtkinter as ctk
from tkinter import messagebox

# -------------------- APP SETTINGS -------------------- #

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# -------------------- MAIN WINDOW -------------------- #

app = ctk.CTk()
app.title("Modern Calculator")
app.geometry("420x620")
app.resizable(False, False)

# -------------------- VARIABLES -------------------- #

expression = ""

# -------------------- FUNCTIONS -------------------- #

def button_click(value):
    global expression
    expression += str(value)
    display_var.set(expression)

def clear_display():
    global expression
    expression = ""
    display_var.set("0")

def calculate():

    global expression

    try:
        result = str(eval(expression))
        display_var.set(result)
        expression = result

    except:
        messagebox.showerror("Error", "Invalid Expression")
        expression = ""
        display_var.set("0")

# -------------------- HEADER -------------------- #

title = ctk.CTkLabel(
    app,
    text="🧮 MODERN CALCULATOR",
    font=("Poppins", 28, "bold"),
    text_color="#6C63FF"
)
title.pack(pady=20)

# -------------------- DISPLAY FRAME -------------------- #

display_frame = ctk.CTkFrame(
    app,
    corner_radius=20,
    fg_color="#1E1E1E"
)
display_frame.pack(fill="x", padx=20, pady=10)

display_var = ctk.StringVar(value="0")

display = ctk.CTkEntry(
    display_frame,
    textvariable=display_var,
    font=("Poppins", 32, "bold"),
    height=80,
    justify="right",
    corner_radius=15,
    state="readonly"
)
display.pack(fill="x", padx=15, pady=15)

# -------------------- BUTTON FRAME -------------------- #

button_frame = ctk.CTkFrame(
    app,
    fg_color="transparent"
)
button_frame.pack(pady=20)

# -------------------- BUTTON STYLE -------------------- #

btn_font = ("Poppins", 22, "bold")

# -------------------- BUTTON LAYOUT -------------------- #

buttons = [
    ['C', '/', '*', '-'],
    ['7', '8', '9', '+'],
    ['4', '5', '6', '='],
    ['1', '2', '3', '.'],
    ['0']
]

# -------------------- CREATE BUTTONS -------------------- #

for row in buttons:

    row_frame = ctk.CTkFrame(
        button_frame,
        fg_color="transparent"
    )
    row_frame.pack(pady=8)

    for button in row:

        # CLEAR BUTTON

        if button == 'C':

            btn = ctk.CTkButton(
                row_frame,
                text=button,
                width=85,
                height=75,
                font=btn_font,
                fg_color="#FF4B5C",
                hover_color="#E63946",
                corner_radius=18,
                command=clear_display
            )

        # EQUAL BUTTON

        elif button == '=':

            btn = ctk.CTkButton(
                row_frame,
                text=button,
                width=85,
                height=75,
                font=btn_font,
                fg_color="#00C853",
                hover_color="#00A844",
                corner_radius=18,
                command=calculate
            )

        # OPERATOR BUTTONS

        elif button in ['+', '-', '*', '/']:

            btn = ctk.CTkButton(
                row_frame,
                text=button,
                width=85,
                height=75,
                font=btn_font,
                fg_color="#6C63FF",
                hover_color="#5A54D1",
                corner_radius=18,
                command=lambda b=button: button_click(b)
            )

        # NUMBER BUTTONS

        else:

            btn = ctk.CTkButton(
                row_frame,
                text=button,
                width=85,
                height=75,
                font=btn_font,
                fg_color="#2A2A2A",
                hover_color="#3A3A3A",
                corner_radius=18,
                command=lambda b=button: button_click(b)
            )

        btn.pack(side="left", padx=8)

# -------------------- FOOTER -------------------- #

footer = ctk.CTkLabel(
    app,
    text="Designed with Python & CustomTkinter",
    font=("Poppins", 12),
    text_color="gray"
)
footer.pack(side="bottom", pady=10)

# -------------------- RUN APP -------------------- #

app.mainloop()