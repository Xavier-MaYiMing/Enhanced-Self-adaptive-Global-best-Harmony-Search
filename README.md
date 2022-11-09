### Enhanced Self-adaptive Global-best Harmony Search

##### Reference: Kaiping Luo, Jie Ma, Qiuhong Zhao. Enhanced self-adaptive global-best harmony search without any extra statistic and external archive. Information Sciences, 2019. 482: 228-247.

| Variables | Meaning                                           |
| --------- | ------------------------------------------------- |
| hms       | Harmony memory size                               |
| ni        | The number of improvisations (iterations)         |
| hmcr      | Harmony memory consideration rate                 |
| par       | Pitch adjustment rate                             |
| bw        | Bandwidth                                         |
| lb        | The lower bound (list)                            |
| ub        | The upper bound (list)                            |
| pos       | The set of harmonies (list)                       |
| score     | The score of harmonies (list)                     |
| dim       | Dimension (list)                                  |
| gbest     | The score of the global best harmony              |
| gbest_pos | The position of the global best harmony (list)    |
| iter_best | The global best score of each iteration (list)    |
| con_iter  | The last iteration number when "gbest" is updated |

#### Test problem: Pressure vessel design

![](C:\Users\dell\Desktop\研究生\个人算法主页\Grey Wolf Optimizer\Pressure vessel design.png)
$$
\text{min}\ f(x)=0.6224x_1x_3x_4+1.7781x_2x_3^2+3.1661x_1^2x_4+19.84x_1^2x_3,\\
\text{s.t.} -x_1+0.0193x_3\leq0,\\
-x_3+0.0095x_3\leq0,\\
-\pi x_3^2x_4-\frac{4}{3}\pi x_3^3+1296000\leq0,\\
x_4-240\leq0,\\
0\leq x_1\leq99,\\
0\leq x_2 \leq99,\\
10\leq x_3 \leq 200,\\
10\leq x_4 \leq 200.
$$


#### Example

```python
if __name__ == '__main__':
    # Parameter settings
    hms = 10
    lb = [0, 0, 10, 10]
    ub = [99, 99, 200, 200]
    ni = 10000 * len(lb)
    print(main(hms, ni, lb, ub))
```

##### Output:

![convergence curve](C:\Users\dell\Desktop\研究生\个人算法主页\Enhanced Self-adaptive Global-best Harmony Search\convergence curve.png)

The ESGHS converges at its 14,294-th iteration, and the global best value is 8050.914044830637. 

```python
{
    'best score': 8050.914044830637, 
    'best solution': [1.3005502310626382, 0.6428626530744853, 67.38602233485172, 10.000000182456352], 
    'convergence iteration': 14294
}
```

