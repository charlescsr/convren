import os 
from PIL import Image

def conv_ren(folder, form, name):
    """
        Convert all images in a folder to a single format(jpg) and single name
    """
    i = 1
    for filename in os.listdir(folder):
        img = Image.open(os.path.join(folder,filename)).convert("RGB")
        try:
            s = str(name)"."+str(i)+str(form)
            img.save(s, str(form))
        except Exception:
            print("Wrong format")
        i += 1