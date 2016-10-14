package fTree;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

/**
 * Given a fractal binary tree. Cond1: Each node either has a binary value (0 or
 * 1) or two child nodes. Cond2: At any point if you see a node that has both
 * children of same value, you can delete the child nodes and replace the node
 * with the child node's value.
 */
class FractalTree {
	Node root = null;

	// Ensure Tree maintains equilibrium at creation.
	public FractalTree(int leftVal, int rightVal) {
		this.root = new Node();
		if(leftVal == rightVal){
			root.val = leftVal;
		}
		else{
			root.left = new Node(leftVal);
			root.right = new Node(rightVal);
		}
	}

	public FractalTree(int rootVal) {
		this.root = new Node();
		root.val = rootVal;
	}

	/**
	 * Returns the value at given node, if it exists.
	 * @throws Exception 
	 */
	public int getValue(int[] route) throws Exception {
		// Go left for 0, Go right for 1
		Node cur = this.root;
		for (int i : route) {
			if (cur == null) {
				throw new Exception("Empty Tree/Subtree: Invalid route..");
			}
			if (cur.val >= 0) {
				// Cond1
				return cur.val;
			} else {
				if (i == 0) {
					cur = cur.left;
				} else {
					cur = cur.right;
				}
			} // End if-else
		} // End for

		return cur != null ? cur.val : -1;
	} // End function getValue

	public void setValue(int[] route, int val) throws Exception {
		Node cur = this.root;
		// Make a shallow copy.
		Node copy = cur;
		Node parent = null;
		for (int i=0; i < route.length; i++) {
			if (cur == null) {
				throw new Exception("Empty Tree/Subtree: Invalid route..");
			}
			if (cur.val >= 0) {
				// This is a compressed node (Cond2).
				// If new val is not equal to node's val, expand and set val
				// Otherwise, ignore.
				if (cur.val != val) {
					if (i > 0){	// No need to check if parent is empty now.
						int baseVal = cur.val;
						cur = parent;
						// Create a sub-tree and add it here.
						if(route[i-1] == 0){
							cur.left = this.expandTreeAndSetVal(Arrays.copyOfRange(route, i, route.length), baseVal, val);
						}
						else{
							cur.right = this.expandTreeAndSetVal(Arrays.copyOfRange(route, i, route.length), baseVal, val);
						}
					}
					else{
						// Replace root with new sub-tree.
						cur = this.expandTreeAndSetVal(Arrays.copyOfRange(route, i+1, route.length), cur.val, val);
					}
				}
				break;	// End for loop
			} else {
				parent = cur;
				if (route[i] == 0) {
					cur = cur.left;
				} else {
					cur = cur.right;
				}
			} // End if-else
		} // End for
		this.root = copy;
	}

	private Node expandTreeAndSetVal(int[] route, int baseVal, int setVal) {
		Node node = new Node();
		// Make a shallow copy.
		Node copy = node;
		for (int i : route) {
			node.left = new Node();
			node.right = new Node();
			if (i == 0) {
				node.right.val = baseVal;
				node = node.left;
			} else {
				node.left.val = baseVal;
				node = node.right;
			} // END if-else
		} // END for

		node.val = setVal;
		
		return copy;
	}
	
	public void printTree(){
		printTree(this.root);
	}
	public void printTree(Node cur) {
		Queue<Node> queue = new LinkedList<Node>();
		queue.add(cur);
		int nodesInCurrentLevel = 1;
		int nodesInNextLevel = 0;
		while (!queue.isEmpty()) {
			cur = queue.remove();
			nodesInCurrentLevel -= 1;
			if (cur != null) {
				if (cur.val < 0) {
					queue.add(cur.left);
					queue.add(cur.right);
					nodesInNextLevel += 2;
				}
				System.out.print(cur.val + "  ");
			}
			if (nodesInCurrentLevel == 0){
				System.out.println();
				nodesInCurrentLevel = nodesInNextLevel;
				nodesInNextLevel = 0;
			}
		} // End while
	}
}
