package Microsoft.Arrays&Strings;
import java.lang.*;
public class isPalindrome {
    // Could reverse the string and check if it is a palindrome

    // Could also have two pointers and check instead to save memory
    static boolean isAlphaNum(char c) {
        if ((48<= c && c <= 57) || (65 <= c && c <= 90) || (97 <= c && c <= 122)) {
            return true;
        }
        return false;
    }

    static char lower(char c) {
        if (65 <= c && c <= 90)
            return (char)(c+32);
        else
            return c;
    }

    public static boolean validPalindrome (String s) {
        int start = 0, end = s.length()-1;

        while (start < end) {
            while (start < end && !isAlphaNum(s.charAt(start))) {
                start++;
            }
            while (start < end && !isAlphaNum(s.charAt(end))) {
                end--;
            }
            if (lower(s.charAt(start)) != lower(s.charAt(end))) {
                return false;
            }

            start++;
            end--;
        }
        return true;
    } 

}
