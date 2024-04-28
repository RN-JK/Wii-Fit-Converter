import os, struct, json

class Tag:
    def Decompile(input,output):
        data=[]
        b=open(input,'rb')
        b.read(4) #BOBJ
        count=struct.unpack('>I',b.read(4))[0]
        for _ in range(count):
            array=[]
            name=b.read(8).replace(b'\x00',b'').decode('utf-8')
            array.append(name)
            for __ in range(10):
                array.append(struct.unpack('>f',b.read(4))[0])

            data.append(array)

        json.dump(data,open(output,'w'))

    def Compile(input,output):
        data=json.load(open(input))
        b=open(output,'wb')
        b.write(b'\x42\x4F\x42\x4A') #BOBJ
        b.write(struct.pack('>I',len(data)))
        namebyte=b'\x00\x00\x00\x00\x00\x00\x00\x00'
        for d in data:
            arraycounter=1
            b.write(namebyte.replace(namebyte[:len(d[0])],d[0].encode('utf-8'), 1))
            for __ in range(10):
                b.write(struct.pack('>f',d[arraycounter]))
                arraycounter+=1
        
        for _ in range(8):
            b.write(b'\xFF')
        b.close()

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
    
    def Compile(input,output):
        data=json.load(open(input))
        b=open(output,'wb')
        for d in data:
            b.write(struct.pack('>H',d[0]))
            b.write(struct.pack('>B',d[1]))
            b.write(struct.pack('>B',d[2]))

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
