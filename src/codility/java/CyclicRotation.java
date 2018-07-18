package codility.java;

/*41m*/
public class CyclicRotation {
    public int[] solution(int[] A, int K) {
    	int[] result = new int[A.length];
    
    	for(int i=0; i<A.length; i++){
    		int value = A[i];
    		
    		int reminder = K%A.length;
    		if ((i+reminder)>=A.length){
    			result[i+reminder-A.length]=value;
    		}else{
    			result[i+reminder]=value;
    		}
    	}
    
    	return result;
    }
}
