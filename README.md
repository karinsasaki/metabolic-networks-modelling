Course designed for the EBI In Silico Systems Biology 2016 course, metabolic networks modelling with COBRApy.
===================================


## Course Aims and Overview

This course teaches the basics of flux balance analysis to model metabolic networks at steady state and simulate the models in python. It integrates explanations and exercises, building the necessary knowledge to enable participants to build and simulate their own genome-scale model (GEM) of yeast metabolism.

The ‘EBI_COBRApy_exercises.ipnb’ is the main tutorial, which consists of explanations and exercises. Solutions are found in ‘EBI_COBRApy_exercises.ipnb’.


## Audience

This course is aimed at people with basic to intermediate knowledge of python and knowledge of basic linear algebra (array manipulation).


## Required tools

Python2.7 (We recommend using the [Anaconda distribution](https://www.continuum.io/downloads) of Python. It's free and comes with a large number of additional modules included ready for importing into your scripts, IPython shell and notebook interfaces, a powerful Python text editor (Spyder), and a good package manager, conda, for updating and installing packages.)

[COBRApy](https://github.com/opencobra/cobrapy)

[Jupyter notebook](http://jupyter.readthedocs.io/en/latest/install.html)




## Instructions on following this course

- This tutorial is organised as an iPython Notebook.

- By following the exercises in ‘EBI_COBRApy_exercises.ipnb’, you should be able to learn about modelling metabolic networks using systems of linear equations (flux balance analysis) and of simulating those models using the python library COBRApy.

- If you run into trouble, you can use the provided solutions as inspiration - however, it is *highly* recommended to spend a lot of time figuring things out yourself, as this is an important part of any programming exercise. You can use the python and COBRApy documentations.



## Concepts discussed in course lectures

1. **Constrained based modelling of metabolic networks**
	* Stoichiometric models (system of linear equations)
	* Optimal distribution of flux
	* Linear programming to optimise a system of linear equations
	* Modelling effect of gene knockouts 

2. **Relevant python language**
	* numpy library
	* COBRApy library
		* Importing a model
		* Editing model reactions, concentrations, conditions, objective function, etc
	* Pandas library for data analysis


		
## Instructors

Paula Jouhten(1, 2), Kiran Patil(2), Karin Sasaki(2), Aleksej Zelezniak(3, 4)

(1). University of Helsinki

(2). EMBL

(3). The Francis Crick Institute

(4). University of Cambridge


## Feedback 

We welcome any feedback on this course! 

Feel free to contact us at *karin.sasaki@embl.de* or *Aleksej.Zelezniak@crick.ac.uk*