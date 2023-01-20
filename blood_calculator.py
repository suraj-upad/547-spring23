def interface():
    print("My Program")
    keep_running = True
    while keep_running:
        print("Options:")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice=='9':
            keep_running = False
    print("program is done")
   
def hdl_input():
    hdl_val = input("enter the hdl result:")
    hdl_val = int(hdl_val)
    return hdl_val

interface()
