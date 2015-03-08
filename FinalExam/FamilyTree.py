class Member(object):
    def __init__(self, founder):
        """ 
        founder: string
        Initializes a member. 
        Name is the string of name of this node,
        parent is None, and no children
        """        
        self.name = founder
        self.parent = None         
        self.children = []    

    def __str__(self):
        return self.name    

    def add_parent(self, mother):
        """
        mother: Member
        Sets the parent of this node to the `mother` Member node
        """
        self.parent = mother   

    def get_parent(self):
        """
        Returns the parent Member node of this Member
        """
        return self.parent 

    def is_parent(self, mother):
        """
        mother: Member
        Returns: Boolean, whether or not `mother` is the 
        parent of this Member
        """
        return self.parent == mother  

    def add_child(self, child):
        """
        child: Member
        Adds another child Member node to this Member
        """
        self.children.append(child)   

    def is_child(self, child):
        """
        child: Member
        Returns: Boolean, whether or not `child` is a
        child of this Member
        """
        return child in self.children 


class Family(object):
    def __init__(self, founder):
        """ 
        Initialize with string of name of oldest ancestor

        Keyword arguments:
        founder -- string of name of oldest ancestor
        """

        self.names_to_nodes = {}
        self.root = Member(founder)    
        self.names_to_nodes[founder] = self.root   

    def set_children(self, mother, list_of_children):
        """
        Set all children of the mother. 

        Keyword arguments: 
        mother -- mother's name as a string
        list_of_children -- children names as strings
        """
        # convert name to Member node (should check for validity)
        mom_node = self.names_to_nodes[mother]   
        # add each child
        for c in list_of_children:           
            # create Member node for a child   
            c_member = Member(c)               
            # remember its name to node mapping
            self.names_to_nodes[c] = c_member    
            # set child's parent
            c_member.add_parent(mom_node)        
            # set the parent's child
            mom_node.add_child(c_member)         
    
    def is_parent(self, mother, kid):
        """
        Returns True or False whether mother is parent of kid. 

        Keyword arguments: 
        mother -- string of mother's name
        kid -- string of kid's name
        """
        mom_node = self.names_to_nodes[mother]
        child_node = self.names_to_nodes[kid]
        return child_node.is_parent(mom_node)
    
    def is_sibling(self, child1, child2):
        """ Returns True if two people are siblings """
        child1_node = self.names_to_nodes[child1]
        child2_node = self.names_to_nodes[child2]
        return child1_node.get_parent() == child2_node.get_parent()
    
    def get_generation(self, child):
        """ 
        Returns the generation from root (zeroth generation)
        """
        generation = 1
        foundRoot = False
        child_node = self.names_to_nodes[child]
        while not foundRoot:
            if child_node.get_parent() == None:
                generation = 0
                foundRoot = True
            elif child_node.get_parent() == self.root:
                foundRoot = True
            else:
                generation += 1
                temp = child_node.get_parent()
                child_node = temp
        return generation
    def are_direct_descendants(self, p1, p2):
        """
        Returns True if two family members are direct descendants
        """
        gen_p1 = self.get_generation(p1)
        gen_p2 = self.get_generation(p2)
        p1_node = self.names_to_nodes[p1]
        p2_node = self.names_to_nodes[p2]
        
        # if same generation, then not direct descendants
        if gen_p1 == gen_p2:
            return False
        # at one generation apart, determine if parent-child relationship exists
        elif abs(gen_p1 - gen_p2) == 1:
            return self.is_parent(p1, p2) or self.is_parent(p2, p1)
        # otherwise move to parent of lower generation
        else:
            if gen_p1 < gen_p2:
                p2_node = p2_node.get_parent()
                temp = p2_node.name
                return self.are_direct_descendants(p1,temp)
            else:
                p1_node = p1_node.get_parent()
                temp = p1_node.name
                return self.are_direct_descendants(temp,p2)
         

    def is_child(self, kid, mother):
        """
        Returns True or False whether kid is child of mother. 

        Keyword arguments: 
        kid -- string of kid's name
        mother -- string of mother's name
        """        
        mom_node = self.names_to_nodes[mother]   
        child_node = self.names_to_nodes[kid]
        return mom_node.is_child(child_node)

    def cousin(self, a, b):
        """
        Returns a tuple of (the cousin type, degree removed) 

        Keyword arguments: 
        a -- string that is the name of node a
        b -- string that is the name of node b

        cousin type:
          -1 if a and b are the same node.
          -1 if either one is a direct descendant of the other
          >=0 otherwise, it calculates the distance from 
          each node to the common ancestor.  Then cousin type is 
          set to the smaller of the two distances, as described 
          in the exercises above

        degrees removed:
          >= 0
          The absolute value of the difference between the 
          distance from each node to their common ancestor.
        """
        
        # convert names to Member nodes
        a_node = self.names_to_nodes[a]
        b_node = self.names_to_nodes[b]
        
        # initialization
        gen_a = self.get_generation(a)
        gen_b = self.get_generation(b)
        degRemoved = abs(gen_a - gen_b)
        
        # function to calculate the cousinType for same generation people
        def calcSameGenCousin(a, b):
            a_node = self.names_to_nodes[a]
            b_node = self.names_to_nodes[b]
            cousinType = 1
            gen_a = self.get_generation(a)
            for i in range(gen_a):
                if self.is_sibling(a_node.get_parent().name, b_node.get_parent().name):
                    break
                else:
                    cousinType += 1
                    a_node = a_node.get_parent()
                    b_node = b_node.get_parent()
            return cousinType
        
        # a and b are the same node
        if a_node == b_node:
            cousinType = -1
            degRemoved = 0
        
        # a and b are direct descendants
        elif self.are_direct_descendants(a, b):
            cousinType = -1
 
        # a and b are siblings
        elif self.is_sibling(a, b):
            cousinType = 0
            degRemoved = 0
        
        # a and b in same generation but not siblings
        elif gen_a == gen_b and not self.is_sibling(a, b):
            cousinType = calcSameGenCousin(a, b)
       
        # a and b different generations, determine if ancestors at same generation
        # are siblings
        else:
            if gen_a < gen_b:
                fixed = a
                var = b
            else:
                fixed = b
                var = a
            var_node = self.names_to_nodes[var]
            for i in range(degRemoved):
                var_node = var_node.get_parent()
            var = var_node.name
            if self.is_sibling(var,fixed):
                cousinType = calcSameGenCousin(var, fixed)-1
            else:
                cousinType = calcSameGenCousin(var, fixed)
                 
        return (cousinType, degRemoved)


f = Family("a")
f.set_children("a", ["b", "c"])
f.set_children("b", ["d", "e"])
f.set_children("c", ["f", "g"])

f.set_children("d", ["h", "i"])
f.set_children("e", ["j", "k"])
f.set_children("f", ["l", "m"])
f.set_children("g", ["n", "o", "p", "q"])

words = ["zeroth", "first", "second", "third", "fourth", "fifth", "non"]

## These are your test cases. 

## The first test case should print out:
## 'b' is a zeroth cousin 0 removed from 'c'
t, r = f.cousin("b", "c")
print "'b' is a", words[t],"cousin", r, "removed from 'c'"

## For the remaining test cases, use the graph to figure out what should 
## be printed, and make sure that your code prints out the appropriate values.

t, r = f.cousin("d", "f")
print "'d' is a", words[t],"cousin", r, "removed from 'f'"

t, r = f.cousin("i", "n")
print "'i' is a", words[t],"cousin", r, "removed from 'n'"

t, r = f.cousin("q", "e")
print "'q' is a", words[t], "cousin", r, "removed from 'e'"

t, r = f.cousin("h", "c")
print "'h' is a", words[t], "cousin", r, "removed from 'c'"

t, r = f.cousin("h", "a")
print "'h' is a", words[t], "cousin", r, "removed from 'a'"

t, r = f.cousin("h", "h")
print "'h' is a", words[t], "cousin", r, "removed from 'h'"

t, r = f.cousin("a", "a")
print "'a' is a", words[t], "cousin", r, "removed from 'a'"
