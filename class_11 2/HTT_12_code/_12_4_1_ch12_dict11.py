#
# HTT Ch 12 code example:
#
# Section 12.4, example 1: ch12_dict11
#

opposites = {'up': 'down', 'right': 'wrong', 'true': 'false'}
alias = opposites

print(alias is opposites)

alias['right'] = 'left'
print(opposites['right'])

print(opposites)