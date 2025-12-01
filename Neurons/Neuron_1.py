from brian2 import *

start_scope()
prefs.codegen.target = "numpy"

20*volt
10*nA*20*mV

tau = 10*ms
eqs = '''
dv/dt = (1-v)/tau : 1
'''

G = NeuronGroup(1, eqs, method = "exact")
print('v before: %s' % G.v[0])
run(100*ms)
print("v after: %s" % G.v[0])
print('Expected value of v = %s' % (1-exp(-100*ms/tau)))

M = StateMonitor(G, 'v', record=True)
run(30*ms)
plot(M.t/ms, M.v[0], label = "Brian")
plot(M.t/ms, 1 - exp(-M.t/tau), "--", label = "Analytic")
legend()
plt.show()



