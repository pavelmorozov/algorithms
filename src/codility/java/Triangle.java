package codility.java;

import java.util.Arrays;
/*
 * 24min. Find solution on web and implemented
 */
public class Triangle {
    public int solution(int[] A) {
    	
    	Arrays.sort(A);
    	
    	for (int i=0; i<A.length-2; i++){
    		if ((long)A[i]+A[i+1]>A[i+2]) return 1;
    	}
    	return 0;
    }
}
