import argparse
import logging
import PIL.Image

def main(args):
    """
    Main entry point for the program, takes in a string of arguments
    and defines the arguments to be taken
    """
    logging.basicConfig(level=logging.DEBUG)

    parser = argparse.ArgumentParser(description="Converts pictures to ASCII")
    parser.add_argument("picture", action="store", type=str)
    parser.add_argument("--width",type=int,action="store",default=80)
    parser.add_argument("--font_ratio",type=float,action="store",default=0.5)

    results = parser.parse_args(args)

    convert(PIL.Image.open(results.picture),results.width,results.font_ratio)
    print(results.font_ratio)

def get_brightness(rgb):
    #Relative luminance - https://en.wikipedia.org/wiki/Relative_luminance
    return (0.2126*rgb[0]+0.7152*rgb[1]+0.0722*rgb[2])/255

def convert(img,width=80,font_aspect_ratio=0.5):
    """
    Takes a PIL image object and converts it to ASCII text with a
    default width of 80 characters
    """
    out = []
    sf = img.width//width
    img = img.resize((round(img.width//sf/font_aspect_ratio),img.height//sf))

    chars = [" ",",","^","#","$"]

    for y in range(img.height):
        out.append([])
        for x in range(img.width):
            out[-1].append(chars[round(
                get_brightness(img.getpixel((x,y)))*len(chars))-1])

    for x in out:
        for y in x:
            print(y,end="")
        print("")

