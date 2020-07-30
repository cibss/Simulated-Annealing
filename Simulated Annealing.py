        import math
        import random

        def SA(x,y):

                xx = x*x
                yy = y*y

                pt1 = math.sin(x) * math.cos(y) 
                pt2 = math.sqrt(xx + yy) / math.pi
                pt3 = math.fabs(1 - pt2)
                pt4 = math.e * pt3
                pt5 = -1 * math.fabs(pt1 * pt2 * pt4)
                
                hasil = pt5

                return hasil

        T = 10000
        c = 0.5

        x,y = random.uniform(-10,10) , random.uniform(-10,10)
        tempSolution = SA(x,y)
        tempEval = tempSolution

        while (T>1):
            newSolution = SA(x,y)
            solution = newSolution - tempSolution

            if (solution < 0):
                tempSolution = solution
                if (tempEval > tempSolution):
                    tempEval = tempSolution
                    print(tempEval)
            else:
                delta = newSolution - tempSolution
                rand = random.random()
                if ((2.71828 * (- delta / T)) > rand):
                    tempEval = newSolution

            T = T *c
        print(newSolution)






