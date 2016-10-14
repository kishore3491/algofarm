package fTree;

class TestFractalTree {

	public static void main(String[] args) throws Exception {
		test1();
		test2();
		test3();
	}

	private static void test1() throws Exception {
		System.out.println("Test 1");
		FractalTree ft = new FractalTree(1);
		int[] a1 = { 0, 1, 1, 0 };
		int[] a2 = { 0 };
		int[] a3 = { 1 };
		int[] a4 = { 1, 1, 1 };
		System.out.println(ft.getValue(a2) == 1);
		System.out.println(ft.getValue(a1) == 1);
		System.out.println(ft.getValue(a2) != 0);
		System.out.println(ft.getValue(a3) == 1);
		System.out.println(ft.getValue(a4) == 1);
		System.out.println("End Test 1");
	}

	private static void test2() throws Exception {
		System.out.println("Test 2");
		FractalTree ft = new FractalTree(0, 1);
		ft.printTree();
		System.out.println("End Test 2");
	}

	private static void test3() throws Exception {
		System.out.println("Test 3");
		FractalTree ft = new FractalTree(0, 1);
		int[] route = { 1, 0, 1 };
		int setVal = 0;
		ft.setValue(route, setVal);
		ft.printTree();
		int val = ft.getValue(route);
		System.out.println("Value set correctly? :" + (setVal == val));
		System.out.println("End Test 3");
	}
}
