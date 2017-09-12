from decimal import *
getcontext().prec = 4

def wacc_calculator():
	
	print 'Enter market value of equity: '
	E = raw_input('')
	E = Decimal(int(E))

	print 'Enter market value of debt: '
	D = raw_input('')
	D = Decimal(int(D))

	print 'Enter cost of equity as percentage (decimal format): '
	Re = raw_input('')
	Re = Decimal(Re)

	print 'Enter cost of debt as percentage (decimal format): '
	Rd = raw_input('')
	Rd = Decimal(Rd)

	print 'Enter corporate tax rate (decimal percentage - 5% = .05)'
	Tc = raw_input('')
	Tc = Decimal(Tc)

	V = E + D

	perc_equity = E / V
	perc_debt = D / V

	tax_deduction = 1 - Tc

	wacc = ((perc_equity * Re) + (perc_debt * Rd)) * (tax_deduction)


	#V = 14000000
	#perc_equity = 600000 / 14000000 = .42
	#perc_debt = 800000 / 14000000 = .58

#	Re = 15%, .15
#	Rd = 08%, .08

#	taxdeduction = 1

# wacc = () + () * (1)
	print 'WACC = ', wacc

	return wacc


def convertStrToLong(s):
    """Convert string to either int or float."""

    ret = long(s)
    

    return ret

wacc_calculator()

