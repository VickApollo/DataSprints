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
```

2. Datasets

All datasets are available on a public url hosted on amazon's web server. Below the link foreach file:
- https://s3.amazonaws.com/data-sprints-eng-test/data-sample_data-nyctaxi-trips-2009-json_corrigido.json
- https://s3.amazonaws.com/data-sprints-eng-test/data-sample_data-nyctaxi-trips-2010-json_corrigido.json
- https://s3.amazonaws.com/data-sprints-eng-test/data-sample_data-nyctaxi-trips-2011-json_corrigido.json
- https://s3.amazonaws.com/data-sprints-eng-test/data-sample_data-nyctaxi-trips-2012-json_corrigido.json

This test was writen in Python making use of Jupyter Notebook to format the test in Dossier style. Is recommended to use Python 3 in order to maintaing compatibility with the modules and functions presented in this project.


# Further improvements/implementations

- For data analysis: A technology we could also use instead of Pandas is Dask. Dask is a parallel computing technology created in Python and extends interfaces from Pandas , Numpy and others known modules. Dask works with "lazy transformation" (same approach as Spark) which provides you the flexibility to design and test in large scale in a very stable and manageable environment.

- For data processing (streaming): On this project we take the advantages of chunk reading to simulate a streaming of data. To make things more realistic, we could actually use streaming tools for that. Suggestion would be a combo of Kafka + Faust (Python Module). Kafka would be the streaming service, receiving messages while Faust would be the actual data processor receiving the data from the streaming service.

- For data visualization: On this project we take the advantages of matplotlib animation capability. To make things more professional I suggest uinge one of the tools below:
  1. <a href="https://help.pentaho.com/Documentation/7.0/0R0/CTools/CDE_Dashboard_Overview">Pentaho CDE</a>
  2. <a href="https://powerbi.microsoft.com/en-us/">Power BI</a>
