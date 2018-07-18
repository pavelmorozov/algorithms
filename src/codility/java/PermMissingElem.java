package codility.java;

import java.util.HashSet;
import java.util.Set;

/*30 min 100%*/
public class PermMissingElem {
	public int solution(int A[], int N) {
		
		int result = 0;
		
		Set<Integer> sampleSet = new HashSet<>();
		for (Integer i=1; i<=A.length+1; i++) {
			sampleSet.add(i);
		}
		
		for (Integer i:A) {
			boolean found = sampleSet.remove(i);
		}
		
		result = sampleSet.iterator().next();
		return result;
	}
}

