import requests, time, re, random, thread

list1 = ["Beck","Glenn","Becker","Carl","Beckett","Samuel","Beddoes","Mick","Beecher","HenryWard","Beethoven","Ludwigvan","Begin","Menachem","Bell","Alexander","Graham","Belloc","Hilaire","Bellow","Saul","Benchley","Robert","Benenson","Peter","BenGurion","David","Benjamin","Walter","Benn","Tony","Bennington","Chester","Benson","Leana","Bent","Silas","Bentsen","Lloyd","Berger","Ric","Bergman","Ingmar","Berio","Luciano","Berle","Milton","Berlin","Irving","Berne","Eric","Bernhard","Sandra","Berra","Yogi","Berry","Halle","Berry","Wendell","Bethea","Erin","Bevan","Aneurin","Bevel","Ken","Biden","Joseph","Bierce","Am","Brose","Biko","Steve","Billings","Josh","Biondo","Frank","Birrell","Augustine","Black","Elk","Blair","Ro","Bert","Blair","Tony","Blake","William","Blakey","Art","Blalock","Jolene","Blanc","Mel","Blanc","Raymond","Blanchet","Cate","Blix","Hans","Blood","Rebecca"]
url = 'https://blog.jdsports.co.uk/apps/FPCompApp.php'

print (time.strftime("[%H:%M:%S]") + " - FP THE TEN Entry Bot // dev. FockNikeTalk")

proxy = {
		"http":"http://" + "127.0.0.1:80",  # If u don't want to use proxy/proxies add a  '#' without the '' at the beginning of the line
		#"https":"https://" + "127.0.0.1:80" # If u don't want to use proxy/proxies add a  '#' without the '' at the beginning of the line
		}

if proxy:
		print(time.strftime("[%H:%M:%S]") + " - Proxies Loaded")
else:
		print(time.strftime("[%H:%M:%S]") + " - No Proxies Loaded")


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',}

class GmailDotEmailGenerator:
  def __init__(self, email):
    self.__username__, self.__domain__ = email.split('@')
  def generate(self):
    return self.__generate__(self.__username__, self.__domain__)
  def __generate__(self, username, domain):
    emails = list()
    username_length = len(username)
    combinations = pow(2, username_length - 1)
    padding = "{0:0" + str(username_length - 1) + "b}"
    for i in range(0, combinations):
        bin = padding.format(i)
        full_email = ""

        for j in range(0, username_length - 1):
            full_email += (username[j]);
            if bin[j] == "1":
                full_email += "."
        full_email += (username[j + 1])
        emails.append(full_email + "@" + domain)
    return emails

def footpatrol(emails):
    for email in \
		(GmailDotEmailGenerator(emails).generate())[:1000000]:

			payload = {
	'cityOfRes': 'Amsterdam', 					# Change to city of res.
	'countryOfRes': 'The Netherlands',		    # Change to country of res.
	'email': email,								# CHECK LINE 67 & 68
	'fullName': list1[random.randint(0, 99)], # Do Not change
	'other': '',						# Do not change.
	'phoneNumber': '+31612121212', 				# Change to phone number.
	'secondTermsAgreed': 'Agrees to second terms', # Do not change.
	'shoeWanted': 'Nike React Hyperdunk',		# Do not change.
	'submit': 'ENTER NOW',				# Do not change.
	'termsAgreed': 'Agrees to terms',	# Do not change.
	}

			postrequest = requests.post('https://blog.jdsports.co.uk/apps/FPCompApp.php', headers=headers, data=payload, proxies=proxy)
			if 'duplicate' in postrequest.text:
		            print(time.strftime("[%H:%M:%S]") + " - Could not enter" + " - " + email )
			else:
		            print(time.strftime("[%H:%M:%S]") + " - Succesfully entered" + " - " + email)

try:
   thread.start_new_thread( footpatrol, ("youremail@gmail.com",) ) # CHANGE TO YOUR EMAIL GMAIL ONLY
   #thread.start_new_thread( footpatrol, ("yoursecondemail@gmail.com",) ) # add another gmail if u want, delete this line if not
   

except:
		print "Error: unable to start thread"
while 1:
		pass
