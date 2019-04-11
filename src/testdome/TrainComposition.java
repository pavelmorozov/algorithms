package testDome;

import java.util.LinkedList;
import java.util.List;

public class TrainComposition {
	
	private final List<Integer> wagons = new LinkedList<>();
	
    public void attachWagonFromLeft(int wagonId) {
    	wagons.add(0, wagonId);
    }

    public void attachWagonFromRight(int wagonId) {
    	wagons.add(wagonId);
    }

    public int detachWagonFromLeft() {
    	return wagons.remove(0);
    }

    public int detachWagonFromRight() {
    	return wagons.remove(wagons.size()-1);
    }

    public static void main(String[] args) {
        TrainComposition tree = new TrainComposition();
        tree.attachWagonFromLeft(7);
        tree.attachWagonFromLeft(13);
        System.out.println(tree.detachWagonFromRight()); // 7 
        System.out.println(tree.detachWagonFromLeft()); // 13
    }
}