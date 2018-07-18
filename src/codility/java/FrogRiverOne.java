package codility.java;

import java.util.HashSet;
import java.util.Set;

/* 19 min */
public class FrogRiverOne {
    public int solution(int X, int[] A) {
    	
    	Set<Integer> positions = new HashSet<>();
    	
    	for (Integer second = 0; second < A.length; second++) {
    		if (A[second]>0 && A[second]<=X) {
    			positions.add(A[second]);
    			
    			if (positions.size()==X) {
    				//Done
    				return second;
    			}
    		}
    	}
    	
    	return -1;
    }
}
