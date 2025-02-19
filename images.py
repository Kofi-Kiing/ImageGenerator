import imagetools
import copy
import math


##### Generating images


def rainbow():
    width, height = 256, 256
    image_matrix = []

    for y in range(height):
        row = []
        for x in range(width):
            #calculating red and grren pixel position
            red = int((y / width) * 255)    #changing red vertically
            green = int((x / height) * 255) #changing green horizontally
            blue = 128 #fixing blue to a val of 128          
            row.append([red, green, blue])      
        image_matrix.append(row)
    return image_matrix

def formular_art():
    width, height = 1000, 1000
    image_matrix = []

    for y in range(height):
        row = []
        for x in range(width):
            #calculating red and green pixel position
            red = int(x%(y+1))%256    
            green = int(y%(x+1))%256 
            blue = 128 #fixing blue to a val of 128          
            row.append([red, green, blue])      
        image_matrix.append(row)
    return image_matrix

def my_formulaic():
    width, height = 1000, 1000
    image_matrix = []
    for y in range(height):
        row = []
        for x in range(width): 
            red = int((x * x + y * 5) % 256)  # Red varies quadratically
            green = 10
            blue = 20    
            row.append([red, green, blue])
        image_matrix.append(row)
    return image_matrix


##### Manipulating images


def width(array):
    arrayCopy=copy.deepcopy(array)
    return len(arrayCopy[0])

def height(array):
    arrayCopy=copy.deepcopy(array)
    return len(arrayCopy)

def grayscale(pic):
    picCopy=copy.deepcopy(pic)
    for i in range(len(picCopy)):
        for j in range(len(picCopy[i])):
            
            array=picCopy[i][j]
            average=sum(array)//len(array)
            round_up=math.ceil(average)
            picCopy[i][j]=[round_up]*len(array)
    return picCopy

def leave_purple(pic):
    picCopy=copy.deepcopy(pic)
    for i in range(len(picCopy)):
        for j in range(len(picCopy[i])):

            if (
                (picCopy[i][j][0]>=0 and picCopy[i][j][0]<=255) and 
                (picCopy[i][j][1]>=0 and picCopy[i][j][1]<=123) and
                (picCopy[i][j][2]>=110 and picCopy[i][j][2]<=255)
            ):
                pass
            else:
                array=picCopy[i][j]
                average=sum(array)//len(array)
                round_up=math.ceil(average)
                picCopy[i][j]=[round_up]*len(array)
    return picCopy

def crop(pic,left,top,right,bottom):
    n_img=copy.deepcopy(pic)
    def rl(pic,right,left):
        nn_img=[]
        i = 0
        while i < len(n_img) :
            if i >= left and i < (len(pic)-right) :
                nn_img.append(n_img[i])
            else:
                pass
            i+=1
        return nn_img

    cropped_tb=rl(pic,right,left) 
    #return cropped_tb
    def bt(pic, bottom, top):
        n_img = copy.deepcopy(pic)
        nn_img = []
        
        for row in n_img:
            lst = []  
            for i in range(len(row)):
                if bottom <= i < len(row) - top:
                    lst.append(row[i])
            nn_img.append(lst)
            
        return nn_img
    
    new_image = bt(cropped_tb,bottom,top)
    return new_image

def enlarge(pic,factor):
    def erow(lst,a):
        new_lst=[]
        for ls in lst:
            for i in range(a):
                new_lst.append(ls)
        return new_lst

    new_img=[]
    for row in pic:
        new_row = erow(row,factor)
        for j in range(factor):
            new_img.append(copy.deepcopy(new_row))
    return new_img

def blur(pic, radius):
    import math
    blurred_image = copy.deepcopy(pic)
    height = len(pic)
    width = len(pic[0])
    for y in range(height):
        for x in range(width):
            sum_r = sum_g = sum_b = 0
            count = 0
            for dy in range(-radius, radius + 1):
                for dx in range(-radius, radius + 1):
                    ny, nx = y + dy, x + dx
                    distance = math.sqrt(dx**2 + dy**2)
                    if (0 <= ny < height) and (0 <= nx < width) and (distance <= radius):
                        sum_r += pic[ny][nx][0]
                        sum_g += pic[ny][nx][1]
                        sum_b += pic[ny][nx][2]
                        count += 1
            if count > 0:
                blurred_image[y][x][0] = sum_r // count
                blurred_image[y][x][1] = sum_g // count
                blurred_image[y][x][2] = sum_b // count
                
    return blurred_image

def my_effect(pic):
    height = len(pic)
    one_third = height // 3
    for row in pic[:one_third]:
        for pixel in row:
            pixel[0] = 0  #setting red pixel values to zero
            pixel[2] = 0  #setting blue pixel values to zero
    for row in pic[one_third:2 * one_third]:
        for pixel in row:
            pixel[0] = 0  #setting red pixel values to zero
            pixel[1] = 0  #setting green pixel values to zero
    for row in pic[2 * one_third:]:
        for pixel in row:
            pixel[1] = 0  #setting green pixel values to zero
            pixel[2] = 0  #setting blue pixel values to zero
    return pic