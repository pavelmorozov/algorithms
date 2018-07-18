package codility.java;
/* 33 min 100% */
public class PassingCars {
    public int solution(int[] A) {
    	//int[] sum = new int[A.length];
    	int multiplier = 0;
    	int pairs=0;
    	for (int i=0; i<A.length; i++) {
    		if (A[i]==0) {
    			multiplier++;
    		}else {
    			pairs += A[i]*multiplier;
    		}
    		if (pairs>1000000000){
    			return -1;
    		}
    	}
    	return pairs;
    }
}
