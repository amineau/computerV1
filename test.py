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
import monomial
from main import *
from math import *


os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

main_file = "main.py"

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
        tab = monomial.__clear__([1.0, 2, 0.0, 0.0])
        self.assertEqual(len(tab), 2)
        tab = monomial.__clear__([1.0, 2, 0.0, 1.0])
        self.assertEqual(len(tab), 4)

    def test_positive(self):
        tab = monomial.__positive__([1.0, -2.0, 0.0])
        self.assertListEqual(tab, [1.0, -2.0, 0.0])
        tab = monomial.__positive__([-1.0, -2.0, 0.0])
        self.assertListEqual(tab, [1.0, 2.0, 0.0])

    def test_merge_monomials(self):
        tab1 = [0.0, 4.2, 3]
        tab2 = [1 , 2, 3, 4, 5]
        result = monomial.__merge__([tab1, tab2])
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
        self.assertEqual(discriminant([1, -1, 2]), -7)

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

    def test_sqrt_facto(self):
        self.assertEqual(sqrt_facto(25.0), 5)
        self.assertListEqual(sqrt_facto(12.0), [2, 3])
        self.assertListEqual(sqrt_facto(72.0), [6, 2])
        self.assertListEqual(sqrt_facto(74.0), [1, 74])

    def test_first_degree_solution(self):
        self.assertEqual(first_degree_solution([4.0, 2.0])[0], '-2')
        self.assertEqual(first_degree_solution([-1.0, 2.0])[0], '1 / 2')

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
        output = self.cmd_output(com)[0]
        self.assertNotIn("Bad number of arguments", output)

    def test_equal_missing(self):
        com = "Hello world"
        output = self.cmd_output(com)[0]
        self.assertIn("'=' statement is missing", output)

    def test_equal_more(self):
        com = "Hel=lo wo=rld"
        output = self.cmd_output(com)[0]
        self.assertIn("Too many '=' statements", output)


    def test_equal_more(self):
        com = "Hello world = "
        output = self.cmd_output(com)[0]
        self.assertIn("At least one monomial is empty", output)


    def test_polynomial_greater(self):
        com = "0 = X^5"
        output = self.cmd_output(com)[0]
        self.assertIn("The polynomial degree is stricly greater than 2, I can't solve.", output)
        self.assertIn("Polynomial degree: 5", output)

    def test_calcul_same_monomial(self):
        com = "X^1 + 3 * X^1 - 2 * X^1 = 0"
        output = self.cmd_output(com)[0]
        self.assertIn("Polynomial degree: 1", output)
        self.assertIn("Reduced form: 2 * X = 0", output)
    
    def test_limb_removal_1(self):
        com = "0 = X^1 + 3 * X^2 - 2"
        output = self.cmd_output(com)[0]
        self.assertIn("Reduced form: - 3 * X^2 - X + 2 = 0", output)


    def test_limb_removal_2(self):
        com = "X^1 -4 * X^2 + X^0 = X^1 + 3 * X^2 - 2"
        output = self.cmd_output(com)[0]
        self.assertIn("Reduced form: - 7 * X^2 + 3 = 0", output)


    def test_solution_linear_function(self):
        com = "2 * X^1 + 4 = 0"
        output = self.cmd_output(com)[0]
        self.assertIn("Polynomial degree: 1", output)
        self.assertIn("x: -2", output)
        com = "2 * X^1 - 8 * X^0 = 0"
        output = self.cmd_output(com)[0]
        self.assertIn("Polynomial degree: 1", output)
        self.assertIn("x: 4", output)

    def test_two_solutions_polynomial_function(self):
        com = "- 1 * X^2 + 2 * X^1 + 3 = 0"
        output = self.cmd_output(com)[0]
        self.assertIn("Polynomial degree: 2", output)
        self.assertIn("x1: 3", output)
        self.assertIn("x2: -1", output)

    def test_one_solution_polynomial_function(self):
        com = "1 * X^2 + 2 * X^1 + 1 = 0"
        output = self.cmd_output(com)[0]
        self.assertIn("Polynomial degree: 2", output)
        self.assertIn("x: -1", output)

    # def test_complex_solution_polynomial_function(self):
    #     com = "4 * X^2 + 2 * X^1 + 1 = 0"
    #     output = self.cmd_output(com)
    #     self.assertIn("Polynomial degree: 2", output[0])
    #     self.assertIn(u"x1: ( -1 − i * √3 ) / 4", output)
    #     self.assertIn(u"x2: ( -1 + i * √3 ) / 4", output[0])

    def test_real_solution_polynomial_function(self):
        com = "4 * X^2 - 4 * X^2 = 0"
        output = self.cmd_output(com)[0]
        self.assertIn("x is a real", output)

    def test_real_solution_polynomial_function(self):
        com = "4 * X^0 = 0 "
        output = self.cmd_output(com)[0]
        self.assertIn("x: empty set", output)

    def test_with_float_monomials(self):
        com = "1.05 * X^2 + 2.5 * X^1 + 0.2 = 0"
        output = self.cmd_output(com)[0]
        self.assertIn("Polynomial degree: 2", output)
        self.assertIn("x1: -2.29806", output)
        self.assertIn("x2: -0.08288", output)

    def test_with_zero_monomials(self):
        com = "1 * X^2 + 0 * X^1 - 1 = 0"
        output = self.cmd_output(com)[0]
        self.assertIn("Polynomial degree: 2", output)
        self.assertIn("Reduced form: X^2 - 1 = 0", output)
        self.assertIn("x1: -1", output)
        self.assertIn("x2: 1", output)

    def test_with_zero_monomials_greater_polynomial(self):
        com = "-X^2 + 2 * X^1 + 3 = 0 * X^5"
        output = self.cmd_output(com)[0]
        self.assertIn("Polynomial degree: 2", output)
        self.assertIn("Reduced form: - X^2 + 2 * X + 3 = 0", output)
        self.assertIn("x1: 3", output)
        self.assertIn("x2: -1", output)

    def test_fraction_in_solution(self):
        com = "10 * X^2 + 2 * X^1 = 0 "
        output = self.cmd_output(com)[0]
        self.assertIn("x1: -1 / 5", output)
        self.assertIn("x2: 0", output)

    def test_with_operator_multiplicate(self):
        com = "4X^2 + 4X^1 + 4 = 0"
        output = self.cmd_output(com)[0]
        self.assertIn("Reduced form: 4 * X^2 + 4 * X + 4 = 0", output)

    def test_with_operator_power(self):
        com = "4 * X^2 + 4 * X + 4 = 0"
        output = self.cmd_output(com)[0]
        self.assertIn("Reduced form: 4 * X^2 + 4 * X + 4 = 0", output)

    def test_reduced_form(self):
        com = "4 * X^2 - 4 * X^1 = -4 * X^0 - 8 * X^1"
        output = self.cmd_output(com)[0]
        self.assertIn("Reduced form: 4 * X^2 + 4 * X + 4 = 0", output)

    def test_result(self):
        com = "2x^2 - 1x - 2 = 0"
        output = self.cmd_output(com)[0]
        self.assertIn("x1: -0.7807764", output)
        self.assertIn("x2: 1.2807764", output)
        com = "-2x^2 -4x + 3 = 0"
        output = self.cmd_output(com)[0]
        self.assertIn("x1: 0.58113", output)
        self.assertIn("x2: -2.58113", output)
        com = "-5x^2 -x + 2 = 0"
        output = self.cmd_output(com)[0]
        self.assertIn("x1: 0.540312", output)
        self.assertIn("x2: -0.740312", output)
        com = "-2x^2 + 4x - 10 = 0"
        output = self.cmd_output(com)[0]
        self.assertIn("x1: 1 - i * 2", output)
        self.assertIn("x2: 1 + i * 2", output)
        com = "x^2 + 1 = 0"
        output = self.cmd_output(com)[0]
        self.assertIn("x1: -i", output)
        self.assertIn("x2: i", output)




if __name__ == '__main__':
    unittest.main()

##### polynomial greater than 2 # x^5 = 0
##### calcul same monomial # x^1 + 3 * x^1 - 2 * x^1 = 0 => reduce form   2 * x^1 = 0
##### limb removal 1  # 0 = x^1 + 3 * x^2 - 2 = 0 => reduce form -3 * x^2 - x^1 + 2 = 0
##### limb removal 2  # x^1 -4 * x^2 + x^0 = x^1 + 3 * x^2 - 2 => reduce form -7 * x^2 + 3 = 0
##### solution 1 linear function  # 2 * x^1 + 4 = 0 => x = -2
##### solution 2 linear function  # 2 * x^1 - 8 * x^0 = 0 => x = 4
##### two solutions  # -x^2 + 2 * x^1 + 3 = 0 => x1 = 3 et x2 = -1
##### one solution  # 1 * x^2 + 2 * x^1 + 1 = 0 => -1
##### complex solution  # 4 * x^2 + 2 * x^1 + 1 = 0 => x1 = (-2−i√12) / 8 et x2 = (-2+i√12) / 8
##### real solution  # 4 * x^2 - 4 * x^2  = 0 => x: ℝ
##### no solution  # 4 * x^0  = 0 => empty set
##### with float  # 1.05 * x^2 + 2.5 * x^1 + 0.2 = 0 => x1 = -2.2980669856774 et x2 = -0.082885395274952
##### with zeros  # 1 * x^2 + 0 * x^1 - 1 = 0 => x = 1
##### with zeros in greater polinomial  # -x^2 + 2 * x^1 + 3 = 0 * X^5 => x1 = 3 et x2 = -1


##### BONUS Tests #####
##### fraction # 4 * x^2 + 4 * x^1 + 4 * x^0 = 0 => x = -1/2
##### without '*' and '^' # 4x^2 + 4x + 4 = 0 => x = -1/2
##### reduce form # 4 * x^2 - 4 * x^1 = -4 * x^0 - 8 * x^1 =>  4x^2 + 4x +4