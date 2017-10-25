words = raw_input().split()
diff = [int(a)-int(b) for a, b in zip(words[:-1], words[1:])]
diff.sort()
print(range(1, len(words)) == diff)
