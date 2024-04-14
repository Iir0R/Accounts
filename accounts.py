def validateUsername(accounts):
  while True:
    nameTaken = False
    username = input('\nEnter a valid username (empty to cancel): ')

    if username == '':
      return
    
    for account in accounts:
      if username == account["Username"]:
        nameTaken = True
        break
    if nameTaken == True:
      print('\nUsername has already been taken!')
      continue

    if len(username) < 5:
      print('\nUsername must be at least 5 character long!')
      continue

    return username
  

def validatePassword():
  while True:
    password = input('\nEnter a valid password (empty to cancel): ')

    if password == '':
      return

    if len(password) < 8:
      print('\nPassword must be at least 8 characters long!')
      continue

    if password == password.lower():
      print('\nPassword must contain at least 1 uppercase character!')
      continue

    return password


def createUser(accounts):
  print('Create a new account')

  username = validateUsername(accounts)
  if username == None:
    print('\nAccount creation was cancelled')
    return

  password = validatePassword()
  if password == None:
    print('\nAccount creation was cancelled')
    return

  accounts.append(dict(Username = username, Password = password))
  print('Account created succesfully!')


def viewUsers(accounts):
  print('View existing accounts:')

  if len(accounts) == 0:
    print('\n(No existing accounts)')
    return

  for account in accounts:
    print(account)


def startProgram():
  accounts = []

  while (True):
    print('\nChoose an action between 1 - 3 \n\n1. Create new account \n2. View existing accounts \n3. Exit program')

    userInput = input('\nUser input:  ')

    if userInput == '1':
      createUser(accounts)
    elif userInput == '2':
      viewUsers(accounts)
    elif userInput == '3':
      print('Shutting down program')
      break
    else:
      print('No action available')

startProgram()