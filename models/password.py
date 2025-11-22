def password_strength(password):
   small_chars = "abcdefghijklmnopqrstuvwxyz"
   capital_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
   symbols = "~!@#$%^&*. "
   numbers = "0123456789"
   small = False
   capital = False
   symbol = False
   number = False

   strength = 0
   for i in password:
      if i in small_chars:
         small = True
      elif i in capital_chars:
         capital = True
      elif i in symbols:
         symbol = True
      elif i in numbers:
         number = True
   
   if small == True:
      strength = strength +1
   if capital == True:
      strength = strength +1
   if symbol == True:
      strength = strength +1
   if number == True:
      strength = strength +1

   if strength == 1:
      return "Too Weak", 25
   elif strength == 2:
      return "Weak", 50
   elif strength == 3:
      return "Strong", 85
   elif strength == 4:
      return "Ulta Strong", 100

def check_choice (password):
    score, strength = password_strength (password)
    length = len(password)
    if length < 8:
        print(f"Password Must Contain At Least 8 Characters.")
        create_password()
    if strength < 85:
        print(f"{strength}% -> {score}: Invalid Password.\nPassword Must Contain At Least Three Of These Conditions:\n- Upper Letter\n- Small Letter\n- Digit\n- Symbol")
        create_password()



def create_password():
    password= input("\nEnter Your Password (Enter * to Exit This Process): ")

    if password == '*':
        return ''
    else:
        check_choice(password)

   
    return password
