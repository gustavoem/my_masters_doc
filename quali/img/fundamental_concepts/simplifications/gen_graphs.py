import sys
sys.path.insert (0, '/home/gustavo/cs/SigNetMS')

import numpy as np
from marginal_likelihood.ODES import ODES

ode = ODES ()
ode.add_equation ('E', '-kf * E * S + (kr + kcat) * ES')
ode.add_equation ('S', '-kf * E * S + kr * ES')
ode.add_equation ('ES', 'kf * E * S - (kr + kcat) * ES')
ode.add_equation ('P', 'kcat * ES')
ode.define_initial_value ('E', '10')
ode.define_initial_value ('S', '100')
ode.define_initial_value ('ES', '0')
ode.define_initial_value ('P', '0')
ode.define_parameter ('kf', 0.06)
ode.define_parameter ('kr', 0.1)
ode.define_parameter ('kcat', 0.2)
ode.print_equations ()

ode.overtime_plot (['S', 'P', 'ES', 'E'], np.linspace (0, 100, 1000), 
        filename='full_system.pdf', xlabel='Time (seconds)', ylabel='Concentration (mol/$\mu m^3$)', title=None)


ode = ODES ()
ode.add_equation ('S', '-kcat * (E_0 * S) / (K_m + S)')
ode.add_equation ('P', 'kcat * (E_0 * S) / (K_m + S)')
ode.add_equation ('ES', '0')
K_m = (0.2 + 0.1) / 0.06
ode.define_initial_value ('S', 100)
ode.define_initial_value ('P', 0)
ode.define_initial_value ('ES', 10 * 100 / (K_m + 100))
ode.define_parameter ('kcat', 0.2)
ode.define_parameter ('E_0', 10)
ode.define_parameter ('K_m', K_m)
ode.print_equations ()

ode.overtime_plot (['S', 'ES', 'P'], np.linspace (0, 100, 1000), 
        filename='mm_system.pdf', xlabel='Time (seconds)', 
        ylabel='Concentration (mol/$\mu m^3$)', title=None)

