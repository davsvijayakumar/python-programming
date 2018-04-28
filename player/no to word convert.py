import inflect
n=int(input())
p = inflect.engine()
v=p.number_to_words(n)
print(v)
