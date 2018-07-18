package codility.java;

import java.util.LinkedHashMap;
import java.util.Map;
/*21 m*/
public class OddOccurrencesInArray {
	public int solution(int[] A) {

		Map<Integer, Integer> valuesMap = new LinkedHashMap<Integer, Integer>();
		
		for (Integer i=0; i<A.length; i++){
			Integer value = A[i];
			if (valuesMap.containsKey(value)){
				valuesMap.remove(value);
			}else{
				valuesMap.put(value, i);
			}
		}
		
		return valuesMap.entrySet().iterator().next().getKey();
    }
}
