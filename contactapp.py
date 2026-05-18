import customtkinter as ctk
from tkinter import messagebox
import json
import os

# -------------------- APP SETTINGS -------------------- #

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# -------------------- MAIN WINDOW -------------------- #

app = ctk.CTk()
app.title("Modern Contact Book")
app.geometry("1100x750")
app.resizable(False, False)

# -------------------- DATA FILE -------------------- #

FILE_NAME = "contacts.json"

contacts = []

selected_contact = None

# -------------------- LOAD CONTACTS -------------------- #

def load_contacts():

    global contacts

    if os.path.exists(FILE_NAME):

        with open(FILE_NAME, "r") as file:

            contacts = json.load(file)

# -------------------- SAVE CONTACTS -------------------- #

def save_contacts():

    with open(FILE_NAME, "w") as file:

        json.dump(contacts, file, indent=4)

# -------------------- CLEAR INPUTS -------------------- #

def clear_inputs():

    name_entry.delete(0, "end")
    phone_entry.delete(0, "end")
    email_entry.delete(0, "end")
    address_entry.delete(0, "end")

# -------------------- DISPLAY CONTACTS -------------------- #

def display_contacts(filtered_contacts=None):

    for widget in contact_frame.winfo_children():
        widget.destroy()

    data = filtered_contacts if filtered_contacts else contacts

    for index, contact in enumerate(data):

        card = ctk.CTkFrame(
            contact_frame,
            fg_color="#1E1E1E",
            corner_radius=15
        )

        card.pack(fill="x", pady=8, padx=10)

        # CONTACT DETAILS

        details = (
            f"👤 {contact['name']}\n"
            f"📞 {contact['phone']}\n"
            f"📧 {contact['email']}"
        )

        label = ctk.CTkLabel(
            card,
            text=details,
            font=("Poppins", 16),
            justify="left"
        )

        label.pack(side="left", padx=20, pady=15)

        # VIEW BUTTON

        view_btn = ctk.CTkButton(
            card,
            text="View",
            width=80,
            fg_color="#6C63FF",
            command=lambda i=index: view_contact(i)
        )

        view_btn.pack(side="right", padx=10)

# -------------------- ADD CONTACT -------------------- #

def add_contact():

    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name == "" or phone == "":

        messagebox.showwarning(
            "Warning",
            "Name and Phone are required!"
        )
        return

    contact = {

        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)

    save_contacts()

    display_contacts()

    clear_inputs()

    messagebox.showinfo(
        "Success",
        "Contact Added Successfully!"
    )

# -------------------- VIEW CONTACT -------------------- #

def view_contact(index):

    global selected_contact

    selected_contact = index

    contact = contacts[index]

    clear_inputs()

    name_entry.insert(0, contact["name"])
    phone_entry.insert(0, contact["phone"])
    email_entry.insert(0, contact["email"])
    address_entry.insert(0, contact["address"])

# -------------------- UPDATE CONTACT -------------------- #

def update_contact():

    global selected_contact

    if selected_contact is None:

        messagebox.showwarning(
            "Warning",
            "Select a contact first!"
        )
        return

    contacts[selected_contact] = {

        "name": name_entry.get(),
        "phone": phone_entry.get(),
        "email": email_entry.get(),
        "address": address_entry.get()
    }

    save_contacts()

    display_contacts()

    clear_inputs()

    messagebox.showinfo(
        "Updated",
        "Contact Updated Successfully!"
    )

# -------------------- DELETE CONTACT -------------------- #

def delete_contact():

    global selected_contact

    if selected_contact is None:

        messagebox.showwarning(
            "Warning",
            "Select a contact first!"
        )
        return

    confirm = messagebox.askyesno(
        "Delete",
        "Are you sure you want to delete?"
    )

    if confirm:

        contacts.pop(selected_contact)

        save_contacts()

        display_contacts()

        clear_inputs()

        selected_contact = None

        messagebox.showinfo(
            "Deleted",
            "Contact Deleted Successfully!"
        )

# -------------------- SEARCH CONTACT -------------------- #

def search_contact():

    keyword = search_entry.get().lower()

    filtered = []

    for contact in contacts:

        if (
            keyword in contact["name"].lower()
            or
            keyword in contact["phone"]
        ):

            filtered.append(contact)

    display_contacts(filtered)

# -------------------- HEADER -------------------- #

title = ctk.CTkLabel(
    app,
    text="📱 MODERN CONTACT BOOK",
    font=("Poppins", 34, "bold"),
    text_color="#6C63FF"
)

title.pack(pady=20)

# -------------------- MAIN FRAME -------------------- #

main_frame = ctk.CTkFrame(
    app,
    fg_color="transparent"
)

main_frame.pack(fill="both", expand=True)

# -------------------- LEFT FRAME -------------------- #

left_frame = ctk.CTkFrame(
    main_frame,
    width=350,
    corner_radius=20,
    fg_color="#181818"
)

left_frame.pack(side="left", fill="y", padx=20, pady=10)

# -------------------- INPUT TITLE -------------------- #

input_title = ctk.CTkLabel(
    left_frame,
    text="Contact Details",
    font=("Poppins", 24, "bold")
)

input_title.pack(pady=20)

# -------------------- INPUT FIELDS -------------------- #

name_entry = ctk.CTkEntry(
    left_frame,
    placeholder_text="Full Name",
    height=50,
    font=("Poppins", 15)
)

name_entry.pack(fill="x", padx=20, pady=10)

phone_entry = ctk.CTkEntry(
    left_frame,
    placeholder_text="Phone Number",
    height=50,
    font=("Poppins", 15)
)

phone_entry.pack(fill="x", padx=20, pady=10)

email_entry = ctk.CTkEntry(
    left_frame,
    placeholder_text="Email Address",
    height=50,
    font=("Poppins", 15)
)

email_entry.pack(fill="x", padx=20, pady=10)

address_entry = ctk.CTkEntry(
    left_frame,
    placeholder_text="Address",
    height=50,
    font=("Poppins", 15)
)

address_entry.pack(fill="x", padx=20, pady=10)

# -------------------- BUTTONS -------------------- #

add_btn = ctk.CTkButton(
    left_frame,
    text="➕ Add Contact",
    height=50,
    font=("Poppins", 16, "bold"),
    corner_radius=12,
    fg_color="#00C853",
    hover_color="#00A844",
    command=add_contact
)

add_btn.pack(fill="x", padx=20, pady=10)

update_btn = ctk.CTkButton(
    left_frame,
    text="✏ Update Contact",
    height=50,
    font=("Poppins", 16, "bold"),
    corner_radius=12,
    fg_color="#FF9800",
    hover_color="#E68900",
    command=update_contact
)

update_btn.pack(fill="x", padx=20, pady=10)

delete_btn = ctk.CTkButton(
    left_frame,
    text="🗑 Delete Contact",
    height=50,
    font=("Poppins", 16, "bold"),
    corner_radius=12,
    fg_color="#FF4B5C",
    hover_color="#E63946",
    command=delete_contact
)

delete_btn.pack(fill="x", padx=20, pady=10)

# -------------------- RIGHT FRAME -------------------- #

right_frame = ctk.CTkFrame(
    main_frame,
    corner_radius=20,
    fg_color="#101010"
)

right_frame.pack(
    side="right",
    fill="both",
    expand=True,
    padx=20,
    pady=10
)

# -------------------- SEARCH BAR -------------------- #

search_entry = ctk.CTkEntry(
    right_frame,
    placeholder_text="🔍 Search by Name or Phone",
    height=50,
    font=("Poppins", 15)
)

search_entry.pack(fill="x", padx=20, pady=20)

search_btn = ctk.CTkButton(
    right_frame,
    text="Search",
    height=45,
    font=("Poppins", 15, "bold"),
    command=search_contact
)

search_btn.pack(padx=20, pady=5)

# -------------------- CONTACT FRAME -------------------- #

contact_frame = ctk.CTkScrollableFrame(
    right_frame,
    fg_color="transparent"
)

contact_frame.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=15
)

# -------------------- LOAD DATA -------------------- #

load_contacts()

display_contacts()

# -------------------- RUN APP -------------------- #

app.mainloop()