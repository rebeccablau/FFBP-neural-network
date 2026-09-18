# Custom FFBP Neural Network 

This project implements a fully custom feed-forward back-propogation neural network built from scratch in Python, using a doubly-linked list data structure to dynamically connect and manage neural layers without high-level machine learning frameworks. 

It functions as a classifier or a regressor provided one of three data sets:
* UC Irvine's Iris Data Set (classifies variant of Irises based on petal or sepal lenghts and widths)
* Results of the sine function (takes an input x and predicts y=sin(x))
* XOR Data (classifies the result of XORing two bits)

# Implementation Details 

## DoublyLinkedList

An implementation of doubly linked list (bi-directional linked list) abstract data type. 

* Underlying data structure for entire network
* Manages linked nodes
* Provides methods for insertion, removal, iteration, and bounds-checking

## Neurode (and MultiLinkNode)

Subclass created from the abstract base class MultilinkNode, which defines node communication. 
 
* Identifies relatonships between nodes (upstream or downstream)
* Processes new neighbors

## LayerList

An subclass of DoublyLinkedList, used to manage each layer of the FFBP network.

* Links, adds, or removes layers of nodes
* Establishes forward and backward references across adjacent layers
* Returns input or output layer nodes

## FFNeurode

The Feed-Forward Neurode class, inherits from Neurode and implements forward pass propogation logic.

* Uses the sigmoid function as the activation function
* Makes data available to downstream node layers
* Set value of input layer nodes

## BPNeurode

The Backpropogation class, inherits from Neurode and implements backwards pass propogation logic.  

* Calculates the delta of a neurode using the derivative of the the sigmoid function
* Collects data from downstream nodes and passes to next layer up
* Adjusts weights and biases of neurodes according to the learning rate
* Set expected value of outputs

## FFBPNeurode

Combines Feed-Forward and Backpropogation Neurodes into a single unit using class inheritance.

## NNData

Neural Network Data Class, used for testing.

* Manages data partitioning, shuffling, and priming for both training and testing sets  
* Delivers a feature and label from a set
* Indicates if a training or testing set has been exhausted

## FFBPNetwork

The complete Feed-Forward Backpropogation Neural Network, including functions to run tests on various data sets (XOR, UCI Iris Data Set, and results of the sine function).

* Integrates LayerList, NNData, FFBPNeurode, and RMSE loss metrics into a unified training interface

## RMSE

Provides loss evaluation metrics for tests using Root Mean Square Error. 

* Implements Euclidean and TaxiCab RMSE calculation to evaluate prediction variance across training and testing epochs

# How to Run!
* Open a terminal, navigate to the neural-network directory
* Activate a virtual environment:

```
python3 -m venv venv

source venv/bin/activate
```

* Install required packages
```
pip install -r requirements.txt
```

* Run the tests in the main function of FFBPNetwork.py

```
python3 FFBPNetwork.py
```
# FFBP-neural-network
