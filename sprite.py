class Sprite:
    def __init__(self,x,y,img):
        self.x=x
        self.y=y
        img=img.split('\n')
        img.pop(0)
        img.pop(len(img)-1)
        self.img=img
        self.w=len(img[0])
        self.h=len(img)
    def render(self,display):
        y=0
        for line in self.img:
            x=0
            for char in line:
                if int(char)==1:
                    display.pixel(self.x+x,self.y+y,1)
                x+=1
            y+=1