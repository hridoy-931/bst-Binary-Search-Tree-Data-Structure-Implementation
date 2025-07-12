from bst import BST

bst = BST()
for val in [10, 5, 15, 3, 7,16,87,98,56,32, 1, 9]:
    bst.insert(val)
print("Inorder:", bst.inorder())

print(bst.pretty_print())