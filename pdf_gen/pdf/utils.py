import os


def count_images(folder_path):
    return sum(
        [
            1
            for f in sorted(os.listdir(folder_path))
            if f.lower().endswith((".png", ".jpg", ".jpeg"))
        ]
    )
