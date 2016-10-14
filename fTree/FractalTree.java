/**
* Given a fractal binary tree.
* Cond1: Each node either has a binary value (0 or 1) or two child nodes.
* Cond2: At any point if you see a node that has both children of same value,
* you can delete the child nodes and
* replace the node with the child node’s value.
*/
class FractalTree{
  Node root = null;

  public FractalTree(){
    this.root = new Node();
  }

  public FractalTree(int rootVal){
    this.root = new Node();
    root.val = rootVal;
  }

  /**
  * Returns the value at given node, if it exists.
  */
  public int getValue(int[] route){
    // Check if tree exists.
    if (this.root == null){
      return -1;
    }
    // Go left for 0, Go right for 1
    Node cur = this.root;
    for(int i : route) {
      if (cur.val >= 0){
        // Cond1
        return cur.val;
      }
      else{
        if (i == 0){
          cur = cur.left;
        }
        else{
          cur = cur.right;
        }
      } // End if-else
    } // End for

    return cur.val;
  } // End function getValue

  public void setValue(int[] route, int val) throws Exception{
    // Check if it is an empty tree.
    if (this.root == null){
      throw new Exception("Empty Tree.");
    }
    Node cur = this.root;
    for(int i : route) {
      if (cur.val >= 0){
        // This is a compressed node (Cond2).
        // If new val is not equal to node's val, expand and set val
        // Otherwise, ignore.
        if (cur.val != val){
          // Create a sub-tree and add it here.
          cur = this.expandTreeAndSetVal(Arrays.copyOfRange(route, i, route.length), cur.val, val);
        }
      }
      else{
        if (i == 0){
          cur = cur.left;
        }
        else{
          cur = cur.right;
        }
      } // End if-else
    } // End for
  }

  private Node expandTreeAndSetVal(int[] route, int baseVal, int setVal){
    Node node = new Node();
    Node copy = node;
    for (int i : route) {
      node.left = new Node();
      node.right = new Node();
      if (i == 0){
        node.right.val = baseVal;
        node = node.left;
      }
      else{
        node.left.val = baseVal;
        node = node.right;
      } // END if-else
    } // END for

    node.val = setVal;
    return copy;
  }
}
