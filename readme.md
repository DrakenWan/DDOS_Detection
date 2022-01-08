# 2021 Update
I have created a new folder named SDN Dataset containing CSV file uploaded [here](https://data.mendeley.com/datasets/jxpfjc64kr/1) by their authors. This dataset was generated in mid 2020 using mininet emulator. The dataset was specifically generated for ML or DL model training which is a plus. I have tested three sklearn models over the dataset in a jupyter notebook.

During pre-processing of data, I removed rows that had null values as well as "O" (Object) data type (which is actually String data). Removal of rows didn't affect the dataset size as it was significantly large. The values of each attribute was scaled using `StandardScaler()`.

Models used to train with their train and test accuracies are:-
* Logistic Regression - ~75
* SGD Classifier -  ~76
* Multi-layer Perceptron neural network - ~99


### NOTE 

One point to note is that it is always better to let the accuracy be not close to 100 as if our model gets new data it doesn't know how to deal with, it
might be less likely to deal with the data input properly. It might be overfitted. One way to look at it is if there is high deviation between train and test accuracies then you might've overfitted the data (if train accuracy is close to 100 but on validation data it is way less). In my case, that isn't the case so there might be other parameters.

I still am going to further investigate the 2020 data. One thing I can proceed with is performing data visualisation on each parameter and find any relationships manually that might've contributed to a certain bias. Maybe some value is occuring somewhere way too many times to be associated well with the predictor in our data given but in actuality is not really related with predictor rather it is just mere coincidence that in our current data that association was made by MLP.

To further elaborate this notion, Let's consider an example where I am classifying images based on the emotions of face and I have pictures of real life people with emotions such as angry, happy, sad, disgusted, etc. There might be a case where like 80% of the images which are classified as angry have a person with blue shirt. The model might associate the blue shirt as the sole factor to be consiered as an emotion of anger. We can solve this by introducing samples of 'angry' people with random coloured shirts or we can just crop out the shirt part from the image for better prediction. In this case, we are dealing with numerical data with thousands of rows. Best way is to use data visualisation techniques to determine any such relation.

Also this is not a simple ML problem. We are supposed to predict based on huge numerical data given if we are being attacked with a DDOS or not. This is not a simple problem. It is complex given the number of attributes.



The linear models had lower accuracy even after scaling the data and normalizing it. Clearly, there is a non-linear relationship between the prediction variable and data attributes which was accurately fit using a Multi-layer perceptron neural network.

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


