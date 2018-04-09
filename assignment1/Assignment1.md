# Assignment1

## SVM

### Loss Function

$$
L=\frac{1}{N}\sum_{i=1}^{N}L_i+\sum_kW_{k}^{2}
\\ L_i=\sum_{j\neq y_j}\max({0,s_j-s_{y_j}+\Delta})
\\ s = f(x;W) = Wx
\\L=\frac{1}{N}\sum_{i=1}^{N}\sum_{j\neq y_i}\max(0,w_jx_i-w_{y_i}x_i+\Delta) +\sum_{k}W_k^{2}
\\
$$

## Softmax

### Loss Function

$$
L=\frac{1}{N}\sum_{i=1}^{N}L_i+\sum_kW_{k}^{2}
\\
L_i =- f_{y_i}+\log\sum_{j}e^{f_j}
\\
f(x_i,W)=Wx_i
$$

