# import tkinter as tk
# # Function to update the expression in the input field
# def button_click(value):
#     current = entry.get()
#     entry.delete(0, tk.END)
#     entry.insert(tk.END, current + value)
# # Function to clear the input field
# def button_clear():
#     entry.delete(0, tk.END)
# # Function to evaluate the expression and display the result
# def button_equal():
#     try:
#         result = eval(entry.get())
#         entry.delete(0, tk.END)
#         entry.insert(tk.END, result)
#     except:
#         entry.delete(0, tk.END)
#         entry.insert(tk.END, "Error")
# # Create the main window
# root = tk.Tk()
# root.title("Calculator")
# # Create the entry widget for displaying the expression
# entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
# entry.grid(row=0, column=0, columnspan=4)
# # Define button labels
# buttons = [
#     ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
#     ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
#     ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
#     ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
#     ('C', 5, 0)
# ]
# # Create the buttons and place them in the grid
# for (text, row, col) in buttons:
#     if text == "=":
#         button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 18), command=button_equal)
#     elif text == "C":
#         button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 18), command=button_clear)
#     else:
#         button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 18), command=lambda value=text: button_click(value))
#     button.grid(row=row, column=col)
#
# # Start the Tkinter event loop
# root.mainloop()


#STACK CONCEPT

l=[]
while True :
    c=int (input('''
    1 Push Element
    2 Pop Element
    3 Peek Element
    4 Display Stack
    5 Exit    import pygame

    # Initialize Pygame
    pygame.init()

    # Set up the screen
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Reptile Cursor")

    # Load reptile image (replace with your own image)
    try:
        reptile_image = pygame.image.load("reptile.png").convert_alpha()
        reptile_image = pygame.transform.scale(reptile_image, (50, 50)) # Adjust size as needed
    except pygame.error as e:
        print(f"Error loading image: {e}")
        pygame.quit()
        exit()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Clear the screen
        screen.fill((255, 255, 255)) # White background

        # Draw the reptile image at the mouse position
        screen.blit(reptile_image, (mouse_x - reptile_image.get_width() // 2, mouse_y - reptile_image.get_height() // 2))

        # Update the display
        pygame.display.flip()

    pygame.quit()
    '''))
    if c==1:
        n=input("Enter the Value :=")
        l.append(n)
        print(l)
    elif c==2:
        if len(l)==0:
            print("Empty Stack ")
        else :
             p=l.pop()
             print(p)
             print(l)
    elif c==3:
        if len(l)==0:
            print("Empty Stack ")
        else:
            print("Last stack:= ",l[-1])
    elif c==4:
        print("Display Stack:=",l)
    else :
        exit()

