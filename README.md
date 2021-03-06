# Journal Analysis: 
The goal of this project is to analyze the focus shift of research areas published in the journal-ASQ over the past 10 years. This is done by categorizing the papers into topics based on topic modelling (using Latent Dirichlet Allocation) and Kmeans clustering. The trends over time in these topics are analyzed to understand the focus shift.  Other attributes of the papers like citations, gender and country of affiliation of the author, country of datasource, methods of research are also analyzed for trends and distributions over topics. 
<br>The **Tableau dashboard** of the analysis can be found at https://public.tableau.com/views/Trends-TopicsCitations/Dashboard1?:language=en-US&:display_count=n&:origin=viz_share_link 

<br>**Data collection**: XML files of all the papers published in the journal- ASQ from 2011 to 2021 are downloaded via API requests (requests_final.py) 
<br>**Preparing the corpus**: Parsing the XML files to extract only relevant text (xml_to_text.py)
<br>**Preprocessing the corpus**: preprocessing is done using using Python NLP toolkit (LDA_No_Essays_no_below=3.ipynb)
<br>**Building the topic clusters** based on Latent Dirichlet Allocation, Doc2vec and K-means clustering (LDA_No_Essays_no_below=3.ipynb, LDA_hyperparameter_tuning_fullcorpus.ipynb, LDA&Kmeans_onDoc2vec.ipynb)
<br>**Analysis of focus shift** based on the topics identified by the model - Analysis_Charts.ipynb
<br>Identifying **methods of research** based on word count of keywords: Identify_methods_of_research_through_keywords.ipynb
<br> https://public.tableau.com/views/Analysis-Methods_new/Methods?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link, https://public.tableau.com/views/Topic-wise_AttributesMethods/Method?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link



<br> Note: The jupyter notebooks are not fully self-explanatory. More detailed documentation is yet to be uploaded. 
