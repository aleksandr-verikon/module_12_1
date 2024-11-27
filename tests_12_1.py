import unittest
class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        begun = Runner('Alex')
        for i in range(10):
            begun.walk()
        self.assertEqual(begun.distance, 50)

    def test_run(self):
        begun = Runner('Gepard')
        for i in range(10):
            begun.run()
        self.assertEqual(begun.distance, 100)

    def test_challenge(self):
        begun = Runner('first')
        begun2 = Runner('second')
        for i in range(10):
            begun.walk()
            begun2.run()
        self.assertNotEqual(begun.distance, begun2.distance)

if __name__ == '__main__':
    unittest.main()


