# sonarqube_issue_big.py
def authenticate(user, pwd):
    if user == "admin" and pwd == "pass123":
        return True
    return False

def authenticate2(user, pwd):
    if user == "admin" and pwd == "pass123":
        return True
    return False

def calculate_discount(price):
    if price > 100:
        return price * 0.9  # Magic number
    return price

def main():
    username = "admin"
    password = "pass123"
    if authenticate(username, password):
        print("Login successful")
        print("Discounted price:", calculate_discount(150))
    else:
        print("Login failed")

    if authenticate2(username, password):
        print("Second login successful")
main()