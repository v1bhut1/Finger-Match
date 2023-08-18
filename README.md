# Finger-Match
Fingerprint matching system - Displays the best match found between two images and visualizes the matched features.

The fingerprint matching system is a powerful tool for identifying individuals based on their fingerprints. It uses feature-based matching techniques to identify the unique patterns present in a person's fingerprints and compare them to a database of known fingerprints. 

**WORKING ->**

The system works by first extracting key features from the input fingerprint images using a **feature detector** and descriptor algorithm such as **SIFT (Scale-Invariant Feature Transform)**. 
These features are then matched with features from a database of known fingerprints using a feature-matching algorithm such as **FLANN (Fast Library for Approximate Nearest Neighbors)**. 

**OUTPUT ->**
1. The system displays the best-matched fingerprint found between two images and visualizes the matched features.
2. _**BEST MATCH**_: is the file name of the best-matched fingerprint.
3. _**SCORE**_: represents the degree of similarity between the input fingerprint and the closest match in the database.


![image](https://github.com/v1bhut1/Finger-Match/assets/85229961/65bffc35-7ad0-4688-8be9-1f76b36729df)

![image](https://github.com/v1bhut1/Finger-Match/assets/85229961/f43aa96a-7b81-45b8-a1ca-6e1c116960c6)
