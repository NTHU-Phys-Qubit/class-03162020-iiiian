import numpy as np
import matplotlib.pyplot as plt


def ran_walk_continue(steps, n):
    ans = np.zeros((n,))
    for i in range(n):
        ran = np.random.random((steps,))
        ran = ran - 0.5
        final_place = np.sum(ran)
        ans[i] = final_place
    return ans


ans1 = ran_walk_continue(1000, 10000)
plt.hist(ans1, bins=50)
plt.show()


def ran_walk_discrete(steps, n):
    ans = np.zeros((n,))
    for i in range(n):
        ran = np.random.randint(2, size=steps)
        ran = ran - 0.5
        final_place = np.sum(ran)
        ans[i] = final_place
    return ans


ans2 = ran_walk_discrete(1000, 10000)
plt.hist(ans1, bins=50)
plt.show()


def rand_walk_2d(steps, n):
    ans_x = np.zeros((n,))
    ans_y = np.zeros((n,))

    for i in range(n):
        ran = np.random.random((steps,))
        ran = ran * 2 * np.pi
        x = np.sin(ran)
        y = np.cos(ran)
        ans_x[i] = np.sum(x)
        ans_y[i] = np.sum(y)

    ans = np.array([ans_x, ans_y])
    return ans


ans3 = rand_walk_2d(1000, 10000)
plt.hist2d(ans3[0], ans3[1], bins=50)
plt.colorbar()
plt.show()
