# Enter your code here. Read input from STDIN. Print output to STDOUT
# This solution is a total cheat because it uses data structures that were not expected
N = int(raw_input())
scores = {}

# Populate the dictionary
for _ in range(N):
    name = raw_input()
    score = float(raw_input())
    
    if not scores.has_key(score):
        scores[score] = []
    scores[score].append(name)
    
# Find the second highest score
uniq = {}
map(uniq.__setitem__, scores.keys(), [])
key = sorted(uniq.keys())[1]

# Print the names
for name in sorted(scores[key]):
    print name
