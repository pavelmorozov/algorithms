package testDome;

import java.util.Arrays;

public class SortedSearch {
//    public static int countNumbers(int[] sortedArray, int lessThan) {
//    	if (sortedArray.length==0) {
//    		return 0;
//    	}
//
//    	
//    	if (sortedArray[0]>=lessThan) return 0;
//
//    	int idx = sortedArray.length/2;
//
//    	int begin = 0;
//    	int end = sortedArray.length-1;
//    	while (begin!=idx && end!=idx) {
//	    	if (sortedArray[idx]<lessThan) {
//	    		//go right
//	    		begin = idx;
//	    		idx = (end-idx)/2+idx ;
//	    	}else {
//	    		//go left
//	    		end = idx;
//	    		idx = (idx-begin)/2+begin;
//	    	}
//    	}
//    	return idx+1;
//    }

	public static int countNumbers(int[] sortedArray, int lessThan) {
		if (sortedArray.length == 0 ) return 0;
		int left = 0, right = sortedArray.length;
		int mid = 0;
		while (left < right) {
			mid = (right + left) / 2;
			if (sortedArray[mid] == lessThan) {
				while (mid>=0 && sortedArray[mid] == lessThan) 
					mid--;
				break;
			}
			else if (sortedArray[mid] > lessThan)
				right = mid;
			else
				left = mid + 1;
		}
		while (mid > -1 && sortedArray[mid] >= lessThan)
			mid--;
		return mid + 1;
	}

	public static void main(String[] args) {

		System.out.println(SortedSearch.countNumbers(new int[] { 4, 5, 6 }, 4)); // 0
		
		System.out.println(SortedSearch.countNumbers(new int[] { 1, 2, 3 }, 4)); // 3

		System.out.println(SortedSearch.countNumbers(new int[] {}, 4)); // 0
		System.out.println(SortedSearch.countNumbers(new int[] { 5 }, 4)); // 0
		System.out.println(SortedSearch.countNumbers(new int[] { 3 }, 4)); // 1

		
		System.out.println(SortedSearch.countNumbers(new int[] { 1, 3, 3, 5, 7 }, 4)); // 3
		System.out.println(SortedSearch.countNumbers(new int[] { 1, 3, 5, 7 }, 4)); // 2
	}
}