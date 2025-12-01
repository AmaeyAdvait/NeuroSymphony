from brian2 import *

start_scope()

%matplotlib inline

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

tau = 10*ms
eqs = '''
dv/dt = (sin(2*pi*100*Hz*t) - v)/tau : 1
'''

G = NeuronGroup(1, eqs, method = "euler")
M = StateMonitor(G, 'v', record=0)

G.v = 5

run(60*ms)

plot(M.t/ms, M.v[0])

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

