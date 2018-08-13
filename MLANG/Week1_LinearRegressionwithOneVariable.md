# Linear Regression with One Variable

----

**1. Consider the problem of predicting how well a student does in her second year of college/university, given how well she did in her first year.**

**Specifically, let x be equal to the number of "A" grades (including A-. A and A+ grades) that a student receives in their first year of college (freshmen year). We would like to predict the value of y, which we define as the number of "A" grades they get in their second year (sophomore year).**

| x | y |
| - | - |
| 5 | 4 |
| 3 | 4 |
| 0 | 1 |
| 4 | 3 |

**Here each row is one training example. Recall that in linear regression, our hypothesis is $h_{\theta}(x) = \theta_0 + \theta_1 x$, and we use mm to denote the number of training examples.**

**For the training set given above (note that this training set may also be referenced in other questions in this quiz), what is the value of $m$? In the box below, please enter your answer (which should be a number between 0 and 10).**

**Answer: 4**

----

**2. For this question, assume that we are using the training set from Q1. Recall our definition of the cost function was $J(\theta_0, \theta_1) = \frac{1}{2m}\sum^m_{i=1}(h_{\theta} x^{(i)} - y^{(i)})$. What is $J(0, 1)$? In the box below, please enter your answer (Simplify fractions to decimals when entering answer, and '.' as the decimal delimiter e.g., 1.5).**

**Answer: 0.5**

----

**3. Suppose we set $\theta_0 = -1, \theta_1 = 2$in the linear regression hypothesis from Q1. What is $h_{\theta}(6)$?**

**Answer: 11**

----

**4. In the given figure, the cost function $J(\theta_0,\theta_1)$ has been plotted against $\theta_0$and $\theta_1$, as shown in 'Plot 2'. The contour plot for the same cost function is given in 'Plot 1'. Based on the figure, choose the correct options (check all that apply).**

![4](https://d396qusza40orc.cloudfront.net/ml/images/4.2-quiz-1.png)

A. Point P (The global minimum of plot 2) corresponds to point C of Plot 1.

B. If we start from point B, gradient descent with a well-chosen learning rate will eventually help us reach at or near point A, as the value of cost function $J(\theta_0,\theta_1)$is maximum at point A.

**C. If we start from point B, gradient descent with a well-chosen learning rate will eventually help us reach at or near point A, as the value of cost function $J(\theta_0,\theta_1)$ is minimum at A.**

**D. Point P (the global minimum of plot 2) corresponds to point A of Plot 1.**

E. If we start from point B, gradient descent with a well-chosen learning rate will eventually help us reach at or near point C, as the value of cost function $J(\theta_0,\theta_1)$ is minimum at point C.

----

**5. Suppose that for some linear regression problem (say, predicting housing prices as in the lecture), we have some training set, and for our training set we managed to find some $\theta_0$, $\theta_1$ such that $J(\theta_0,\theta_1) = 0$.**

**Which of the statements below must then be true? (Check all that apply.)**

A. Gradient descent is likely to get stuck at a local minimum and fail to find the global minimum.

**B. Our training set can be fit perfectly by a straight line, i.e., all of our training examples lie perfectly on some straight line.**

C. For this to be true, we must have $y^{(i)} = 0$ for every value of $i = 1, 2, \ldots, m$.

D. For this to be true, we must have $\theta_0 = 0$ and $\theta_1 = 0$ so that $h_\theta(x) = 0$