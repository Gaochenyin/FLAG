# Logistic Regression

----

**1. Suppose that you have trained a logistic regression classifier, and it outputs on a new example xx a prediction $h_\theta(x)$= 0.7. This means (check all that apply):**

A. Our estimate for $P(y = 1|x; \theta)$ is 0.3.

B. Our estimate for $P(y = 0|x; \theta)$ is 0.7.

**C. Our estimate for $P(y = 1|x; \theta)$ is 0.7.**

**D. Our estimate for $P(y = 0|x; \theta)$ is 0.3.**

----

**2. Suppose you have the following training set, and fit a logistic regression classifier $h_{\theta}(x) = g(\theta_0 + \theta x_1 + \theta_2 x_2)$**.

![2-1](https://github.com/phdsky/FLAG/blob/master/MLANG/images/Week3_LogisticRegression/2-1.png)

![2-2](https://github.com/phdsky/FLAG/blob/master/MLANG/images/Week3_LogisticRegression/2-2.png)

**Which of the following are true? Check all that apply.**

**A**. Adding polynomial features (e.g., instead using $h_{\theta}(x) = g(\theta_0 + \theta_1 x_1 + \theta_2 x_2 + \theta_3 x^2_1 + \theta_4 x_1 x_2 + \theta x^2_2)$) could increase how well we can fit the training data.

**B**. At the optimal value of $\theta$ (e.g., found by fminunc), we will have $J(\theta) \ge 0$.

C. Adding polynomial features (e.g., instead using $h_{\theta}(x) = g(\theta_0 + \theta_1 x_1 + \theta_2 x_2 + \theta_3 x^2_1 + \theta_4 x_1 x_2 + \theta x^2_2)$) would increase $J(\theta)$ because we are now summing over terms.

D. If we train gradient descent for enough iterations, for some examples $x^{(i)}$ in the training set it is possible to obtain $h_{\theta}(x^{(i)}) > 1$

----

**3. For logistic regression, the gradient is given by $\frac{\partial}{\partial\theta_j}J(\theta) = \frac{1}{m}\sum^m_{i=1}(h_{\theta}(x) - y^{(i)})x_j^{(i)}$. Which of these is a correct gradient descent update for logistic regression with a learning rate of $\alpha$? Check all that apply.**

A. $\theta := \theta - \alpha\frac{1}{m}\sum^m_{i=1}(\theta^Tx - y^{(i)})x^{(i)}$

**B**. $\theta_j := \theta_j - \alpha\frac{1}{m}\sum^m_{i=1}(h_{\theta}(x^{(i)}) - y^{(i)})x_j^{(i)}$(simultaneously update for all $j$)

C. $\theta_j := \theta_j - \alpha\frac{1}{m}\sum^m_{i=1}(h_{\theta}(x^{(i)}) - y^{(i)})x^{(i)}$(simultaneously update for all $j$)

**D**. $\theta_j := \theta_j - \alpha\frac{1}{m}\sum^m_{i=1}(\frac{1}{1+e^{-\theta^Tx^{(i)}}} - y^{(i)})x_j^{(i)}$(simultaneously update for all $j$)

----

**4. Which of the following statements are true? Check all that apply.**

A. For logistic regression, sometimes gradient descent will converge to a local minimum (and fail to find the global minimum). This is the reason we prefer more advanced optimization algorithms such as fminunc (conjugate gradient/BFGS/L-BFGS/etc).

B. Linear regression always works well for classification if you classify by using a threshold on the prediction made by linear regression.

**C. The cost function $J(\theta)$ for logistic regression trained with $m \ge 1$ examples is always greater than or equal to zero.**

**D. The sigmoid function $g(z) = \frac{1}{e^{-z}}$ is never greater than one ($>1$).**

----

**5. Suppose you train a logistic classifier $h_{\theta}(x) = g(\theta_0 + \theta_1 x_1 + \theta_2 x_2)$. Suppose $\theta_0 = -6, \theta_1 = 0, \theta_2 = 1$. Which of the following figures represents the decision boundary found by your classifier?**

A. ![5-1](https://github.com/phdsky/FLAG/blob/master/MLANG/images/Week3_LogisticRegression/5-1.png)

B. ![5-2](https://github.com/phdsky/FLAG/blob/master/MLANG/images/Week3_LogisticRegression/5-2.png)

C. ![5-3](https://github.com/phdsky/FLAG/blob/master/MLANG/images/Week3_LogisticRegression/5-3.png)

**D**. ![5-4](https://github.com/phdsky/FLAG/blob/master/MLANG/images/Week3_LogisticRegression/5-4.png)
