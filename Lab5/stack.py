# stack.py module

def push(stack,ele):
  t = [x for x in stack]
  t.append(ele)
  return tuple(t)

def pop(stack):
  if isEmpty(stack):
    print("Cannot pop")
  return stack[:-1]

def isEmpty(stack):
  if(len(stack)==0):
    return True
  else:
    return False