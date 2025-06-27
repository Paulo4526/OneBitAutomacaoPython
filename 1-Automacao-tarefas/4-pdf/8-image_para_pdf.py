#Para converter imagem em pdf devemos baixar a biblioteca pillow com o comando 'pip install Pillow'
import os.path

from PIL import Image

#1 - Convertendo imagem para PDF
def convert_img_to_pdf(image_file):
    my_image = Image.open(image_file)
    img = my_image.convert('RGB')
    filename = f'{os.path.splitext(image_file)[0]}.pdf'
    img.save(filename)

convert_img_to_pdf('files/background_goroh.jpeg')