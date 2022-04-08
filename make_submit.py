submit_ans = []
one_dic = {"symptom": [], "disease":""}
with open('save.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        if "symptom" in line:
            one_dic['symptom'].append(line.split('@@@')[1].strip())
        if "disease" in line:
            one_dic['disease'] = line.split('@@@')[1].strip()

print(one_dic['symptom'])
print(one_dic['disease'])
