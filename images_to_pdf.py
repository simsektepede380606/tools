# importing necessary libraries
from PIL import Image
import os
import sys

if(len(sys.argv) == 1 or sys.argv[1] == "-h"):
    print("USAGE: python ./your_script.py path_to_directory_of_images output_file")
    exit()

# storing image directory (take this from arguments)
img_dir = sys.argv[1] # dir for images

# storing pdf path
pdf_path = sys.argv[2] # path for output

imagesFilenames = os.listdir(img_dir)

imagesObjects = []


for fileName in imagesFilenames:
    img_path = os.path.join(img_dir,fileName)

    # opening image
    image = Image.open(img_path)

    imagesObjects.append(image)


imagesObjects[0].save(pdf_path, "PDF", save_all=True, append_images=imagesObjects[1:])

# output
print(f"Your pdf is now on the path : {os.path.abspath(pdf_path)} !")

