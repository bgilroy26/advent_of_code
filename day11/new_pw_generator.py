import sys
import password_tools
    
def main(initial_pw):
    trial_pw = password_tools.increment_password(initial_pw)
    while not password_tools.iol_absent(trial_pw):
        trial_pw = password_tools.increment_password(trial_pw)

    while (not password_tools.doubles_test(trial_pw)) or \
            (not password_tools.series_test(trial_pw)): 
        trial_pw = password_tools.increment_password(trial_pw)
        while not password_tools.iol_absent(trial_pw):
            trial_pw = password_tools.increment_password(trial_pw)
    
    print(trial_pw.decode('utf-8'))

if __name__ == '__main__':
    inp = sys.stdin.read()
    main(inp.encode('utf-8'))

