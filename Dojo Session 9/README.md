### ANSIBLE AUTOMATION

**THIS SESSION IS IN DEV**

*For next session*

```Bash

sudo dnf update -y

sudo dnf install -y ansible-core

ansible --version

ssh-keygen -t ed25519 -N "" -f ~/.ssh/id_ed25519

ssh-copy-id username@192.168.1.50

ssh username@192.168.1.50

mkdir ~/ansible-demo

cd ~/ansible-demo
```

```ini
[webservers]
192.168.1.50

[dbservers]
192.168.1.51
```

```Bash
ansible all -i inventory.ini -m ping

ansible webservers -i inventory.ini -m command -a "uptime"
```

```yaml
---
- name: Configure Secure Web Server (HTTPS)
  hosts: webservers
  become: yes
  tasks:
    - name: Install Apache and the SSL module
      ansible.builtin.dnf:
        name: 
          - httpd
          - mod_ssl
        state: present

    - name: Ensure firewalld permits HTTPS traffic
      ansible.posix.firewalld:
        service: https
        permanent: true
        state: enabled
        immediate: true

    - name: Ensure Apache is running and enabled on boot
      ansible.builtin.systemd:
        name: httpd
        state: started
        enabled: yes
```

```Bash
ansible-playbook -i inventory.ini setup_webserver.yml -K
```

NOTE: Note: The -K or --ask-become-pass flag prompts you for the remote user's sudo password, which is required for package installation