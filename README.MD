# Historical News NLP Datathon Project
![alt text](https://github.com/nickrwu/Datathon-NLP/blob/main/images/proquest.png)

Detecting advertisement properties in historical copies of the New York Times and the Atlanta Daily World
* Data (Omitted from Repo): Around 10 million historical New York Times and Atlanta Daily World advertisements, articles, cover pages, etc. represented in XML files. The text of these files were produced through OCR software.

## 1) **XML Parser.ipynb** - Retrieving Text from XML Files
* ### Extracted Properties:
    * Full Text Data
    * Publish Date
    * Newspaper Publisher
* ### Input:
  * ProQuest Datathon zip files (ours was split downloaded 11 parts)
  * New York Times & Atlanta Daily World Advertisement csv
* ### Output:
  * AdData.csv (Complete csv with 2 mil+ data points of advertisement OCR data)

## 2) **Data Cleaning.ipynb** - Handling OCR Errors
* ### Input:
  * AdData.csv
* ### Output:
  * TrainingData.csv (1000 observations picked to train Name Entity Recognition Model)$$

## 3) **Modeling.ipynb** - Training and Testing Custom NER Model
* ### **label.py** - Labeling training and testing data
* ### Input:
  * Training and Testing Data
* ### Output:
  * Recall
  * Precision
  * F1-Score
