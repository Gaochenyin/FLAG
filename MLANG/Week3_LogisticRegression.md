# Logistic Regression

----

**1. Suppose that you have trained a logistic regression classifier, and it outputs on a new example xx a prediction $h_\theta(x)$= 0.7. This means (check all that apply):**

A. Our estimate for $P(y = 1|x; \theta)$ is 0.3.

B. Our estimate for $P(y = 0|x; \theta)$ is 0.7.

**C. Our estimate for $P(y = 1|x; \theta)$ is 0.7.**

**D. Our estimate for $P(y = 0|x; \theta)$ is 0.3.**

----

**2. Suppose you have the following training set, and fit a logistic regression classifier $h_{\theta}(x) = g(\theta_0 + \theta x_1 + \theta_2 x_2)$**.

![2-1](https://d18ky98rnyall9.cloudfront.net/vDH1Eb5xEeSVRiIAC2sM-Q_Screen-Shot-2015-02-27-at-3.09.52-AM.png?Expires=1533859200&Signature=H9vXo49Vsi8rDs8xvKYk93GaNH1ZNxv-AK5OK2Sc1TZrK~vKJl4VKzBl9~cepgs1JOALBf1Ey1SkbeyoWEx5rv26kpFRKaz4D3RJpkdRZ~qtZNBISyaQ8P8xRcRIcvXWLZfw36ZGJ4QoRBzMknZe8QGrr~oCA4c8ZmDtkBvM8lM_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)

![2-2](https://d18ky98rnyall9.cloudfront.net/x6wwkr5xEeSVRiIAC2sM-Q_Screen-Shot-2015-02-27-at-3.10.20-AM.png?Expires=1533859200&Signature=hwUKU4aN~Fa-dPCMLZFucFtanvTAvQg6OP5~WVRtmm8zz0NWC~kIdLGFH9VYzYHC8cNN3ly7PSWzO~IrknyhePJk1xPd~xKjT4aj3wPLZ9g1m2wWuqT64m9u3Yf0mcQdfCAhZNNoDNYagX9pmxIBFFgzD5ifcIP9YaSNdONzklg_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)

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

A. ![5-1](https://d18ky98rnyall9.cloudfront.net/vQ1aWL7jEeSZtCIACx4DqA_Screen-Shot-2015-02-27-at-2.32.48-PM.png?Expires=1533859200&Signature=C8OCHMrIpew3kpjcjWwqOCgPv7KTZdVdHbJQ3UYlCz3VQ4-wWRFTUZqG9tGJA1C7RmsOcMoCWNzTpmaxdl79HczPEmrE9iYoGx3Qazwt-dUV8fbAO8BBh863PFfmoFhjG22CFXNhYoDykKU2FmRAZV-2LQY62HbX-swirgA79gc_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)

B. ![5-2](https://d18ky98rnyall9.cloudfront.net/3-XyOb7jEeSZtCIACx4DqA_Screen-Shot-2015-02-27-at-2.34.53-PM.png?Expires=1533859200&Signature=bnpdboJzICF7xJ3zzpo-LwMIvT3LwgsHnhiP9PisEGinZtd3ZuOE3rbcBzuUVO3Ba6M2U~ZWSPn34f30pdZVaicxAShMgOkCz8l7YTCVf2yrVffj7PMOvryY57W8l5lCmUw34menJO358j6e6fouydoZvg4OQ3qF81z0Yv3eq~E_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)

C. ![5-3](https://d18ky98rnyall9.cloudfront.net/8Lxmyr7jEeSZtCIACx4DqA_Screen-Shot-2015-02-27-at-2.51.03-PM.png?Expires=1533859200&Signature=UIbDzPzRROf4jWgDRUTOsFoAbextlVE62o0uigGJR7PjqQQj9LDrFothvyFV4jL2RKHcm9V-CASasJm7HXb7fTZ8TUHQIvCFYvlTp8~PglmylC5V~XWlJUSL0zCiC0KA0ZiLr633UcU-3srDET5Gj9xNk1n5GKfnKd1-LJ0-UzI_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)

**D**. ![5-4](https://d18ky98rnyall9.cloudfront.net/8HjYsb7kEeSZtCIACx4DqA_Screen-Shot-2015-02-27-at-2.53.08-PM.png?Expires=1533859200&Signature=czUqcDGk77BPh0foQkL~i5Mfs9H4fhStz5GjqiNVT5i4QsBrbsmRGTsI6AiTTFLLMxFfMUCOKetNCQSJYjuPN1i1JBMb4uOkfCWWjCJlZOPmI0FV5-3CHYDgiNq5ZdF0zCpVRQO4hm3ZH811XmweMePIFUHLAj8rETrkObEZOpw_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)
