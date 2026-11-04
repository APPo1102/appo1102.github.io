import sys
from Crypto.Cipher import ARC4

def interactive_rc4_decrypt():
    print("=" * 60)
    print("        OpenSSL 0.9.5a RC4 互動式封包解密工具")
    print("=" * 60)
    
    # 1. 讀取並驗證金鑰輸入
    key_input = input("[1/2] 請輸入 5 位元組金鑰 (Hex 格式，如 2A284771F6): ").strip()
    key_input = key_input.replace(" ", "").replace(":", "") # 移除空格或冒號
    
    try:
        KEY = bytes.fromhex(key_input)
        if len(KEY) != 5:
            print(f"[-] 警告：偵測到金鑰長度為 {len(KEY)} 位元組，並非標準的 5 位元組（40-bit）。")
            confirm = input("    是否繼續執行？(y/n): ").strip().lower()
            if confirm != 'y':
                return
    except ValueError:
        print("[-] 錯誤：金鑰必須是正確的十六進位 (Hex) 格式！")
        return

    # 2. 讀取並驗證密文輸入
    print("-" * 60)
    print("[2/2] 請輸入要解密的連線封包密文 (Hex 格式):")
    print("      (支援 Wireshark 複製的 Hex Stream，允許含有空格或換行)")
    
    ciphertext_lines = []
    while True:
        try:
            line = input()
            if not line: # 如果直接按 Enter 鍵且前面已有輸入，就結束讀取
                if ciphertext_lines:
                    break
                else:
                    print("[-] 請輸入密文數據！")
                    continue
            ciphertext_lines.append(line)
        except (KeyboardInterrupt, EOFError):
            break
            
    ciphertext_input = "".join(ciphertext_lines).replace(" ", "").replace(":", "").replace("\n", "").replace("\r", "")
    
    try:
        ciphertext = bytes.fromhex(ciphertext_input)
    except ValueError:
        print("[-] 錯誤：密文包含非十六進位字元，請確認格式！")
        return

    # 3. 執行 RC4 解密
    try:
        cipher = ARC4.new(KEY)
        decrypted_bytes = cipher.decrypt(ciphertext)
    except Exception as e:
        print(f"[-] 解密核心出錯: {e}")
        return

    # 4. 顯示輸出結果
    print("=" * 60)
    print(f"[+] 使用金鑰: {KEY.hex().upper()}")
    print(f"[+] 密文長度: {len(ciphertext)} 位元組")
    print("-" * 60)
    
    # 輸出 Hex 結果
    print(f"[+] 解密結果 (Hex):\n{decrypted_bytes.hex().upper()}")
    print("-" * 60)
    
    # 輸出 String 明文結果
    try:
        # 使用 replace 替換掉無法辨識的編碼，防止程序崩潰
        plaintext_str = decrypted_bytes.decode('utf-8', errors='replace')
        # 將不可見字元（控制碼）轉換為點點，方便閱讀文字
        readable_str = "".join([c if c.isprintable() else "." for c in plaintext_str])
        print(f"[+] 解密結果 (明文字串可讀區域):\n{readable_str}")
    except Exception as e:
        print(f"[-] 字串轉換失敗: {e}")
    print("=" * 60)

if __name__ == "__main__":
    try:
        while True:
            interactive_rc4_decrypt()
            print("\n")
            again = input("是否繼續解密下一個封包？(y/n): ").strip().lower()
            if again != 'y':
                print("[*] 謝謝使用，再見！")
                break
            print("\n" * 2)
    except KeyboardInterrupt:
        print("\n[*] 程式已強制結束。")