def AllConstruct(target, words):
  if target == "":
    return [[]]
  
  table = [[] for _ in range(len(target) + 1)]
  table[0] = [[]]

  for i in range(len(table)):
      for word in words:
        if word == target[i: i + len(word)]:
          newResult = [result + [word] for result in table[i]]
          table[i + len(word)].extend(newResult)

  return table[len(target)]


print(AllConstruct("abcdef", ["ab", "abc", "c", "def", "abcd"]))