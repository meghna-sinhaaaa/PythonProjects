multiples = [x*7 for x in range(1,11)]
print(multiples)


languages=["python","perl","ruby","go","java","c"]
lengths = [len(language) for language in languages]
print(lengths)

z = [x for x in range(0,101) if x%3==0]
print(z)