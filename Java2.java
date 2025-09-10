public class IssueDemo {
    public static boolean login(String u, String p) {
        int unused = 42; // Unused variable
        if (u.equals("admin") && p.equals("1234")) { // Hardcoded credentials
            return true;
        }
        return false;
    }

    public static boolean login2(String u, String p) {
        if (u.equals("admin") && p.equals("1234")) { // Duplicate logic
            return true;
        }
        return false;
    }

    public static void main(String[] args) {
        String user = "admin";
        String pass = "1234";
        if (login(user, pass)) {
            System.out.println("Logged in!");
        }
        if (login2(user, pass)) {
            System.out.println("Logged in again!");
        }
        System.out.println(100); // Magic number
    }
}