#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    k = []
    for i in range(len(my_list_1)):
        try:
            k.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
        except (TypeError, TypeError):
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            return k
