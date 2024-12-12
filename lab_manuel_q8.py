# Create a database using list and tuples using classes, inheritence and instances

class database:
    def insert_data(self,id,name,age,salary):
        self.data = []
        self.data.append((id,name,age,salary))
    def display_data(self):
        print("ID  | Name | Age |salary ")
        print("-----------------------------")
        for i in self.data:
            print(f"{i[0]:<3} | {i[1]:<15} | {i[2]:<3} | {i[3]}")

class database2(database):
    def add_data(self,id,name,age,salary):
        self.data.append((id,name,age,salary))

    def remove_row(self,id):
        self.data.pop(id-1)



e = database2()
e.insert_data(1,"Rushil",19,480000)
e.add_data(2,"Akshat",20,50000)
e.add_data(3,"Ojas",21,51000)



e.display_data()
