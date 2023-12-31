
# Markov chain

I'm maintaining and updating the KDA algorithm developed by Joost! We aim to extend the project and develop new additions to the algorithms.

This module contains tools to evaluate Markov chains.

## Installation 

### Prerequisites

Ensure that the following is properly installed:
- Python 3
- pydotplus. See https://pypi.org/project/pydotplus/. Note that pydotplus has also some requirements. 
Among them is Graphviz, which can be installed from https://www.graphviz.org/. After installing Graphviz, do not to forget to add the folder "INSTALL_FOLDER_GRAPHVIZ\bin" to the PATH environment variable in Windows. 
- tarjan. See https://pypi.org/project/tarjan/.

### When using conda:

Open Anaconda prompt in the source folder. Activate an environment with Python 3. Run consequently,

    python setup.py install

this will install the package locally.

### When python is located in PATH:

Open the cmd in the source folder and type

    python setup.py install

this will install the package locally.

## Getting Started

After installation, example usage is as follows:

    # -*- coding: utf-8 -*-
    """
    Created on 5/14/2019
    
    Author: Joost Berkhout (CWI, email: j.berkhout@cwi.nl)
    
    Description: Demonstrates the use of the Markov_chain package.
    """
    
    from Markov_chain.Markov_chain_new import MarkovChain
    from Markov_chain.KDA import KDA
    
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

## Running the tests

Run file Test3.py to test using the current working directory.


## Authors

Joost Berkhout
Email j.berkhout@cwi.nl

Maintained by: Thao Le
Email: t.p.t.le@businessdatascience.nl

## License

None

## Acknowledgments

...
