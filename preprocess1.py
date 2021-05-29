# 拆数据集

inputs = open('input/environment.txt', 'r', encoding='utf-8')

# outputs = open('output/a2.txt', 'w',encoding='utf-8')
n = 0
for line in inputs:
    line_seg = line[1:-2]  # 这里的返回值是字符串
    outputs = open('output/a'+str(n)+'.txt', 'w',encoding='utf-8')
    outputs.write(line_seg)
    outputs.close()
    n += 1
inputs.close()