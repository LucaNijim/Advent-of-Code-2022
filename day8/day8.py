import numpy as np


def first_val_greater(arr, val):
    for index, x in np.ndenumerate(arr):
        if x >= val:
            return index[0] + 1
    return len(arr)


def string_to_forest(list_of_strings):
    dim = len(list_of_strings)
    forest = np.zeros(shape=(dim, dim), dtype=int)
    for indexrow in np.arange(dim):
        for indexcolumn in np.arange(dim):
            forest[indexrow, indexcolumn] = list_of_strings[indexrow][indexcolumn]
    return forest


def num_trees_visible(forest):
    visible_counter = 0
    for indexrow in range(forest.shape[0]):
        for indexcolumn in range(forest.shape[1]):
            if indexrow == 0 or indexrow == forest.shape[0] - 1 or indexcolumn == 0 or indexcolumn == forest.shape[
                    1] - 1:
                visible_counter += 1
            else:
                tree_height = forest[indexrow, indexcolumn]
                if tree_height > np.max(forest[:indexrow, indexcolumn]) or tree_height > np.max(
                        forest[indexrow + 1:, indexcolumn]) or tree_height > np.max(
                        forest[indexrow, :indexcolumn]) or tree_height > np.max(forest[indexrow, indexcolumn + 1:]):
                    visible_counter += 1

    return visible_counter


def max_vis_score(forest):
    vis_score = np.zeros_like(forest)

    for index, x in np.ndenumerate(forest):
        vis_dist_list = [first_val_greater(forest[index[0], index[1] + 1:].reshape(-1), x),
                         first_val_greater(np.flip(forest[index[0], :index[1]]).reshape(-1), x),
                         first_val_greater(forest[index[0] + 1:, index[1]].reshape(-1), x),
                         first_val_greater(np.flip(forest[:index[0], index[1]]).reshape(-1), x)]
        vis_score[index] = vis_dist_list[0] * vis_dist_list[1] * vis_dist_list[2] * vis_dist_list[3]

    return np.max(vis_score)


def main():
    list_of_strings = open('day8input.txt').readlines()
    forest = string_to_forest(list_of_strings)
    print(num_trees_visible(forest))
    print(max_vis_score(forest))


if __name__ == '__main__':
    main()