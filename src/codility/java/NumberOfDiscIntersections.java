package codility.java;

import java.util.Arrays;

/*
 * 92 m, find python coded solution 81% 
 * (because no proper long cast implemented)
 * and I missed task about > 10 000 000 return -1
 */
public class NumberOfDiscIntersections {
	
	public class Event implements Comparable<Event>{
		long coordinate;
		boolean begin;
		@Override
		public int compareTo(Event e) {
			if (this.coordinate < e.coordinate){
				return -1;
			} else if (this.coordinate == e.coordinate) {
				if (this.begin==true) return -1;
				else return 1;
			}else return 1;
		}
	}
	
	public int solution(int[] A) {
		Event[] events = new Event[A.length*2];
		for (int i=0; i<A.length; i++){
			Event event = new Event();
			event.coordinate = ((long)i-A[i]);
			event.begin=true;
			events[2*i] = event;
			event = new Event();
			event.coordinate = ((long)i+A[i]);
			event.begin=false;
			events[2*i+1] = event;
		}
		
		Arrays.sort(events);
		
		int intersections=0;
		int activeCircles=0;
		for (int i=0; i<events.length; i++){
			int countDelta = (events[i].begin==true) ? 1 : -1;
			if (countDelta>0){
				intersections += activeCircles*countDelta;				
			}
			activeCircles += countDelta;
			if (intersections > 10000000) return -1;
		}
		
		return intersections;
    }
}

