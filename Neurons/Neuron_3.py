from brian2 import *

start_scope()
prefs.codegen.target = "numpy"

tau = 10*ms
eqs = '''
dv/dt = (1-v)/tau : 1 (unless refractory)
'''

G = NeuronGroup(1, eqs, threshold = "v>0.8", reset = "v = 0", refractory = 5*ms, method = "exact")

statemon = StateMonitor(G, 'v', record = 0)
spikemon = SpikeMonitor(G)

run(100*ms)

print('Spike times: %s' % spikemon.t[:])
plot(statemon.t/ms, statemon.v[0], label = "Brian")
for t in spikemon.t:
    axvline(t/ms, ls = '--', c = 'C1', lw = 3)
legend()
plt.show()