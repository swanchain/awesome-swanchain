import sys
import os
def print_usage():
    print("[+] Usage: docker run -it --rm github-to-lagrange-tool <wallet> <lagrange-api> <lagrange-space>   <github-url>")
    print("[+] ex: docker run -it --rm github-to-lagrange-tool 0x72b4952E1b1e6D318101314acB4517bA99264e70 xxxx awesome-swanchain https://github.com/swanchain/awesome-swanchain")

def main():
    # Check if the number of arguments is correct
    if len(sys.argv) != 5:
        print("Error: Incorrect number of arguments")
        print_usage()
        sys.exit(1)

    # Retrieve command-line arguments
    wallet = sys.argv[1]
    lagrange_api = sys.argv[2]
    lagrange_space = sys.argv[3]
    github_url = sys.argv[4]



    # Print the provided arguments
    print(f"[+] wallet: {wallet}")
    print(f"[+] Lagrange API: {lagrange_api}")
    print(f"[+] Lagrange Space: {lagrange_space}")
    print(f"[+] GitHub URL: {github_url}")


    print("[+] configure lagrange-cli")
    os.system(f"lag config --api-token {lagrange_api}")
    
    print("[+] donwload github repo")
    os.system(f"git clone {github_url} workshop")
    
    print("[+] init lagrange repo")
    os.system(f"lag clone https://lagrangedao.org/spaces/{wallet}/{lagrange_space}")
    
    print("[+] copy files to lagrange dir")
    os.system(f"cp -r workshop/. {lagrange_space}/")
    print("[+] remove git files")
    os.system(f"rm -rf  {lagrange_space}/.git")
    
    print("[+] add and commit")
    os.system(f"cd {lagrange_space} && lag add .")
    os.system(f"cd {lagrange_space} && lag commit -m  'github to lagrange tool' ")
    
    print("[+] push to lagrange")
    os.system(f"cd {lagrange_space} &&  lag push https://lagrangedao.org/spaces/{wallet}/{lagrange_space}")
    
if __name__ == "__main__":
    main()

