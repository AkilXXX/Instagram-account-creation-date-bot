"""  
لاتصير فرخ وتغيير الحقوق
"""

import telebot,requests,random,json
from telebot import types 

t =  '\033[1;30m'
r = '\033[1;31m' 
g = '\033[1;32m'
g2 = '\033[1;33m'
g3 = '\033[1;34m'
g4 = '\033[1;35m'
g5= '\033[1;36m'
مدري = '\033[1;39m'
b = "            INSTAGRAM ACCOUNT DATE BOT\n                      BY @AKIL828 - @FFFFFFM \n\n\n"
def hshdhdhvdvd(bbb):   
   y = ""
   for zz in bbb:
   	n = random.choice([g,r,t,g2,g3,g4,g5,مدري])
   	y =  y+n+zz   
   return y
   
def inp(te):
   m = input(f"{g}┌── ({r}root@localhost{g}){t}-{g}[{t}~{g}]\n└─{r}${g2}  {te}")
   return m
   
def tok(ex):
	i = inp(ex)
	if(i == "" or i == " " ):
		tok(ex)
	else:
		return i

print(hshdhdhvdvd(b))
ccc = tok("YOUR BOT TOKEN : ")
print(hshdhdhvdvd("\n\n\n                      BOT IS RUNNING....."))
akil = telebot.TeleBot(ccc)
akil.remove_webhook()

@akil.message_handler(commands=['start'])
def startmasg(message):
	inline = types.InlineKeyboardMarkup(row_width=3)
	زر  = types.InlineKeyboardButton("المطور ",url="https://t.me/akil828")	
	inline.add(زر)
	akil.send_message(chat_id=(message.chat.id),text=f'*مرحبا بك  في بوت فحص تاريخ انشاء حساب الانستاء  \n \n قم بارسال اليوزر *',reply_markup=inline,parse_mode='markdown')
	
@akil.message_handler(func=lambda m:True)
def bsbeheueuueuruduuru(message):
    get = requests.get(f"http://akil-api.ga/api/Instagram/?user={message.text}")
    akil.send_message(chat_id=(message.chat.id),text=f'*{get.json()["date"]}*',parse_mode='markdown')
    
    
if __name__ == "__main__":
    akil.polling(none_stop=True)
	