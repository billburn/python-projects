from PIL import Image

webp_image = Image.open('owl.webp')
webp_image.save('owl.png', 'png')