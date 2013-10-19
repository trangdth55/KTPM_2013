def is_triangle(a,b,c):
    return True if(a<b+c and b<a+c and c<a+b) else False

def is_equilateral(a,b,c):
    return True if a==b==c else False

def is_isosceles(a,b,c):
    return True if a==b or b==c or a==c else False

def main(a,b,c):
    '''
    a:[-9;13][15;20]
    b:[5;10][11;12][17;37]
    c:[0;9][14;16][45;67][90;100]
    '''
    return 0