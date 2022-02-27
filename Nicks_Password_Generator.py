# Password Generator

import random

uppercase1 = chr(random.randint(65,90))
uppercase2 = chr(random.randint(65,90))
lowercase1 = chr(random.randint(97,122))
lowercase2 = chr(random.randint(97,122))
digit1 = chr(random.randint(48,57))
digit2 = chr(random.randint(48,57))
punctual1 = chr(random.randint(32,152))
punctual2 = chr(random.randint(32,152))

password_generator = uppercase2 + uppercase1 + lowercase1 + lowercase2 + digit2 + digit1 + punctual2 + punctual1

print(password_generator)