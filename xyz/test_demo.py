
class Test_credence15:
    def test_sum(self):
        a=50
        b=58
        sum = a+b
        print("Resultent sum:-",sum)
        if sum == 108:
            assert True
        else:

            assert False


    def test_mul(self):
        a=5
        b=8
        mul=a*b
        print("multiplication result=",mul)
        if mul == 40:
            print('good')
            assert True
        else:
            print("wrong")
            assert False

    def test_sub(self):
        a=56
        b=26
        sub = a-b
        print("subtraction value=",sub)
        if sub==30:
            print('good')
            assert True
        else:
            print('khalash')
            assert False


























