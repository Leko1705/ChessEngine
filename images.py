import PIL.Image as Image

# Load the images
image_path = '/home/kali/PycharmProjects/ChessEngine/res/pieces.png'
image = Image.open(image_path)

# Define the size of each piece
piece_width = 150
piece_height = 150

# Define the number of pieces in the image
pieces_per_row = 8
pieces_per_column = 2

# Loop through the images and crop each piece
for row in range(pieces_per_column):
    for col in range(pieces_per_row):
        left = col * piece_width
        upper = row * piece_height
        right = left + piece_width
        lower = upper + piece_height

        # Crop the image
        piece = image.crop((left,upper,right,lower))

        # Save cropped pieces
        piece.save(f'piece_{row}_{col}.png')
