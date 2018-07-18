package codility.java;
/* 15 min */
public class FrogJump {
	public int solution(int X, int Y, int D){
		int jumpsNumber=0;
		if ((Y-X)%D==0){
			jumpsNumber = (Y-X)/D;			
		}else{
			jumpsNumber = (Y-X)/D+1;
		}
		return jumpsNumber;
	}
}
