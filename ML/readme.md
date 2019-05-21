
reference_svm script will read 'mfcc_results.csv' file located in the current working directory then create an SVM model using an RBF kernel. The SVM model will be serialized and saved using pickle to 'pickle_model.pkl' in the current working directory for consistent classification. 

** Important note: SVM model serialization and deserialization (with pickle) is both Python version dependent and CPU ISA dependent. Do not use a pickle model created with a different version of Python or one created on a machine with a different ISA. For security, any pickle model used should be one created on your own local machine. **  
