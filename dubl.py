rez = []
s = [{'key1': 'value1'}, {'k1': 'v1', "k2": "v2", "k3": "v3"}, {}, {}, {"key1": "value1"}, {"key1": "value1"}, {"key2": "value2"}]
for val in s:
    if val not in rez:
        rez.append(val)
print(rez)
