# Journal-Analysis: 
Topic modeling and analysis of focus shift in papers published in the journal-ASQ over the past 10 years

Data collection: All the papers published in the journal- ASQ from 2011 to 2021 are downloaded via API requests (requests_final.py) 
Preparing the corpus: Parsing the XML files to extract only relevant text (xml_to_text.py)  
Preprocessing the corpus: preprocessing is done using using Python NLP toolkit (LDA_No_Essays_no_below=3.ipynb)  
Building the topic clusters based on Latent Dirichlet Allocation, Doc2vec and K-means clustering (LDA_No_Essays_no_below=3.ipynb, LDA_hyperparameter_tuning_fullcorpus.ipynb, LDA&Kmeans_onDoc2vec.ipynb)
Analysis of focus shift based on the topics identified by the model - Identify_methods_of_research_through_keywords.ipynb, Identify_methods_of_research_through_keywords.ipynb
The Tableau dashboard of the analysis can be found at https://public.tableau.com/views/Trends-TopicsCitations/Dashboard1?:language=en-US&:display_count=n&:origin=viz_share_link 
