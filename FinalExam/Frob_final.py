# -*- coding: utf-8 -*-
class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name
        
def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
    """          
    
    ###### Base cases
    # atMe has no before and newFrob is less or equal to than atMe
    if atMe.myName() > newFrob.myName() and atMe.getBefore() == None:
        atMe.setBefore(newFrob)
        newFrob.setAfter(atMe)
        return None
    
    # atMe has no after and newFrob is greater than or equal to atMe
    if atMe.myName() <= newFrob.myName() and atMe.getAfter() == None:
        atMe.setAfter(newFrob)
        newFrob.setBefore(atMe)
        return None

    # newFrob is greater than atMe but less than or equal to atMe.after
    if (newFrob.myName() >= atMe.myName() and
        newFrob.myName() <= atMe.getAfter().myName()):
        newFrob.setAfter(atMe.getAfter())
        atMe.getAfter().setBefore(newFrob)    
        atMe.setAfter(newFrob)
        newFrob.setBefore(atMe)
        return None
    
    # newFrob is less than or equal to atMe but greater than or equal to atMe.before
    if (newFrob.myName() <= atMe.myName() and
        newFrob.myName() >= atMe.getBefore().myName()):
        newFrob.setBefore(atMe.getBefore())
        atMe.getBefore().setAfter(newFrob)
        atMe.setBefore(newFrob)
        newFrob.setAfter(atMe)
        return None
    
    ##### General cases
    # newFrob is greater than atMe and greater than atMe.after
    if (newFrob.myName() > atMe.myName() and
        newFrob.myName() > atMe.getAfter().myName()):
        insert(atMe.getAfter(),newFrob)
    
    # newFrob is less than or equal to atMe and less than or equal to atMe.before
    if (newFrob.myName() <= atMe.myName() and
        newFrob.myName() <= atMe.getBefore().myName()):
        insert(atMe.getBefore(),newFrob)

def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list 
    """
    #base case
    if start.getBefore() == None:
        return start
    return findFront(start.getBefore())