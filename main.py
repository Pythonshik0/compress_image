import PySimpleGUI as sg
from PIL import Image
import os


Image.MAX_IMAGE_PIXELS = None

def compress_image(input_path, quality, png_compress_level):
    output_path = input_path
    with Image.open(input_path) as img:
        if input_path.lower().endswith('.png'):
            img.save(output_path, "PNG", compress_level=png_compress_level)
        else:
            img.save(output_path, "JPEG", quality=quality)


def process_folder(folder_path, quality, png_compress_level):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            file_path = os.path.join(folder_path, filename)
            try:
                compress_image(file_path, quality, png_compress_level)
                print(f"Compressed {filename} to {file_path}")

            except Exception as e:
                print(f"Error processing {filename}: {e}")

layout = [
    [sg.Text('Select Folder'), sg.InputText(), sg.FolderBrowse()],
    [sg.Text('Quality (1-100):'), sg.InputText('70', size=(5, 1))],
    [sg.Text('PNG Compression Level (0-9):'), sg.InputText('9', size=(5, 1))],
    [sg.Output(size=(80, 20))],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('Image Compressor', layout)

while True:
    try:
        event, values = window.read()
        if event in (None, 'Cancel'):
            break
        if event == 'Submit':
            folder_path = values[0]
            quality = int(values[1])
            png_compress_level = int(values[2])

            if not folder_path:
                print('Error: No folder selected.')

            elif not (1 <= quality <= 100):
                print('Error: Quality must be between 1 and 100.')

            elif not (0 <= png_compress_level <= 9):
                print('Error: PNG compression level must be between 0 and 9.')

            else:
                print(f'Processing folder: {folder_path} with quality: {quality} and PNG compression level: {png_compress_level}')
                process_folder(folder_path, quality, png_compress_level)
                print('Processing complete.')

    except Exception as err:
        pass

window.close()