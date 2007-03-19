# (c) francois schnell 2007  

from PIL import Image,ImageDraw,ImageFont

class picFoot(object):
    """
    A class to write a footer on a picture
    
    Problem: PIL don't keep the EXIF intact ...
    """
    def __init__(self,picture):
        self.im = Image.open(picture)
        self.picture=picture
    def writeFoot(self,footer,heightPercentage=0.025,align="center"):
        """Write footer"""
        print self.im.size
        draw=ImageDraw.Draw(self.im)
        font = ImageFont.truetype("arial.ttf", int(self.im.size[1]*heightPercentage))
        print font.getsize(footer)
        if align=="left":
            draw.text((self.im.size[0]-font.getsize(footer)[0],
            self.im.size[1]-font.getsize(footer)[1]-self.im.size[1]/100),
            footer,font=font)
        if align=="center":
            draw.text((self.im.size[0]/2-font.getsize(footer)[0]/2,
            self.im.size[1]-font.getsize(footer)[1]-self.im.size[1]/100),
            footer,font=font)
        del draw
        self.im.show()
        self.im.save("m-"+self.picture,"JPEG")

if __name__=="__main__":
    foot=picFoot("IMG_1493.JPG")
    foot.writeFoot("Hello World !")





