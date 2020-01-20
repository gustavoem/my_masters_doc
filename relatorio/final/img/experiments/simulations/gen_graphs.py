import sys
sys.path.insert (0, '/home/gustavo/cs/SigNetMS')
import matplotlib.pyplot as plt
import numpy as np
from experiment.ExperimentSet import ExperimentSet

# Smallest
exp_file = '/home/gustavo/cs/SigNetMS/input/smallest/experiment.data'
experiments = ExperimentSet (exp_file)
exp = experiments[-1]
pts_label = 'Observation #' + str (1)
plt.plot (exp.times, exp.values, 'o', label=pts_label)
plt.xlabel ("Time (s)")
plt.ylabel ("[B]")
plt.savefig ("smallest_data.pdf")
plt.clf ()

# Girolami
exp_file = '/home/gustavo/cs/SigNetMS/input/bioinformatics/experiment.data'
experiments = ExperimentSet (exp_file)
exp = experiments[-1]
pts_label = 'Observation #' + str (1)
plt.plot (exp.times, exp.values, 'o', label=pts_label)
plt.xlabel ("Time (s)")
plt.ylabel ("[R$_{pp}$]")
plt.savefig ("girolami_data.pdf")

