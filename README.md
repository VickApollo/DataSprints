# DataSprints

Project to show technical skills related to Data Engineering.

# Requirements

1. Directory Structure

To run the test on your computer you must have the following folder structure:
```
.
+-- Parent Directory
|   +-- DATA
|       +-- data-sample_data-nyctaxi-trips-2009-json_corrigido.json
|       +-- data-sample_data-nyctaxi-trips-2010-json_corrigido.json
|       +-- data-sample_data-nyctaxi-trips-2011-json_corrigido.json
|       +-- data-sample_data-nyctaxi-trips-2012-json_corrigido.json
|   +-- low_memory_dataframe.py
|   +-- DataSprint - Pandas.ipynb
|   +-- consumer.py
|   +-- producer.py
```

2. Datasets

All datasets are available on a public url hosted on amazon's web server. Below the link foreach file:
- https://s3.amazonaws.com/data-sprints-eng-test/data-sample_data-nyctaxi-trips-2009-json_corrigido.json
- https://s3.amazonaws.com/data-sprints-eng-test/data-sample_data-nyctaxi-trips-2010-json_corrigido.json
- https://s3.amazonaws.com/data-sprints-eng-test/data-sample_data-nyctaxi-trips-2011-json_corrigido.json
- https://s3.amazonaws.com/data-sprints-eng-test/data-sample_data-nyctaxi-trips-2012-json_corrigido.json

This test was writen in Python making use of Jupyter Notebook to format the test in Dossier style. Is recommended to use Python 3 in order to maintaing compatibility with the modules and functions presented in this project.

# Streaming Configuration
#point to file

# Further improvements/implementations

- For data analysis: A technology we could also use instead of Pandas is Dask. Dask is a parallel computing technology created in Python and extends interfaces from Pandas , Numpy and others known modules. Dask works with "lazy transformation" (same approach as Spark).

- For data streaming: There are also other options for Streaming. One well known that has capabilities related also to data analysis is Spark.

- For data processing (performance): To reduce performance issues a suggestion for data manipulation would be to load only the features/columns in our dataset by taking the advantages of parquet. That way, we can perform all the calculations for each question without allocating unnecessary memory.

- For data visualization: On this project we take the advantages of matplotlib animation capability. To make things more professional I suggest uinge one of the tools below:
  1. <a href="https://help.pentaho.com/Documentation/7.0/0R0/CTools/CDE_Dashboard_Overview">Pentaho CDE</a>
  2. <a href="https://powerbi.microsoft.com/en-us/">Power BI</a>

- Security: To avoid loss of data it's recommended to implement redundancies and security schemas on each interface of the streaming processor.

  ```flow 
  Request ---------> Stream Processor ----------> Data Consumer
         (Interface)                  (Interface)
  ```
 
