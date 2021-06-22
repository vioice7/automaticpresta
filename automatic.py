# Helium library and documentations for automatic testing here https://github.com/mherrmann/selenium-python-helium 
from helium import *
import random
import time

# use the alternative website if the primer exeeds bandwith limitations
start_chrome("automationpractice.com/index.php")
#start_chrome("prestashop-demo.inno-mods.io/v.1.6/")
time.sleep(1)

# this code is only used for the alternative prestashop demo if
# the original exeeds badwith limit since it had a popup banner

#if S(".infobar-dismiss").exists():
#	    click(S(".infobar-dismiss"))

# proceed to next step
click(Link("Add to cart"))
time.sleep(1)

#if S(".infobar-dismiss").exists():
#	    click(S(".infobar-dismiss"))
	
# proceed to next step	
click(Link("Proceed to checkout"))
time.sleep(1)

#if S(".infobar-dismiss").exists():
#	    click(S(".infobar-dismiss"))

# proceed to next step	
click(Link("Proceed to checkout"))
time.sleep(1)

#if S(".infobar-dismiss").exists():
#	    click(S(".infobar-dismiss"))

#complete all the necesary data
write("aimaeo@gmail.com", into=S("#email_create"))
time.sleep(1)
click(S("#SubmitCreate"))
time.sleep(2)
click(RadioButton("Mr.", below="Title"))

write("Aim", into=S("#customer_firstname"))
write("Tim", into=S("#customer_lastname"))
write("Tim@#10@#10@#10", into=S("#passwd"))

click(S("#uniform-days"))
press(ARROW_DOWN)
press(ENTER)
click(S("#uniform-months"))
press(ARROW_DOWN)
press(ENTER)
click(S("#uniform-years"))
press(ARROW_DOWN)
press(ENTER)

scroll_down(300)

click(S("#uniform-newsletter"))
click(S("#uniform-optin"))

write("Test Corp", into=S("#company"))
write("Test street, Nr. 10, P.O. BOX 10000", into=S("#address1"))
write("Test street, Nr. 20, P.O. BOX 12000", into=S("#address2"))
write("Test", into=S("#city"))
click(S("#uniform-id_state"))
press(ARROW_DOWN)
press(ARROW_DOWN)
press(ARROW_DOWN)
press(ARROW_DOWN)
press(ARROW_DOWN)
press(ARROW_DOWN)
press(ENTER)
write("12000", into=S("#postcode"))
write("This is all information I need", into=S("#other"))
write("0743 000 000", into=S("#phone"))
write("0743 000 000", into=S("#phone_mobile"))
write("MyAdressAlias", into=S("#alias"))
click("Register")

# proceed to next step
write("This is a test order for some original product.", into=S(".form-control"))
click("Proceed to checkout")

# proceed to next step
click(S(".checker"))
click("Proceed to checkout")

# proceed to next step
click(S(".bankwire"))
time.sleep(3)
click("I confirm my order")

# check if the order has been completed (the text should be available)
if Text("Your order on My Store is complete.").exists():
	print("The order is complete")
