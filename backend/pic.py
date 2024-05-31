from PIL import Image

# Load the images
image1_path = "frontend/my-app/public/IMG_0170.jpg"
image2_path = "frontend/my-app/public/shutterstock_747440269-e1633997358135-1024x567.jpg"
image1 = Image.open(image1_path)
image2 = Image.open(image2_path)

# Determine the height of the final collage (use the smaller height to ensure no skewing)
final_height = min(image1.height, image2.height)

# Resize images to the same height
aspect_ratio1 = image1.width / image1.height
aspect_ratio2 = image2.width / image2.height
new_width1 = int(aspect_ratio1 * final_height)
new_width2 = int(aspect_ratio2 * final_height)
resized_image1 = image1.resize((new_width1, final_height), Image.LANCZOS)
resized_image2 = image2.resize((new_width2, final_height), Image.LANCZOS)

# Create a blank canvas for the collage
collage_width = new_width1 + new_width2
collage = Image.new('RGB', (collage_width, final_height), (255, 255, 255))

# Paste the images onto the canvas
collage.paste(resized_image1, (0, 0))
collage.paste(resized_image2, (new_width1, 0))

# Save the collage
collage_path_side_by_side = "frontend/my-app/public/collage_side_by_side.jpg"
collage.save(collage_path_side_by_side)
collage.show()
