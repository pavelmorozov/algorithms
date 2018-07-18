package codility.java;

/* 8min 50% */
public class CountDiv {
	public int solution(int A, int B, int K) {
		int counter = 0;

		for (int i = A; i <= B; i++) {
			if (i % K == 0) {

				int interval = B - i;
				counter = interval / K + 1;

				break;
			}
		}

		return counter;
	}
}
