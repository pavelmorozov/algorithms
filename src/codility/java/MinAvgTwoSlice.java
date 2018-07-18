package codility.java;

/*
 * Algortithm was not clear initially
 */
public class MinAvgTwoSlice {
	public int solution(int[] A) {
		
		if (A.length<2) return -1;
		
		int minIndex;
		float minValue;

		minIndex=0;
		minValue=(float)(A[0]+A[1])/2;
		
		for (int i=0; i<=A.length; i++){
			if (i+1<A.length){
				float avg=(float)(A[i]+A[i+1])/2;
				if (avg<minValue){
					minIndex=i;
					minValue=avg;
				}
			}
			if (i+2<A.length){
				float avg=(float)(A[i]+A[i+1]+A[i+2])/3;
				if (avg<minValue){
					minIndex=i;
					minValue=avg;
				}
			}
		}

		return minIndex;
	}
}
