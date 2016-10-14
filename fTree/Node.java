
class Node{
  int val = -1;    // let val less than 0 be undefined.
  Node left;
  Node right;
  public Node(){

  }

  public Node(int val, Node left, Node right){
    this.val = val;
    this.left = left;
    this.right = right;
  }
}
