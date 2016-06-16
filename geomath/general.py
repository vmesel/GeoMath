# General file for corrections, problem solving and others!

numbers = {int,float}

class General():
    def useful_info():
        return("There will be some useful information here!")

    def fix_float(self, floatNum):
        # This function application is to get float numbers and
        # Convert them into a fraction that is easy to reproduce
        flt = str(floatNum).split(".")
        if len(flt[1]) >= 4:
            from fractions import Fraction
            frac = Fraction(floatNum).limit_denominator(9)
            return(str(frac.numerator) + "/" + str(frac.denominator))
        else:
            return(floatNum)

    def equation_parser(self, equation, typ):
        pass
