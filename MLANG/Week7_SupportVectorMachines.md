# Support Vector Machines

----

**1. Suppose you have trained an SVM classifier with a Gaussian kernel, and it learned the following decision boundary on the training set:**

![1](http://spark-public.s3.amazonaws.com/ml/images/12.1-b.jpg)

When you measure the SVM's performance on a cross validation set, it does poorly. Should you try increasing or decreasing $C$? Increasing or decreasing $\sigma^2$

A. It would be reasonable to try **increasing** $C$. It would also be reasonable to try **increasing** $\sigma^2$

**B**. It would be reasonable to try **decreasing** $C$. It would also be reasonable to try **increasing** $\sigma^2$

C. It would be reasonable to try **decreasing** $C$. It would also be reasonable to try **decreasing** $\sigma^2$

D. It would be reasonable to try **increasing** $C$. It would also be reasonable to try **decreasing** $\sigma^2$

----

**2. The formula for the Gaussian kernel is given by $similarity (x,l^{(1)})=exp(-\frac{\left \| x-l^{(1)} \right \|^{2}}{2\sigma^{2} })$**

**The figure below shows a plot of $f_1 = similarity{(x, l^{(1)})}$ when $\sigma^2 = 1$**

![2](http://spark-public.s3.amazonaws.com/ml/images/12.2-question.jpg)

**Which of the following is a plot of $f_1$ when $\sigma^2 = 0.25$?**

A. ![2-1](http://spark-public.s3.amazonaws.com/ml/images/12.2-a.jpg)

**B**. ![2-2](http://spark-public.s3.amazonaws.com/ml/images/12.2-b.jpg)

C. ![2-3](http://spark-public.s3.amazonaws.com/ml/images/12.2-c.jpg)

D. ![2-4](http://spark-public.s3.amazonaws.com/ml/images/12.2-d.jpg)

----

**3. The SVM solves**

$$min_{\theta} \ C \sum{^m_{i=1}}y^{(i)}cost{_1}(\theta^{T}x^{(i)})+(1-y^{(i)})cost_{0}(\theta^{T}x^{(i)})+\sum{^{n}_{j=1}}\theta{{^2_j}}$$

where the functions $\text{cost}_0(z)$ and $\text{cost}_1(z)$ look like this:

![3](http://spark-public.s3.amazonaws.com/ml/images/12.3.jpg)

The first term in the objective is:

$$C \sum{^m_{i=1}}y^{(i)}cost{_1}(\theta^{T} x^{(i)})+(1-y^{(i)})cost_{0}(\theta^{T}x^{(i)})$$

This first term will be zero if two of the following four conditions hold true. Which are the two conditions that would guarantee that this term equals zero?

A. For every example with $y^{(i)} = 0$, we have that $\theta^{T}x^{(i)} \leqslant 0$.

B. For every example with $y^{(i)} = 1$, we have that $\theta^{T}x^{(i)} \geqslant 0$.

**C. For every example with $y^{(i)} = 0$, we have that $\theta^{T}x^{(i)} \leqslant -1$.**

**D. For every example with $y^{(i)} = 1$, we have that $\theta^{T}x^{(i)} \geqslant 1$.**

----

**4. Suppose you have a dataset with n = 10 features and m = 5000 examples.**

**After training your logistic regression classifier with gradient descent, you find that it has underfit the training set and does not achieve the desired performance on the training or cross validation sets.**

**Which of the following might be promising steps to take? Check all that apply.**

A. Use an SVM with a linear kernel, without introducing new features.

**B. Create / add new polynomial features.**

**C. Use an SVM with a Gaussian Kernel.**

D. Increase the regularization parameter $\lambda$.

----

**5. Which of the following statements are true? Check all that apply.**

A. If you are training multi-class SVMs with the one-vs-all method, it is not possible to use a kernel.

**B. The maximum value of the Gaussian kernel (i.e., $sim(x, l^{(1)})$) is 1.**

**C. Suppose you have 2D input examples (ie, $x^{(i)} \in \mathbb {R}^2$). The decision boundary of the SVM (with the linear kernel) is a straight line.**

D. If the data are linearly separable, an SVM using a linear kernel will return the same parameters $\theta$ regardless of the chosen value of $C$ (i.e., the resulting value of $\theta$ does not depend on $C$).
