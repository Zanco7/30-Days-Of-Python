import qrcode

# 30-day Python challenge
print("------30-day Python challenge 27/30------")
print("QR Code Generator (Website URL)")

def generate_qr():
    while True:
        website_url = input("\nEnter Website URL: ").strip()

        if not website_url:
            print("❌ URL cannot be empty.")
            continue

        if not (website_url.startswith("http://") or website_url.startswith("https://")):
            print("❌ URL must start with http:// or https://")
            continue

        qr = qrcode.make(website_url)

        file_name = "website_qr.png"
        qr.save(file_name)

        print(f"✅ QR Code generated successfully!")
        print(f"📁 Saved as: {file_name}")

        while True:
            again = input("\nGenerate another QR code? (y/n): ").lower()
            if again == "y":
                break
            elif again == "n":
                print("Goodbye! 👋")
                return
            else:
                print("Please enter y or n.")

generate_qr()
