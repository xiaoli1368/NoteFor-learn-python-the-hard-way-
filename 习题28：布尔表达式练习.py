test=[
True and True, # 1
False and True, # 0 
1 == 1 and 2 == 1, # 0
"test" == "test", # 1
1 == 1 or 2 != 1, # 1
True and 1 == 1, # 1
False and 0 != 0, # 0
True or 1 == 1, # 1
"test" == "testing", # 0
1 != 0 and 2 == 1, # 0
"test" != "testing", # 1
"test" == 1, # 0
not (True and False), # 1 
not (1 == 1 and 0 != 1), # 0 
not (10 == 1 or 1000 == 1000), # 0
not (1 != 10 or 3 == 4), # 0
not ("testing" == "testing" and "Zed" == "Cool Guy"), # 1
1 == 1 and not ("testing" == 1 or 1 == 0), # 1
"chunky" == "bacon" and not (3 == 4 or 3 == 3), # 0
3 == 3 and not ("testing" == "testing" or "Python" == "Fun"), # 0
]

print(test)