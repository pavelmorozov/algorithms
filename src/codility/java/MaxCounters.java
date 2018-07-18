package codility.java;
/* 30 min 40% */
public class MaxCounters {
    public int[] solution(int N, int[] A) {
    	
    	int[] counters = new int[N];
    	for (int i = 0; i< N; i++) {
    		counters[i]=0;
    	}
    	
    	int currentMax=0;
    	int updateMax=0;
    	for (int a:A) {
    		if (a>=1 && a<=N) {
				if (counters[a-1]<updateMax){
					counters[a-1]=updateMax+1;
				}else{
		    			counters[a-1]++;
				}
    			if (counters[a-1]>currentMax) currentMax=counters[a-1];
    		}else if (a==N+1) {
    			updateMax=currentMax;
    		}
    	}
    	
    	for (int i=0; i<counters.length; i++) {
    		if (counters[i]<updateMax) {
    			counters[i]=updateMax;
    		}
    	}
    	return counters;
    }
}
