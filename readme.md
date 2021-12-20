# 2021 Update
I have created a new folder named SDN Dataset which has three standard sklearn models trained over SDN dataset uploaded [here](https://data.mendeley.com/datasets/jxpfjc64kr/1) by their authors. This dataset was generated in mid 2020 using mininet emulator. The dataset was specifically generated for ML or DL model training which is a plus.

During pre-processing of data, I removed rows that had null values as well as "O" (Object) data type. Removal of rows didn't affect the dataset size as it was significantly large. The values of each attribute was scaled using `StandardScaler()`.

Models used to train with their train and test accuracies are:-
* Logistic Regression - ~75
* SGD Classifier -  ~76
* Multi-layer Perceptron neural network - ~99

The linear models had lower accuracy even after scaling the data and normalizing it. Clearly, there is a non-linear relationship between the prediction variable and data which was accurately fit using a neural network.

The test size was 30%.

Check out the [notebook](https://github.com/DrakenWan/DDOS_Detection/blob/master/SDN%20Dataset/SDN_Classification.ipynb) file.

# DDOS Detector Using Machine Learning (2019)

Project Authored by: Kartikay Kaul, Revanth Regeti

If you do not wish to read the verbose below just scroll
to the END OF THIS DOCUMENT (Ensure you have all the python packages installed
advised in start) and execute the given statements in windows cmd (ensure
to run those commands where all project files are)

========================================================
## Contents:

- Running The program as its
- Dataset
- Running Notebooks

=========================================================

### RUNNING THE PROGRAM AS IT IS

There are two main programs:
	train.py 	test.py

* train.py is used to train the models(sklearn ones) on different protocols
 which will also take some parameters as input
 The file will exclusively ask for pretrained model to be stored on the system

* test.py is used to extract the pretrained model and test the model on
 the parameters given

* You need to have following softwares and python packages to run the python files successfully:
 * python3.6 or above
 * python packages: numpy, sklearn, pandas, matplotlib, pickle, tqdm
 * instead of above softwares you can simply install the anaconda distribution on python/R at this [link](https://www.anaconda.com/distribution/). It will install all necessary python packages for data science for you
 * It is necessary for these python packages to be installed to run the train.py and test.py
    python files.


#### TRAINING OUR MODEL (This will take a lot of time)


go to windows commandline or anaconda prompt and type `python train.py icmp 0`

this will actually train the data set on `icmp` protocol with the KNN model.

If you wish to use the second model type `python train.py icmp 1`

You can even change the protocol from the choices "udp", "tcp_syn" and "icmp". 
So if you want to use tcp_syn protocol type and train it with KNN model type:
   `python train.py tcp_syn 0`

At the end of executing this command you will get something like this:

```` 
Data preprocessing done.
The model has been fit.
Save the fitted model?(y/n)
```` 


asking you to save the pre-trained model for future use. type "y" and press enter

CONGRATULATIONS! You saved your pre-trained model.


#### TESTING OUR MODEL
This is fast but a little tricky. You have to ensure how many parameters you input for testing out the class.

type `python test.py tcp_syn -1.5 1.0 2.0 30.0 1.0`

This will use the tcp_syn pre-trained model and test the given parameters on it.

Now each protocol has different parameter length as input. While tcp_syn protocol takes
a length of 5 float value inputs others may take different inputs.

> NOTE:

> ICMP TAKES 7 ARGUMENTS

> UDP TAKES 5 ARGUMENTS

> TCP_SYN TAKES 5 ARGUMENTS


I have put command line statements below for you to execute and test the dataset.

`python test.py tcp_syn -1.5 1.0 2.0 1.0 1.0`

`python test.py tcp_syn -1.5 1.0 2.0 30.0 1.0`

`python test.py icmp 0.0 0.0 30.0 0.0 1.0 0.0 0.0`

`python test.py icmp -0.1 30.0 0.0 2.0 0.0 0.0 2.0`

`python test.py udp 146.0 0.0 105.0 254.0 2.0`

`python test.py udp 45.0 -0.3 45.0 236.0 2.0`


### DATASET
  All of the generated, consolidated and split dataset is stored in dataset folder and
  is open to use by any. The cleaned.csv file is KD99 generated dataset.

### JUPYTER NOTEBOOKS
   
".ipynb" files can be run by installing jupyter on your system.

run `pip3 install jupyter` on your cmd


# END OF FILE 

Just follow below. You need not read the entire instructions given above.

EXECUTE FOLLOWING COMMANDS ON YOUR CMD:

`python test.py tcp_syn -1.5 1.0 2.0 1.0 1.0`

`python test.py tcp_syn -1.5 1.0 2.0 30.0 1.0`

`python test.py icmp 0.0 0.0 30.0 0.0 1.0 0.0 0.0`

`python test.py icmp -0.1 30.0 0.0 2.0 0.0 0.0 2.0`

`python test.py udp 146.0 0.0 105.0 254.0 2.0`

`python test.py udp 45.0 -0.3 45.0 236.0 2.0`


