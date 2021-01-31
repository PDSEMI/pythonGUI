from tkinter import *
import numpy as np

class RefiEval:
	def __init__(self):
		window = Tk()
		window.title("Refinance Evaluator")
		#input
		Label(window, text = "Loan Amount",
			font ="Helvetica 16").grid(row=1,column=1,sticky=W)
		Label(window, text = "Interest Rate",
			font ="Helvetica 16").grid(row=2,column=1,sticky=W)
		Label(window, text = "term (years)",
			font ="Helvetica 16").grid(row=3,column=1,sticky=W)
		Label(window, text = None).grid(row=4,column=1,sticky=W)

		#output
		Label(window, text = "Patment").grid(row=5,column=1,sticky=W)
		Label(window, text = "Total Payments").grid(row=6,column=1,sticky=W)

		Button(window, text="Calculate Payment",
			command=self.calcPayment, 
			font="Helvetica 14").grid(row=7,column=2,padx=(100,5),pady=5)
		#variable to store input
		self.pv = StringVar()
		self.interst_rate = StringVar()
		self.term = StringVar()

		self.pmt = StringVar()
		self.total = StringVar()

		#Assign variable
		Entry(window, textvariable = self.pv, 
				justify=RIGHT).grid(row=1,column=2,padx =(0,5))
		Entry(window, textvariable = self.interst_rate, 
				justify=RIGHT).grid(row=2,column=2,padx =(0,5))
		Entry(window, textvariable = self.term, 
				justify=RIGHT).grid(row=3,column=2,padx =(0,5))

		Label(window, textvariable = self.pmt,
			font = "Helvetica 12 bold",
			justify=RIGHT).grid(row=5,column=2,sticky=E)
		Label(window, textvariable = self.total,
			font = "Helvetica 12 bold",
			justify=RIGHT).grid(row=6,column=2,sticky=E)

		window.mainloop()

	def calcPayment(self):
		pv = float(self.pv.get())
		rate = float(self.interst_rate.get())
		term = float(self.term.get())

		pmt = np.pmt(rate/1200, term * 12, -pv,0)
		total = pmt*12*term

		self.pmt.set("$"+format(pmt,"5,.2f"))
		self.total.set("$"+format(total, "8,.2f"))

RefiEval()
