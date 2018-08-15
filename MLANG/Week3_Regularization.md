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

**A**. ![4-1](https://github.com/phdsky/FLAG/blob/master/MLANG/images/Week3_Regularization/4-1.png)

B. ![4-2](https://github.com/phdsky/FLAG/blob/master/MLANG/images/Week3_Regularization/4-2.png)

C. ![4-3](https://github.com/phdsky/FLAG/blob/master/MLANG/images/Week3_Regularization/4-3.png)

D. ![4-4](https://github.com/phdsky/FLAG/blob/master/MLANG/images/Week3_Regularization/4-4.png)

----

**5. In which one of the following figures do you think the hypothesis has underfit the training set?**

**A**. ![5-1](https://github.com/phdsky/FLAG/blob/master/MLANG/images/Week3_Regularization/5-1.png)

B. ![5-2](https://github.com/phdsky/FLAG/blob/master/MLANG/images/Week3_Regularization/5-2.png)

C. ![5-3](https://github.com/phdsky/FLAG/blob/master/MLANG/images/Week3_Regularization/5-3.png)

D. ![5-4](https://github.com/phdsky/FLAG/blob/master/MLANG/images/Week3_Regularization/5-4.png)
