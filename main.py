from functions import*


def main():
    root = Tk()

    root.title("Alisia")
    root.iconbitmap("hnet.com-image.ico")

    # uploading all the images and buttons_icons
    array = upload_images(root)

    # Creating the interface
    # array[0] = list of main images
    # array[1] = list of button icons
    create_interface(root, array[0], array[1])
    mainloop()


main()




