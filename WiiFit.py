import os, struct, json

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
