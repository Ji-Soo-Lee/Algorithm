import sys

def div(paper, white, blue):
    color = set(sum(paper, []))
    
    if len(color) == 2:
        cuts = [[] for _ in range(4)]
        n = len(paper)//2
        for idx in range(n):
            cuts[0].append(paper[idx][:n])
            cuts[1].append(paper[idx][n:])
            cuts[2].append(paper[n + idx][:n])
            cuts[3].append(paper[n + idx][n:])

        for cut in cuts:
            white, blue = div(cut, white, blue)
    else:
        if color == {1}:
            blue += 1
        else:
            white += 1
        
    return white, blue
    
n = int(sys.stdin.readline().rstrip())
paper = []

for _ in range(n):
    paper.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))

white, blue = div(paper, 0, 0)

print(white)
print(blue)
