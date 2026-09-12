##### DAY 2 — Decision Making & Business Logic #####
# Plan - Monthly Usage 
# free -  100
# pro  -  1,000
# business -  10,000
# enterprise - sınırsız

users = [
 {
    "plan": "pro",
    "is_active": True,
    "payment_status": "paid",
    "monthly_usage": 72
},
  {
    "plan": "free",
    "is_active": True,
    "payment_status": "unpaid",
    "monthly_usage": 20
},
   {
    "plan": "business",
    "is_active": False,
    "payment_status": "paid",
    "monthly_usage": 100
},

]

plan_features = {
    "free": ["basic_search"],
    "pro": ["basic_search", "advanced_search", "export"],
    "business": ["basic_search", "advanced_search", "export", "team"],
    "enterprise": ["basic_search", "advanced_search", "export", "team", "priority_support"]
}

# User inactive ise --> Access denied: account inactive
# Payment "failed" veya "unpaid" ise --> Access denied: payment failed
# Kullanici aktif ve ödeme sorunu yoksa plan limitine bak, limit aşılmışsa --> Access denied: usage limit reached
# Her şey uygunsa --> Access granted: welcome to the platform
def can_use_service(user):
    if not user["is_active"]:
        return "Access denied: account inactive"
    if user["payment_status"] != 'paid':
        return "Access denied: payment failed"
    
    plan_limit = {
        "free": 100,
        "pro": 1000,
        "business": 10000,
        "enterprise": float('inf')  # sınırsız
    }
    
    if user["monthly_usage"] > plan_limit[user["plan"]]:
        return "Access denied: usage limit reached"
    
    return "Access granted: welcome to the platform"

# NOT: Şöyle bir şey yapabilirsin: if user["is_active"] == False  ama şu daha pythonic'tir --> if not user["is_active"]:
# if user["payment_status"] == 'paid' yerine if user["payment_status"] != 'paid' daha pythonic'tir



def has_feature(user, feature):
    if feature in plan_features[user["plan"]]:
        print(f"User has access to {feature} feature.")
        return True
    else:
        print(f"User does not have access to {feature} feature.")
        return False


has_feature(users[0], "export")  # True
print(can_use_service(users[0]))  # Access granted: welcome to the platform