# custom raceBERT

## preparation

1. make sure the folder structure remains the same  

```
root  
|-- data/  
|-- models/  
|-- trainied_models/  
```


    a. data in the data folder  
    b. `.py` files in the models folder  
    c. trained_models exist to store the trained models


2. make sure the data in the data folder follows the same structure as `nmzpAgeSexFL.csv`, or edit `preprocess_data.py` to produce the right `.parquet` files for training

3. make sure you have connection to transformer hub to download raceBERT/BERT models, or edit `raceBERT_train.py` to load models from local

## run
run the following commands in the <span style="color:red">**root**</span> folder
```
python -m models.preprocess_data data/nmzpAgeSexFL.csv
python -m models.raceBERT_train raceBERT florida_5label
```

## details

preprocess_data.py
1. `python -m models.preprocess_data [data_file]`
2. if using different data, need to follow the column structure in `nmzpAgeSexFL.csv`

raceBERT_train.py
1. `python -m models.raceBERT_train [model_label] [data_label]`
2. check `raceBERT_train.py` for existing `model_label` and `data_label`, or edit `raceBERT_train.py` for custom options