# pypi.org

# pip install prettytable

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmender"])
table.add_column("Type",["Electric","Water","Fire"])
table.add_column("Power",[500,345,789])

table.align = "l"   # left alignment
# you can search more attributes using wiki page
print(table)



