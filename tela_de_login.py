import customtkinter as ctk

login = ctk.CTk()
login.title("Login")
login.geometry("1920x1080")

frame_login = ctk.CTkFrame(login)
frame_login.pack(pady=20, padx=20, fill="both")

entry_nome_email = ctk.CTkEntry(frame_login)
entry_nome_email.pack(pady=5)

entry_senha = ctk.CTkEntry(frame_login)
entry_senha.pack(pady=10)

login.mainloop()
