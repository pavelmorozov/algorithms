package codility.java;

import java.util.HashSet;
import java.util.Set;

/*20 min*/
public class MissingInteger {
    public int solution(int[] A) {
    	Set<Integer> values = new HashSet();
    	for (Integer a:A) {
    		values.add(a);
    	}
    	
    	Integer i = 1;
    	while (i>0) {
    		if (!values.contains(i)) {
    			break;
    		}
    		i++;
    	}
    	
    	return i;
    }
}
