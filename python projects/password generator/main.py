#can be used for != hacking
# can be used for generating passwords for gamil, google, youtube, etc.

import string
import random

while True:
    if __name__ == '__main__':
        s1 = string.ascii_lowercase
        # print(s1)
        s2 = string.ascii_uppercase
        # print(s2)
        s3 = string.digits
        # print(s3)
        s4 = string.punctuation
        # print(s4)
        try:
            plen = int(input("Enter the pawssword length in digits\n"))
            s = []
            s.extend(list(s1))
            s.extend(list(s2))
            s.extend(list(s3))
            s.extend(list(s4))
            # print(s)
            random.shuffle(s)
            # print(s)
            print("your password is:")
            print("".join(random.sample(s, plen))

        except Exception as e:
            print("unable to generate the passowrd because you entered a wrong digit")
