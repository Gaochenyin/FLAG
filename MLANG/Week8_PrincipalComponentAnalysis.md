# Principal Component Analysis

----

**1. Consider the following 2D dataset:**

![1](https://github.com/phdsky/FLAG/blob/master/MLANG/images/Week8_PrincipalComponentAnalysis/1.jpg)

**Which of the following figures correspond to possible values that PCA may return for $u^{(1)}$ (the first eigenvector / first principal component)? Check all that apply (you may have to check more than one figure).**

**A**. ![1-1](https://github.com/phdsky/FLAG/blob/master/MLANG/images/Week8_PrincipalComponentAnalysis/1-1.jpg)

**B**. ![1-2](https://github.com/phdsky/FLAG/blob/master/MLANG/images/Week8_PrincipalComponentAnalysis/1-2.jpg)

C. ![1-3](https://github.com/phdsky/FLAG/blob/master/MLANG/images/Week8_PrincipalComponentAnalysis/1-3.jpg)

D. ![1-4](https://github.com/phdsky/FLAG/blob/master/MLANG/images/Week8_PrincipalComponentAnalysis/1-4.jpg)

----

**2. Which of the following is a reasonable way to select the number of principal components $k$? (Recall that $n$ is the dimensionality of the input data and $m$ is the number of input examples.)**

A. Choose $k$ to be the largest value so that at least 99% of the variance is retained

**B. Choose $k$ to be the smallest value so that at least 99% of the variance is retained.**

C. Use the elbow method.

D. Choose $k$ to be 99% of $m$ (i.e., $k=0.99∗m$, rounded to the nearest integer).

----

**3. Suppose someone tells you that they ran PCA in such a way that "95% of the variance was retained." What is an equivalent statement to this?**

A. $\frac{\frac{1}{m}\sum^{m}_{i=1} \| x^{(i)} - x_{approx}^{(i)} \|^{2}} {\frac{1}{m}\sum^{m}_{i=1} \| x^{(i)} \|^{2}}\geqslant 0.95$

**B**. $\frac{\frac{1}{m}\sum^{m}_{i=1} \| x^{(i)} - x_{approx}^{(i)} \|^{2}} {\frac{1}{m}\sum^{m}_{i=1} \| x^{(i)} \|^{2}}\leqslant 0.05$

C. $\frac{\frac{1}{m}\sum^{m}_{i=1} \| x^{(i)} - x_{approx}^{(i)} \|^{2}} {\frac{1}{m}\sum^{m}_{i=1} \| x^{(i)} \|^{2}}\leqslant 0.95$

D. $\frac{\frac{1}{m}\sum^{m}_{i=1} \| x^{(i)} - x_{approx}^{(i)} \|^{2}} {\frac{1}{m}\sum^{m}_{i=1} \| x^{(i)} \|^{2}}\geqslant 0.05$

----

**4. Which of the following statements are true? Check all that apply.**

A. PCA is susceptible to local optima; trying multiple random initializations may help.

**B. Given input data $x \in \mathbb {R}^n$, it makes sense to run PCA only with values of $k$ that satisfy $k≤n$. (In particular, running it with $k = n$ is possible but not helpful, and $k > n$ does not make sense.)**

**C. Even if all the input features are on very similar scales, we should still perform mean normalization (so that each feature has zero mean) before running PCA.**

D. Given only $z^{(i)}$ and $U_{\rm reduce}$, there is no way to reconstruct any reasonable approximation to $x^{(i)}$.

----

**5. Which of the following are recommended applications of PCA? Select all that apply.**

A. Preventing overfitting: Reduce the number of features (in a supervised learning problem), so that there are fewer parameters to learn.

**B. Data visualization: Reduce data to 2D (or 3D) so that it can be plotted.**

**C. Data compression: Reduce the dimension of your data, so that it takes up less memory / disk space.**

D. To get more features to feed into a learning algorithm.

