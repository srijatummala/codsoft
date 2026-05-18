import customtkinter as ctk
import random
import string
from tkinter import messagebox

# -------------------- APP SETTINGS -------------------- #

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# -------------------- MAIN WINDOW -------------------- #

app = ctk.CTk()
app.title("Password Strength Checker")
app.geometry("700x650")
app.resizable(False, False)

# -------------------- GENERATE PASSWORD -------------------- #

def generate_password():

    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = "".join(
        random.choice(characters)
        for _ in range(14)
    )

    password_entry.delete(0, "end")
    password_entry.insert(0, password)

    check_password()

# -------------------- CHECK PASSWORD STRENGTH -------------------- #

def check_password():

    password = password_entry.get()

    if password == "":

        messagebox.showwarning(
            "Warning",
            "Please enter a password!"
        )
        return

    score = 0

    # ---------------- LENGTH ---------------- #

    if len(password) >= 8:
        score += 20

    if len(password) >= 12:
        score += 20

    # ---------------- UPPERCASE ---------------- #

    if any(char.isupper() for char in password):
        score += 15

    # ---------------- LOWERCASE ---------------- #

    if any(char.islower() for char in password):
        score += 15

    # ---------------- NUMBERS ---------------- #

    if any(char.isdigit() for char in password):
        score += 15

    # ---------------- SYMBOLS ---------------- #

    if any(char in string.punctuation for char in password):
        score += 15

    # ---------------- BONUS ---------------- #

    unique_chars = len(set(password))

    if unique_chars >= 10:
        score += 10

    # ---------------- LIMIT ---------------- #

    if score > 100:
        score = 100

    # ---------------- UPDATE PROGRESS ---------------- #

    progress_bar.set(score / 100)

    percentage_label.configure(
        text=f"{score}% Secure Password"
    )

    # ---------------- PASSWORD STATUS ---------------- #

    if score <= 40:

        result_label.configure(
            text="❌ Weak Password",
            text_color="red"
        )

    elif score <= 75:

        result_label.configure(
            text="⚠ Medium Password",
            text_color="orange"
        )

    else:

        result_label.configure(
            text="✅ Strong Password",
            text_color="green"
        )

# -------------------- COPY PASSWORD -------------------- #

def copy_password():

    password = password_entry.get()

    if password == "":

        messagebox.showwarning(
            "Warning",
            "No password found!"
        )
        return

    app.clipboard_clear()
    app.clipboard_append(password)

    messagebox.showinfo(
        "Copied",
        "Password copied successfully!"
    )

# -------------------- HEADER -------------------- #

title = ctk.CTkLabel(
    app,
    text="🔐 PASSWORD STRENGTH CHECKER",
    font=("Poppins", 32, "bold"),
    text_color="#6C63FF"
)

title.pack(pady=20)

subtitle = ctk.CTkLabel(
    app,
    text="Check how secure your password is",
    font=("Poppins", 15),
    text_color="gray"
)

subtitle.pack()

# -------------------- MAIN FRAME -------------------- #

main_frame = ctk.CTkFrame(
    app,
    fg_color="#1E1E1E",
    corner_radius=20
)

main_frame.pack(
    fill="both",
    expand=True,
    padx=25,
    pady=25
)

# -------------------- PASSWORD ENTRY -------------------- #

entry_title = ctk.CTkLabel(
    main_frame,
    text="Enter Your Password",
    font=("Poppins", 18, "bold")
)

entry_title.pack(pady=(25, 10))

password_entry = ctk.CTkEntry(
    main_frame,
    height=60,
    font=("Poppins", 20, "bold"),
    corner_radius=15,
    justify="center",
    placeholder_text="Type your password here..."
)

password_entry.pack(
    fill="x",
    padx=30,
    pady=10
)

# -------------------- BUTTON FRAME -------------------- #

button_frame = ctk.CTkFrame(
    main_frame,
    fg_color="transparent"
)

button_frame.pack(pady=20)

# CHECK BUTTON

check_button = ctk.CTkButton(
    button_frame,
    text="✅ Check Strength",
    width=200,
    height=50,
    font=("Poppins", 16, "bold"),
    corner_radius=15,
    fg_color="#6C63FF",
    hover_color="#574FD6",
    command=check_password
)

check_button.grid(row=0, column=0, padx=10)

# GENERATE BUTTON

generate_button = ctk.CTkButton(
    button_frame,
    text="⚡ Generate",
    width=180,
    height=50,
    font=("Poppins", 16, "bold"),
    corner_radius=15,
    fg_color="#FF9800",
    hover_color="#E68900",
    command=generate_password
)

generate_button.grid(row=0, column=1, padx=10)

# COPY BUTTON

copy_button = ctk.CTkButton(
    button_frame,
    text="📋 Copy",
    width=150,
    height=50,
    font=("Poppins", 16, "bold"),
    corner_radius=15,
    fg_color="#00C853",
    hover_color="#00A844",
    command=copy_password
)

copy_button.grid(row=1, column=0, columnspan=2, pady=15)

# -------------------- PROGRESS BAR -------------------- #

progress_bar = ctk.CTkProgressBar(
    main_frame,
    height=25,
    corner_radius=15
)

progress_bar.set(0)

progress_bar.pack(
    fill="x",
    padx=50,
    pady=20
)

# -------------------- PERCENTAGE LABEL -------------------- #

percentage_label = ctk.CTkLabel(
    main_frame,
    text="0% Secure Password",
    font=("Poppins", 22, "bold"),
    text_color="#6C63FF"
)

percentage_label.pack(pady=10)

# -------------------- RESULT LABEL -------------------- #

result_label = ctk.CTkLabel(
    main_frame,
    text="",
    font=("Poppins", 24, "bold")
)

result_label.pack(pady=10)

# -------------------- TIPS -------------------- #

tips_label = ctk.CTkLabel(
    main_frame,
    text=(
        "Tips:\n"
        "✔ Use uppercase letters\n"
        "✔ Use lowercase letters\n"
        "✔ Add numbers\n"
        "✔ Add symbols\n"
        "✔ Keep password length above 12"
    ),
    font=("Poppins", 14),
    text_color="gray",
    justify="left"
)

tips_label.pack(pady=20)

# -------------------- FOOTER -------------------- #

footer = ctk.CTkLabel(
    app,
    text="Designed with Python & CustomTkinter",
    font=("Poppins", 12),
    text_color="gray"
)

footer.pack(pady=10)

# -------------------- RUN APP -------------------- #

app.mainloop()