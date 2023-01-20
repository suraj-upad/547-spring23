def interface():
    print("My Program")
    keep_running = True
    while keep_running:
        print("Options:")
        print("1: HDL")
        print("2: LDL")
        print("3: Total Cholesterol")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice=='9':
            keep_running = False
        elif choice == '1':
            hdl_driver()
        elif choice == '2':
            ldl_driver()
        elif choice == '3':
            tot_driver()
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


def tot_driver():
    tot_in = tot_input()
    tot_anly= tot_anal(tot_in)
    tot_output(tot_in, tot_anly)
    
def tot_input():
    tot_val = input("enter the Total Cholesterol result:")
    tot_val = int(tot_val)
    return tot_val

def tot_anal(tot_int):
    if tot_int >= 240:
        return "High"
    elif tot_int>= 200:
        return "Borderline High"
    else:
        return "Normal"
    
def tot_output(tot_val, tot_analy):
    print("The Total Cholesterol result of {} is considered {}".format(tot_val, tot_analy))
    return

interface()
