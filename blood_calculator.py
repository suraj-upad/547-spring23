def interface():
    print("My Program")
    keep_running = True
    while keep_running:
        print("Options:")
        print("1: HDL")
        print("2: LDL")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice=='9':
            keep_running = False
        elif choice == '1':
            hdl_driver()
        elif choice == '2':
            ldl_driver()
    print("program is done")
   
    
def hdl_driver():
    hdl_in = hdl_input()
    hdl_anly= hdl_anal(hdl_in)
    hdl_output(hdl_in, hdl_anly)
    
def hdl_input():
    hdl_val = input("enter the hdl result:")
    hdl_val = int(hdl_val)
    return hdl_val

def hdl_anal(hdl_int):
    if hdl_int >= 60:
        return "Normal"
    elif hdl_int>= 40:
        return "borderline Low"
    else:
        return "Low"
    
def hdl_output(hdl_val, hdl_analy):
    print("The HDL result of {} is considered {}".format(hdl_val, hdl_analy))
    return


def ldl_driver():
    ldl_in = ldl_input()
    ldl_anly= ldl_anal(ldl_in)
    ldl_output(ldl_in, ldl_anly)
    
def ldl_input():
    ldl_val = input("enter the ldl result:")
    ldl_val = int(ldl_val)
    return ldl_val

def ldl_anal(ldl_int):
    if ldl_int >= 190:
        return "Very High"
    elif ldl_int>= 160:
        return "High"
    elif ldl_int >= 130:
        return "Borderline High"
    else:
        return "Normal"
    
def ldl_output(ldl_val, ldl_analy):
    print("The LDL result of {} is considered {}".format(ldl_val, ldl_analy))
    return


interface()
