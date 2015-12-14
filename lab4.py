#!/usr/bin/env python3

""" Graded Lab #4 for Inf1340, Fall 2015

    This program computes federal and provincial sales tax.
    Assume that the provincial sales tax is 5 percent and
    the federal sales tax is 2.5 percent. It displays the
    amount of the purchase, the provincial sales tax, the
    federal sales tax, the total tax, and the total of the
    sale.
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

# Rewrite this code to use global constants, local variables and functions
# Output the text to a file instead of printing it

provincial_sales_tax = .05
federal_sales_tax = .025


def write_to_file(purchase, p_tax, f_tax, t_tax, t_sale):
    file_name = "output.txt"
    f = open("output.txt", 'w')
    f.write("Amount of purchase: {0:.2f}\n".format(purchase))
    f.write("Provincial tax: {0:.2f}\n".format(p_tax))
    f.write("Federal tax: {0:.2f}\n".format(f_tax))
    f.write("Total tax: {0:.2f}\n".format(t_tax))
    f.write("Total sale: {0:.2f}\n".format(t_sale))
    f.close()


def bill_of_sale(purchase):
    p_tax = purchase * provincial_sales_tax
    f_tax = purchase * federal_sales_tax
    t_tax = purchase * (provincial_sales_tax + federal_sales_tax)
    t_sale = purchase * (1+provincial_sales_tax+federal_sales_tax)
    write_to_file(purchase, p_tax, f_tax, t_tax, t_sale)

bill_of_sale(20)