import sys
from PIL import Image, ImageOps

def main():
    if len(sys.argv) <3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".jpg") and not sys.argv[1].endswith(".JPG") and not sys.argv[1].endswith(".jpeg") and not sys.argv[1].endswith(".JPEG") and not sys.argv[1].endswith(".png") and not sys.argv[1].endswith(".PNG"):
        sys.exit("Invalid input")
    elif not sys.argv[2].endswith(".jpg") and not sys.argv[1].endswith(".JPG") and not sys.argv[1].endswith(".jpeg") and not sys.argv[1].endswith(".JPEG") and not sys.argv[1].endswith(".png") and not sys.argv[1].endswith(".PNG"):
        sys.exit("Invalid input")
    elif not same_extension(sys.argv[1],sys.argv[2]):
        sys.exit("Input and output have different extensions")
    else:
        try:
            image = Image.open(sys.argv[1])
            shirt = Image.open("shirt.png")
            size = shirt.size
            image2 = ImageOps.fit(image,size)
            image2.paste(shirt,shirt)
            image2.save(sys.argv[2])

        except FileNotFoundError:
            sys.exit("File not found")
def same_extension(file1,file2):
    filename1 ,extension1 = file1.lower().split(".")
    filename2 ,extension2 = file2.lower().split(".")
    if extension1 == extension2:
        return True
    else:
        return False

if __name__ == "__main__":
    main()

