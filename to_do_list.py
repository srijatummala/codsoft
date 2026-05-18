import customtkinter as ctk
import json
import os
from tkinter import messagebox

# ---------------------- SETTINGS ---------------------- #

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

APP_WIDTH = 900
APP_HEIGHT = 650

TASK_FILE = "tasks.json"

# ---------------------- MAIN APP ---------------------- #

class TodoApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        # WINDOW
        self.title("CODSOFT Task Manager")
        self.geometry(f"{APP_WIDTH}x{APP_HEIGHT}")
        self.resizable(False, False)

        # TASK STORAGE
        self.tasks = []

        # ---------------------- HEADER ---------------------- #

        self.header = ctk.CTkLabel(
            self,
            text="📝 CODSOFT TASK MANAGER",
            font=("Poppins", 32, "bold"),
            text_color="#6C63FF"
        )
        self.header.pack(pady=20)

        # ---------------------- INPUT FRAME ---------------------- #

        self.input_frame = ctk.CTkFrame(
            self,
            corner_radius=15,
            fg_color="#1E1E1E"
        )
        self.input_frame.pack(fill="x", padx=20, pady=10)

        # TASK ENTRY

        self.task_entry = ctk.CTkEntry(
            self.input_frame,
            placeholder_text="Enter your task here...",
            height=50,
            font=("Poppins", 16),
            corner_radius=12
        )
        self.task_entry.pack(side="left", padx=15, pady=15, fill="x", expand=True)

        # ADD BUTTON

        self.add_button = ctk.CTkButton(
            self.input_frame,
            text="➕ Add Task",
            height=50,
            width=140,
            font=("Poppins", 15, "bold"),
            corner_radius=12,
            command=self.add_task
        )
        self.add_button.pack(side="right", padx=15)

        # ---------------------- SEARCH BAR ---------------------- #

        self.search_entry = ctk.CTkEntry(
            self,
            placeholder_text="🔍 Search tasks...",
            height=45,
            font=("Poppins", 15),
            corner_radius=12
        )
        self.search_entry.pack(fill="x", padx=20, pady=10)

        self.search_entry.bind("<KeyRelease>", self.search_task)

        # ---------------------- TASK FRAME ---------------------- #

        self.task_frame = ctk.CTkScrollableFrame(
            self,
            width=850,
            height=420,
            corner_radius=15,
            fg_color="#121212"
        )
        self.task_frame.pack(padx=20, pady=10, fill="both", expand=True)

        # ---------------------- FOOTER ---------------------- #

        self.footer = ctk.CTkLabel(
            self,
            text="Total Tasks: 0",
            font=("Poppins", 16, "bold")
        )
        self.footer.pack(pady=10)

        # LOAD EXISTING TASKS
        self.load_tasks()

    # ---------------------- ADD TASK ---------------------- #

    def add_task(self):

        task = self.task_entry.get()

        if task.strip() == "":
            messagebox.showwarning("Warning", "Task cannot be empty!")
            return

        task_data = {
            "task": task,
            "completed": False
        }

        self.tasks.append(task_data)

        self.display_task(task_data)

        self.task_entry.delete(0, "end")

        self.update_counter()

        self.save_tasks()

    # ---------------------- DISPLAY TASK ---------------------- #

    def display_task(self, task_data):

        task_container = ctk.CTkFrame(
            self.task_frame,
            corner_radius=15,
            fg_color="#1F1F1F",
            height=70
        )
        task_container.pack(fill="x", pady=8, padx=8)

        # TASK LABEL

        task_label = ctk.CTkLabel(
            task_container,
            text=task_data["task"],
            font=("Poppins", 16),
            anchor="w"
        )
        task_label.pack(side="left", padx=20)

        # COMPLETE BUTTON

        complete_btn = ctk.CTkButton(
            task_container,
            text="✔",
            width=45,
            height=40,
            fg_color="green",
            hover_color="#008000",
            font=("Arial", 16, "bold"),
            corner_radius=10,
            command=lambda: self.complete_task(task_label, task_data)
        )
        complete_btn.pack(side="right", padx=10)

        # DELETE BUTTON

        delete_btn = ctk.CTkButton(
            task_container,
            text="✖",
            width=45,
            height=40,
            fg_color="red",
            hover_color="#B22222",
            font=("Arial", 16, "bold"),
            corner_radius=10,
            command=lambda: self.delete_task(task_container, task_data)
        )
        delete_btn.pack(side="right")

        # COMPLETED STYLE

        if task_data["completed"]:
            task_label.configure(
                text_color="gray",
                font=("Poppins", 16, "overstrike")
            )

        # STORE REFERENCES
        task_data["container"] = task_container
        task_data["label"] = task_label

    # ---------------------- COMPLETE TASK ---------------------- #

    def complete_task(self, label, task_data):

        task_data["completed"] = not task_data["completed"]

        if task_data["completed"]:

            label.configure(
                text_color="gray",
                font=("Poppins", 16, "overstrike")
            )

        else:

            label.configure(
                text_color="white",
                font=("Poppins", 16)
            )

        self.save_tasks()

    # ---------------------- DELETE TASK ---------------------- #

    def delete_task(self, container, task_data):

        answer = messagebox.askyesno(
            "Delete Task",
            "Are you sure you want to delete this task?"
        )

        if answer:

            container.destroy()

            self.tasks.remove(task_data)

            self.update_counter()

            self.save_tasks()

    # ---------------------- SEARCH TASK ---------------------- #

    def search_task(self, event):

        search_text = self.search_entry.get().lower()

        for task in self.tasks:

            task_name = task["task"].lower()

            if search_text in task_name:

                task["container"].pack(
                    fill="x",
                    pady=8,
                    padx=8
                )

            else:

                task["container"].pack_forget()

    # ---------------------- UPDATE COUNTER ---------------------- #

    def update_counter(self):

        completed = len([t for t in self.tasks if t["completed"]])

        total = len(self.tasks)

        self.footer.configure(
            text=f"Total Tasks: {total}   |   Completed: {completed}"
        )

    # ---------------------- SAVE TASKS ---------------------- #

    def save_tasks(self):

        clean_tasks = []

        for task in self.tasks:

            clean_tasks.append({
                "task": task["task"],
                "completed": task["completed"]
            })

        with open(TASK_FILE, "w") as file:

            json.dump(clean_tasks, file, indent=4)

    # ---------------------- LOAD TASKS ---------------------- #

    def load_tasks(self):

        if os.path.exists(TASK_FILE):

            with open(TASK_FILE, "r") as file:

                saved_tasks = json.load(file)

            for task in saved_tasks:

                self.tasks.append(task)

                self.display_task(task)

            self.update_counter()

# ---------------------- RUN APP ---------------------- #

if __name__ == "__main__":

    app = TodoApp()

    app.mainloop()