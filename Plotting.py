import matplotlib
import matplotlib.style
from matplotlib import pyplot as plt
import numpy as np
from pygame import color

matplotlib.style.use('ggplot')

ASTAR = "A star"
REIN = "Reinforcement Learning"
XLABEL = 'path length'
YLABEL = 'execution time'

def plot_astar_vs_reinforcement_1():

    #Environment 1
    plt.figure(figsize=(10,5))
    path_length = [18,18, 16, 18, 5]

    astar_time = [0.005982398986816406, 0.023934602737426758, 0.005980730056762695, 0.015931129455566406, 0.0009975433349609375]
    plt.plot(path_length, astar_time, label = ASTAR)
    
    reinforcement_time = [0.0, 0.0, 0.0009648799896240234,0.0009634494781494141,0.0]
    plt.plot(path_length, reinforcement_time, label = REIN)
    
    plt.xlabel(XLABEL)
    plt.ylabel(YLABEL)
    plt.title('Path Length Vs Execution Time of Astar and Reinforcement Learning in Environment 1')
    
    plt.legend()    
    plt.show()

def plot_astar_vs_reinforcement_2():

    #Environment 2
    plt.figure(figsize=(10,5))
    path_length = [21,21, 0, 0, 6]

    astar_time = [0.012962579727172852, 0.009973287582397461, 0.0019948482513427734, 0.000997304916381836, 0.0009968280792236328]
    plt.plot(path_length, astar_time, label = ASTAR)
    
    reinforcement_time = [0.0009593963623046875, 0.0010006427764892578, 0.0, 0.0,0.0]
    plt.plot(path_length, reinforcement_time, label = REIN)
    
    plt.xlabel(XLABEL)
    plt.ylabel(YLABEL)
    plt.title('Path Length Vs Execution Time of Astar and Reinforcement Learning in Environment 2')
    
    plt.legend()    
    plt.show()

def plot_astar_vs_reinforcement_3():

    #Environment 3
    plt.figure(figsize=(10,5))
    path_length = [24,17, 24, 11, 7]

    astar_time = [0.009972810745239258, 0.009972333908081055, 0.021940946578979492, 0.004019975662231445, 0.0009996891021728516]
    plt.plot(path_length, astar_time, label = ASTAR)
    
    reinforcement_time = [0.000997304916381836, 0.0, 0.0,0.0009591579437255859,0.0]
    plt.plot(path_length, reinforcement_time, label = REIN)
    
    plt.xlabel(XLABEL)
    plt.ylabel(YLABEL)
    plt.title('Path Length Vs Execution Time of Astar and Reinforcement Learning in Environment 3')

    plt.legend()    
    plt.show()

def plot_astar_vs_reinforcement_4():

    #Environment 4
    plt.figure(figsize=(10,5))
    path_length = [29,28, 28, 29, 21, 28]

    astar_time = [0.009014606475830078, 0.010007858276367188, 0.010968923568725586, 0.01692676544189453, 0.0019931793212890625, 0.006978511810302734]
    plt.plot(path_length, astar_time, label = ASTAR)
    
    reinforcement_time = [0.0009791851043701172, 0.0010030269622802734, 0.000997781753540039, 0.0005519390106201172, 0.0009996891021728516, 0.0009984970092773438]
    plt.plot(path_length, reinforcement_time, label = REIN)
    
    plt.xlabel(XLABEL)
    plt.ylabel(YLABEL)
    plt.title('Path Length Vs Execution Time of Astar and Reinforcement Learning in Environment 4')

    plt.legend()    
    plt.show()

def plot_astar_vs_treinforcement_1():

    #Environment 1
    plt.figure(figsize=(10,5))
    path_length = [18,18, 16, 18, 5]

    astar_time = [0.005982398986816406, 0.023934602737426758, 0.005980730056762695, 0.015931129455566406, 0.0009975433349609375]
    plt.plot(path_length, astar_time, label = ASTAR)
    
    reinforcement_time = [10.016407489776611, 9.687103033065796, 8.175344944000244, 8.388458728790283, 2.4893951416015625]
    plt.plot(path_length, reinforcement_time, label = REIN)
    
    plt.xlabel(XLABEL)
    plt.ylabel(YLABEL)
    plt.title('Path Length Vs Total Execution Time of Astar and Reinforcement Learning in Environment 1')
    
    plt.legend()    
    plt.show()

def plot_astar_vs_treinforcement_2():

    #Environment 2
    plt.figure(figsize=(10,5))
    path_length = [21,21, 0, 0, 6]

    astar_time = [0.012962579727172852, 0.009973287582397461, 0.0019948482513427734, 0.000997304916381836, 0.0009968280792236328]
    plt.plot(path_length, astar_time, label = ASTAR)
    
    reinforcement_time = [9.925861835479736, 8.535706281661987, 23.427186250686646, 20.250776767730713, 2.8344390392303467]
    plt.plot(path_length, reinforcement_time, label = REIN)
    
    plt.xlabel(XLABEL)
    plt.ylabel(YLABEL)
    plt.title('Path Length Vs Total Execution Time of Astar and Reinforcement Learning in Environment 2')
    
    plt.legend()    
    plt.show()

def plot_astar_vs_treinforcement_3():

    #Environment 3
    plt.figure(figsize=(10,5))
    path_length = [24,17, 24, 11, 7]

    astar_time = [0.009972810745239258, 0.009972333908081055, 0.021940946578979492, 0.004019975662231445, 0.0009996891021728516]
    plt.plot(path_length, astar_time, label = ASTAR)
    
    reinforcement_time = [8.540255546569824, 7.262346506118774, 9.241945028305054, 4.803429126739502, 2.929039478302002]
    plt.plot(path_length, reinforcement_time, label = REIN)
    
    plt.xlabel(XLABEL)
    plt.ylabel(YLABEL)
    plt.title('Path Length Vs Total Execution Time of Astar and Reinforcement Learning in Environment 3')

    plt.legend()    
    plt.show()

def plot_astar_vs_treinforcement_4():

    #Environment 4
    plt.figure(figsize=(10,5))
    path_length = [29,28, 28, 29, 21, 28]

    astar_time = [0.009014606475830078, 0.010007858276367188, 0.010968923568725586, 0.01692676544189453, 0.0019931793212890625, 0.006978511810302734]
    plt.plot(path_length, astar_time, label = ASTAR)
    
    reinforcement_time = [7.5931618213653564, 7.51235032081604, 7.537204265594482, 7.179185152053833, 6.327882528305054, 7.509089231491089]
    plt.plot(path_length, reinforcement_time, label = REIN)
    
    plt.xlabel(XLABEL)
    plt.ylabel(YLABEL)
    plt.title('Path Length Vs Total Execution Time of Astar and Reinforcement Learning in Environment 4')

    plt.legend()    
    plt.show()

def plot_average_astar_vs_reinforcement():

    #Environment 4
    plt.figure(figsize=(10,5))

    x_label = ['1','2','3','4']
    arrange = np.arange(4)
    width = 0.3

    astar_time = [0.010565280914307, 0.005384969711304, 0.009381151199341, 0.009314974149068]
    reinforcement_time = [ 0.0003856658935547, 0.0003920078277588, 0.0003912925720215, 0.0009216864903768]
        
    plt.bar(arrange,  astar_time, color = "b", width = width, edgecolor = 'black', label = ASTAR)
    plt.bar(arrange + width, reinforcement_time, color = "r", width = width, edgecolor = 'black', label = REIN)
    
    plt.xticks(arrange + width / 2, x_label)
    
    plt.xlabel("Environments")
    plt.ylabel("Average Execution Time")
    plt.title('Average Execution Time of Astar and Proposed Solution in Environments')

    plt.legend()    
    plt.show()

def plot_average_astar_vs_treinforcement():

    #Environment 4
    plt.figure(figsize=(10,5))

    x_label = ['1','2','3','4']
    arrange = np.arange(4)
    width = 0.3

    astar_time = [0.010565280914307, 0.005384969711304, 0.009381151199341, 0.009314974149068]
    reinforcement_time = [7.7513418674469, 12.994794034958, 6.555403137207, 7.2764788866043]
        
    # plt.bar(arrange,  astar_time, color = "b", width = width, edgecolor = 'black', label = ASTAR)
    # plt.bar(arrange + width, reinforcement_time, color = "r", width = width, edgecolor = 'black', label = REIN)
    
    plt.plot(x_label, astar_time, color ='b', label = ASTAR)
    plt.plot(x_label, reinforcement_time, color = 'r', label = REIN)

    # plt.xticks(arrange + width / 2, x_label)
    
    plt.xlabel("Environments")
    plt.ylabel("Average Execution Time")
    plt.title('Average Execution Time of Astar and Reinforcement Learning in Environments')

    plt.legend()    
    plt.show()

plot_astar_vs_reinforcement_1()
plot_average_astar_vs_reinforcement()