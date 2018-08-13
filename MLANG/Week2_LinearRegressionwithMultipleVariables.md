# Linear Regression with Multiple Variables

----

**1. Suppose m=4 students have taken some class, and the class had a midterm exam and a final exam. You have collected a dataset of their scores on the two exams, which is as follows:**

midterm exam | $(midterm \ exam)^2$ | final exam
---|------|----
89 | 7921 | 96
72 | 5184 | 74
94 | 8836 | 87
69 | 4761 | 78

**You'd like to use polynomial regression to predict a student's final exam score from their midterm exam score. Concretely, suppose you want to fit a model of the form $h_{\theta}(x) = \theta_0 + \theta_1 x_1 + \theta_2 x_2$, where $x_1$ is the midterm score and $x_2$ is $(midterm \ score)^2$. Further, you plan to use both feature scaling (dividing by the "max-min", or range, of a feature) and mean normalization.**

**What is the normalized feature $x_1^{(1)}$? (Hint: midterm = 89, final = 96 is training example 1.) Please round off your answer to two decimal places and enter in the text box below.**

**$Normalized \ x_1^{(1)} = \frac{89 - \mu_1}{s_1} = \frac{89 - \frac{89 + 72 + 94 + 69}{4}}{94 - 69} = 0.32$**

----

**2. You run gradient descent for 15 iterations with $\alpha = 0.3$ and compute $J(\theta)$ after each iteration. You find that the value of $J(\theta)$ increases over time. Based on this, which of the following conclusions seems most plausible?**

A. Rather than use the current value of $\alpha$, it'd be more promising to try a larger value of $\alpha$ (say $\alpha = 1.0$).

**B. Rather than use the current value of $\alpha$ , it'd be more promising to try a smaller value of $\alpha$ (say $\alpha = 0.1$).**

C. $\alpha = 0.3$ is an effective choice of learning rate.

----

**3. Suppose you have $m = 28$ training examples with $n = 4$ features (excluding the additional all-ones feature for the intercept term, which you should add). The normal equation is $\theta = (X^T X)^{-1} X^T y$. For the given values of mm and nn, what are the dimensions of $\theta$, $X$, and $y$ in this equation?**

**A. $X$ is 28 x 5, $y$ is 28 x 1, $\theta$ is 5 x 1**

B. $X$ is 28 x 4, $y$ is 28 x 1, $\theta$ is 4 x 1

C. $X$ is 28 x 5, $y$ is 28 x 5, $\theta$ is 5 x 5

D. $X$ is 28 x 4, $y$ is 28 x 1, $\theta$ is 4 x 4

----

**4. Suppose you have a dataset with $m = 1000000$ examples and $n = 200000$ features for each example. You want to use multivariate linear regression to fit the parameters $\theta$ to our data. Should you prefer gradient descent or the normal equation?**

A. Gradient descent, since it will always converge to the optimal $\theta$.

**B. Gradient descent, since $(X^TX)^{-1}$ will be very slow to compute in the normal equation.**

C. The normal equation, since it provides an efficient way to directly find the solution.

D. The normal equation, since gradient descent might be unable to find the optimal $\theta$.

----

**5. Which of the following are reasons for using feature scaling?**

**A. It speeds up gradient descent by making it require fewer iterations to get to a good solution.**

B. It prevents the matrix $X^TX$ (used in the normal equation) from being non-invertable (singular/degenerate).

C. It speeds up solving for $\theta$ using the normal equation.

D. It is necessary to prevent gradient descent from getting stuck in local optima.
