class Patient:
    
    def __init__(self, first_name, last_name, mrn, age):
        self.first_name = first_name
        self.last_name = last_name
        self.mrn = mrn
        self.age = age
        self.tests=[]
        
    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)
    
    def is_adult(self):
        if self.age<18:
            return False
        else:
            return True
        
def main():
    new_patient = Patient("Ann", "Ables", 1, 34)
    print(new_patient.first_name)
    
if "__name__"== "__main__":
    main()