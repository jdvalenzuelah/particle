import simulation.config as config

class Simulation():

    def __init__(self, m, q, vo):
        """
        """
        self.particle = {
            'mass': m,
            'charge': q,
        }
        self.initial_velocity = vo

    def __get_vf(self, h):
        """
        """
        m, q = self.particle.values()
        u = m*h*config.GRAVITY
        v = u/q
        vf = ((2*q*v)/m) + self.initial_velocity**2
        return (vf**(1/2))
    
    def simulate(self, data):
        import matplotlib.pyplot as plt
        plt.axis([0, 100, 0, 100])
        for i in data:
            vf = self.__get_vf(int(i['x']))
            self.initial_velocity = vf
            print(i['v'],vf)
            plt.scatter(i['v'],vf)
            plt.pause(1)
        plt.show()
    