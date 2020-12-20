# COVIDSim
A project that I created in CECS 274 to simulate COVID-19 cases in or out of lockdown. The user can set their own parameters, or use the default parameters set by the project. The user can choose to run their simulation with or without lockdown, and for how many days they want their simulation to run. The program will return the simulation day by day and produce a graph of cases. This project is intended to show the benefits of a lockdown to the general population to reduce cases from the COVID-19 pandemic.  

*IMPORTANT NOTES: The Interfaces.py file was written by my professor, Dr. Morales Ponce, and he also wrote a skeleton file for the data structure implementations. Other than that, all of the rest of this project is my work.*

## Simulation Class
### init(parameters)

First, I initialized the parameters for the simulation either based on user input or the default parameters for the project. Then, I set constants to determine a Node's state to make it easier to read. Next, I initialized an ArrayList called "Nodes" of n size to store every "Node" object for the simulation. Then, based on INITIAL_SETTING, a random number of Nodes are set to be infected. Finally, an interaction graph is initialized

### getInteractionGraph()

I started off by declaring an AdjacencyList to store the interactions of the Nodes. The loop to determine interactions will repeat INTERACTION times. A random node is chosen, and it has an ALPHA chance to be added as an edge, or else one of that node's neighbors will be added as an edge to the graph. This simulates random interactions during COVID-19.

### run(days)

First, I started out with determining the statistics of the current nodes and relaying them to the user, and setting up the lists for the matplotlib graph. Then, I use a loop to find any INFECTED nodes. If an INFECTED node has interacted with a CLEAN node as per the interaction graph, then that CLEAN node has a TRANSMISSION_RATE chance to become infected. Each day, the number of days left to recover for an infected node is reduced by 1. When there are 0 days left to recover, then there is a FATALITY_RATE chance for that Node to become DEAD. This process repeats for however many days set by the user, and produces a graph at the end for the user to view.
