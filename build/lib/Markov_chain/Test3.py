#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 20:47:50 2023

@author: thaole
"""


from Markov_chain_new import MarkovChain
from KDA import KDA

# Courtois karate club
MC = MarkovChain('Courtois', verbose=True)
KDA_MC = KDA(MC, CO_A='CO_A_3(3)', CO_B='CO_B_1(1)', SC=False)
KDA_MC.MC.plot('Courtois network after Kemeny decomposition algorithm')
KDA_MC.plot()

# Zacharys karate club
MC = MarkovChain('ZacharysKarateClub', verbose=True)
KDA_MC = KDA(MC, CO_A='CO_A_3(3)', CO_B='CO_B_1(1)', SC=False)
KDA_MC.MC.plot('Zacharys karate club network after Kemeny decomposition algorithm')
KDA_MC.plot()