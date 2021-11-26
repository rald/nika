#!/usr/bin/env python3

import os
import csv

class POSmachine:

    def __init__(self):
        """
        Initialize the fields.

        Make sure that the last line of this method is the following:
        self.start()
        """
        # Initialize your fields here
        self.price_list_file = None
        self.invoice_file = None
        self.price_list = None
        self.invoice = None
        self.start()

    def start(self):
        self.printWelcomeMessage()
        while True:
            self.printAllOptions()

            while True:
                try:
                    inp = int(input())
                    break
                except:
                    print("Invalid input")

            if inp == 1:
                self.setPriceList()
            elif inp == 2:
                self.printPriceList()
            elif inp == 3:
                self.makeNewTransaction()
            elif inp == 4:
                break
            else:
                print("Invalid input")

    def printWelcomeMessage(self):
        """
        Print a welcome message for the user.

        Remove/delete the "pass" keyword below.
        """
        # Add your code here
        print("Welcome to Shop Nice!\n")


    def printAllOptions(self):
        """
        Print all actions the user can do

        Remove/delete the "pass" keyword below.
        """
        print("What do you want to do today? (input the number)")
        print("1 - Set the price list")
        print("2 - Show the price list")
        print("3 - Make a new transaction")
        print("4 - Close the POS machine")

    def setPriceList(self):
        """
        Load the price list from the provided file.
        The program should send a warning if the provided file
        is invalid.

        Remove/delete the "pass" keyword below.
        """
        # Add your code here
        while True:
            self.price_list_file=input("Set the price list file: ")
            if self.price_list_file=="" or not os.path.exists(self.price_list_file):
                print(f"File not found: '{self.price_list_file}'");
            else:
                break

        self.price_list=[]
        if self.price_list_file.endswith("csv"):
            delimiter=","
        elif self.price_list_file.endswith("txt"):
            delimiter="\t"
        with open(self.price_list_file) as csvfile:
            csvreader=csv.DictReader(csvfile,delimiter=delimiter)
            for row in csvreader:
                self.price_list.append(row)

    def printPriceList(self):
        """
        Print the current price list

        Remove/delete the "pass" keyword below.
        """
        # Add your code here
        if self.price_list==None:
            print("Set the price list first")
        else:
            print("ID Product Price")
            for row in self.price_list:
                print(f"{row['ID']} {row['Product']} {row['Price']}")


    def addProductToTransaction(self, product, quantity):
        """
        Calculate the price for the given product and quantity
        and add this to the current invoice

        Remove/delete the "pass" keyword below.
        """
        # Add your code here
        found=False
        for row in self.price_list:
            if product==int(row["ID"]):
                found=True
                total=float(row["Price"])*quantity;
                self.invoice.append({"ID":row["ID"],"Product":row["Product"],"Price":row["Price"],"Quantity":quantity,"Total":total})
                break
        if not found:
            print("Invalid product ID")


    def makeNewTransaction(self):
        """
        Create a new transaction. Print the price list once.
        Have the user to add products (given a quantity >= 1).
        When the user inputs a blank, print the invoice.

        Remove/delete the "pass" keyword below.
        """

        # Add your code here
        if self.price_list==None:
            print("Set the price list first")
        else:
            self.invoice=[]
            print("Input the product and quantities (Input blank to complete the transaction)")
            while True:
                line=input()
                if line=="":
                    break
                product,quantity=line.split(",")
                product=int(product)
                quantity=int(quantity)

                if quantity<1:
                    print("Invalid quantity")
                    continue

                self.addProductToTransaction(product,quantity)
            self.createSalesInvoice()

    def createSalesInvoice(self):
        """
        Print (into the console) the sales invoice, detailing
        the price and quantity of the products purchased, and
        the total amount.

        Save the same print output as a text file.

        Remove/delete the "pass" keyword  below.
        """
        # Add your code here
        grand_total=0
        print("ID Product Price Quantity Total")
        for row in self.invoice:
            grand_total+=float(row["Total"])
            print(f"{row['ID']} {row['Product']} {row['Price']} {row['Quantity']} {row['Total']}")
        print(f"Grand Total: {grand_total}")

        while True:
            self.invoice_file=input("Set the invoice file: ")
            if os.path.exists(self.invoice_file):
                print("Warning file exists")
            else:
                break

        with open(self.invoice_file,"w") as writer:
            writer.write("{:>4} {:32} {:>12} {:>8} {:>12}\n".format("ID","Product","Price","Quantity","Total"))
            for row in self.invoice:
                writer.write("{:>4d} {:32s} {:>12,.2f} {:>8,d} {:>12,.2f}\n".format(int(row["ID"]),row["Product"],float(row["Price"]),int(row["Quantity"]),float(row["Total"])))
        with open(self.invoice_file,"a") as writer:
            writer.write(f"                                               Grand Total: {grand_total:>12,.2f}\n")


p = POSmachine()


