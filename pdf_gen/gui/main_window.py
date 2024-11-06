import os
from tkinter import filedialog, messagebox

import customtkinter as ctk

from pdf_gen.pdf import count_images, images_to_pdf


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gerador de PDF")
        self.geometry("400x300")

        self.selected_folder = None
        self.image_count = None
        self.setup_widgets()

    def setup_widgets(self):
        self.grid_columnconfigure((0, 1), weight=1)
        select_folder_button = ctk.CTkButton(
            self, text="Escolher pasta", command=self.select_folder
        )
        select_folder_button.pack(pady=20)

        self.folder_label = ctk.CTkLabel(
            self, text="Pasta não selecionada", wraplength=300
        )
        self.folder_label.pack(pady=10)

        self.image_counter = ctk.CTkLabel(self, text="", wraplength=300)
        self.image_counter.pack(pady=10)

        generate_pdf_button = ctk.CTkButton(
            self, text="Gerar PDF", command=self.generate_pdf
        )
        generate_pdf_button.pack(pady=20)

    def select_folder(self):
        self.selected_folder = filedialog.askdirectory()
        if self.selected_folder:
            self.folder_label.configure(
                text=f"Pasta selecionada:\n{self.selected_folder}"
            )
            self.image_count = count_images(self.selected_folder)
            self.image_counter.configure(
                text=f"{self.image_count} imagens encontradas."
            )

    def generate_pdf(self):
        if not self.selected_folder:
            messagebox.showwarning(
                "Pasta não selecionada", "Selecione uma pasta"
            )
            return

        output_pdf = os.path.join(self.selected_folder, "imagens.pdf")

        try:
            result = images_to_pdf(self.selected_folder, output_pdf)
            messagebox.showinfo("Sucesso", result)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao gerar PDF: {e}")
