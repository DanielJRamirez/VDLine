# VDLine
Line-level source code vulnerability detection project using Doc2Vec and binary classification

# File Descriptions
dataset_scraper.py: Scraper program used to extract dataset from GitHub repositories and combine them into vulnerable_sourcecode.pkl
                    Initially used on a previous version of VDLine and is now outdated. Including for record purposes.
                    
preprocess.py: Python file used to hold the function used to tokenize and otherwise preprocess a code file.
               Depending on input parameters, output can be used to test or train the Doc2Vec model
               
main.py: Main python file used to train and evaluate the Doc2Vec model and binary classification model

vul_detector.py: Python script using saved Doc2Vec and classifier models to predict vulnerability probabilities for each line of the code file passed into it
