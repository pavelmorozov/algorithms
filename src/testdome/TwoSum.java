package testDome;

import java.util.HashMap;
import java.util.Map;

public class TwoSum {
	
	
	
    public static int[] findTwoSum(int[] list, int sum) {

        Map<Long, Integer> complements = new HashMap<>();

        for (int i = 0; i < list.length; i++) {
            Integer complementIndex = complements.get((long)list[i]);
            if (complementIndex != null) {
                return new int[]{complementIndex, i};
            }

            // it's possible that for large targets and a negative input
            // that we might overflow the int type
            long complement = (long)sum - list[i];
            complements.put(complement, i);
        }

        return null;
    }

    public static void main(String[] args) {
        int[] indices = findTwoSum(new int[] { 3, 1, 5, 7, 5, 9 }, 10);
        if(indices != null) {
            System.out.println(indices[0] + " " + indices[1]);
        }
    }
}