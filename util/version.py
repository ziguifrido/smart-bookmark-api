import os
import re 

def get_version():
    if os.path.isfile('version.txt'):
        with open('version.txt', 'r') as f:
            version = f.read()           
    return version

def save_version(new_version):
    with open('version.txt', 'w') as f:
        f.write(new_version)
    print(f'\nNew version saved: {new_version}')

def main():
    version = get_version()
    message = f'''

        Current version: {version}
        
            1. Bump Major
            2. Bump Minor
            3. Bump Patch
            4. Custom version
        
    '''
    print(message)
    choice = input('Enter your choice: ')
    
    if choice == '4':
        new_version = input('\nEnter new version: ')
        if not re.match(r'^[0-9]+\.[0-9]+\.[0-9]+$', new_version):
            print('\nInvalid version!')
            return
        save_version(new_version)
        return
    
    major, minor, patch = version.split('.')
    match choice:
        case '1':
            major = str(int(major) + 1)
            minor = '0'
            patch = '0'
        case '2':
            minor = str(int(minor) + 1)
            patch = '0'
        case '3':
            patch = str(int(patch) + 1)
        case _:
            print('\nInvalid choice!')
            return

    save_version(f'{major}.{minor}.{patch}')
    

if __name__ == '__main__': main()