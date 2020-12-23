from tkinter import*
from PIL import ImageTk, Image

def upload_images(root):
    main1_image = ImageTk.PhotoImage(Image.open("1.png"))
    main2_image = ImageTk.PhotoImage(Image.open("2.png"))
    main3_image = ImageTk.PhotoImage(Image.open("3.png"))

    left_button_image = ImageTk.PhotoImage(Image.open("left_Arrow.png").resize((60, 50)))
    right_button_image = ImageTk.PhotoImage(Image.open("right_Arrow.png").resize((60, 50)))
    exit_button_image = ImageTk.PhotoImage(Image.open("Exit.png").resize((60, 50)))

    # Frist array contains the main images
    # Second array contains the button images
    return [main1_image, main2_image, main3_image], [left_button_image,exit_button_image, right_button_image]


def create_interface(root, main_images_list, buttons_list):
    # creating and displaying the first main image
    main_label = Label(root, image=main_images_list[0])
    main_label.grid(columnspan=3)



    # creating and displaying the buttons
    left_button = Button(root, image=buttons_list[0], command=lambda:Command(root, main_label, 0, main_images_list, buttons_list,-1))
    left_button.grid(column=0, row=1)
    exit_button = Button(image=buttons_list[1], command=root.quit)
    exit_button.grid(column=1, row=1)
    right_button = Button(root, image=buttons_list[2], command=lambda:Command(root, main_label, 0, main_images_list, buttons_list,1))
    right_button.grid(column=2, row=1)


def Command(root, main_label, position, main_images_list, buttons_list, option):
    if option == -1:
        if position > 0:
            main_label.grid_forget()
            main_label = Label(root, image=main_images_list[position - 1])
            main_label.grid(row=0, column=0, columnspan=3)
            # creating and displaying the buttons
            left_button = Button(root, image=buttons_list[0],
                                 command=lambda: Command(root, main_label, position-1, main_images_list, buttons_list, -1))
            left_button.grid(column=0, row=1)
            exit_button = Button(image=buttons_list[1], command=root.quit)
            exit_button.grid(column=1, row=1)
            right_button = Button(root, image=buttons_list[2],
                                  command=lambda: Command(root, main_label, position-1, main_images_list, buttons_list, 1))
            right_button.grid(column=2, row=1)
        elif position == 0:
            left_button = Button(root, image=buttons_list[0],state=DISABLED)
            left_button.grid(column=0, row=1)


    elif option == 1:
        if position < 2:
            main_label.grid_forget()
            main_label = Label(root, image=main_images_list[position + 1])
            main_label.grid(row=0, column=0, columnspan=3)

            # creating and displaying the buttons
            left_button = Button(root, image=buttons_list[0],
                                 command=lambda: Command(root, main_label, position + 1, main_images_list, buttons_list, -1))
            left_button.grid(column=0, row=1)
            exit_button = Button(image=buttons_list[1], command=root.quit)
            exit_button.grid(column=1, row=1)
            right_button = Button(root, image=buttons_list[2],
                                  command=lambda: Command(root, main_label,position + 1, main_images_list, buttons_list, 1))
            right_button.grid(column=2, row=1)
        elif position == 2:
            right_button = Button(root, image=buttons_list[2],state=DISABLED)
            right_button.grid(column=2, row=1)


