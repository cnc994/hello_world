import math
class Calibration:
    def __init__(self):
        return

    def Calibration_OU(S, dt):
        a = math.log(2)
        delta = dt
        n = len(S)-1
        Sx  = sum( S[0:n] )
        Sy  = sum( S[1:n+1] )
        return Sy

S=[1,2,3,4,5]
