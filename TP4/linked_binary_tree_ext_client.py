from apython_ed_fcad_uner.data_structures.trees.linked_binary_tree import LinkedBinaryTree
from LinkedBinaryTreeExt import LinkedBinaryTreeExt
from apython_ed_fcad_uner.data_structures.trees.binary_tree_node import BinaryTreeNode

nodo_a = BinaryTreeNode('A')
nodo_b = BinaryTreeNode('B')
nodo_c = BinaryTreeNode('C')
nodo_d = BinaryTreeNode('D')
nodo_f = BinaryTreeNode('F')
nodo_g = BinaryTreeNode('G')
nodo_h = BinaryTreeNode('H')
nodo_i = BinaryTreeNode('I')
nodo_j = BinaryTreeNode('J')
nodo_k = BinaryTreeNode('J')
nodo_m = BinaryTreeNode('K')
nodo_n = BinaryTreeNode('N')

arbol = LinkedBinaryTreeExt()
arbol.add_left_child(None, nodo_a)

arbol.add_left_child(nodo_a, nodo_b)
arbol.add_right_child(nodo_a, nodo_f)

arbol.add_left_child(nodo_b, nodo_c)
arbol.add_right_child(nodo_b, nodo_d)

arbol.add_left_child(nodo_f, nodo_g)
arbol.add_right_child(nodo_f, nodo_k)

arbol.add_left_child(nodo_g, nodo_h)
arbol.add_right_child(nodo_g, nodo_i)

arbol.add_left_child(nodo_k, nodo_m)
arbol.add_right_child(nodo_k, nodo_n)

print(arbol)
print ("METODO HERMANOS: ","Son hermanos" if arbol.hermanos(nodo_b, nodo_f) == True else "No son hermanos")

lista_hojas = arbol.hojas()
print("LISTA DE NODOS HOJAS: ", lista_hojas)

lista_internos = arbol.internos()
print("LISTA DE NODOS INTERNOS",lista_internos)

print("PROFUNDIDAD DEL NODO M:", arbol.profundidad(nodo_m))
print("ALTURA DEL NODO A:", arbol.altura(nodo_a))