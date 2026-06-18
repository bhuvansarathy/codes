import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Read the entire line of text (including spaces)
        String input = scanner.nextLine();
        
        String result = reverseCase(input);
        System.out.println(result);
        
        scanner.close();
    }

    public static String reverseCase(String str) {
        StringBuilder output = new StringBuilder();

        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);

            if (Character.isUpperCase(ch)) {
                output.append(Character.toLowerCase(ch));
            } 
            else if (Character.isLowerCase(ch)) {
                output.append(Character.toUpperCase(ch));
            } 
            else {
                output.append(ch);
            }
        }

        return output.toString();
    }
}
