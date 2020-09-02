#!/usr/bin/python

import hashlib
import array
from functools import reduce
from PIL import Image, ImageDraw

"""
Module containing functions to convert string into an identicon
"""

def main(word):
    """
    method that triggers all the operations necessary to create an identicon.

    An identicon is a image to uniquely identify some entity. Several websites such as
    github and github use identicons to identify users when no image is provided.
    The identicon takes an md5 hash of the entitie's name and generates a grid
    and draws it using a color made of the first three bytes of the hash

    Args:
        word (str): word that should be converted into an identicon
    """
    hex = hash_input(word)
    color = pick_color(hex)
    grid = build_grid(hex)
    grid = filter_odd_squares(grid)
    pixel_map = build_pixel_map(grid)
    draw_image(word,color,pixel_map)
    

def hash_input(expression):
    """
    Hashes the user input using the md5 alghorithm.

    A hash function is any function that can map data of arbitrary size to fixed size values. The 
    return values of a hash function are usually called digest. MD5 is the hashing algorithm with
    the shortest digest of 128 bits or 16 bytes (1 byte = 8 bits). This function uses the python
    hashlib library to generate an md5 hash of the expression provided and then the hash is con-
    verted to a list bytes represented by their number.

    Args:
        expression (str): expression to be hashed 

    Returns:
        list: list of numbers representing the bytes of the resulting hash of the expression
    """
    return list(array.array('B',hashlib.md5(expression.encode()).digest())) 


def pick_color(hex):
    """
    Takes first three bytes of an md5 and converts them to an
    rgb(red, green, blue) code.

    Args:
        hex (list): list of bytes from hash

    Returns:
        tuple: rgb code resulting from first three bytes of the hash
    """
    return (hex[0],hex[1],hex[2])


def build_grid(hex):
    """
    Builds a grid in order to paint the pixels of the identicon.

    The identicon we plan to build is made of a grid of 25 squares. Considering that the result
    of the hash is a 16 byte list we are going to ignore the last byte and mirror the bytes of each
    row (e.g.: row one has bytes 1,2 and 3 after mirroring the row will contain bytes 1,2,3,2 and 1).
    To do this: first chunk the list of bytes into chunks of 3, and we remove the last element; next
    we mirror each chunk, i.e. we sum the chunk itself with the last element removed and reversed;
    after that we flatten the grid by unpacking all chunks; and finally we pair each element with its
    position in the array (this will be important in the following operations)

    Args:
        hex (list): list of bytes from hash

    Returns:
        list: list of tuples each containing the byte number and the position of the byte in the list
    """
    chuncked_list = [hex[i : i + 3] for i in range(0,len(hex),3)]
    chuncked_list = chuncked_list[:-1]
    mirrored_chuncked_list = list(map(lambda chunk: chunk + chunk[:-1][::-1], chuncked_list))
    flattened_list = [item for sublist in mirrored_chuncked_list for item in sublist]
    # flattened_list = list(reduce(lambda chunkx,chunky: chunkx + chunky, mirrored_chuncked_list))
    return [(flattened_list[position],position) for position in range(len(flattened_list))]


def filter_odd_squares(grid):
    """
    Filters elements of a flattened list that contain bytes with odd number.

    To paint the identicon first we need to identify what pixels should be colored. For
    this example we only pains the even bytes.

    Args:
        grid (list): of bytes followed by their positions in the list.

    Returns:
        list: list of bytes that are even and their corresponding positions in the grid
    """
    return list(filter(lambda x: x[0] % 2 == 0, grid))


def build_pixel_map(grid):
    """
    Converts grid of bytes to grid of coordinates to draw in a 250x250 pixel image.

    The identicon is a 250x250 pixels image with squares of 50x50 pixels. To draw these squares 
    the coordinates of the top left and bottom right corners of each squares need to be calculated. 

    Args:
        grid (list): list of bytes and their positions in the grid

    Returns:
        list: list of coordinates of top left corners and bottom right corners of squares that make the identicon
    """
    return list(map(calc_vertices, grid))


def calc_vertices(cell):
    """
    This function calculates the coordinates of the top left and bottom right corners by multiplying 
    the remainder of dividing the position of the square by 5, with 50, to get the horizontal coordinate 
    of the top left. Next the result of the integer division of the positon of the square by 5 is multiplied 
    by 5 to obtain the vertical coordinate of the top left corner. Finnaly, now that we know the coordinates
    of the top left corner we add 50 to the abscissa and ordinate of the coordinates to get the coordinates of
    the bottom right corner of the square.

    Args:
        cell (tuple): byte number and position of the byte in the grid

    Returns:
        tuple: coordinates of top left and bottom right corners of a square in the identicon
    """
    horizontal = cell[1]%5*50
    vertical = cell[1]//5*50

    top_lef = (horizontal,vertical)
    bottom_right = (horizontal+50,vertical+50)

    return (top_lef,bottom_right)


def draw_image(expression, color, pixel_map):
    """
    Draws the identicon and saves it to the project directory.

    Now that we have the color and the pixel map (list of coordinates of corners of squares) we 
    can now draw the identicon using the Pillow library.

    Args:
        word (expression): expression corresponing to the identicon (user input).
        color (tuple): rgb code of the color to paint the squares of the identicon.
        pixel_map (list): list of coordinates of corners of the identicon squares.
    """
    image = Image.new('RGB', (250,250), 'white')
    idraw = ImageDraw.Draw(image)

    for pixel in pixel_map:
        idraw.rectangle(pixel,fill=color)
    
    image.save(format_image_name(expression)+".png")


def format_image_name(expression):
    """
    Makes string lowercase, and replaces spaces by underscores

    Args:
        expression (str): expression that is to be formated

    Returns:
        str: lowercase string with underscores instead of spaces
    """
    return expression.lower().replace(' ','_')
    

if __name__=='__main__':
    word = input("Write something: \n")
    main(word)