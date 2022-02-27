from tkinter.messagebox import YES


a=input()
b=input()
def ann(a):
  return ''.join(sorted(a))

if ann(a) in ann(b):
    print(YES)
else:
    print("NO")
