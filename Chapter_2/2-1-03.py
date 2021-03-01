a = [242, 256, 237, 223, 263, 81, 46]
print('A =', a)

import matplotlib.pyplot as plt

x_data = ['MON', 'TUE', 'WED', 'THR', 'FRI', 'SAT', 'SUN']
# 그래프에 제목 붙이기
plt.title('Floating Population Weekly', fontsize = 16)
plt.xlabel('Floating Population', fontsize = 12)
plt.ylabel('Day', fontsize=12)
# 꺾은선 그래프 그리기
plt.scatter(x_data, a)
plt.plot(x_data, a)
plt.show()
