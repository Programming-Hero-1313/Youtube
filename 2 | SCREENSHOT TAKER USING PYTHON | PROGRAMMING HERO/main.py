# importing the ImageGrab function from PILLOW (PIL) Module
from PIL import ImageGrab

# to take the screenshot of your pc (Main Function)
screenshot = ImageGrab.grab()

# saving the screenshot in your pc (screenshot will be saved in the directory you are working)
screenshot.save()

# To open the screenshot in the default image viewer (Optional)
screenshot.show()
