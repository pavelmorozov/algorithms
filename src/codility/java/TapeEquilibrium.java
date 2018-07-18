package codility.java;

import java.util.Arrays;

/*30 minutes*/
public class TapeEquilibrium {
	public int solution(int[] a){
		Integer sum = 0;
		for (int value: a){
			sum+=value;
		}
		int sumLeft=0;
		int sumRight;
		int minDifference=0;
		for (int p=1;p<a.length;p++){
			sumLeft += a[p-1];
			sumRight = sum-sumLeft;
			int difference = Math.abs(sumLeft-sumRight);
			if (p==1){
				minDifference=difference;				
			}else{
				if (difference<minDifference){
					minDifference = difference;
				} 
			}
		}
		
		return minDifference;
	}
}
