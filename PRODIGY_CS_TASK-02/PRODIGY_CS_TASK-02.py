from PIL import Image

def encrypt_image(image_path, key):
    
    # Open the image
    img = Image.open(image_path)
    width, height = img.size

    # Encrypt the image
    encrypted_pixels = []
    for y in range(height):
        for x in range(width):
            
            # Get the pixel value
            pixel = img.getpixel((x, y))
            
            # Apply encryption using the key
            encrypted_pixel = tuple((p + key) % 256 for p in pixel)
            encrypted_pixels.append(encrypted_pixel)

    # Create a new image with the encrypted pixels
    encrypted_img = Image.new(img.mode, img.size)
    encrypted_img.putdata(encrypted_pixels)

    # Save the encrypted image
    encrypted_img.save("encrypted_image.png")
    print("The image encrypted successfully.")

def decrypt_image(encrypted_image_path, key):
    # Open the encrypted image
    img = Image.open(encrypted_image_path)
    width, height = img.size

    # Decrypt the image
    decrypted_pixels = []
    for y in range(height):
        for x in range(width):
           
            # Get the encrypted pixel value
            pixel = img.getpixel((x, y))
            
            # Apply decryption using the key
            decrypted_pixel = tuple((p - key) % 256 for p in pixel)
            decrypted_pixels.append(decrypted_pixel)

    # Create a new image with the decrypted pixels
    decrypted_img = Image.new(img.mode, img.size)
    decrypted_img.putdata(decrypted_pixels)

    # Save the decrypted image
    decrypted_img.save("decrypted_image.png")
    print("The image decrypted successfully.")

# Get user input for image path and key
image_path = input("Please enter the path of the image you want to encrypt: ")
key = int(input("Please enter the encryption/decryption key: "))

# Encrypt the image
encrypt_image(image_path, key)

# Decrypt the encrypted image
decrypt_image("encrypted_image.png", key)