import qrcode
import re

"""
This module creates a QR code
"""

class URLError(Exception):
    """
    Exception to be raised when the string presented is not a url
    """
    def __init__(self, message="The provided URL is not valid"):
        self.message = message
        super().__init__(self.message)


def generateQRCodeFor(website, toLocation):
    """generates a QR code for a given website and saves it in the project directory.
    Raises URLError if the URL presented is not valid

    Args:
        website (str): URL of the website for which to generate QR code
        toLocation (str, optional): location to which to save file. Defaults to "qr.png".
    """
    valid = validateURL(website)

    if not valid:
        raise URLError

    img = qrcode.make(website)

    img.save(toLocation)


def validateURL(url):
    """Validates if presented url is valid

    Args:
        url (str): url to be validated
    """
    pattern = re.compile("^https*:\/\/\w+(\.\w+){2}[\/A-Za-z\d\?\=]*$")
    match = pattern.match(url)

    return True if match else False


if __name__=='__main__':
    import argparse
    argumentParser = argparse.ArgumentParser(description="generates a QR code and saves it to location")
    argumentParser.add_argument('-l','--location',type=str,default="qr.png",help="location to which to save QR")
    argumentParser.add_argument('website',help="name of the website for which to generate QR code")
    args = argumentParser.parse_args()
    generateQRCodeFor(args.website,args.location)



