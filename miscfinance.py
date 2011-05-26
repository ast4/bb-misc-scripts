import math

def impliedjump(iv1,iv2,t1,t2):
    if iv1 > iv2:
        s12 = math.sqrt((pow(iv2,2)*t2-pow(iv1,2)*t1)/(t2-t1))
        se = math.sqrt(t1*(pow(iv1,2)-pow(s12,2)))
        er =  math.sqrt(2/math.pi)*se
        return er
    else:
        return 0
