# Steganography-Hide-Data-in-Images-Using-Python
The mystery information can be information of any organization like content or even a record. More or less, the primary intention of steganography is to conceal the planned data inside any document, generally a picture, sound, or video, without really changing the outer appearance of the record, for example it should look equivalent to previously.


# Encoding 

There are tons of algorithms which will be wont to encode data into the image, and actually , you'll also make one yourself. The one getting used during this blog is straightforward to know and implement, as well.
The algorithm is as follows:

1. For each character within the data, its ASCII value is taken and converted into 8-bit binary [1].

2. Three pixels are read at a time having a complete of 3*3=9 RGB values. the primary eight RGB values are wont to store one character that's converted into an 8-bit binary.

3. The corresponding RGB value and binary data are compared. If the digit is 1 then the RGB value is converted to odd and, otherwise, even.

4. The ninth value determines if more pixels should be read or not. If there's more data to be read, i.e. encoded or decoded, then the ninth pixel changes to even. Otherwise, if we would like to prevent reading pixels further, then make it odd.


# Decoding
For decoding, we shall attempt to find the way to reverse the previous algorithm that we wont to encode data.
Again, three pixels are read at a time. the primary 8 RGB values give us information about the key data, and therefore the ninth value tells us whether to maneuver forward or not.

1. For the primary eight values, if the worth is odd, then the binary bit is 1, otherwise it's 0.

2. The bits are concatenated to a string, and with every three pixels, we get a byte of secret data, which suggests one character.
Now, if the ninth value is even then we keep reading pixels three at a time, or otherwise, we stop.

