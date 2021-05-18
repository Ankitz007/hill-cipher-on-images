# Image Encryption/Decryption using Hill Cipher

This repository contains an implementation of Hill Cipher to encrypt/decrypt images. Make sure that the image which you are using for encryption has 3 channels only. The code is not valid for images having more than 3 channels.  

In order to execute the scripts, follow the steps:  

- Open `Encrypt.py` and mention the path to the input image.
- Open terminal and run `python3 Encrypt.py`.
- At this point of time, the encrypted image as well as the key will be generated and saved in your current directory. Feel free to view them.
- To decrypt the image, run `python3 Decrypt.py` on your terminal.
- The decrypted image will be saved to your current directory.

## Sample Images

### Original Image
![Original Image](./images/1.jpg)

### Encrypted Image
![Encrypted Image](./images/Encrypted.png)

### Key
![Key](./images/Key.png)

### Decrypted Image
![Decrypted Image](./images/Decrypted.png)

## Important

The algorithm implementation has been taken from the following paper:  
Acharya, Bibhudendra & Panigrahy, Saroj Kumar & Patra, Sarat & Panda, Ganapati. (2009). "Image Encryption Using Advanced Hill Cipher Algorithm". International Journal of Recent Trends in Engineering. Vol 1. 

