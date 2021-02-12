import csv
from polydiavlika import myglobal

class Buffer():
    def __init__(self,size):
        self.size=size
        self.db=[]

    def has_packets(self):
        if len(self.db)>0:
            return True

    def get_next_packet(self):
        mypacket=self.db[0]
        self.db.pop(0)
        return mypacket

    def add(self,packet):
        current_buffer_size=self.get_current_size()
        if current_buffer_size+packet.packet_size<=self.size:
            self.db.append(packet)
            return True
        else:
            return False #drop

    def delete_by_id(self,id):
        for element in self.db:
            if element.id==id:
                self.db.remove(element)
                break

    def get_current_size(self):
        mysize=0
        for element in self.db:
            mysize=mysize+element.packet_size
        return mysize



