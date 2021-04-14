with open('salary.txt', 'r') as salary_file, \
     open('salary_year.txt', 'w') as salary_year_file:
    for salary in salary_file:
        salary_year_file.write(f"{str(int(salary) * 12)}\n")
