import unittest
from bst import BST

class TestBST(unittest.TestCase):
    def setUp(self):
        self.bst = BST()
        for val in [10, 5, 15, 3, 7, 12, 18]:
            self.bst.insert(val)

    def test_insert_and_traversals(self):
        self.assertEqual(self.bst.inorder(), [3, 5, 7, 10, 12, 15, 18])
        self.assertEqual(self.bst.preorder(), [10, 5, 3, 7, 15, 12, 18])
        self.assertEqual(self.bst.postorder(), [3, 7, 5, 12, 18, 15, 10])
        self.assertEqual(self.bst.level_order(), [10, 5, 15, 3, 7, 12, 18])

    def test_search_and_contains(self):
        self.assertTrue(self.bst.search(7))
        self.assertFalse(self.bst.search(42))
        self.assertTrue(5 in self.bst)
        self.assertFalse(100 in self.bst)

    def test_delete(self):
        self.bst.delete(10)
        self.assertEqual(self.bst.inorder(), [3, 5, 7, 12, 15, 18])
        with self.assertRaises(ValueError):
            self.bst.delete(42)

    def test_reverse_traversals(self):
        self.assertEqual(self.bst.reverse("inorder"), [18, 15, 12, 10, 7, 5, 3])
        self.assertEqual(self.bst.reverse("preorder"), [10, 15, 18, 12, 5, 7, 3])
        self.assertEqual(self.bst.reverse("postorder"), [18, 15, 12, 7, 5, 3, 10])
        with self.assertRaises(ValueError):
            self.bst.reverse("invalid")

    def test_min_max_sum_count_height(self):
        self.assertEqual(self.bst.find_min(), 3)
        self.assertEqual(self.bst.find_max(), 18)
        self.assertEqual(self.bst.sum_nodes(), sum([10,5,15,3,7,12,18]))
        self.assertEqual(len(self.bst), 7)
        self.assertEqual(self.bst.height(), 3)

    def test_valid_and_depth_lca(self):
        self.assertTrue(self.bst.is_valid_bst())
        self.assertEqual(self.bst.get_depth(7), 2)
        self.assertEqual(self.bst.lowest_common_ancestor(3, 7), 5)

    def test_kth_and_from_list(self):
        self.assertEqual(self.bst.kth_smallest(3), 7)
        with self.assertRaises(ValueError):
            self.bst.kth_smallest(10)
        tree2 = BST.from_list([2,1,3])
        self.assertEqual(tree2.inorder(), [1,2,3])

    def test_pretty_print(self):
        empty = BST()
        empty.pretty_print()  # Should not error
        self.bst.pretty_print()

class TestBSTEdgeCases(unittest.TestCase):
    def test_empty_tree(self):
        empty = BST()
        self.assertEqual(empty.inorder(), [])
        self.assertEqual(empty.preorder(), [])
        self.assertEqual(empty.postorder(), [])
        self.assertEqual(empty.level_order(), [])
        self.assertFalse(empty.search(5))
        self.assertEqual(empty.reverse("inorder"), [])
        self.assertEqual(len(empty), 0)
        self.assertEqual(empty.sum_nodes(), 0)
        self.assertEqual(empty.height(), 0)
        with self.assertRaises(ValueError):
            empty.find_min()
        with self.assertRaises(ValueError):
            empty.find_max()
        with self.assertRaises(ValueError):
            empty.delete(1)
        with self.assertRaises(ValueError):
            empty.get_depth(1)

    def test_single_node_tree(self):
        single = BST()
        single.insert(42)
        self.assertEqual(single.inorder(), [42])
        self.assertEqual(single.reverse("preorder"), [42])
        self.assertTrue(single.search(42))
        self.assertEqual(single.find_min(), 42)
        self.assertEqual(single.find_max(), 42)
        self.assertEqual(single.height(), 1)
        single.delete(42)
        self.assertFalse(single)

    def test_skewed_trees(self):
        skew = BST.from_list([1,2,3,4,5])
        self.assertEqual(skew.height(), 5)
        self.assertEqual(skew.get_depth(5), 4)
        skew.delete(3)
        self.assertFalse(3 in skew)
        skew2 = BST.from_list([5,4,3,2,1])
        self.assertEqual(skew2.height(), 5)
        self.assertTrue(skew2.search(1))
        skew2.insert(0)
        self.assertEqual(skew2.find_min(), 0)

    def test_invalid_parameters(self):
        bst = BST.from_list([10,20,30])
        with self.assertRaises(ValueError):
            bst.reverse("foo")
        with self.assertRaises(ValueError):
            bst.to_list("bar")
        with self.assertRaises(ValueError):
            bst.kth_smallest(0)
        with self.assertRaises(ValueError):
            bst.kth_smallest(10)

if __name__ == '__main__':
    unittest.main()
