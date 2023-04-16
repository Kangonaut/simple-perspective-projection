# Simple Perspective Projection

## Basic Operations

### Scaling

$$
\mathbf{S} =
\begin{bmatrix}
s_x & 0 & 0 & 0 \\
0 & s_y & 0 & 0 \\
0 & 0 & s_z & 0 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}

\cdot

\begin{bmatrix}
x \\
y \\
z \\
1 \\
\end{bmatrix}
$$

### Rotation

#### Rotation around the $x$-Axis

- the $x$-coordinate is unchanged and doesn’t influence the result
- the $y$ and $z$ components are projected onto the rotated basis vectors
  - $\mathbf{\hat{i}}$ is simply rotated by $\theta$
  - $\mathbf{\hat{j}}$ can be determined by rotating $\mathbf{\hat{i}}$ by $90°$

$$
\mathbf{\hat{i}} =
\begin{bmatrix}
cos(\theta) \\
sin(\theta)
\end{bmatrix},
\space
\mathbf{\hat{j}} =
\begin{bmatrix}
-sin(\theta) \\
cos(\theta)
\end{bmatrix}
$$

- thus the resulting rotation matrix is:

$$
\mathbf{R}_x = 
\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & cos(\theta) & -sin(\theta) & 0 \\
0 & sin(\theta) & cos(\theta) & 0 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}

\cdot

\begin{bmatrix}
x \\
\mathbf{y} \\
\mathbf{z} \\
1 \\
\end{bmatrix}
$$

#### Rotation around the $y$-Axis

$$
\mathbf{R}_y =
\begin{bmatrix}
cos(\theta) & 0 & -sin(\theta) & 0 \\
0 & 1 & 0 & 0 \\
sin(\theta) & 0 & cos(\theta) & 0 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}

\cdot

\begin{bmatrix}
\mathbf{x} \\
y \\
\mathbf{z} \\
1 \\
\end{bmatrix}
$$



#### Rotation around the $z$-Axis

$$
\mathbf{R}_y =
\begin{bmatrix}
cos(\theta) & -sin(\theta) & 0 & 0 \\
sin(\theta) & cos(\theta) & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}

\cdot

\begin{bmatrix}
\mathbf{x} \\
\mathbf{y} \\
z \\
1 \\
\end{bmatrix}
$$

### Translation

- translation is done by performing a **shear transformation** in the $4^{th}$ dimension of the homogeneous coordinate system

- to do this, we project our point onto the modified basis vector of the $4^{th}$ dimension

$$
\mathbf{T} =
\begin{bmatrix}
1 & 0 & 0 & t_x \\
0 & 1 & 0 & t_y \\
0 & 0 & 1 & t_z \\
0 & 0 & 0 & 1 \\
\end{bmatrix}

\cdot

\begin{bmatrix}
x \\
y \\
z \\
\mathbf{1} \\
\end{bmatrix}
$$

