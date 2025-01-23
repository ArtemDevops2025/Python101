#Expression 	Example 	Meaning
# < 	x < y 	Is x less than y?
# <= 	x <= y 	Is x lesser or equal to y?
# > 	x > y 	Is x greater than y?
# >= 	x >= y 	Is x greater or equal to y?
# == 	x == y 	Is x equal to y?
# != 	x != y 	Is x different from y?

# Operator 	Example 	Meaning
# and 	P and Q 	Are P and Q both true?
# or 	P or Q 	Is at least one of the expressions among P and Q true?
# not 	not P 	The negation of the expression P

# Bernadette
seniority = 12
salary = 2400

# Does Bernadette have less than 5 years of seniority and is her salary is less than 1500€?
criterion1 = seniority < 5 and salary < 1500
# Does Bernadette have between 5 and 10 years of seniority and is her salary between 1500€ and 2300€?
criterion2 = (5 <= seniority <= 10) and (1500 <= salary <= 2300)
# Does Bernadette have more than 10 years of seniority and is her salary less than 1500€ or higher than 2300€?
criterion3 = (seniority > 10) and (1500 > salary or salary > 2300)
# Can Bernadette receive the bonus?
print ("Can Bernadette receive the bonus?", criterion1 or criterion2 or criterion3)


# Marc
seniority = 6
salary = 1490
# Does Marc have less than 5 years of seniority and is his salary is less than 1500€?
criterion1 = seniority < 5 and salary < 1500
# Does Marc have between 5 and 10 years of seniority and is his salary between 1500€ and 2300€?
criterion2 = (5 <= seniority <= 10) and (1500 <= salary <= 2300)
# Does Marc have more than 10 years of seniority and is his salary less than 1500€ or highis than 2300€?
criterion3 = (seniority > 10) and (1500 > salary or salary > 2300)
# Can Marc receive the bonus?
print ("Can Marc receive the bonus?", criterion1 or criterion2 or criterion3)
