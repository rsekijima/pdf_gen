import os

from PIL import Image


def images_to_pdf(folder_path, output_pdf="output.pdf"):
    pdf_width = int(os.getenv("PDF_WIDTH", "2234"))
    pdf_height = int(os.getenv("PDF_HEIGHT", "1571"))
    dpi = int(os.getenv("DPI", "200"))
    image_list = []

    for filename in sorted(os.listdir(folder_path)):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            image_path = os.path.join(folder_path, filename)
            img = Image.open(image_path)

            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")

            image_list.append(img)

    pdf_pages = []

    for i in range(0, len(image_list), 2):
        a4_canvas = Image.new("RGB", (pdf_width, pdf_height), "white")

        img1 = image_list[i]
        img2 = image_list[i + 1] if i + 1 < len(image_list) else None

        total_height = img1.height + (img2.height if img2 else 0)

        num_images = 2 if img2 else 1
        padding = (pdf_height - total_height) // (num_images + 1)

        current_y = padding

        a4_canvas.paste(img1, ((pdf_width - img1.width) // 2, current_y))
        current_y += img1.height + padding

        if img2:
            a4_canvas.paste(img2, ((pdf_width - img2.width) // 2, current_y))

        pdf_pages.append(a4_canvas)

    if pdf_pages:
        pdf_pages[0].save(
            output_pdf,
            save_all=True,
            append_images=pdf_pages[1:],
            dpi=(dpi, dpi),
        )
        return f"PDF criado com sucesso: {output_pdf}"
    else:
        raise Exception(
            "Não foram encontradas images PNG ou JPEG na pasta especificada."
        )
