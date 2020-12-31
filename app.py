if __name__ == '__main__':
  secrets = input().strip().split('#')
  for index,secret, in enumerate(secrets):
      print(index,"=",secret)
