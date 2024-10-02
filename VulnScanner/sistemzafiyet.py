import subprocess

def check_root_access():
    """ROOT OLUP OLMADIGINI KONTROL ET!"""
    return subprocess.call(['id', '-u']) == 0

def check_ssh_root_login():
    """SSH UZERINDEN ROOT OLUP OLMADIGINI KONTROL ET!"""
    try:
        with open('/etc/ssh/sshd_config', 'r') as file:
            for line in file:
                if "PermitRootLogin" in line:
                    return "PermitRootLogin" in line and "no" not in line.lower()
    except FileNotFoundError:
        return False

def check_firewall():
    """GUVENLIK DUVARINI KONTROL ET!"""
    try:
        result = subprocess.run(['ufw', 'status')], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return "active" in result.stdout.decode().lower()
    except FileNotFoundError:
        return False

def check_updates():
    """GUNCELLEMELERI KONTROL ET!"""
    result = subprocess.run(['apt', 'list', '--upgradable'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return "upgradable" in result.stdout.decode()

if __name__ == "__main__":
    print("sistem zafiyet tarayıcısı")

    # root kontrolü

    if check_root_access():
        print("root erişimi hakim.")
    else:
        print("root erişimi yok.")

    # ssh root giriş kontrolü
    if check_ssh_root_login():
        print("ssh ile kök girişi hakim.")
    else:
        print("ssh ile kök girişi yasak.")

    # güvenlik duvarı
    if check_firewall():
        print("firewall etkin.")
    else:
        print("firewall etkin degil.")

    #güncellemeler
    if check_updates():
        print("güncelleme mevcut.")
    else:
        print("sistem güncel.")
