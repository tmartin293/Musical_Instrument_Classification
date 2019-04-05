TODO: make a Python implementation of the Feature Extraction algorithm.
1) Normalize sampled data (remove abs( sample ) <= 0.009)
2) Compute the N-point symmetric Hamming window filter (win_size = 882)
3) Apply the Hamming Filter to the normalized sample data (element wise multiplication)
4) Calculate the Discrete Cosine Transform of the interval of the filtered data that was normalized
5) Calculate the inverse discrete cosine transform of the transformed data
