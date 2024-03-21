import os, struct, json

class RhythmKungFu:
    def Decompile(input,output):
        running=True
        data=[]
        b=open(input,'rb')
        
        while running==True:
            duration=b.read(2)
            if duration==b'\xFF\xFF' or duration==b'':
                break
            else:
                array=[]
                array.append(struct.unpack('>H',duration)[0])
                array.append(struct.unpack('>B',b.read(1))[0])
                array.append(struct.unpack('>B',b.read(1))[0])
                data.append(array)

        json.dump(data,open(output,'w'))
    
    def Compile(input,output,type):
        data=json.load(open(input))
        b=open(output,'wb')
        for d in data:
            b.write(struct.pack('>H',d[0]))
            b.write(struct.pack('>B',d[1]))
            b.write(struct.pack('>B',d[2]))

        if type==0:
            for _ in range(28):
                b.write(b'\xFF')
        if type==1:
            for _ in range(24):
                b.write(b'\xFF')
        
        b.close()

class RhythmParade:
    def Decompile(input,output):
        data=[]
        b=open(input,'rb')
        count=struct.unpack('>H',b.read(2))[0]
        for _ in range(count):
            array=[]
            for __ in range(4):
                array.append(struct.unpack('>B',b.read(1))[0])
            data.append(array)

        json.dump(data,open(output,'w'))

    def Compile(input,output):
        data=json.load(open(input))
        b=open(output,'wb')
        b.write(struct.pack('>H',len(data)))
        for d in data:
            for a in d:
                b.write(struct.pack('>B',a))

        b.close()

class Step:
    def Decompile(input,output):
        data=[]
        b=open(input,'rb')
        count=struct.unpack('>H',b.read(2))[0]
        for _ in range(count):
            b.read(1) #00
            data.append(struct.unpack('>B',b.read(1))[0])

        json.dump(data,open(output,'w'))

    def Compile(input,output):
        data=json.load(open(input))
        b=open(output,'wb')
        b.write(struct.pack('>H',len(data)))
        for d in data:
            b.write(b'\x00'+struct.pack('>B',d))

        b.close()
