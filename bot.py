import requests
from telethon import TelegramClient, events, sync
import re,os
from time import sleep
o = ("xaBdBoT")
tokenbot = "6555481969:AAEbGyGj9__ddTn9Y5pkXfhwPPTokUgTi94" #توكن البوت الي يوصلك عليه الصيد
dragon = "6376489778" #ايديك
app =  TelegramClient("SwapBot",api_id=15145595,api_hash="c3f60ecf742e136436acc9082ac8d9a4")
app.start()
qq = 0
numche = 1
bio = "α𝖻᥆᥆ძ - ᥒᥙ𝗆𝖻𝖾𝗋 1 , 𝗍h𝖾 𝗌𝗍𝗋᥆ᥒ𝗀 𝗍𝖾α𝗆 Ꭵ𝗌 , @YaBhTeam🐊 ," #نبذه البوت الي من ينصاد يخلي بيها اذا ماتعرف عوفها
namebot = "ᥲხ᥆᥆ძ ᥡᥲხɦ #1"
app.send_message("botfather",f'/newbot')
app.send_message("botfather",namebot)
def fucker(o):
    global qq
    if 7==7:
    	qq+=1
    	url = f"https://t.me/{o}"
    	req = requests.get(url)
    	if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
    		app.send_message("botfather",f'{o}')
    		app.send_message("botfather",f'/setabouttext')
    		app.send_message("botfather",f"@{o}")
    		app.send_message("botfather",f'{bio}')
    		y = requests.post(f"""https://api.telegram.org/bot{tele_bot}/sendmessage?chat_id={own_id}&text= 𝑰𝒔 𝒂 𝑵𝒆𝒘 𝒖𝒔𝒆𝒓 𝑩𝒚 : 𝒂𝑩𝒐𝒐𝑫 𝒀𝒂𝑩𝒉 🐊,
এ〔 ᥙ᥉ᥱᖇꪀᥲꪔᥱ 〕: @{o}
এ〔 ᥴᥣᎥᥴƙ᥉ 〕: {qq}
এ〔 ᥉ᥲ᥎ᥱ 〕: ხ᥆ƚ
এ〔 ꪀᥙꪔხᥱᖇ 〕 : {numche}
এ〔 ᥴɦ 〕: @YaBhTeam""")    		
while True:
	print("[ "+str(qq)+" ] : @"+o)
	fucker(o)
app.run() 
