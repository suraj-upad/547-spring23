def interface():
    print("My Program")
    keep_running = True
    while keep_running:
        print("Options:")
        print("1: HDL")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice=='9':
            keep_running = False
        elif choice == '1':
            hdl_driver()
    print("program is done")
   
    
def hdl_driver():
    hdl_in = hdl_input()
    return hdl_anal(hdl_in)
    
    
def hdl_input():
    hdl_val = input("enter the hdl result:")
    hdl_val = int(hdl_val)
    return hdl_val

def hdl_anal(hdl_int):
    if hdl_int >= 60:
        return "Normal"
    elif hdl>= 40:
        return "borderline Low"
    else:
        return "Low"

interface()
