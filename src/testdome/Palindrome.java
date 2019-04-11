package testDome;

public class Palindrome {
    public static boolean isPalindrome(String word) {
        String lowcaseWord = word.toLowerCase();
        for (int i = 0; i<= lowcaseWord.length()/2; i++) {
        	if (lowcaseWord.charAt(i)!=lowcaseWord.charAt(lowcaseWord.length()-1- i)) return false; 
        } 
        return true;
    }
    
    public static void main(String[] args) {
        System.out.println(Palindrome.isPalindrome("Deleveled"));
    }
}