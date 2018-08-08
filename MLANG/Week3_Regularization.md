# Regularization

----

**1. You are training a classification model with logistic regression. Which of the following statements are true? Check all that apply.**

A. Introducing regularization to the model always results in equal or better performance on examples not in the training set.

B. Introducing regularization to the model always results in equal or better performance on the training set.

**C. Adding a new feature to the model always results in equal or better performance on examples in the training set.**

D. Adding many new features to the model makes it more likely to overfit the training set.

**Note: ABD is not suitable in some certain conditions - A.D. when underfitting B. just wrong**

----

**2. Suppose you ran logistic regression twice, once with $\lambda = 0$, and once with $\lambda = 1$. One of the times, you got parameters $\theta = \begin{bmatrix} 26.29 \\ 65.41 \end{bmatrix}$, and the other time you got $\theta = \begin{bmatrix} 2.75 \\ 1.32 \end{bmatrix}$. However, you forgot which value of $lambda$ corresponds to which value of $\theta$. Which one do you think corresponds to $\lambda = 1$?**

A. $\theta = \begin{bmatrix} 26.29 \\ 65.41 \end{bmatrix}$

**B. $\theta = \begin{bmatrix} 2.75 \\ 1.32 \end{bmatrix}$**

----

**3. Which of the following statements about regularization are true? Check all that apply.**

**A. Using too large a value of $\lambda$ can cause your hypothesis to underfit the data.**

B. Because regularization causes $J(\theta)$ to no longer be convex, gradient descent may not always converge to the global minimum (when $\lambda > 0$, and when using an appropriate learning rate $\alpha$).

C. Because logistic regression outputs values $0 \le h_{\theta}(x) \le 1$,  its range of output values can only be "shrunk" slightly by regularization anyway, so regularization is generally not helpful for it.

D. Using a very large value of $\lambda$ cannot hurt the performance of your hypothesis; the only reason we do not set $\lambda$ to be too large is to avoid numerical problems.

**E. Consider a classification problem. Adding regularization may cause your classifier to incorrectly classify some training examples (which it had correctly classified when not using regularization, i.e. when $\lambda = 0$).**

----

**4. In which one of the following figures do you think the hypothesis has overfit the training set?**

**A**. ![4-1](https://d18ky98rnyall9.cloudfront.net/6w-qg77oEeSZtCIACx4DqA_Screen-Shot-2015-02-27-at-5.24.59-PM.png?Expires=1533859200&Signature=Esf~5t1TLMJdXxbKQMuU70R~e7Lg-MdDsoXVu7nHpaMDeqt0yn~OTXXYfyPyjyJQrKaJdyVIlAd6xFEhvYN5L6lg6TP39rPlYonxpCjpuRRVZgEwF6XrLi2111qdFze33SuOxh4I~1DUXxNx-3VnUjemHpW1h-~5uTt25ylAtIo_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)

B. ![4-2](https://d18ky98rnyall9.cloudfront.net/B--iib7pEeSjMiIAC7MDiQ_Screen-Shot-2015-02-27-at-5.25.16-PM.png?Expires=1533859200&Signature=B0ih2rrxUVQ8lYZYxKDqQC7g369YhZVN2jNNC-Jp0RhW1woIsW8S4~5F10fYSW-KfI-lC-TNC9sQCz5qhikYKkDe4SUuLqaHnHUl0PY4OoUBGNc3FUHukzOoixNBYvXQfu~PViWyg~GfO9B~fkUbxo8tvSXAxpaTR2NuOZssobY_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)

C. ![4-3](https://d18ky98rnyall9.cloudfront.net/MMTSK77pEeSjMiIAC7MDiQ_Screen-Shot-2015-02-27-at-5.25.39-PM.png?Expires=1533859200&Signature=FYTfXVBZUtOzyBErgX-jKgBpi6jcBt07fv8CKpwSUXtr3bKEM1DvIRnvmlJcWufGHjuQOY-lYPbrY4wOmUe0hQEJfwjz8K-wPzlgttX72qBV~AZMttC3lpUNUxyPw98cHV5vO0kOnCcUqcxVWS907ePIDYpBnaUx0RW0NJy06eQ_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)

D. ![4-4](https://d18ky98rnyall9.cloudfront.net/SlZinr7pEeSKOiIAC1ARFQ_Screen-Shot-2015-02-27-at-5.25.45-PM.png?Expires=1533859200&Signature=fH7~B0gdWAe1Kal7ANvXfinyArb45N4endLfw0C1~FVHwaKsTCZ3I1BMIkMrje10aG4g9nvoz~ReAtLfrnFri-C~DsQeMZhvOzOOX5PmslJ42UnTHf5SgbaCX2ze4T8xbLYCh077yQQumXabeN85KIR-nMtTMw4rg0El2bbsUMk_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)

----

**5. In which one of the following figures do you think the hypothesis has underfit the training set?**

**A**. ![5-1](https://d18ky98rnyall9.cloudfront.net/4qRnjr7pEeSjMiIAC7MDiQ_Screen-Shot-2015-02-27-at-5.30.48-PM.png?Expires=1533859200&Signature=Dyky06ntUZJGRoz4~~DXWyVrTTco7zvKqrMm8nBk0KECUx25PUtwKX0ApaMX5jNhVJ4f9qLHlB2-6BX7Vz9zq9CbvYC4-fMCb3c3-up3fC1H8gDpgGIAoZomdgS6GJ88dN3WthEF1P7JE~urXsnJR5AHdcjIFEaIyyhbVXmXM6w_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)

B. ![5-2](https://d18ky98rnyall9.cloudfront.net/8kfaFb7pEeSZtCIACx4DqA_Screen-Shot-2015-02-27-at-5.30.56-PM.png?Expires=1533859200&Signature=ge7BwnvRnERneWvHN8-DcWvdlasfAtqgxbkUyFylgQ7ETvGje-S~qwLWQZG8Ay3CQ3mXRYH3Yj0gDAXlIpvQ8rME7D4f8-JrMZkM0hmDsMveSDZTuBVUq59g1s~6Z5KJnoBb9Kawq0~gJqd4bCECkkNk5z5UXBAsNVa7ZiJfwVQ_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)

C. ![5-3](https://d18ky98rnyall9.cloudfront.net/BRZOFr7qEeSZtCIACx4DqA_Screen-Shot-2015-02-27-at-5.31.02-PM.png?Expires=1533859200&Signature=gSXeF-iMsBv6regkE7QoRkTMV4IElc4ZNnLNXTrWiyv5nmbyZSqTImB9-aOFzabYqZdZGirNWzupQcLPtcBpXy54jf3FYsjkmPpdg~t5uV1w9Ev9TfVP8~V5nYsI1R6PE9nseSb6x~rqcEF2Leizjpz7ni4jCW0JaB5g0XO3Nno_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)

D. ![5-4](https://d18ky98rnyall9.cloudfront.net/GX7qX77qEeSjMiIAC7MDiQ_Screen-Shot-2015-02-27-at-5.31.10-PM.png?Expires=1533859200&Signature=aKxAsBCgfn5MNjFPtnQAAkcnNgEIY7xa8Qa-vxP8jgqN6nSZYhQK1ZUyM6czK6USm60V-2Rvg1xPYYV1eXVUfSFYPPC05L2Z6ZQedRCSnVaJLDFpFNzt3sFwC~1dNahrCw2lFLf7M6pKKrx8DFXR-jlsrob0wIjw8VOh1AReFOs_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)