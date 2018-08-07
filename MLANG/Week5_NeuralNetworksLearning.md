# Neural Networks: Learning

----

**1. You are training a three layer neural network and would like to use backpropagation to compute the gradient of the cost function. In the backpropagation algorithm, one of the steps is to update**

$\Delta^{(2)}_{ij}:=\Delta^{(2)}_{ij}+\delta^{(3)}_{i}*(a^{(2)})_{j}$

**for every $i$, $j$. Which of the following is a correct vectorization of this step?**

A. $\Delta^{(2)}:=\Delta^{(2)} + \delta^{(3)} * {(a^{(2)})}^T$

B. $\Delta^{(2)}:=\Delta^{(2)} + \delta^{(3)} * {(a^{(3)})}^T$

C. $\Delta^{(2)}:=\Delta^{(2)} + {(a^{(2)})}^T * \delta^{(3)}$

D. $\Delta^{(2)}:=\Delta^{(2)} + {(a^{(3)})}^T * \delta^{(2)}$

----

**2. Suppose $Theta1$ is a 5x3 matrix, and $Theta2$ is a 4x6 matrix. You set $thetaVec = [Theta1(:); Theta2(:)]$. Which of the following correctly recovers $Theta2$?** 

A. reshape(thetaVec(16 : 39), 4, 6)

B. reshape(thetaVec(15 : 38), 4, 6)

C. reshape(thetaVec(16 : 24), 4, 6)

D. reshape(thetaVec(15 : 39), 4, 6)

E. reshape(thetaVec(16 : 39), 4, 6)

----

**3. Let $J(\theta) = 3\theta^4 + 4$. Let $\theta = 1$, and $\epsilon = 0.01$. Use the formula $\frac{J(\theta + \epsilon) - J(\theta - \epsilon)}{2\epsilon}$ to numerically compute an approximation to the derivative at $\theta = 1$. What value do you get?(When $\theta$ = 1, the true/exact derivative is $\frac{}{}$)**

A. 

B. 

C. 

D. 

----

**4. **

A. 

B. 

C. 

D. 

----

**5. **

A. 

B. 

C. 

D. 
