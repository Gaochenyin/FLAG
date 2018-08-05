# Anomaly Detection

----

**1. For which of the following problems would anomaly detection be a suitable algorithm?**

A. From a large set of hospital patient records, predict which patients have a particular disease (say, the flu). 

**B. In a computer chip fabrication plant, identify microchips that might be defective.**

**C. From a large set of primary care patient records, identify individuals who might have unusual health conditions.**

D. Given data from credit card transactions, classify each transaction according to type of purchase (for example: food, transportation, clothing). 

----

**2. Suppose you have trained an anomaly detection system for fraud detection, and your system that flags anomalies when p(x) is less than $\varepsilon$, and you find on the cross-validation set that it mis-flagging far too many good transactions as fradulent. What should you do?**

 **A. Decrease $\varepsilon$**
 
 B. Increase $\varepsilon$

----

**3. Suppose you are developing an anomaly detection system to catch manufacturing defects in airplane engines. You model uses**

$$p(x) = \prod_{j=1}^{n}p(x_{j};\mu_{j},\sigma_{j}^{2})$$

**You have two features $x_1$ = vibration intensity, and $x_2$ = heat generated. Both x1 and x2 take on values between 0 and 1 (and are strictly greater than 0), and for most "normal" engines you expect that $x_1 \approx x_2$. One of the suspected anomalies is that a flawed engine may vibrate very intensely even without generating much heat (large x1, small x2), even though the particular values of x1 and x2 may not fall outside their typical ranges of values. What additional feature x3 should you create to capture these types of anomalies:**

**A. $x_3 = \frac{x_1}{x_2}$**

B. $x_3 = \frac{1}{x_1}$

C. $x_3 = \frac{1}{x_2}$

D. $x_3 = x_1 + x_2$

----

**4. Which of the following are true? Check all that apply.**

A. When evaluating an anomaly detection algorithm on the cross validation set (containing some positive and some negative examples), classification accuracy is usually a good evaluation metric to use.

**B. In anomaly detection, we fit a model p(x) to a set of negative (y=0) examples, without using any positive examples we may have collected of previously observed anomalies.**

**C. When developing an anomaly detection system, it is often useful to select an appropriate numerical performance metric to evaluate the effectiveness of the learning algorithm.**

D. In a typical anomaly detection setting, we have a large number of anomalous examples, and a relatively small number of normal/non-anomalous examples.

----

**5. You have a 1-D dataset $\{x(1),\ldots,x(m)\}$ and you want to detect outliers in the dataset. You first plot the dataset and it looks like this:**

![5](https://d18ky98rnyall9.cloudfront.net/ee5JoL54EeSVRiIAC2sM-Q_Screen-Shot-2015-02-27-at-4.01.53-AM.png?Expires=1533600000&Signature=GC7vulsMZPQKiQMM96PPELzSWn~4CwZJk9G8ueyFZx9srEYWwCosRdbNgxAxGK0~bBz~niINZsrIrBBShToAx9NP9G3wOg-aoYlwgyXkHmiZV~SCeWa834PDtq~tQBRqWXbBlQIr6AS12aWzOxig8nKKWD4e8MMxtj3dZU7Ss-c_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)

**Suppose you fit the gaussian distribution parameters $\mu_1$ and $\sigma^2_1$ to this dataset. Which of the following values for $\mu_1$ and $\sigma^2_1$ might you get?**

**A. $\mu_1$ = -3, $\sigma^2_1$ = 4**

B. $\mu_1$ = -6, $\sigma^2_1$ = 4

C. $\mu_1$ = -3, $\sigma^2_1$ = 2

D. $\mu_1$ = -6, $\sigma^2_1$ = 2
