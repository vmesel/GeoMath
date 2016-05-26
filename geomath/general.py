# General file for corrections, problem solving and others!

class General():
    def useful_info():
        return("There will be some useful information here!")
    
    def fix_float(self,floatNum):
        flt = str(floatNum).split(".")
        if len(flt[1]) >= 4:
            from fractions import Fraction
            frac = Fraction(floatNum).limit_denominator(9)
            return(str(frac.numerator) + "/" + str(frac.denominator))
        else:
            return(floatNum)
        
    def equation_parser(self,equation,typ):
        pass
    