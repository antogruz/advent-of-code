def findAllMethods(object):
    return [method for method in dir(object) if callable(getattr(object, method))]


class Tester:
    def runTests(self):
        methodNames = findAllMethods(self)
        testNames = [m for m in methodNames if "test" in m]
        for test in testNames:
            print(test)
            self.__init__()
            getattr(self, test)()


def assert_equals(expected, actual):
    if expected != actual:
        print("Expected", expected, "got", actual)
        raise Exception("Error in test")
