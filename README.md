# CheckProgress
ComfyUI Custom Node (draft)

I was looking for a node to put in place to ensure my prompt etc where going as expected before the rest of the flow executed. 
To end the session, I just return the input image as None (see expected error).

Recommend using it alongside PreviewImage, then output to the rest of the flow and Save Image.

Possible Use Case:
![Screenshot from 2024-01-09 17-32-13](https://github.com/MrAdamBlack/CheckProgress/assets/25074127/3554bc5e-6846-4f1e-8b01-8374c18c6078)

The expected error to receive:
![Screenshot from 2024-01-09 17-32-36](https://github.com/MrAdamBlack/CheckProgress/assets/25074127/f02f9449-40d0-4ea2-a4a4-a1fbcacc03f2)
