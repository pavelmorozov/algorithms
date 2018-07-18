package codility.java;

import java.util.HashSet;
import java.util.Set;

/*21 min*/
public class PermCheck {
	
	public int solution(int[] A) {
		
		Set<Integer> sampleSet = new HashSet<>();
		for (Integer i = 1; i <= A.length; i++) {
			sampleSet.add(i);
		}
		
		Boolean existFlag;
		for (Integer i: A) {
			existFlag = sampleSet.remove(i);
			if (!existFlag) {
				return 0;
			}
		}
		
		if (sampleSet.size()>0) return 0;
		
		return 1;
    }
	
}
