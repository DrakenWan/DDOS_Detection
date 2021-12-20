The parameters were just chosen using Random forest Tree classifier 
and best 5/7 features were considered as parameters to train the model.

# DDOS Detector Using Machine Learning
# Project Authored by: Kartikay Kaul, Revanth Regeti

If you do not wish to read the verbose below just scroll
to the END OF THIS DOCUMENT (Ensure you have all the python packages installed
advised in start) and execute the given statements in windows cmd (ensure
to run those commands where all project files are)

+++++++++++++++++++LICENSE+++++++++++++++++++++++++++++
Copyright 2019 Kartikay Kaul

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++


========================================================
Contents:

1. Running The program as its
2. Dataset
3. Running Notebooks

=========================================================

1. RUNNING THE PROGRAM AS IT IS
There are two main programs:
	train.py 	test.py
*train.py is used to train the models(sklearn ones) on different protocols
 which will also take some parameters as input
 The file will exclusively ask for pretrained model to be stored on the system

*test.py is used to extract the pretrained model and test the model on
 the parameters given

You need to have following softwares and python packages to run
the python files successfully:
 => python3.6 or above
 => python packages: numpy, sklearn, pandas, matplotlib, pickle, tqdm
 => instead of above softwares you can simply install the anaconda distribution
    on python/R at this link: https://www.anaconda.com/distribution/
    it will install all necessary python packages for data science for you
 => It is necessary for these python packages to be installed to run the train.py and test.py
    python files.

  ============

  TRAINING OUR MODEL (This will take a lot of time)
   go to windows commandline or anaconda prompt and type
     "python train.py icmp 0"
   this will actually train the data set on "icmp" protocol with the KNN model.
   If you wish to use the second model type:
     "python train.py icmp 1"
   You can even change the protocol from the choices "udp", "tcp_syn" and "icmp". 
   So if you want to use tcp_syn protocol type and train it with KNN model type:
      "python train.py tcp_syn 0"
   
   At the end of executing this command you will get something like this:

    Data preprocessing done.
    The model has been fit.
    Save the fitted model?(y/n)

   asking you to save the pre-trained model for future use. type "y" and press enter
   CONGRATULATIONS! You saved your pre-trained model.


  TESTING OUR MODEL
   This is fast but a little tricky
   You have to ensure how many parameters you input for testing out the class.
    type "python test.py tcp_syn -1.5 1.0 2.0 30.0 1.0"
   This will use the tcp_syn pre-trained model and test the given parameters on it.
   Now each protocol has different parameter length as input. While tcp_syn protocol takes
   a length of 5 float value inputs others may take different inputs.
   NOTE:
	ICMP TAKES 7 ARGUMENTS
	UDP TAKES 5 ARGUMENTS
	TCP_SYN TAKES 5 ARGUMENTS
   I have put command line statements below for you to execute and test the dataset.
	"python test.py tcp_syn -1.5 1.0 2.0 1.0 1.0"
	"python test.py tcp_syn -1.5 1.0 2.0 30.0 1.0"
	"python test.py icmp 0.0 0.0 30.0 0.0 1.0 0.0 0.0"
	"python test.py icmp -0.1 30.0 0.0 2.0 0.0 0.0 2.0"
	"python test.py udp 146.0 0.0 105.0 254.0 2.0"
	"python test.py udp 45.0 -0.3 45.0 236.0 2.0"

2. DATASET
  All of the generated, consolidated and split dataset is stored in dataset folder and
  is open to use by any. The cleaned.csv file is KD99 generated dataset. It is not ours.
  Our dataset is the refined ones and we are not providing it.
3. JUPYTER NOTEBOOKS
   
   ".ipynb" files can be run by installing jupyter on your system.
   run "pip3 install jupyter" on your cmd
   and to run jupyter go to cmd type "jupyter notebook" and a browser window will open itself.
   careful which drive you choose to open it in, If your jupyter files are in D: drive and
   you execute "jupyter notebook" while directory is in C: disk then you cannot access files
   from the other drive unless you copy/upload them onto that drive where you need them.
   So it is advised to ensure your files and cmd are on same drive letter.
   Ensure that the dataset is where the python notebooks are or you can just adjust the URLs
   of the dataset in the python notebooks.

=============END OF FILE =============================

Just follow below.

EXECUTE FOLLOWING COMMANDS ON YOUR CMD:

	"python test.py tcp_syn -1.5 1.0 2.0 1.0 1.0"
	"python test.py tcp_syn -1.5 1.0 2.0 30.0 1.0"
	"python test.py icmp 0.0 0.0 30.0 0.0 1.0 0.0 0.0"
	"python test.py icmp -0.1 30.0 0.0 2.0 0.0 0.0 2.0"
	"python test.py udp 146.0 0.0 105.0 254.0 2.0"
	"python test.py udp 45.0 -0.3 45.0 236.0 2.0"
	
Edited by Kartikay Kaul
