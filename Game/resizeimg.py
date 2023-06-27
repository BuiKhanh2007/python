from PIL import Image

# Open the original image
image = Image.open("layer_1.png")

# Resize the image to the desired dimensions
resized_image = image.resize((550, 450))

# Save the resized image
resized_image.save("layer_1.png")
