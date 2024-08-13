userInput = input("File name: ").lower().strip()

if ".gif" in userInput:
    print("image/gif")
elif ".jpg" in userInput or ".jpeg" in userInput:
    print("image/jpeg")
elif ".png" in userInput:
    print("image/png")
elif ".pdf" in userInput:
    print("application/pdf")
elif ".txt" in userInput:
    print("text/plain")
elif ".zip" in userInput:
    print("application/zip")
else:
    print("application/octet-stream")
