import matplotlib.pyplot as plt

from random_walk import RandomWalk
while True:
    rw = RandomWalk(5000)
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))

    plt.figure(figsize=(10, 6))
    plt.plot(rw.x_values , rw.y_values , linewidth = 1)
    plt.scatter(0 , 0 , c='red' , s = 10)
    plt.scatter(rw.x_values[-1] , rw.y_values[-1] , c = 'green' , s=10)
    plt.title('Pollen grain movement on water surface' , fontsize = 15)
    
    plt.axis('off')
    # ax.get_xaxis().set_visible(False)
    # ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another Walk? (y/n): ")
    if keep_running == 'n':
        break