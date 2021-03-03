def arithmetic_arranger(problems, solution=False):

    # Variables
    final_top_string = ""
    final_bottom_string = ""
    final_line_string = ""
    final_result_string = ""

    for problem in problems:
        splitted_problem = problem.split(" ")

        # Error Handling
        if len(problems) > 5:
            return 'Error: Too many problems.'
        # Check for invalid operators
        if splitted_problem[1] == "*" or splitted_problem[1] == "/":
            return "Error: Operator must be '+' or '-'."
        # Check if the numbers are only digits
        if splitted_problem[0].isdigit() == False or splitted_problem[2].isdigit() == False:
            return 'Error: Numbers must only contain digits.'
        # Check if the number len is 4 or less
        if len(splitted_problem[0]) > 4 or len(splitted_problem[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        first_operand = splitted_problem[0]
        operator = splitted_problem[1]
        second_operand = splitted_problem[2]

        if operator == "+":
            result = str(int(first_operand)+int(second_operand))
        elif operator == "-":
            result = str(int(first_operand)-int(second_operand))

        length = max(len(first_operand), len(second_operand)) + 2
        top_string = str(first_operand).rjust(length)
        bottom_string = operator + str(second_operand).rjust(length - 1)
        line_string = ""
        result_string = str(result).rjust(length)

        for i in range(length):
            line_string += "-"

        if problem != problems[-1]:
            final_top_string += top_string + "    "
            final_bottom_string +=  bottom_string + "    "
            final_line_string +=  line_string + "    "
            final_result_string +=  result_string + "    "
        else:
            final_top_string += top_string
            final_bottom_string +=  bottom_string
            final_line_string +=  line_string
            final_result_string +=  result_string

        if solution:
            arranged_problems = final_top_string + "\n" + final_bottom_string + "\n" + final_line_string + "\n" + final_result_string
        else:
            arranged_problems = final_top_string + "\n" + final_bottom_string + "\n" + final_line_string

    return arranged_problems