

class Range:
    def __init__(self, interval):
        self.interval = interval

        first_number_end = interval.find(',')

        if (interval[0] == '['):
            self.start_point = int(interval[1:first_number_end])
        else:
            self.start_point = int(interval[1:first_number_end]) + 1

        first_digit = first_number_end + 1
        last_digit = len(interval) - 2
        if (interval[len(interval) - 1] == ']'):
            self.end_point = int(interval[first_digit:last_digit + 1])
        else:
            self.end_point = int(interval[first_digit:last_digit + 1]) - 1
         
    def contains_integers(self, integers):
        numbers = integers[1:len(integers) - 1].split(",")
        for number in numbers:
            if (not (int(number) >= self.start_point and int(number) <= self.end_point)):
                return False

        return True

    def get_all_points(self):
        elements = list(range(self.start_point, self.end_point + 1))
        elements = map(str, elements)
        string_to_return = "{"
        string_to_return += ",".join(elements)
        string_to_return += "}"
        return string_to_return

    def contains_range(self, other_range):
        second_range = Range(other_range)
        if (second_range.start_point <= self.end_point and  second_range.end_point <= self.end_point):
            return True
        else:
            return False    

    def end_points(self):
        return "{" + str(self.start_point)  + "," + str(self.end_point) + "}"

    def overlaps_range(self, other_range):
        second_range = Range(other_range)
        if (second_range.start_point <= self.end_point):
            return True
        else:
            return False

    def equals(self, other_range):
        return self.interval == other_range
