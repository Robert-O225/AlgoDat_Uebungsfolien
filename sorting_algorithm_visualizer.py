"""
Sorting Algorithm Visualizer

This module implements and visualizes the sorting algorithms
BubbleSort, InsertionSort, and SelectionSort. It provides an interactive
console interface that allows you to follow the algorithms' operation
step by step.

Included Functions:
- bubbleSort: Implementation of the BubbleSort algorithm.
- insertionSort: Implementation of the InsertionSort algorithm.
- selectionSort: Implementation of the SelectionSort algorithm.
- Worst-Case-Scenarion: Shows the worst-case scenarion for an algorithm
    - Input example: 2w -> Worst-case for InsertionSort
- Custom array input: The user can enter a custom array to be sorted
    - Input exampe: 3i -> The enterd array will be sorted using SelectionSort
        - The user is prompted to enter an array
        - Array input example: 54,23,84,39,85,34 -> There must be only one comma between the numbers
        - When using single digit numbers of numbers with more then 2 digits the markers might not be aligned correctly

Requirements:
    Python 3.10 or higher

Usage:
    Run the file and follow the menu options:
    >>> python3 sorting_algorithm_visualizer.py

Author: Robert-Olivier Hahn
Date: June 2026
"""

import random
import time
from typing import Callable

comparing = False

iteration_counter = 0


def show_info():
    """Outputs the text for the menu."""

    print(
        "\n#\n#    Choose an algorithm:\n#    - 1: Bubblesort\n#    - 2: Insertionsort\n#    - 3: Selectionsort\n#    - a: Compare all algorithms with each other\n#    - <algortihm>w: WorstCase-scenario\n#    - <algorithm>i: Input a custom array\n#    - 0: Exit program\n#\n#    > ",
        end="",
    )


def reset_counter() -> int:
    """Resets the global iteration counter and returns its previous value.

    Returns:
        int: The value of the iteration counter before it was reset.
    """

    global iteration_counter

    tmp = iteration_counter

    iteration_counter = 0

    return tmp


def get_array(array: list[int]) -> list[int]:
    """Prompts the user to input a comma-separated array and returns it as a list of integers.

    Args:
        array: The current array (unused, but kept for consistency).

    Returns:
        list[int]: The user-provided array as a list of integers.
    """

    print("\n#\n#    Enter the array you want to sort:\n#    > ", end="")

    string_array = input()

    array = [int(x) for x in string_array.split(",")]

    return array


def swap(swap_array: list[int], first_index: int, second_index: int):
    """Swaps the elements at the given indices in the provided array.

    Args:
        swap_array: The array in which elements are to be swapped.
        first_index: Index of the first element to swap.
        second_index: Index of the second element to swap.
    """

    first_int = swap_array[first_index]

    swap_array[first_index] = swap_array[second_index]

    swap_array[second_index] = first_int


def sort(algorithm: Callable[[list[int]], None], sorting_array: list[int]):
    """Executes the given sorting algorithm on the provided array and displays the result.

    If not in comparison mode, prints the array before and after sorting,
    along with the number of iterations performed.

    Args:
        algorithm: The sorting algorithm function (e.g., bubbleSort, insertionSort).
        sorting_array: The array to be sorted. Modified in-place.
    """

    global iteration_counter

    if not comparing:
        algorithm_name = algorithm.__name__.capitalize()

        print(
            f"\n# -----------------------------------------------\n#\n#    The following array is sorted using {algorithm_name}:\n#\n#    {sorting_array}\n#"
        )

        time.sleep(0.5)

    algorithm(sorting_array)

    if not comparing:
        print(
            f"\n#    +++++++\n#    Result:           Iterations: {iteration_counter}\n#    +++++++\n#\n#    {sorting_array}\n#\n# -----------------------------------------------"
        )

        iteration_counter = 0


def start_sorting(array: list[int], algorithm: Callable[[list[int]], None]):
    array = random_array()

    sort(algorithm, array)


def random_array() -> list[int]:
    """Generates a random array of 10 integers between 10 and 100.

    Returns:
        list[int]: A list of 10 random integers.
    """

    return [random.randint(10, 100) for _ in range(10)]


def underscore(number: int):
    """Prints a series of underscores to the console for visualization purposes.

    Args:
        anzahl: The number of underscores to print.
    """

    if number > 1:
        for i in range(number - 1):
            print("___", end=" ")

    print("___", end="")


def slashes(distance: int):
    """Prints a visual representation of slashes with spacing for sorting visualization.

    Args:
        distance: The distance between the slashes, determining the spacing.
    """

    print("/", end="")

    for i in range(distance - 1):
        print("    ", end="")

    print("   ", end="")

    print("\\", end="")


def settingMarkers(first_index: int, second_index: int, counter: int):
    """Prints markers for visualizing the current iteration and compared elements.

    Args:
        first_index: Index of the first element being compared.
        second_index: Index of the second element being compared.
        counter: Current iteration number.
    """

    difference = second_index - first_index

    print(f"\n#\n#    Iteration: {counter}\n#       ", end="")

    for i in range(first_index):
        print("    ", end="")

    underscore(difference)

    print("\n#      ", end="")

    for i in range(first_index):
        print("    ", end="")

    slashes(difference)


def sortingStep(first_index: int, second_index: int, array_step: list[int]):
    """Visualizes a single step of the sorting process.

    Increments the iteration counter and prints the current state of the array
    along with markers, if not in comparison mode.

    Args:
        first_index: Index of the first element involved in the step.
        second_index: Index of the second element involved in the step.
        array_step: The current state of the array during sorting.
    """

    global iteration_counter

    iteration_counter += 1

    if not comparing:
        settingMarkers(first_index, second_index, iteration_counter)

        print(f"\n#    {array_step}\n#")

        time.sleep(0.35)


def bubbleSort(sorting_array: list[int]):
    """Sorts the given array using the Bubble Sort algorithm.

    Iterates through the array, swapping adjacent elements if they are in the wrong order,
    and visualizes each swap step.

    Args:
        sorting_array: The array to be sorted. Modified in-place.
    """

    length = len(sorting_array)

    for i in range(length):
        for j in range(length - i - 1):
            if sorting_array[j] > sorting_array[j + 1]:
                swap(sorting_array, j, j + 1)

                sortingStep(j, j + 1, sorting_array)


def insertionSort(sorting_array: list[int]):
    """Sorts the given array using the Insertion Sort algorithm.

    Builds the sorted array one element at a time by inserting each new element
    into its correct position and visualizes each insertion step.

    Args:
        sorting_array: The array to be sorted. Modified in-place.
    """

    for i in range(1, len(sorting_array)):
        inserted = False

        key = sorting_array[i]

        j = i

        while j > 0 and sorting_array[j - 1] > key:
            inserted = True

            sorting_array[j] = sorting_array[j - 1]

            j = j - 1

        sorting_array[j] = key

        if inserted:
            sortingStep(j, i, sorting_array)


def selectionSort(sorting_array: list[int]):
    """Sorts the given array using the Selection Sort algorithm.

    Repeatedly finds the minimum element from the unsorted part and puts it at the beginning,
    visualizing each swap step.

    Args:
        sorting_array: The array to be sorted. Modified in-place.
    """

    length = len(sorting_array)
    for i in range(length - 1):
        index_min_number = i

        for j in range(i + 1, length):
            if sorting_array[j] < sorting_array[index_min_number]:
                index_min_number = j

        if index_min_number > i:
            swap(sorting_array, i, index_min_number)

            sortingStep(i, index_min_number, sorting_array)


def main():
    """Main function of the program. Starts the interactive console application.

    Displays a menu, reads user input, and executes the selected sorting algorithms.
    Supports test arrays and custom user inputs.
    """
    global comparing

    array = [0]

    while True:
        show_info()

        user_input = input()

        match user_input:
            case "0":
                print("\n#\n#    The program is exiting...\n#")

                time.sleep(0.4)

                break

            case "1":
                start_sorting(array, bubbleSort)

            case "2":
                start_sorting(array, insertionSort)

            case "3":
                start_sorting(array, selectionSort)

            case "1w":
                array = [
                    random.randint(110 - (10 * (1 + x)), 110 - (10 * x))
                    for x in range(10)
                ]

                sort(bubbleSort, array)

            case "2w":
                array = [
                    random.randint(110 - (10 * (1 + x)), 110 - (10 * x))
                    for x in range(10)
                ]

                sort(insertionSort, array)

            case "3w":
                array = [random.randint(10 * x, 10 * (1 + x)) for x in range(10)]

                array[0] = random.randint(100, 110)

                sort(selectionSort, array)

            case "3w?":
                array = [
                    random.randint(110 - (10 * (1 + x)), 110 - (10 * x))
                    for x in range(10)
                ]

                sort(selectionSort, array)

            case "1i":
                array = get_array(array)

                sort(bubbleSort, array)

            case "2i":
                array = get_array(array)

                sort(insertionSort, array)

            case "3i":
                array = get_array(array)

                sort(selectionSort, array)

            case "a":
                bubble_array = random_array()

                insertion_array = bubble_array.copy()

                selection_array = bubble_array.copy()

                comparing = True

                print(
                    f"\n# -----------------------------------------------\n#\n#    Alle Algorithmen werden auf das gleiche Array angewendet.\n#\n#    Array: {bubble_array}\n#\n#",
                    end="",
                )

                time.sleep(0.5)

                sort(bubbleSort, bubble_array)

                bubble_iterations = reset_counter()

                sort(insertionSort, insertion_array)

                insertion_iterations = reset_counter()

                sort(selectionSort, selection_array)

                selection_iterations = reset_counter()

                comparing = False

                if bubble_array == insertion_array == selection_array:
                    print(
                        f"\n#    +++++++\n#    Result:\n#    +++++++\n#\n#    {bubble_array}\n#\n#\n#    +++++++++++++++++++++\n#    Number of Iterations:\n#    +++++++++++++++++++++\n#\n#    Bubblesort: {bubble_iterations}\n#    Insertionsort: {insertion_iterations}\n#    Selectionsort: {selection_iterations}\n#\n# -----------------------------------------------"
                    )
                else:
                    print("Something went wrong. Try again.")

            case _:
                print(
                    "\n#\n#    Not a valid input!\n#    Please choose an action from the options presented.\n#"
                )

        time.sleep(0.3)


# Runs the main function if the script is executed directly
if __name__ == "__main__":
    main()
