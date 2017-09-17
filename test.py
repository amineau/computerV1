#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    Computer v1
    42 Projet
    amineau <amineau@student.42.fr>
"""

import unittest
import os
import subprocess as cmd
from main import *


os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

main_file = "main.py"

# Le code à tester doit être importable. On
# verra dans une autre partie comment organiser
# son projet pour cela.
 
# Cette classe est un groupe de tests. Son nom DOIT commencer
# par 'Test' et la classe DOIT hériter de unittest.TestCase.
class TestComputerV1(unittest.TestCase):
 
    def cmd_prepare(self):
        com = "python %s"%(main_file)
        return com.split()

    def cmd_output(self, argv):
        com = self.cmd_prepare()
        com.append(argv)
        pipe = cmd.Popen(com, stdout=cmd.PIPE, stderr=cmd.PIPE)
        output, errput = pipe.communicate()
        return output.decode("utf-8") , errput.decode("utf-8") 

    def test_clear(self):
        tab = clear([1.0, 2, 0.0, 0.0])
        self.assertEqual(len(tab), 2)
        tab = clear([1.0, 2, 0.0, 1.0])
        self.assertEqual(len(tab), 4)

    def test_positive(self):
        tab = positive([1.0, -2.0, 0.0])
        self.assertListEqual(tab, [1.0, -2.0, 0.0])
        tab = positive([-1.0, -2.0, 0.0])
        self.assertListEqual(tab, [1.0, 2.0, 0.0])

    def test_merge_members(self):
        tab1 = [0.0, 4.2, 3]
        tab2 = [1 , 2, 3, 4, 5]
        result = merge_members([tab1, tab2])
        self.assertListEqual(result, [-1.0, 2.2, 0.0, -4.0, -5.0])

    def test_pgcd(self):
        self.assertEqual(pgcd(5, 1), 1)
        self.assertEqual(pgcd(5, 5), 5)
        self.assertEqual(pgcd(3, 9), 3)

    def test_fraction(self):
        success = fraction(3.0, 9.0)
        failureInt = fraction(10.0, 2.0)
        self.assertEqual(success, "1 / 3")
        self.assertEqual(failureInt, "5")

    def test_convert_if_integer(self):
        self.assertEqual(convert_if_integer(2.0), 2)
        self.assertEqual(convert_if_integer(2.2), 2.2)

    def test_discriminant(self):
        self.assertEqual(discriminant([1, 4, 1]), 12)
        self.assertEqual(discriminant([0, 4, 1]), 16)
        self.assertEqual(discriminant([2, 3, 1]), 1)
        self.assertEqual(discriminant([5, 0, 2]), -40)
        self.assertEqual(discriminant([-3, 2, 2]), 28)

    def test_abs(self):
        self.assertEqual(abs(8.9), 8.9)
        self.assertEqual(abs(-9), 9)
        self.assertEqual(abs(0), 0)
        self.assertEqual(abs(-0), 0)

    def test_sqrt(self):
        self.assertEqual(sqrt(25), 5)
        self.assertEqual(sqrt(81), 9)
        self.assertEqual(sqrt(1296), 36)
        self.assertAlmostEqual(sqrt(20), 4.472136, places=6)

    def test_first_degree_solution(self):
        self.assertEqual(first_degree_solution([4.0, 2.0]), '-2')
        self.assertEqual(first_degree_solution([-1.0, 2.0]), '1 / 2')

    def test_fail_argc(self):
        com = "python %s"%(main_file)
        pipe = cmd.Popen(com.split(), stdout=cmd.PIPE)
        output = pipe.communicate()
        self.assertIn("Bad number of arguments", output[0])   
        com = "python %s hello world"%(main_file)
        pipe = cmd.Popen(com.split(), stdout=cmd.PIPE)
        output = pipe.communicate()
        self.assertIn("Bad number of arguments", output[0])
     
    def test_success_argc(self):
        com = "hello world"
        output = self.cmd_output(com)
        self.assertNotIn("Bad number of arguments", output[0])

    def test_equal_missing(self):
        com = "Hello world"
        output = self.cmd_output(com)
        self.assertIn("'=' statement is missing", output[0])

    def test_equal_more(self):
        com = "Hel=lo wo=rld"
        output = self.cmd_output(com)
        self.assertIn("Too many '=' statements", output[0])


    def test_equal_more(self):
        com = "Hello world = "
        output = self.cmd_output(com)
        self.assertIn("At least one member is empty", output[0])


    def test_polynomial_greater(self):
        com = "0 = X^5"
        output = self.cmd_output(com)
        self.assertIn("The polynomial degree is stricly greater than 2, I can't solve.", output[0])
        self.assertIn("Polynomial degree: 5", output[0])

    def test_calcul_same_member(self):
        com = "X^1 + 3 * X^1 - 2 * X^1 = 0"
        output = self.cmd_output(com)
        self.assertIn("Polynomial degree: 1", output[0])
        self.assertIn("Reduced form: 2 * X = 0", output[0])
    
    def test_limb_removal_1(self):
        com = "0 = X^1 + 3 * X^2 - 2"
        output = self.cmd_output(com)
        self.assertIn("Reduced form: - 3 * X^2 - X + 2 = 0", output[0])


    def test_limb_removal_2(self):
        com = "X^1 -4 * X^2 + X^0 = X^1 + 3 * X^2 - 2"
        output = self.cmd_output(com)
        self.assertIn("Reduced form: - 7 * X^2 + 3 = 0", output[0])


# Ceci lance le test si on exécute le script
# directement.
if __name__ == '__main__':
    unittest.main()



# # Chaque méthode dont le nom commence par 'test_'
# # est un test.
# def test_missing_argv(self):
#     output = cmd_output("")[0]
#     self.assertEqual(output, 'Argument is missing')


# print("##### Syntactic tests #####")
# print("##### argument missing")
# print("##### too many arguments")
# print("##### '=' missing")
# print("##### too many '='")
# print("##### member empty")
# print("##### different unknown of x")
# print("##### lexical 1")
# print("##### lexical 2")
# print("##### lexical 3")

# print("##### Function Tests #####")
# print("##### polynomial greater than 2") # x^5 = 0
# print("##### calcul same member") # x^1 + 3 * x^1 - 2 * x^1 = 0 => reduce form   2 * x^1 = 0
# print("##### limb removal 1 ") # 0 = x^1 + 3 * x^2 - 2 = 0 => reduce form -3 * x^2 - x^1 + 2 = 0
# print("##### limb removal 2 ") # x^1 -4 * x^2 + x^0 = x^1 + 3 * x^2 - 2 => reduce form -7 * x^2 + 3 = 0
# print("##### solution test 1 linear function")  # 2 * x^1 + 4 = 0 => x = -2
# print("##### solution test 2 linear function")  # 2 * x^1 - 8 * x^0 = 0 => x = 4
# print("##### two solutions")  # -x^2 + 2 * x^1 + 3 = 0 => x1 = 3 et x2 = -1
# print("##### one solution")  # 1 * x^2 + 2 * x^1 + 1 = 0 => -1
# print("##### complex solution")  # 4 * x^2 + 2 * x^1 + 1 = 0 => x1 = (-2−i√12) / 8 et x2 = (-2+i√12) / 8
# print("##### real solution")  # 4 * x^2 - 4 * x^2  = 0 => real
# print("##### no solution")  # 4 * x^0  = 0 => empty set

# print("##### BONUS Tests #####")
# print("##### fraction") # 4 * x^2 + 4 * x^1 + 4 * x^0 = 0 => x = -1/2
# print("##### without '*' and '^'") # 4x^2 + 4x + 4 = 0 => x = -1/2
# print("##### reduce form") # 4 * x^2 - 4 * x^1 = -4 * x^0 - 8 * x^1 =>  4x^2 + 4x +4