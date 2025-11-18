#!/usr/bin/env python
# coding: utf-8

# In[1]:


from brian2 import *

start_scope()


# In[2]:


tau = 10*ms
Vt = -50*mV
Vr = -65*mV
El = -65*mV
R = 10*Mohm
I = 2.5*nA

eqs = '''
        dV/dt = (-(V-El)  +R*I)/tau : volt
    '''


# In[3]:


G = NeuronGroup(1, model = eqs, threshold = 'V>Vt', reset = 'V = Vr', method = 'exact')
G.V = El
M = StateMonitor(G, 'V', record = 0)
spikemon = SpikeMonitor(G)
run(100*ms)

figure(figsize = (10,4))
plot(M.t/ms, M.V[0]/mV)
xlabel('Time(in ms)')
ylabel('Membrane Potential(in mV)')
title('Leaky Integrate and Fire Neuron')


# In[ ]:




