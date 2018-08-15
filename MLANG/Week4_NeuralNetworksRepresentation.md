# Neural Networks: Representation

----

**1. Which of the following statements are true? Check all that apply.**

A. A two layer (one input layer, one output layer; no hidden layer) neural network can represent the XOR function.

B. Suppose you have a multi-class classification problem with three classes, trained with a 3 layer network. Let $a^{(3)}_1 = (h_{\theta}(x))_1$ be the activation of the first output unit, and similarly $a^{(3)}_2 = (h_{\theta}(x))_2$ and $a^{(3)}_3 = (h_{\theta}(x))_3$. Then for any input $x$, it must be the case that $a^{(3)}_1 + a^{(3)}_2 + a^{(3)}_3 = 1$.

**C. Any logical function over binary-valued (0 or 1) inputs $x_1$ and $x_2$ can be (approximately) represented using some neural network.**

**D. The activation values of the hidden units in a neural network, with the sigmoid activation function applied at every layer, are always in the range (0, 1).**

----

**2. Consider the following neural network which takes two binary-valued inputs $x_1, x_2 \in \{0, 1\}$ and outputs $h_{\theta}{(x)}$. Which of the following logical functions does it (approximately) compute?**

![2](https://github.com/phdsky/FLAG/blob/master/MLANG/images/Week4_NeuralNetworksRepresentation/2.png)

**A. OR**

B. AND

C. NAND(meaning "NOT AND")

D. XOR(exclusive OR)

----

**3. Consider the neural network given below. Which of the following equations correctly computes the activation $a^{(3)}_1$? Note: $g(z)$ is the sigmoid activation function.**

![3](https://github.com/phdsky/FLAG/blob/master/MLANG/images/Week4_NeuralNetworksRepresentation/3.png)

**A**. $a^{(3)}_1 = g(\Theta^{(2)}_{1,0}a^{(2)}_0 + \Theta^{(2)}_{1,1}a^{(2)}_1 + \Theta^{(2)}_{1,2}a^{(2)}_2)$

B. $a^{(3)}_1 = g(\Theta^{(2)}_{1,0}a^{(1)}_0 + \Theta^{(2)}_{1,1}a^{(1)}_1 + \Theta^{(2)}_{1,2}a^{(1)}_2)$

C. $a^{(3)}_1 = g(\Theta^{(1)}_{1,0}a^{(2)}_0 + \Theta^{(1)}_{1,1}a^{(2)}_1 + \Theta^{(1)}_{1,2}a^{(2)}_2)$

D. $a^{(3)}_1 = g(\Theta^{(2)}_{2,0}a^{(2)}_0 + \Theta^{(2)}_{2,1}a^{(2)}_1 + \Theta^{(2)}_{2,2}a^{(2)}_2)$

----

**4. You have the following neural network:**

![4-1](https://github.com/phdsky/FLAG/blob/master/MLANG/images/Week4_NeuralNetworksRepresentation/4-1.png)

**You'd like to compute the activations of the hidden layer $a^{(2)} \in \mathbb R^3$**. One way to do so is the following Octave code:

![4-2](https://github.com/phdsky/FLAG/blob/master/MLANG/images/Week4_NeuralNetworksRepresentation/4-2.png)

**You want to have a vectorized implementation of this (i.e., one that does not use for loops). Which of the following implementations correctly compute $a^{(2)}$? Check all that apply.**

**A. z = Theta1 * x; a2 = sigmoid (z);**

B. a2 = sigmoid (x * Theta1);

C. a2 = sigmoid (Theta2 * x);

D. z = sigmoid(x); a2 = sigmoid (Theta1 * z);

----

**5. You are using the neural network pictured below and have learned the parameters $\Theta^{(1)} = \begin{bmatrix} 1 & 2.1 & 1.3 \\ 1 & 0.6 & -1.2\end{bmatrix}$(used to compute $a^{(2)}$) and $\Theta^{(2)} = \begin{bmatrix} 1 & 4.5 & 3.1\end{bmatrix}$(used to compute $a^{(3)}$ as a function of $a^{(2)}$). Supposed you swap the parameters for the first hidden layer between its two units so $\Theta^{(1)} = \begin{bmatrix} 1& 0.6 & -1.2 \\ 1 & 2.1 & 1.3\end{bmatrix}$ and also swap the output layer so $\Theta^{(2)} = \begin{bmatrix} 1 & 3.1 & 4.5 \end{bmatrix}$. How will this change the value of the output $h_{\theta}(x)$?**

![5](https://github.com/phdsky/FLAG/blob/master/MLANG/images/Week4_NeuralNetworksRepresentation/5.png)

**A. It will stay the same.**

B. It will increase.

C. It will decrease

D. Insufficient information to tell: it may increase or decrease.
