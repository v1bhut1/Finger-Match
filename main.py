import os 
import cv2

sample = cv2.imread(r'D:\AI_Lab_6_sem\archive\SOCOFing\Altered\Altered-Hard\11__M_Left_index_finger_Obl.BMP')

best_score = 0
filename = None
image = None
kp1, kp2, mp = None, None, None

path = r"D:\AI_Lab_6_sem\archive\SOCOFing\Real"
files = [f for f in os.listdir(path)][:1000]

for file in files:
    image_path = os.path.join(path, file)
    fingerprint_image = cv2.imread(image_path)
    # if fingerprint_image is not None:
    sift = cv2.SIFT_create() 

    keypoints_1, descriptors_1 = sift.detectAndCompute(sample, None)
    keypoints_2, descriptors_2 = sift.detectAndCompute(fingerprint_image, None)

    matches = cv2.FlannBasedMatcher({'algorithm': 1, 'trees': 10}, {}).knnMatch(descriptors_1, descriptors_2, k=2)
    match_points = []

    # filters out unreliable matches by comparing the distance between the two best matches (p and q).   
    for p, q in matches:
        if p.distance < 0.1 * q.distance:
            match_points.append(p)

    # Calculating the score
    keypoints = 0
    if len(keypoints_1) < len(keypoints_2):
        keypoints = len(keypoints_1)
    else:
        keypoints = len(keypoints_2)

    if len(match_points) / keypoints * 100 > best_score:
        best_score = len(match_points) / keypoints * 100
        filename = file
        image = fingerprint_image
        kp1, kp2, mp = keypoints_1, keypoints_2, match_points


# Generating OUTPUT 
if filename is not None:
    print("BEST MATCH: " + filename)
else:
    print("No match found.")

print("SCORE:" + str(best_score))

result = cv2.drawMatches(sample, kp1, image, kp2, mp, None)
result = cv2.resize(result, None, fx=4, fy=4)
cv2.imshow("Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()