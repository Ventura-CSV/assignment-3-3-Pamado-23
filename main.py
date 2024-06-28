def main():
    email = input('Enter your email: ')
    """
    ########################################
    Code Your Program here
    ########################################
    """

    result = True

    if not (email[0].isalpha()):
        result = False
    elif not (5 < len(email) < 30):
        result = False
    elif email.find('@') == -1:
        result = False
    else:
        index = email.index('@')
        if email.find('.', index) == -1:
            result = False

    print (f'{result}')
    

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
