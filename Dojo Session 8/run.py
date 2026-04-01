from RHELAutomator import bot                                   # Import an instance of RHELAutomator (bot) set within the file


dir = bot.run_command(['pwd'])                                  # store the returned string of pwd command execution

lscpu_res = bot.run_command(['lscpu'])                          # store the returned string of lscpu command execution

lines = lscpu_res.split('\n')                                   # split the returned string on a new line and store each line in an array

for line in lines:                                              # loop through the lines
    if "Virtualization" in line:                                # check if Virtualization is found in current line evaluted in lines
        virt_type = line.replace("Virtualization:", "").strip() # replace return string "Virtualization" with "" or empty string then strip spaces

print(f'Virtual machine support: {virt_type}')                  # print the virtual machine support type

print(f"Running VM Automator from {dir}")                       # display where this script is being executed from

vm_count = input("How many VMs would you like to create?: ")    # Ask the user to specify how many virtual machines to create

if vm_count:                                                    # If vm_count exists (not "", None, or null)

    while int(vm_count) > 0:                                    # run the following code while vm_count is greater than 0

        if (int(vm_count) > 1):                                 # Handle plurality 
            print(f"Spinning up {vm_count} VMs.")
        else:
            print(f"Spinning up {vm_count} VM.")

        update_sys_pkgs = input("Update system packages before starting? [ y | n ]: ")  # ask user to update system packages / subs

        if update_sys_pkgs == 'y':                                                      # if input is equal to y         
            sys_update_lines = bot.run_command(['sudo', 'dnf', 'update', '-y'])         # run system updates
            sys_update_lines = sys_update_lines.split("\n")                             # split returned string on new lines

            for line in sys_update_lines:                                               # loop through the lines and print each
                print(line)
                                                                                        
        virt_tools_verify = input("Press enter to install KVM hypervisor and virt...")  # enter to continue

        kvm_virt_install = bot.run_command(['sudo', 'dnf', 'install', 'qemu-kvm', 'libvirt', 'virt-install', 'virt-viewer']) # run install commands

        kvm_virt_lines = kvm_virt_install.split("\n")                                   # split returned lines from install comannd on new line and save in array

        for line in kvm_virt_lines:                                                     # loop through split lines array
            print(line)
            
        cockpit_install = input("Press enter to install Cockpit...")                    # Prompt the user for next step

        cockpit_line = bot.run_command(['sudo', 'dnf', 'install', 'cockpit', '-y'])

        print(cockpit_line)

        cockpit_line = bot.run_command(['sudo', 'dnf', 'install', 'cockpit-machines', '-y']) # Run command for cockpit

        print(cockpit_line)                                                             # NOTE: For some reason this did not require a loop???
        
        print("Enabling libvirt (systemctl)...")

        bot.run_command(['sudo', 'systemctl', 'enable', '--now', 'libvirtd'])

        print("libvirt enabled")

        print("Enabling cockpit (systemctl)...")

        bot.run_command(['sudo', 'systemctl', 'enable', '--now', 'cockpit.socket'])
        
        print("cockpit enabled")

        print("Allowing cockpit on firewall...")

        allow_cockpit = bot.run_command(['sudo', 'firewall-cmd', '--add-service=cockpit', '--permanent'])

        print(f"Firewall permission status: {allow_cockpit}")

        bot.run_command(['sudo', 'firewall-cmd', '--reload'])

        print("Firewall reloaded with permissions. Cockpit is live at https://localhost:9090.")

        input("Press enter to verify KVM modules installed...")

        lsmod_lines = bot.run_command(['lsmod'])            # Run lsmod to find kvm services
        lsmod_lines = lsmod_lines.split("\n")               # split returned lines from command on new line and save in array

        kvm_found = False                                   # make a bool initialized as False

        for line in lsmod_lines:                            # loop through lines
            if "kvm" in line:                               # if keyword kvm is found
                kvm_found = True                            # set bool to true
                print(line)                                 # print the lines where keyword kvm was found
        
        if not kvm_found:                                   # if bool not
            print("KVM Hypervisor not found. Try exiting the program and running again or manually install KVM.")

        print("The rest of the program should be set up using your own specifications.")
        print("The automated VM setup should be handled based on environment needs or utility.")
        input("Press enter to continue...")

        for i in range(int(vm_count)):                      # loop through the vm_count specified at the beginning of the program
            input(f"This input shows for all {vm_count} VMs. Press Enter to continue...")   # placeholder for VM info input

        print("Run complete. Exiting.")                     # Notify of completion
        break                                               # then break out of the while loop to exit the program
        






