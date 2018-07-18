package codility.java;
/* 25 min. 80% Tailing zeros */
public class BinaryGap {
	int solution(int N){
		String binaryString = Integer.toBinaryString(N);
		int longestGapLength=0;
		int currentGapLength=0;
		for (int i=0; i<binaryString.length(); i++){
			char c = binaryString.charAt(i);
			if (c=="0".charAt(0)){
				currentGapLength++;
			}else{
				if (longestGapLength<=currentGapLength){
					longestGapLength=currentGapLength;
				}				
				currentGapLength=0;
			}
		}
		return longestGapLength;
	}
}
