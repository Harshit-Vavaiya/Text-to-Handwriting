from PIL import Image
# import pytesseract
import random

# 

def get_concat_h_cut(im1, im2):
    dst = Image.new('RGB', (im1.width + im2.width, min(im1.height, im2.height)))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst

dic = {
    '_':['F:\\Projects\\Handwriting\\Data\\_\\_.PNG'],
    'A':['F:\\Projects\\Handwriting\\Data\\A\\1.PNG','F:\\Projects\\Handwriting\\Data\\A\\2.PNG'],
    'B':['F:\\Projects\\Handwriting\\Data\\B\\1B.PNG','F:\\Projects\\Handwriting\\Data\\B\\2B.PNG'],
    'C':['F:\\Projects\\Handwriting\\Data\\C\\1C.PNG','F:\\Projects\\Handwriting\\Data\\C\\2C.PNG'],
    'D':['F:\\Projects\\Handwriting\\Data\\D\\1D.PNG','F:\\Projects\\Handwriting\\Data\\D\\2D.PNG'],
    'E':['F:\\Projects\\Handwriting\\Data\\E\\1E.PNG','F:\\Projects\\Handwriting\\Data\\E\\2E.PNG'],
    'F':['F:\\Projects\\Handwriting\\Data\\F\\1F.PNG','F:\\Projects\\Handwriting\\Data\\F\\2F.PNG'],
    'G':['F:\\Projects\\Handwriting\\Data\\G\\1G.PNG','F:\\Projects\\Handwriting\\Data\\G\\2G.PNG'],
    'H':['F:\\Projects\\Handwriting\\Data\\H\\1H.PNG','F:\\Projects\\Handwriting\\Data\\H\\2H.PNG'],
    'I':['F:\\Projects\\Handwriting\\Data\\I\\1I.PNG','F:\\Projects\\Handwriting\\Data\\I\\2I.PNG'],
    'J':['F:\\Projects\\Handwriting\\Data\\J\\1J.PNG','F:\\Projects\\Handwriting\\Data\\J\\2J.PNG'],
    'K':['F:\\Projects\\Handwriting\\Data\\K\\1K.PNG','F:\\Projects\\Handwriting\\Data\\K\\2K.PNG'],
    'L':['F:\\Projects\\Handwriting\\Data\\L\\1L.PNG','F:\\Projects\\Handwriting\\Data\\L\\2L.PNG'],
    'M':['F:\\Projects\\Handwriting\\Data\\M\\1M.PNG','F:\\Projects\\Handwriting\\Data\\M\\2M.PNG'],
    'N':['F:\\Projects\\Handwriting\\Data\\N\\1N.PNG','F:\\Projects\\Handwriting\\Data\\N\\2N.PNG'],
    'O':['F:\\Projects\\Handwriting\\Data\\O\\1O.PNG','F:\\Projects\\Handwriting\\Data\\O\\2O.PNG'],
    'P':['F:\\Projects\\Handwriting\\Data\\P\\1P.PNG','F:\\Projects\\Handwriting\\Data\\P\\2P.PNG'],
    'Q':['F:\\Projects\\Handwriting\\Data\\Q\\1Q.PNG','F:\\Projects\\Handwriting\\Data\\Q\\2Q.PNG'],
    'R':['F:\\Projects\\Handwriting\\Data\\R\\1R.PNG','F:\\Projects\\Handwriting\\Data\\R\\2R.PNG'],
    'S':['F:\\Projects\\Handwriting\\Data\\S\\1S.PNG','F:\\Projects\\Handwriting\\Data\\S\\2S.PNG'],
    'T':['F:\\Projects\\Handwriting\\Data\\T\\1T.PNG','F:\\Projects\\Handwriting\\Data\\T\\2T.PNG'],
    'U':['F:\\Projects\\Handwriting\\Data\\U\\1U.PNG','F:\\Projects\\Handwriting\\Data\\U\\2U.PNG'],
    'V':['F:\\Projects\\Handwriting\\Data\\V\\1V.PNG','F:\\Projects\\Handwriting\\Data\\V\\2V.PNG'],
    'W':['F:\\Projects\\Handwriting\\Data\\W\\1W.PNG','F:\\Projects\\Handwriting\\Data\\W\\2W.PNG'],
    'X':['F:\\Projects\\Handwriting\\Data\\X\\1X.PNG','F:\\Projects\\Handwriting\\Data\\X\\2X.PNG'],
    'Y':['F:\\Projects\\Handwriting\\Data\\Y\\1Y.PNG','F:\\Projects\\Handwriting\\Data\\Y\\2Y.PNG'],
    'Z':['F:\\Projects\\Handwriting\\Data\\Z\\1Z.PNG','F:\\Projects\\Handwriting\\Data\\Z\\2Z.PNG'],
    'a':['F:\\Projects\\Handwriting\\Data\\small\\a\\3a.PNG','F:\\Projects\\Handwriting\\Data\\small\\a\\2a.PNG'],
    'b':['F:\\Projects\\Handwriting\\Data\\small\\b\\3b.PNG','F:\\Projects\\Handwriting\\Data\\small\\b\\2b.PNG'],
    'c':['F:\\Projects\\Handwriting\\Data\\small\\c\\3c.PNG','F:\\Projects\\Handwriting\\Data\\small\\c\\2c.PNG'],
    'd':['F:\\Projects\\Handwriting\\Data\\small\\d\\3d.PNG','F:\\Projects\\Handwriting\\Data\\small\\d\\2d.PNG'],
    'e':['F:\\Projects\\Handwriting\\Data\\small\\e\\3e.PNG','F:\\Projects\\Handwriting\\Data\\small\\e\\2e.PNG'],
    'f':['F:\\Projects\\Handwriting\\Data\\small\\f\\3f.PNG','F:\\Projects\\Handwriting\\Data\\small\\f\\2f.PNG'],
    'g':['F:\\Projects\\Handwriting\\Data\\small\\g\\3g.PNG','F:\\Projects\\Handwriting\\Data\\small\\g\\2g.PNG'],
    'h':['F:\\Projects\\Handwriting\\Data\\small\\h\\3h.PNG','F:\\Projects\\Handwriting\\Data\\small\\h\\2h.PNG'],
    'i':['F:\\Projects\\Handwriting\\Data\\small\\i\\3i.PNG','F:\\Projects\\Handwriting\\Data\\small\\i\\2i.PNG'],
    'j':['F:\\Projects\\Handwriting\\Data\\small\\j\\3j.PNG','F:\\Projects\\Handwriting\\Data\\small\\j\\2j.PNG'],
    'k':['F:\\Projects\\Handwriting\\Data\\small\\k\\3k.PNG','F:\\Projects\\Handwriting\\Data\\small\\k\\2k.PNG'],
    'l':['F:\\Projects\\Handwriting\\Data\\small\\l\\3l.PNG','F:\\Projects\\Handwriting\\Data\\small\\l\\2l.PNG'],
    'm':['F:\\Projects\\Handwriting\\Data\\small\\m\\3m.PNG','F:\\Projects\\Handwriting\\Data\\small\\m\\2m.PNG'],
    'n':['F:\\Projects\\Handwriting\\Data\\small\\n\\3n.PNG','F:\\Projects\\Handwriting\\Data\\small\\n\\2n.PNG'],
    'o':['F:\\Projects\\Handwriting\\Data\\small\\o\\3o.PNG','F:\\Projects\\Handwriting\\Data\\small\\o\\2o.PNG'],
    'p':['F:\\Projects\\Handwriting\\Data\\small\\p\\3p.PNG','F:\\Projects\\Handwriting\\Data\\small\\p\\2p.PNG'],
    'q':['F:\\Projects\\Handwriting\\Data\\small\\q\\3q.PNG','F:\\Projects\\Handwriting\\Data\\small\\q\\2q.PNG'],
    'r':['F:\\Projects\\Handwriting\\Data\\small\\r\\3r.PNG','F:\\Projects\\Handwriting\\Data\\small\\r\\2r.PNG'],
    's':['F:\\Projects\\Handwriting\\Data\\small\\s\\3s.PNG','F:\\Projects\\Handwriting\\Data\\small\\s\\2s.PNG'],
    't':['F:\\Projects\\Handwriting\\Data\\small\\t\\3t.PNG','F:\\Projects\\Handwriting\\Data\\small\\t\\2t.PNG'],
    'u':['F:\\Projects\\Handwriting\\Data\\small\\u\\3u.PNG','F:\\Projects\\Handwriting\\Data\\small\\u\\2u.PNG'],
    'v':['F:\\Projects\\Handwriting\\Data\\small\\v\\3v.PNG','F:\\Projects\\Handwriting\\Data\\small\\v\\2v.PNG'],
    'w':['F:\\Projects\\Handwriting\\Data\\small\\w\\3w.PNG','F:\\Projects\\Handwriting\\Data\\small\\w\\2w.PNG'],
    'x':['F:\\Projects\\Handwriting\\Data\\small\\x\\3x.PNG','F:\\Projects\\Handwriting\\Data\\small\\x\\2x.PNG'],
    'y':['F:\\Projects\\Handwriting\\Data\\small\\y\\3y.PNG','F:\\Projects\\Handwriting\\Data\\small\\y\\2y.PNG'],
    'z':['F:\\Projects\\Handwriting\\Data\\small\\z\\3z.PNG','F:\\Projects\\Handwriting\\Data\\small\\z\\2z.PNG'],
}
# Cap = 'abcdefghikjlmnopqrstuvwxyz'
with open('sample.txt','r') as file:
    l = file.read()
    image = Image.new('RGB',(500,500),color=(224,224,224))
    c = 0
    h=0
    for i,v in enumerate(l):
        if v == '\n':
            c = 0
            h += 32    
            continue
        if v==' ':
            v='_'
        # print(v,end='')
        im = Image.open(random.choice(dic[v]))
        image1 = Image.new('RGB',(im.size[0],32),color=(224,224,224))
        # print(im.size)
        image1.paste(im,(0,32-im.size[1]))
        
    # #     # break
        image.paste(image1,(c,h))
        c+=im.size[0]
    image.save('output.png')
