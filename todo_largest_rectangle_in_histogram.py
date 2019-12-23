"""
84. Largest Rectangle in Histogram
Hard

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1,
find the area of largest rectangle in the histogram.

Example:

Input: [2,1,5,6,2,3]
Output: 10
"""
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        # This function calulates maximum
        # rectangular area under given
        # histogram with n bars

        # Create an empty stack. The stack
        # holds indexes of histogram[] list.
        # The bars stored in the stack are
        # always in increasing order of
        # their heights.
        stack = list()

        max_area = 0  # Initialize max area

        # Run through all bars of
        # given histogram
        index = 0
        histogram = heights
        while index < len(histogram):

            # If this bar is higher
            # than the bar on top
            # stack, push it to stack

            if (not stack) or (histogram[stack[-1]] <= histogram[index]):
                stack.append(index)
                index += 1

            # If this bar is lower than top of stack,
            # then calculate area of rectangle with
            # stack top as the smallest (or minimum
            # height) bar.'i' is 'right index' for
            # the top and element before top in stack
            # is 'left index'
            else:
                # pop the top
                top_of_stack = stack.pop()

                # Calculate the area with
                # histogram[top_of_stack] stack
                # as smallest bar
                area = (histogram[top_of_stack] *
                        ((index - stack[-1] - 1)
                         if stack else index))

                # update max area, if needed
                max_area = max(max_area, area)

                # Now pop the remaining bars from
        # stack and calculate area with
        # every popped bar as the smallest bar
        while stack:
            # pop the top
            top_of_stack = stack.pop()

            # Calculate the area with
            # histogram[top_of_stack]
            # stack as smallest bar
            area = (histogram[top_of_stack] *
                    ((index - stack[-1] - 1)
                     if stack else index))

            # update max area, if needed
            max_area = max(max_area, area)

            # Return maximum area under
        # the given histogram
        return max_area


if __name__ == '__main__':
    heights = [2, 1, 5, 6, 2, 3]
    target = 10
    output = Solution().largestRectangleArea(heights)
    assert target == output, f'Expected: {target}, but got {output}'
