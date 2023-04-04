import arxiv as ar
import matplotlib.pyplot as plt

search = ar.Search(
    query='sciencedirect 2021',
    max_results=100,
)

l21 = []
for result in search.results():
    l21.append(result.journal_ref)

a = sum(x is not None for x in l21)
print('Ilość referencji dla sciencedirect 2021:', a)

# 2
search2 = ar.Search(
    query='sciencedirect 2011',
    max_results=100,
)
l11 = []
for result in search2.results():
    l11.append(result.journal_ref)

b = sum(x is not None for x in l11)
print('Ilość referencji dla sciencedirect 2011:', b)
# 3
search3 = ar.Search(
    query='IEEE',
    max_results=100,
)
l16 = []
lt = []

for result in search3.results():
    if type(result.journal_ref) is str:
        l16.append([result.journal_ref, result.title])
        print( [result.title, result.comment])
  

c = sum(x is not None for x in l16)

# plot
left = [1, 2, 3]
height = [a, b, c]
tick_label = ["sciencedirect 2021", "sciencedirect 2011", "IEEE"]
plt.bar(left, height, tick_label=tick_label, width=0.8,
        color=["orange", "green", "cyan"])
plt.ylabel('Ilość referencji')
plt.xlabel('Wyszukiwane hasło')
plt.show()
