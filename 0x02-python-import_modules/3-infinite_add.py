
if __name__ == "__main__":
    def sum_all(*args):
        sum_ = 0
        for i in args:
            sum_ += i
        return sum_

    print(sum_all(20, 70))


    sum_all()