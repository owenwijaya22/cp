 from matplotlib import pyplot as plt
def make_int(lists):
    return list(map(float, lists))
    
t_cos_theta = make_int([input("t cos(\u03F4): ") for _ in range(int(input("How many values: ")))])
x_minus_x0 = make_int([input("x-x0: ") for _ in range(int(input("How many values: ")))])

x = range(len(x_minus_x0))
y = range(len(t_cos_theta))


plt.xticks(x, x_minus_x0)
# plt.yticks(y, t_cos_theta)

plt.plot(x, t_cos_theta)
plt.show()