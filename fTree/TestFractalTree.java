class TestFractalTree {

  public static void main(String[] args){
    test1();
  }

  public void test1(){
    FractalTree fTree = new FractalTree(1);
    assert(fTree.getValue({0,1,1,0}) == 1);
    assert(fTree.getValue({0}) == 1);
    assert(fTree.getValue({1) == 1);
    assert(fTree.getValue({1,1,1}) == 1);
  }
}
