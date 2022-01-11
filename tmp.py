f = open('/Users/ryutani18/Dropbox/My Mac (RyuheiのMacBook Pro)/Desktop/python_lesson/tmp.txt','r')

h,w = map(int,f.readline().split(' '))

board=[]
for _ in range(h):
  board.append(list(map(int,f.readline().split(' '))))

if h==1:
  print(max(board[0]))
  exit()


def getMaxVal(board,row,col):
  max_val=0
  if col>0:
    max_val=max(max_val,board[row][col-1])

  max_val=max(max_val,board[row][col])

  if col<len(board[row])-1:
    max_val=max(max_val,board[row][col+1])

  return max_val

dp = [[0]*w for _ in range(h)]

for i in range(h-1):
  for j in range(w):
    if i==0:
      dp[i][j]=board[i][j]

    dp[i+1][j]= getMaxVal(dp,i,j)+board[i+1][j]

print(dp)

print(max(dp[h-1]))
