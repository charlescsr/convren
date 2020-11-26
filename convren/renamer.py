import os
from PIL import Image

class Renamer():
    """
        Renamer instance to convert images to user defined format
    """
    def __init__(self):
        pass

    def conv_ren(self, folder, form='jpeg', name=None):
        """
            Converts image to format 'form' with the name 'name' in the folder 'folder'
            Args:
                folder (string): folder to look in (preferably with all images)
                form (string): Format to convert to (Default:jpeg)
                name (string): Name to specify for the image (Default:None). If None is specified, 
                then name does not change.  
            Returns:
                None
        """
        i = 1
        for filename in os.listdir(folder):
            img = Image.open(os.path.join(folder,filename)).convert("RGB")
            try:
                s = str(name)+"."+str(i)+str(form) if name != None else filename
                os.remove(os.path.join(folder,filename))
                img.save(os.path.join(folder,s), form)
            except Exception:
                print("Check if you have the right format going on. JPG is JPEG. File path should be absolute")
                break
            i += 1

    def null_images(self, folder):
        """

        """
