import random


def main():
    while True:
        response = input('You: ')
        # if response = ('Hey grandma'):
        #     s = input('Grandma: HUH?! SPEAK UP, SONY!')
        #     if response = ('HEY GRANDMA'):
        #         p = input('NO. NOT SINCE 1945!')
        #         if response = ('BYE'):
        #             e = ('BYE SONNY')
        # return None

        if response == ('BYE'):
            break
        elif response.isupper():
            print('Grandma: NO. NOT SINCE', random.randint(1930, 1950), '!')
        else:
            print('Grandma: HUH?! SPEAK UP, SONNY!')


if __name__ == '__main__':
    main()
