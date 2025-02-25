# 🕵️‍♂️ Steganography-Based Secret Message Encoding and Decoding System

**Hide your secrets in plain sight!**  
This project is a Python-based tool that lets you **encode secret messages into images** and **decode them back** using the **Least Significant Bit (LSB)** technique. Whether you're a privacy enthusiast, a cybersecurity student, or just someone who loves cool tech, this tool is for you!

---

## 🌟 Why Steganography?

In a world where data privacy is more important than ever, traditional encryption methods like AES or RSA are great, but they have one problem: **encrypted messages look suspicious**. Steganography solves this by hiding messages in plain sight—inside ordinary files like images, audio, or even text. The result? Your secrets stay hidden, and no one even knows they exist!

This project focuses on **image steganography**, where text messages are embedded into the pixels of an image. The best part? The changes are so subtle that the human eye can't detect them!

---

## 🎯 What Does This Project Do?

This tool allows you to:
- **Encode**: Hide a secret message inside an image.
- **Decode**: Extract the hidden message from the image.
- **Secure**: Protect your message with a password.
- **Preserve**: Keep the original image quality intact.

---

## 🛠️ How It Works

### The Magic of LSB (Least Significant Bit)
The LSB technique works by replacing the **least significant bits** of the image's pixel values with the bits of your secret message. Since these bits contribute the least to the overall color of the pixel, the changes are virtually invisible to the human eye.

#### Encoding Process:
1. Convert the secret message into binary.
2. Replace the LSBs of the image's pixel values with the binary message.
3. Save the modified image.

#### Decoding Process:
1. Extract the LSBs from the image's pixel values.
2. Convert the binary data back into the original message.

---

## 🚀 Features

- **Hide Text in Images**: Embed secret messages into PNG, JPEG, or BMP files.
- **Lossless Quality**: The encoded image looks identical to the original.
- **Easy to Use**: Simple command-line interface for quick encoding/decoding.
- **Cross-Platform**: Works on Windows, macOS, and Linux.

---

## 💻 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mahesh-space/Steganography-Project.git
   cd Steganography-Project
