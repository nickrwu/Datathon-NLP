# News Diggers NLP Datathon Project
## 1. **XML Parser.ipynb** - Retrieving Text from XML Files
* ### Extracted Properties:
    * Full Text Data
    * Publish Date
    * Newspaper Publisher
* ### Input:
  * ProQuest Datathon zip files (ours was split downloaded 11 parts)
  * New York Times & Atlanta Daily World Advertisement csv
* ### Output:
  * AdData.csv (Complete csv with 2 mil+ data points of advertisement OCR data)

## 2. **Data Cleaning.ipynb** - Handling OCR Errors
* ### Input:
  * AdData.csv
* ### Output:
  * TrainingData.csv (1000 observations picked to train Name Entity Recognition Model)$$

## 3. **Modeling.ipynb** - Training and Testing Model