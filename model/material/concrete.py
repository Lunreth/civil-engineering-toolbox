import math

class Concrete:
    def __init__(self):
        pass

    def Gc(self, fc=None, Ec=None, concrete_poisson_ratio=0.2):
        """
        Return Estimated shear modulus
        :param fc: Concrete strength (MPa)
        :param Ec: Concrete Young modulus (MPa)
        :param concrete_poisson_ratio: Concrete Poisson's ratio
        :return: Shear modulus (MPa)
        """
        if Ec is None:
            Ec = 4700*math.sqrt(fc)
        Gc = Ec/(2*(1+concrete_poisson_ratio))  # MPa
        return Gc

    def Mn(self, **val):
        """
        Calculate nominal moment strength of reinforced concrete
        of rectangular area
        :param val: Dictionary of passing value of material
        :return: Nominal moment strength, Mn (KN)
        """
        fyr = val.get('fyr')  # MPa
        fc = val.get('fc')  # MPa
        width = val.get('b')  # mm
        height = val.get('h')  # mm
        cover = val.get('cover')  # mm
        n = val.get('n')  # number
        diameter = val.get('diameter')  # mm

        As = self.As(n, diameter)  # mm2
        a = self.a(As, fyr, fc, width)  # mm
        d = height-cover
        jd = self.jd(d, a)
        Mn = As*fyr*jd
        return Mn

    def As(self, n, diameter):
        '''
        Calculate area of n reinforcement
        :param n: Number of reinforcement
        :param diameter: Diameter of reinforcement
        :return: Area of reinforcement
        '''
        return math.pi*diameter**2/4 * n

    def a(self, As, fyr, fc, width):
        '''
        Return equivalent height of compression (a) on concrete.
        This equivalent height is well known as Withney's stress block
        a = c*beta1
        with c      = height of compression area above neutral axis
             beta1  = coefficient, 0.85 if fc below 28 MPa
        This function calculates value of (a) using force equilibrium.
        :param As: Area of tensile reinforcement
        :param fyr: Reinforcement tensile strength
        :param fc: Concrete compressive strength
        :param width: Width of rectangular area
        :return: Equivalent height of compression on concrete
        '''
        A = As*fyr  # N
        B = 0.85*fc*width  # N/mm
        return A/B  # mm

    def jd(self, d, a):
        '''
        Return moment length, as length of center of tension force to
        center of compressive force
        :param d: Distance from center of tensile reinforcement to the further
        compressive concrete
        :param a: equivalent height of compression on concrete
        :return: moment length
        '''
        return d-a/2

    def beta1(self, fc):
        '''
        Return value of coefficient that define equivalent height of Whitney's
        stress block.
        :param fc: Concrete compressive strength
        :return: beta1
        '''
        if fc <= 28:
            return 0.85
        elif fc <= 56:
            return 0.85 - 0.05*(fc-28)/7
        else:
            return 0.65

    def rho_balance(self, fc, fyr):
        '''
        Return ratio of tension reinforcement to concrete area
        when balance condition occur. Balance condition is when
        tension reinforcement reach yield strain exactly when compression
        concrete reach ultimate strain.
        :param fc: Concrete compressive strength
        :param fyr: Steel yield tension strength
        :return: beta1
        '''
        beta1 = self.beta1(fc)
        return 0.85*beta1*fc/fyr*600/(600+fyr)

    def rho_max(self, fc, fyr):
        return 0.75*self.rho_balance(fc, fyr)

    def phi(self, eps_t):
        return 0.65 + (eps_t-0.002)*250/3