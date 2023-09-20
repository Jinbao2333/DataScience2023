text = "数据科学与工程导论"
text_width = len(text)
print(((chr)(0x2605) + " ") * (text_width + 3))
print(((chr)(0x2605) + "  ") + text + " ★")
print(((chr)(0x2605) + " ") * (text_width + 3))
