from os import chdir, getcwd


print("*"*30)
old_dir = getcwd()
print(getcwd())
chdir("PrespectiveFloor")
print(getcwd())
chdir(old_dir)
print(getcwd())
print("*"*30)