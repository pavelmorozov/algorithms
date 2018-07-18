package codility.java;

import java.util.Arrays;

public class Starter {
	public static void main(String[] args) {
		System.out.println("Hello Codility!");
		int[] input = {3,1,2,4,3};
		TapeEquilibrium tapeEquilibrium = new TapeEquilibrium();
		int result = tapeEquilibrium.solution(input);
		System.out.println("TapeEquilibrium result is: "+result);
		
		FrogJump frogJump = new FrogJump();
		result = frogJump.solution(10, 85, 30);
		System.out.println("FrogJump result is: "+result);
		
		BinaryGap binaryGap = new BinaryGap();
		result = binaryGap.solution(20);
		System.out.println("BinaryGap result is: "+result);
		
		int[] input1 = {9, 3, 9, 3, 9, 7, 9};
		OddOccurrencesInArray oddOccurrencesInArray = new OddOccurrencesInArray();
		result = oddOccurrencesInArray.solution(input1);
		System.out.println("OddOccurrencesInArray result is: "+result);
		
		int[] input2 = {3, 8, 9, 7, 6};
		int k = 5;
		CyclicRotation cyclicRotation = new CyclicRotation();
		int[] result1 = cyclicRotation.solution(input2, k);
		System.out.println("CyclicRotation result is: "+Arrays.toString(result1));
		
		//////////////////
		PermMissingElem permMissingElem = new PermMissingElem();
		int[] a = {2,3,1,5};
		result = permMissingElem.solution(a, 4);
		System.out.println("PermMissingElem result is: "+result);
		PermCheck permCheck = new PermCheck();
		int[] b = {4,1,3,2};
		result = permCheck.solution(b);
		System.out.println("PermCheck result is: "+result);
		int[] c = {4,1,3};
		result = permCheck.solution(c);
		System.out.println("PermCheck result is: "+result);
		int[] d = {4,1,3,3,5};
		result = permCheck.solution(d);
		System.out.println("PermCheck result is: "+result);
		FrogRiverOne frogRiverOne = new FrogRiverOne();
		int[] e= {1,3,1,4,2,3,5,4};
		int x = 5;
		result = frogRiverOne.solution(x, e);
		System.out.println("FrogRiverOne result is: "+result);
		MissingInteger missingInteger = new MissingInteger();
		int[] f = {1,3,6,4,1,2,-1};
		result = missingInteger.solution(f);
		System.out.println("MissingInteger result is: "+result);
		MaxCounters maxCounters = new MaxCounters();
		int[] g = {3,4,4,6,1,4,4};
		int n = 5;
		int[] resultArray;
		resultArray = maxCounters.solution(n, g);
		System.out.println("MaxCounters result is: "+Arrays.toString(resultArray));
		CountDiv countDiv = new CountDiv();
		result = countDiv.solution(6, 11, 2);
		System.out.println("CountDiv result is: "+result);
		PassingCars passingCars = new PassingCars();
		int[] h = {0,1,0,1,1};
		result = passingCars.solution(h);
		System.out.println("PassingCars result is: "+result);
		
		GenomicRangeQuery genomicRangeQuery = new GenomicRangeQuery();
//		String S = "CAGCCTA";
//		int[] P = {2,5,0};
//		int[] Q = {4,5,6};
//		String S = "C";
//		int[] P = {0};
//		int[] Q = {0};
		String S = "CG";
		int[] P = {0,0,1};
		int[] Q = {0,1,1};		
		System.out.println("GenomicRangeQuery :"+Arrays.toString(genomicRangeQuery.solution(S, P, Q)));
		
		MinAvgTwoSlice minAvgTwoSlice = new MinAvgTwoSlice();
		int[] i = {4,2,2,5,1,5,8};
		result = minAvgTwoSlice.solution(i);
		System.out.println("MinAvgTwoSlice result is: "+result);
		
		MaxProductOfThree maxProductOfThree = new MaxProductOfThree();
		int[] A = {-3,1,2,-2,5,6};
		result = maxProductOfThree.solution(A);
		System.out.println("MaxProductOfThree result is: "+result);
		
		Triangle triangle = new Triangle();
		int[] A1 = {10,2,5,1,8,20};
		result = triangle.solution(A1);
		System.out.println("Triangle result is: "+result);
		int[] A2 = {10,50,5,1};
		result = triangle.solution(A2);
		System.out.println("Triangle result is: "+result);
		
		NumberOfDiscIntersections numberOfDiscIntersections = new NumberOfDiscIntersections();
		int[] A3 = {1,5,2,1,4,0};
		result = numberOfDiscIntersections.solution(A3);
		System.out.println("NumberOfDiscIntersections result is: "+result);
	}
}
