def deleteNode(root, key):
  if not root:
    return None
  if root.val == key:
    left = root.left
    right = root.right
    if not left:
      return right
    if not right:
      return left
    target = right
    while target.left:
      target = target.left
    target.left = left
    return right
  if root.val > key:
    root.left = deleteNode(root.left, key)
  elif root.val < key:
    root.right = deleteNode(root.right, key)
  return root

def deleteNode2(root, key):
  if not root:
    return None
  if root.val == key:
    left = root.left
    right = root.right
    if not left:
      return right
    if not right:
      return left
    target = right
    while target.left:
      target = target.left
    root.val = target.val
    root.right = deleteNode2(right, target)
  if root.val > key:
    root.left = deleteNode2(root.left, key)
  elif root.val < key:
    root.right = deleteNode2(root.right, key)
  return root