class Arrays:
    def __init__(self):
        
        pass


    def add_in_list(self, The_list, add_item):
        new = [add_item]
        The_list = The_list + new
        return The_list


    def replace_to_index(self, The_list, index, value):
        new_list =[]
        for item in range(len(The_list)):
            if item == index:
                The_list[item]= value
        return The_list
    
        
    def remove_last(self, The_list):
        if len(The_list) == 0:
            return []
        else:
            new_list= []
            for item in range(len(The_list)-1):
               new_list=self.add_in_list(new_list, The_list[item])
            
            return new_list
    

    def remove_value(self, The_list, value):
        new_list=[]
        for item in The_list:
            if item != value:
                new_list = self.add_in_list(new_list, item)
        return new_list
    

    def poper(self, The_list, value):
    
        if isinstance(value, int):
            now_value=The_list[value]
            

            return self.remove_value(The_list, now_value)
        
        elif isinstance(value, str):
            

            return self.remove_value(The_list, value)
        
        else:
            return f"Type Error: invalid value Type  {value}"

                    
            
        
        
    


        
        

    
        
    


