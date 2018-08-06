# Principal Component Analysis

----

**1. Consider the following 2D dataset:**

![1](https://d18ky98rnyall9.cloudfront.net/lkk6_L7kEeSZtCIACx4DqA_15.1-question.jpg?Expires=1533686400&Signature=ZniVLFW6lLsSR2R2rdHfcySn1F1XeFnQgqVCORWkzCFHQb~qZ-GiOdYeyU3DUij84WGHfYFsoGlfTA-g8xFJopl5CQQiVkuQs8bjxtRl4yX9eCLdAYrrD2q8Rr1xJpK2wF7m7CZ8YTu7dwDnQcRRzTqXN9s9gYHTTp~I4~hw5Yw_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)

**Which of the following figures correspond to possible values that PCA may return for $u^{(1)}$ (the first eigenvector / first principal component)? Check all that apply (you may have to check more than one figure).**

**A**. ![1-1](https://d18ky98rnyall9.cloudfront.net/wBdxSL7kEeSKOiIAC1ARFQ_15.1-a.jpg?Expires=1533686400&Signature=V23w6w6B-7OTZ2ZbwRk7S6GorjyxUVKTtZy1yqXcYLv6GJZF4ZPtAIcdCi1hBUPvyjR5bVzbl2kPklofnqLtaHjYSUrz4TEmQxxUXlfqa7z4f~QTleMZkWMMdAdRiPVLZBawd8a7bhvIb1c95mObCgIJ6AFYq990i4gTQrRlukI_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)

**B**. ![1-2](https://d18ky98rnyall9.cloudfront.net/6lGHcL7kEeSZtCIACx4DqA_15.1-b.jpg?Expires=1533686400&Signature=J5q6k3OQcKJUThuka3c5pNUgiWlgcun66~NMHdl3aS2T22BsNKRlqxP1tq6MwNGX8x5FJ8sCqnE2pUKb-f5kG55tPo3PdyNXkBXzeN5wnROi6fO6mUQKLe057KkWti~W3DaXyQNGnVrYEo778crgabJyzBF8ZdbN7PBKl7ac~~Y_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)

C. ![1-3](https://d18ky98rnyall9.cloudfront.net/_Say2r7kEeSKOiIAC1ARFQ_15.1-c.jpg?Expires=1533686400&Signature=WjLldgIFdjtYtDjlnjQ3IJbzKV1wYaESGOXVmFxE1qLGMBvdS7fwUbn4UC1MlsMbMYvyQI3yAv~AYD6m~5P80J4l~4S-JGTACrdtCMQBz20dL972hiItP6VfnITWTGd0TwNxHDcj~h1quOktzvhkZa2J1Fcczt~0WRBccyyN5z8_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)

D. ![1-4](https://d18ky98rnyall9.cloudfront.net/DoOVFr7lEeSjMiIAC7MDiQ_15.1-d.jpg?Expires=1533686400&Signature=QJOZJk3Hv2XUW8JG9Q19mus1Vb~TMWSZ9KGPXFcRvLLwZbvClxZmsUbrlTb6L5nweh04YKQhECJvzFKAFmf5qJjN6leCmcfLWQcKHc3Ud38GttUN4mRPWidfqZ3TRJOGPYswgyB4hoL7WVIF-quOrmZn8dLq0rviF~FNSeftbAQ_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)

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

