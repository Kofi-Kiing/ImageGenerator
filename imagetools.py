import tkinter
import ast



class App:
    def __init__(self, t, pixelArray):
        h = len(pixelArray[0])
        w = len(pixelArray)
        self.i = tkinter.PhotoImage(width=w,height=h)

        pixelList = []
        for y in range(h):
            for x in range(w):
                pixelList.append(pixelArray[x][h-y-1])

        trying = iter(pixelList)
        pixels=" ".join(("{"+" ".join(('#%02x%02x%02x' % tuple(next(trying)) for i in range(w)))+"}" for j in range(h)))

        self.i.put(pixels,(0,0,w,h))

        c = tkinter.Canvas(t, width=w, height=h); c.pack()
        c.create_image(0, 0, image = self.i, anchor=tkinter.NW)

def draw(pixelArray):
    #creates a new window showing the given image
    t = tkinter.Tk()
    t.wm_title("Image")
    a = App(t, pixelArray)    
    t.mainloop()


#### File-handling functions
# .mpf = "my picture format" = extension for files made by this program


def pixels_to_mpf(im, filename):
    #saves pixel array to file
    with open(filename, "w") as f:
        f.write(str(im))

def mpf_to_pixels(filename):
    #takes file saved by this program and returns the pixel array
    with open(filename, "r") as f:
        x = f.read()
    return ast.literal_eval(x)


