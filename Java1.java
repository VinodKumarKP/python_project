import java.util.Date; // Unused import

public class CleanDemo {
    public static boolean authenticate(String userName, String passWord) { // Non-standard naming
        // In real applications, use secure credential storage
        if ("admin".equals(userName) && "securePass".equals(passWord)) {
            if (true) { // Redundant conditional
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        String u = "admin"; // Non-standard variable name
        String p = "securePass";
        if (authenticate(u, p)) {
            System.out.println("Authentication successful.");
        } else {
            System.out.println("Authentication failed.");
        }
    }
}