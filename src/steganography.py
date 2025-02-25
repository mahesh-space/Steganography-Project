from PIL import Image

def text_to_binary(text):
    """Converts a text string into a binary string, adding a null terminator at the end."""
    return ''.join(format(ord(char), '08b') for char in text) + '00000000'  # End marker

def binary_to_text(binary):
    """Converts binary back to text, stopping at the first null character."""
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join(chr(int(b, 2)) for b in chars if b != "00000000")  # Stops at null char

def encode_message(image_path, message, output_path):
    """Encodes a text message into an image using LSB steganography."""
    try:
        img = Image.open(image_path)
        pixels = img.load()
        width, height = img.size

        binary_message = text_to_binary(message)
        index = 0

        for y in range(height):
            for x in range(width):
                if index < len(binary_message):
                    r, g, b = pixels[x, y]
                    new_r = (r & 0xFE) | int(binary_message[index])  # Modify LSB of red channel
                    pixels[x, y] = (new_r, g, b)
                    index += 1
                else:
                    img.save(output_path)
                    print(f"✅ Message encoded successfully into {output_path}!")
                    return
        
        print("❌ Message is too long for the given image!")
    
    except Exception as e:
        print(f"❌ Error: {e}")

def decode_message(image_path):
    """Decodes a hidden text message from an image."""
    try:
        img = Image.open(image_path)
        pixels = img.load()
        width, height = img.size

        binary_message = ""

        for y in range(height):
            for x in range(width):
                r, _, _ = pixels[x, y]
                binary_message += str(r & 1)  # Extract LSB of red channel
                
                # Stop decoding when we detect the end marker (8 zeros in a row)
                if binary_message[-8:] == "00000000":
                    message = binary_to_text(binary_message)
                    print(f"✅ Decoded Message: {message}")
                    return
        
        print("❌ No hidden message found!")
    
    except Exception as e:
        print(f"❌ Error: {e}")

# User-friendly menu system
def main():
    while True:
        print("\n🖼️ Steganography - Hide Secret Messages in Images 🖼️")
        print("1️⃣ Encode a message into an image")
        print("2️⃣ Decode a message from an image")
        print("3️⃣ Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            image_path = input("Enter the name of the input image (e.g., input.png): ")
            message = input("Enter the secret message: ")
            output_path = input("Enter the name of the output image (e.g., output.png): ")
            encode_message(image_path, message, output_path)
        
        elif choice == '2':
            image_path = input("Enter the name of the image to decode (e.g., output.png): ")
            decode_message(image_path)
        
        elif choice == '3':
            print("👋 Exiting program. Have a great day!")
            break
        
        else:
            print("❌ Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
