import sys
import no_interaction_mode as i1, interaction_mode as i2

def read_arguments():
    if len(sys.argv) == 1:
        print('no arguments passed!')
        sys.exit(1)
    elif len(sys.argv)==3: 
        user=sys.argv[1]
        password=sys.argv[2]
        driver=i1.no_interaction(user,password)
    elif sys.argv[1]=='-i' and len(sys.argv)==4:
        user=sys.argv[2]
        password=sys.argv[3]
        browser_choice=input('Use chrome or microsoft edge (Enter c or e): ')
        while browser_choice != 'c' and browser_choice !='e':
            browser_choice=input('Invalid choice for browser. Enter \'c\' for chrome or \'e\' for edge: ')
        if browser_choice=='e':
            driver_path=input('Enter driver path: ') #/usr/local/bin/msedgedriver
            binary_path=input('Enter browser path: ') #/usr/bin/microsoft-edge-dev
            driver=i2.interaction_e(driver_path,binary_path)
        else:
            driver=i2.interaction_c()
    else:
        print('arguments missing or in wrong order!')
        sys.exit(1)
    return user,password,driver