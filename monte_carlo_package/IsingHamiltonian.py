import numpy as np
import monte_carlo_package as montecarlo
from .bitstring import BitString 

class IsingHamiltonian:
    """Class for an Ising Hamiltonian of arbitrary dimensionality

    .. math::
        H = \\sum_{\\left<ij\\right>} J_{ij}\\sigma_i\\sigma_j + \\sum_i\\mu_i\\sigma_i

    """

    def __init__(self, J=[[()]], mu=np.zeros(1)):
        """Constructor

        Parameters
        ----------
        J: list of lists of tuples, optional
            Strength of coupling, e.g,
            [(4, -1.1), (6, -.1)]
            [(5, -1.1), (7, -.1)]
        mu: vector, optional
            local fields
        """
        self.J = J
        self.mu = mu

        self.nodes = []
        self.js = []

        for i in range(len(self.J)):
            self.nodes.append(np.zeros(len(self.J[i]), dtype=int))
            self.js.append(np.zeros(len(self.J[i])))
            for jidx, j in enumerate(self.J[i]):
                self.nodes[i][jidx] = j[0]
                self.js[i][jidx] = j[1]
        self.mu = np.array([i for i in self.mu])
        self.N = len(self.J)

    def energy(self, config):
        """Compute energy of configuration, `config`

            .. math::
                E = \\left<\\hat{H}\\right>

        Parameters
        ----------
        config   : BitString
            input configuration

        Returns
        -------
        energy  : float
            Energy of the input configuration
        """
        if len(config.config) != len(self.J):
            error("wrong dimension")

        e = 0.0
        for i in range(config.N):
            # print()
            # print(i)
            for j in self.J[i]:
                if j[0] < i:
                    continue
                # print(j)
                if config.config[i] == config.config[j[0]]:
                    e += j[1]
                else:
                    e -= j[1]

        e += np.dot(self.mu, 2 * config.config - 1)
        return e

    def delta_e_for_flip(self, i, config):
        """Compute the energy change incurred if one were to flip the spin at site i

        Parameters
        ----------
        i        : int
            Index of site to flip
        config   : :class:`BitString`
            input configuration

        Returns
        -------
        energy  : list[BitString, float]
            Returns both the flipped config and the energy change
        """
        return del_e


    def metropolis_sweep(self, conf, T=1.0):
        """Perform a single sweep through all the sites and return updated configuration

        Parameters
        ----------
        conf   : :class:`BitString`
            input configuration
        T      : int
            Temperature

        Returns
        -------
        conf  : :class:`BitString`
            Returns updated config
        """

    def compute_average_values(self, T):
        """Compute Average values exactly

        Parameters
        ----------
        T      : int
            Temperature

        Returns
        -------
        E  : float
            Energy
        M  : float
            Magnetization
        HC : float
            Heat Capacity
        MS : float
            Magnetic Susceptability
        """
        E = 0.0
        M = 0.0
        Z = 0.0
        EE = 0.0
        MM = 0.0

        conf = BitString(self.N)

        for i in range(2**conf.N):
            conf.set_int_config(i)
            Ei = self.energy(conf)
            Zi = np.exp(-Ei / T)
            E += Ei * Zi
            EE += Ei * Ei * Zi
            Mi = np.sum(2 * conf.config - 1) # type: ignore
            M += Mi * Zi
            MM += Mi * Mi * Zi
            Z += Zi

        E = E / Z
        M = M / Z
        EE = EE / Z
        MM = MM / Z

        HC = (EE - E * E) / (T * T)
        MS = (MM - M * M) / T
        return E, M, HC, MS
    
    def get_lowest_energy_config(self):
        """Compute the lowest energy Bitstring configuration

        Returns
        -------
        emin  : float
            Minimum Energy
        xmin  : list[int]
            Minimum Energy Configuration
        """
        xmin = None # configuration of minimum energy configuration
        emin = 0 # minimum of energy
        my_bs = BitString(self.N)
        xmin = BitString(self.N)
        # Add code here to find the lowest energy configuration

        for a in range(0,2**len(my_bs)):
            my_bs.set_int_config(a) 
            if (self.energy(my_bs) < self.energy(xmin)):
                xmin.set_int_config(a)
                emin = self.energy(xmin)
        return emin, xmin