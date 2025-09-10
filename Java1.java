// CleanDemo.java
public class CleanDemo {
    /**
     * Authenticates a user with provided credentials.
     * @param username The username.
     * @param password The password.
     * @return true if credentials are valid, false otherwise.
     */
    public static boolean authenticate(String username, String password) {
        // In real applications, use secure credential storage
        return "admin".equals(username) && "securePass".equals(password);
    }

    public static void main(String[] args) {
        String username = "admin";
        String password = "securePass";
        if (authenticate(username, password)) {
            System.out.println("Authentication successful.");
        } else {
            System.out.println("Authentication failed.");
        }
    }
}