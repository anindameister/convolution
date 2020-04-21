from PIL import Image
def main():
    filename="download (1).jpg"
    
    image=Image.open(filename);
    print (image.size)
    
    del image;
    
if (__name__=="__main__"):
    main();

#(299, 168)
#https://www.youtube.com/watch?v=CWN0LHU-yyM