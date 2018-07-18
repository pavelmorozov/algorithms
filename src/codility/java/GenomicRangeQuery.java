package codility.java;

/*
 * 14:05 31 m time complexity limit not passed
 * 17 more minutes - test passed but bug if just one
 * char in string
 * new bug 2 char string
 * Need to check once more for simplest solution
 * and train to get result faster than 30 minutes  
 */
public class GenomicRangeQuery {
	public int[] solution(String S, int[] P, int[] Q) {
		
		int[][] tempArray = new int [S.length()][4];
		int[] result = new int [P.length];
		
		for (int i=0; i<S.length(); i++){
			int factor;
			if ((S.charAt(i))=='A') factor = 1;
			else if ((S.charAt(i))=='C') factor = 2;
			else if ((S.charAt(i))=='G') factor = 3;
			else factor = 4;
			
			for (int j=0; j<4; j++){
				if (i==0){
					if (j==factor-1) tempArray[i][j] = 1;						
					else tempArray[i][j] = 0;
				}else{
					if (j==factor-1){
						tempArray[i][j] = tempArray[i-1][j]+1;
					}else{
						tempArray[i][j] = tempArray[i-1][j];
					}
				}
			}
		}
				
		for (int i=0; i<P.length; i++){
			int x = P[i];
			int y = Q[i];

			for (int j=0; j<4; j++){
				
				int sub = 0;
				if (x>0) sub = tempArray[x-1][j];

				if (tempArray[y][j]-sub>0){
					result[i] = j+1;
					break;
				}
			}
		}
		
		return result;
    }
}
