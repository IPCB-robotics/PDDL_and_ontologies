#!/usr/bin/python

from pathlib import Path
import fire

class objects:
    def __init__(self, obj, name, prefix=None):
        if len(obj) != (len(name) or len(obj) != len(prefix)):
            raise SystemExit("Error: The variables is don't have same size")
        self.obj = obj
        self.name = name
        self.prefix = prefix


def write_obj(object,class_name):  
    sum_obj = ""
    for i in range(len(object.obj)):
            
        if object.prefix[i] is None:
            a =  "self."+str(object.obj[i]) + " = " + str(class_name)+"Domain."+ object.obj[i] +".create_objs(['"+object.name[i]+"'])"
        else:
            a =  "self."+str(object.obj[i]) + " = " + str(class_name)+"Domain."+ object.obj[i] +".create_objs("+str(object.name[i])+", prefix='"+object.prefix[i]+"')"
        sum_obj += a + "\n\t\t"
    return sum_obj

class Init_Cond:
    def __init__(self, function, obj, conditions): 
        
        if len(function) > (len(obj) or len(function) > len(conditions)):
            raise SystemExit("Error: The variable function is larger than the variables functions or condiditons")
        if len (str(obj).split(',')) != len (str(conditions).split(',')):
            raise SystemExit("Error: The variable obj is don't have the same size of variable conditions")
        self.function = function
        self.obj = obj
        self.conditions = conditions
       
def write_init_or_goal(Cond_Init):  
    c = ""
    for i in range(len(Cond_Init.function)):
    
        if "," in Cond_Init.obj[i] or ";" in Cond_Init.obj[i]:

            objects = []
            for a in [Cond_Init.obj[i]]:
                a = a.split(",")
                objects.extend(a)  
            conditions = []
            for b in [Cond_Init.conditions[i]]:
                b = b.split(",")
                conditions.extend(b) 

            list = ["self." + str(objects[e])+"["+str(conditions[e])+"],"  for e in range(0, len(objects)) ]
            
            listToStr = ' '.join(map(str, list))           
           
            if not c:
                c +=  "self." + str(Cond_Init.function[i]) +"("+ listToStr.rstrip(',') + ")"
            else:
                c = ", " + "self." + str(Cond_Init.function[i]) +"("+ listToStr.rstrip(',') + ")"
                   
        else:
            if not c: 
                c += "self." + str(Cond_Init.function[i]) + "(self." + str(Cond_Init.obj[i]) + "[" + str(Cond_Init.conditions[i]) + "])"
            else:
                c += ", " + "self." + str(Cond_Init.function[i]) + "(self." + str(Cond_Init.obj[i]) + "[" + str(Cond_Init.conditions[i]) + "])"
    
    end = "return [" + c + "]"
    return (end)



def init(filename):
  
    # Name
    class_name = "Robot"
    class_name = sanitise(class_name)
    class_name = class_name[0].upper() + class_name[1:]

    # Define objects and your names
    object = objects(["waypoint","robot"], ["[1,2,3,4,5,6]","Kenny"],["wp", None]) 
    
    # Define Initial conditions 
    Initial_Cond = Init_Cond(["robot_at","docked","docked_at"],["robots,waypoints","robots","waypoints"],["'Kenny',1","'Kenny'","1"])
    
    # Define goals
    Cond_Goal = Init_Cond(["visited","visited","visited","docked"],["waypoints","waypoints","waypoints","robots"],["1","2","3","'Kenny'"])
    

    """
    Args:
        filename (str): name of file ending with `.py`
    """
    path = Path(filename)
    # if path.exists():
    #     raise FileExistsError("This file already exists. Use a different filename.")


    problem_header = \
f"""
class {class_name}Problem({class_name}Domain):
"""

    section_object = \
f"""\
    def __init__(self):
        super().__init__()
        {write_obj(object,class_name)}
        
"""  
        

    section_init = \
f"""\
    @init
    def init(self) -> list:
        {write_init_or_goal(Initial_Cond)}
        
"""

    section_goal = \
f"""\
    @goal
    def goal(self) -> list:
        {write_init_or_goal(Cond_Goal)}
"""


    template = problem_header + "\n" + section_object + \
        "\n" + section_init + "\n" + section_goal

    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(template)
        print(f"File written to {filename}")


def sanitise(text):
    return text.strip().replace("-", "_")


if __name__ == "__main__":
    fire.Fire(init)


