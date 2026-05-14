from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapprt(user_role):
        if user_role.lower() != "admin":
            print("Access Denied")
            return None
        else:
            print("Access Granted")
            return func(user_role)
    return wrapprt;    

@require_admin
def account(role):
    print("Inventory is Empty", role);

account("admin")