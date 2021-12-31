"""
@date: 2/11/2021
@author: Nihar Satasia
@PID: niharsatasia
@assignment: HW4
@note: Do NOT alter the function headers that are well documented, 
Do put your hw answers in the spaces provided within function headers
"""


def log_base_2(number: float) -> str:
    """ Gives the approximate log base 2 calculation of the input number
    @param number: float to calculate on
    @precondition: number is > 0
    @return str: A string description of the approximate result
    parts i-iii from HW
i.  Work out the steps to figure out the 2 concrete examples of 256 and 81
    step by step and briefly explain your work and thinking(5pts)
     
    The log base 2 calculation for 256 is 8 because 2^8 is 256. The log base 2
    calculation for 81 is somewhere between 6 and 7 because 2^6 is 64 and 2^7 is
    128. Since 81 falls between those 2 values the log base 2 of 81 must be
    somewhere between 6 and 7. Due to my previous expeirence with logarithms, I
    know that in order to calculate a log base of 2 calculation, you must figure
    out n, which is 2^n. So, using that prior knowledge on 256 and 81, gave me the
    correct answers of 8 and somewhere between 6 and 7.

ii. Find and describe a pattern and attempt to generalize (5pts)

    Since we need to figure out how many times 2 can be squared to reach any number,
    we can work backwards to make the solution easier. Once given an input (any number),
    we can create a loop and keep dividing the input by 2 until it gets so small that
    it equals exactly 1 or a little bit less than 1. If it hits exactly 1, then the
    loop should end and get a value (count) for the log base 2 calculation. If it does not hit
    exactly 1, then the loop should end the moment the input drops below 1 after being
    divided. Once it is below 1, we know that the answer must be an in between. Thus the
    value for the log base 2 calculation would be between count-1 and count. So for 256,
    count would be 8, since 256 can be divided by 2, 8 times until hitting 1. But for 257,
    the count would be 9 since 257 is not perfectly divisible by 2, which results in the
    answer being somewhere between 8 and 9.
    
    *COUNT IS A VARIABLE IN THAT KEEPS TRACK OF HOW MANY TIMES THE INPUT IS DIVIDED BY 2*

iii. Investigate and explain special cases to see if the pattern holds up (5pts)

    Special cases in my solution would be inputs that are not perfectly divisble by 2, which
    means that when they are constantly divided by 2, they will never equal exactly 1. Examples
    of these inputs would be: 81, 123, 49, 51, 401, etc. However, my solution takes into account
    for these special cases since if the input goes below 1 when it is divided,then the loop
    will end and display an output. The output would be in between the number of times the input
    was divided by 2 and 1 less than that number. So, for a log base 2 calculation for 3, the
    output would be in between 1 and 2 since 3 can be divided by 2 twice until it goes under 1
    and 2 minus 1 equals 1.
    """
    
    count = 0
    if number == 1:
            return str(count)
    if number <= 0:
        return ("invalid number entered")
    while number >=1:
        number = number/2.0
        count +=1
        if number == 1:
            return str(count)
        elif number<1:
            strCount = str(count)
            strCount1 = str(count-1)
            return ("between "+strCount1+ " and "+strCount)



def reverse_list(aList: list) -> list:
    """Gives a list with the elements in reversed order
    @param aList: list input that's going to be reversed
    @return list: the reversed version of the input list
    parts i-iii from HW
i.  Work out the steps to figure out a concrete example and briefly explain
    your work and thinking(5pts)

    An example of a list reversed would be as follows:
    input : [1,2,3,4,5]
    output : [5,4,3,2,1]
    In order to do this, first the user will have to enter a list of numbers, and then
    by gathering each element in each certain index, the output would have to reverse the
    list. This can be done by many different ways, but the first way that comes to mind
    would be creating a loop and creating a new list in the loop to which the elements
    would be added in reverse. So, rather than trying to reverse the orginial list, I
    would create a new list that has the same element in reverse. However, creating a
    new list is not an option, so the other way to do this would be to swap the first
    number in index 0 with the number in the last index. Since it all needs to be in one
    list, this would be the easiest way to do so. So for example each time the loop iterates
    the input [1,2,3,4,5] would change to [5,2,3,4,1], then [5,4,3,2,1].

ii. Find and describe a pattern and attempt to generalize (5pts)

    The pattern here would be to access the first index and last index of aList and simply
    swap the numbers in the indexes. In order to do this, 2 variables would be needed. One
    for the last index and one for the first index. To get the last index, it would just be
    the length of aList-1 and to get the first index it would just be 0. Then, since both of
    those variables will increase by 1 and decrease by 1 respectively, the loop should iterate
    until the value of 0 overcomes the value of the length of aList-1. With the example of
    [1,2,3,4,5], the first iteration will have k = 0 and length-1 = 4 which will result in
    the zero and fourth indexes swapping number values to be [5,2,3,4,1]. Then, k will
    increase by 1 and length will decrease by 1 so the second iteration will have k = 1 and
    length-1 = 3 which will result in the first and third indexes swapping to be [5,4,3,2,1]
    Then on the third iteration k is now equal to 2 and length-1 is now equal to 2, since length
    is no longer greater than k, the loop ends and the solution is complete.

iii. Investigate and explain special cases to see if the pattern holds up (5pts)

    The only special cases that come to mind would be if there are an even amount of numbers
    in the list, or if there are an odd amount of numbers in the list. However, as explained above
    since the loop will end the moment length-1 is less or equal to k, it will not matter if the
    amount of values is even or odd. For instance above there was an odd amount of values, so here
    is an example of an even amount of values. On the first iteration, [0,1,2,3,4,5] would go to
    [5,1,2,3,4,0] with k equaling 1 and length - 1 equaling 4. On the second interation, it would go
    to [5,4,2,3,1,0] with k equaling 2 and length - 1 equaling 3. Since the length-1 is still higher
    than k, on the third iteration it would go to [5,4,3,2,1,0] with k equaling 3 and length-1 equaling
    2, which would finally end the loop and give the solution.
    """
    k = 0            
    length = len(aList)-1 
    while k<length:
        aList[k],aList[length] = aList[length],aList[k]
        k += 1
        length -= 1
    return aList
