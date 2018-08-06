# Application: Photo OCR

----

**1. Suppose you are running a sliding window detector to find text in images. Your input images are 1000x1000 pixels. You will run your sliding windows detector at two scales, 10x10 and 20x20 (i.e., you will run your classifier on lots of 10x10 patches to decide if they contain text or not; and also on lots of 20x20 patches), and you will "step" your detector by 2 pixels each time. About how many times will you end up running your classifier on a single 1000x1000 test set image?**

A. 1,000,000

B. 250,000

**C. 500,000**

D. 100,000

----

**2. Suppose that you just joined a product team that has been developing a machine learning application, using m = 1,000 training examples. You discover that you have the option of hiring additional personnel to help collect and label data. You estimate that you would have to pay each of the labellers $10 per hour, and that each labeller can label 4 examples per minute. About how much will it cost to hire labellers to label 10,000 new training examples?**

A. $600

B. $250

C. $10,000

**D. $400**

----

**3. What are the benefits of performing a ceiling analysis? Check all that apply.**

A. If we have a low-performing component, the ceiling analysis can tell us if that component has a high bias problem or a high variance problem.

**B. It gives us information about which components, if improved, are most likely to have a significant impact on the performance of the final system.**

C. A ceiling analysis helps us to decide what is the most promising learning algorithm (e.g., logistic regression vs. a neural network vs. an SVM) to apply to a specific component of a machine learning pipeline.

**D. It can help indicate that certain components of a system might not be worth a significant amount of work improving, because even if it had perfect performance its impact on the overall system may be small.**

----

**4. Suppose you are building an object classifier, that takes as input an image, and recognizes that image as either containing a car ($y=1$) or not ($y=0$). For example, here are a positive example and a negative example:**

![4](https://d18ky98rnyall9.cloudfront.net/8azR1r56EeSVRiIAC2sM-Q_Screen-Shot-2015-02-27-at-4.16.22-AM.png?Expires=1533686400&Signature=lE4Ns0ktGF0TDAIYQBeWapr-iNYmYSnz6CP-HVJHgqWkXq81UFN22wTELHTmHtTYIrmTVngNZeq7CpCdCgyNOcDo3oabMprCS7-klo8VanNcYhaM4SK-JE1LIb9Eqs--R7dX5ZOMMiIpCawlbHDxYT7owyoJKVz7Bt9PtzcKXt8_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)

After carefully analyzing the performance of your algorithm, you conclude that you need more positive ($y=1$) training examples. Which of the following might be a good way to get additional positive examples?

**A. Mirror your training images across the vertical axis (so that a left-facing car now becomes a right-facing one).**

B. Take a few images from your training set, and add random, gaussian noise to every pixel.

C. Take a training example and set a random subset of its pixel to 0 to generate a new example.

D. Select two car images and average them to make a third example.

----

**5. Suppose you have a PhotoOCR system, where you have the following pipeline:**

![5-1](https://d18ky98rnyall9.cloudfront.net/5gV29L57EeShsSIACwKbzw_Screen-Shot-2015-02-27-at-4.21.30-AM.png?Expires=1533686400&Signature=SxFvwjqkES9ENtb~BzV4eX2cwQrN8jqGInO3Gil7OEG85JQBonAicMAqOq4tmcMleaWq9Y4Av0uQnq6m7VKNAhwovfB~wLw2kDbMPsmAhWNyOMb3Uf6UlA5pqMANgbDLYcq~IuFykYNV~kC5NwCmvXI9cbG3IaYik8QVp8ZfoxU_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)

**You have decided to perform a ceiling analysis on this system, and find the following:**

![5-2](https://d18ky98rnyall9.cloudfront.net/82LxZb57EeShsSIACwKbzw_Screen-Shot-2015-02-27-at-4.21.49-AM.png?Expires=1533686400&Signature=elm70C~MWkgRhDngkJxViiNzr~PSNEDPCs07KXtJmzniQPcevAIxvR2b1W-GV7DzVyRdDYH4WizemjbZBazDinijz2o-2ayC1yid47ig-ooVa-jAl~xfBKfrWWmIH-mMQBBcLoX7h5AL-INwxfdMHHSmBiwj~elhXiGcF2lkAQA_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)

**Which of the following statements are true?**

**A. There is a large gain in performance possible in improving the character recognition system.**

**B. Performing the ceiling analysis shown here requires that we have ground-truth labels for the text detection, character segmentation and the character recognition systems.**

C. The least promising component to work on is the character recognition system, since it is already obtaining 100% accuracy.

D. The most promising component to work on is the text detection system, since it has the lowest performance (72%) and thus the biggest potential gain.
