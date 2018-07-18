package codility.java;

import java.util.Arrays;

// 12 min
public class MaxProductOfThree {
    public int solution(int[] A) {
       Arrays.sort(A);
       
       int max1 = A[0]*A[1]*A[A.length-1];
       int max2 = A[A.length-3]*A[A.length-2]*A[A.length-1];
       
       return (max1>max2) ? max1 : max2;
    }
}
