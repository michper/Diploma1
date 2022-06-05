import matplotlib.pyplot as plt
import test as test
from scipy.misc import imread
import matplotlib.cbook as cbook

def plotTSP(path, points, num_iters=1):
    """
    path: List of lists with the different orders in which the nodes are visited
    points: coordinates for the different nodes
    num_iters: number of paths that are in the path list

    """

    # Unpack the primary TSP path and transform it into a list of ordered
    # coordinates

    x = [];
    y = []
    for i in path[0]:
        x.append(points[i][0])
        y.append(points[i][1])

    # plt.plot(x, y, 'co')
    #
    # Set a scale for the arrow heads (there should be a reasonable default for this, WTF?)
    a_scale = float(max(x)) / float(100)

    # Draw the older paths, if provided
    if num_iters > 1:

        for i in range(1, num_iters):

            # Transform the old paths into a list of coordinates
            xi = [];
            yi = [];
            for j in path[i]:
                xi.append(points[j][0])
                yi.append(points[j][1])

            plt.arrow(xi[-1], yi[-1], (xi[0] - xi[-1]), (yi[0] - yi[-1]),
                      head_width=a_scale, color='r',
                      length_includes_head=True, ls='dashed',
                      width=0.0001 / float(num_iters))
            for i in range(0, len(x) - 1):
                plt.arrow(xi[i], yi[i], (xi[i + 1] - xi[i]), (yi[i + 1] - yi[i]),
                          head_width=a_scale, color='r', length_includes_head=True,
                          ls='dashed', width=0.0001 / float(num_iters))


    for i in range(0, len(x) - 1):
        plt.arrow(x[i], y[i], (x[i + 1] - x[i]), (y[i + 1] - y[i]), head_width=a_scale,
                  color='#ff6600', width=5, length_includes_head=True )

    # Set axis too slitghtly larger than the set of x and y
    plt.xlim(0, 1180)
    plt.ylim(0, 760)
    datafile = cbook.get_sample_data(r"C:\Users\Michal\Desktop\PracaInzV2\mapa.png")
    img = imread(datafile)
    plt.scatter(x, y, zorder=1)
    plt.imshow(img, zorder=0, extent=[0, 1180, 0, 760])
    plt.show()


if __name__ == '__main__':

    x_cor = [553, 552, 462, 462, 642, 642, 688, 688, 723, 734, 726, 743, 793, 817, 845, 799, 846, 863, 861, 887, 896, 888, 910, 932, 963, 970, 1023, 1077, 1069, 1055, 1030, 1023, 1021, 1001, 982, 995, 978, 981, 1004, 962, 942, 919, 925, 921, 942, 887, 908, 920, 918, 906, 859, 885, 901, 923, 938, 953, 954, 970, 988, 1028, 1030, 1013, 998, 953, 842, 945, 823, 814, 771, 747, 731, 729, 756, 794, 831, 836, 793, 865, 852, 782, 811, 744, 722, 721, 691, 702, 686, 644, 689, 689, 733, 729, 562, 566, 487, 494, 501, 532, 569, 588, 592, 568, 643, 516, 486, 476, 462, 462, 443, 409, 394, 387, 365, 309, 260, 203, 146, 213, 287, 398, 417, 400, 376, 339, 337, 312, 305, 389, 553, 688, 1002, 462, 552, 552, 602, 174, 644, 730, 690]
    y_cor = [82, 116, 116, 238, 239, 117, 114, 211, 213, 202, 134, 117, 118, 193, 109, 285, 184, 252, 282, 291, 158, 139, 98, 84, 84, 58, 46, 70, 132, 211, 229, 265, 329, 347, 326, 302, 268, 242, 161, 138, 186, 194, 244, 270, 243, 308, 311, 327, 342, 374, 451, 476, 548, 555, 559, 559, 527, 417, 402, 431, 510, 562, 562, 586, 627, 598, 597, 535, 538, 520, 533, 479, 459, 430, 439, 489, 411, 326, 305, 323, 388, 384, 378, 413, 450, 431, 415, 423, 551, 580, 577, 549, 438, 478, 447, 508, 420, 428, 422, 404, 383, 359, 352, 356, 375, 397, 357, 409, 447, 458, 486, 528, 551, 581, 534, 533, 637, 636, 616, 240, 365, 312, 117, 119, 160, 120, 140, 190, 82, 240, 122, 177, 239, 280, 429, 582, 300, 506, 500]


    points = []
    for i in range(0, len(x_cor)):
        points.append((x_cor[i], y_cor[i]))

    print(points)

    path1 = test.getRoute([])
    print(path1)
    # Pack the paths into a list
    paths = [path1]

    plotTSP(paths, points, 1)
