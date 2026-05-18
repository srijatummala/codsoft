import customtkinter as ctk
import random

# -------------------- APP SETTINGS -------------------- #

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# -------------------- MAIN WINDOW -------------------- #

app = ctk.CTk()
app.title("Rock Paper Scissors")
app.geometry("900x700")
app.resizable(False, False)

# -------------------- VARIABLES -------------------- #

user_score = 0
computer_score = 0
draw_score = 0

choices = ["Rock", "Paper", "Scissors"]

# -------------------- GAME FUNCTION -------------------- #

def play(choice):

    global user_score
    global computer_score
    global draw_score

    computer_choice = random.choice(choices)

    # ---------------- RESULT ---------------- #

    if choice == computer_choice:

        result = "🤝 MATCH DRAW"
        result_color = "orange"
        draw_score += 1

    elif (
        (choice == "Rock" and computer_choice == "Scissors")
        or
        (choice == "Paper" and computer_choice == "Rock")
        or
        (choice == "Scissors" and computer_choice == "Paper")
    ):

        result = "🎉 YOU WIN!"
        result_color = "green"
        user_score += 1

    else:

        result = "💻 COMPUTER WINS!"
        result_color = "red"
        computer_score += 1

    # ---------------- UPDATE LABELS ---------------- #

    your_choice_label.configure(
        text=f"🧑 Your Choice: {choice}"
    )

    computer_choice_label.configure(
        text=f"💻 Computer Choice: {computer_choice}"
    )

    result_label.configure(
        text=result,
        text_color=result_color
    )

    score_label.configure(
        text=(
            f"🧑 You: {user_score}     "
            f"🤝 Draw: {draw_score}     "
            f"💻 Computer: {computer_score}"
        )
    )

# -------------------- RESET GAME -------------------- #

def reset_game():

    global user_score
    global computer_score
    global draw_score

    user_score = 0
    computer_score = 0
    draw_score = 0

    score_label.configure(
        text="🧑 You: 0     🤝 Draw: 0     💻 Computer: 0"
    )

    result_label.configure(
        text="Choose Your Move",
        text_color="white"
    )

    your_choice_label.configure(
        text="🧑 Your Choice:"
    )

    computer_choice_label.configure(
        text="💻 Computer Choice:"
    )

# -------------------- HEADER -------------------- #

title = ctk.CTkLabel(
    app,
    text="🎮 ROCK PAPER SCISSORS",
    font=("Poppins", 36, "bold"),
    text_color="#6C63FF"
)

title.pack(pady=20)

subtitle = ctk.CTkLabel(
    app,
    text="Modern Python Game UI",
    font=("Poppins", 16),
    text_color="gray"
)

subtitle.pack()

# -------------------- MAIN FRAME -------------------- #

main_frame = ctk.CTkFrame(
    app,
    fg_color="#1E1E1E",
    corner_radius=25
)

main_frame.pack(
    fill="both",
    expand=True,
    padx=30,
    pady=25
)

# -------------------- SCORE BOARD -------------------- #

score_label = ctk.CTkLabel(
    main_frame,
    text="🧑 You: 0     🤝 Draw: 0     💻 Computer: 0",
    font=("Poppins", 24, "bold"),
    text_color="#00C853"
)

score_label.pack(pady=25)

# -------------------- RESULT LABEL -------------------- #

result_label = ctk.CTkLabel(
    main_frame,
    text="Choose Your Move",
    font=("Poppins", 32, "bold")
)

result_label.pack(pady=20)

# -------------------- CHOICE LABELS -------------------- #

your_choice_label = ctk.CTkLabel(
    main_frame,
    text="🧑 Your Choice:",
    font=("Poppins", 20)
)

your_choice_label.pack(pady=10)

computer_choice_label = ctk.CTkLabel(
    main_frame,
    text="💻 Computer Choice:",
    font=("Poppins", 20)
)

computer_choice_label.pack(pady=10)

# -------------------- BUTTON FRAME -------------------- #

button_frame = ctk.CTkFrame(
    main_frame,
    fg_color="transparent"
)

button_frame.pack(pady=40)

# -------------------- ROCK BUTTON -------------------- #

rock_btn = ctk.CTkButton(
    button_frame,
    text="🪨\nROCK",
    width=200,
    height=140,
    font=("Poppins", 24, "bold"),
    corner_radius=25,
    fg_color="#6C63FF",
    hover_color="#574FD6",
    command=lambda: play("Rock")
)

rock_btn.grid(row=0, column=0, padx=20)

# -------------------- PAPER BUTTON -------------------- #

paper_btn = ctk.CTkButton(
    button_frame,
    text="📄\nPAPER",
    width=200,
    height=140,
    font=("Poppins", 24, "bold"),
    corner_radius=25,
    fg_color="#FF9800",
    hover_color="#E68900",
    command=lambda: play("Paper")
)

paper_btn.grid(row=0, column=1, padx=20)

# -------------------- SCISSORS BUTTON -------------------- #

scissors_btn = ctk.CTkButton(
    button_frame,
    text="✂\nSCISSORS",
    width=200,
    height=140,
    font=("Poppins", 24, "bold"),
    corner_radius=25,
    fg_color="#00C853",
    hover_color="#00A844",
    command=lambda: play("Scissors")
)

scissors_btn.grid(row=0, column=2, padx=20)

# -------------------- RESET BUTTON -------------------- #

reset_btn = ctk.CTkButton(
    main_frame,
    text="🔄 RESET GAME",
    width=250,
    height=60,
    font=("Poppins", 20, "bold"),
    corner_radius=18,
    fg_color="#FF4B5C",
    hover_color="#E63946",
    command=reset_game
)

reset_btn.pack(pady=30)

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