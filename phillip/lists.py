universities = [
    ["California Institute of Technology", 2175, 37704],
    ["Harvard", 19627, 39849],
    ["Massachusetts Institue of Technology", 10566, 40732],
    ["Princeton", 7802, 37000],
    ["Rice", 5879, 35551],
    ["Stanford", 19535, 40569],
    ["Yale", 11701, 40500]
]

def enrollment_stats(info_list):
    student_pop_list = []
    tuition_list = []
    for schools in info_list:
        student_pop_list.append(schools[1])
        tuition_list.append(schools[2])
    return student_pop_list, tuition_list

def not_sum(number_list):
    return reduce(lambda x, y: x + y, number_list)

def mean(number_list):
    total = not_sum(number_list)
    return total / len(number_list)

def median(number_list):
    middle_index = len(number_list) / 2
    number_list.sort()
    if len(number_list) % 2 == 0:
        calc_median = (number_list[middle_index] + number_list[middle_index - 1]) / 2
        return calc_median
    else:
        return number_list[middle_index]
students_pops, tuitions = enrollment_stats(universities)

print "***************************"
print "Total students:      {}".format(not_sum(students_pops))
print "Total tuition:      ${}".format(not_sum(tuitions))
print "\n"
print "Mean student pop:    {}".format(mean(students_pops))
print "Median student pop:  {}".format(median(students_pops))
print "\n"
print "Mean tuition:       ${}".format(mean(tuitions))
print "Median tuition      ${}".format(median(tuitions))
print "***************************"
