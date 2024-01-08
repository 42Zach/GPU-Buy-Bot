#Install Selenium if you already don't!
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import smtplib
from email.mime.text import MIMEText

refreshUrl = "https://www.bestbuy.com/site/gigabyte-geek-squad-certified-refurbished-nvidia-geforce-rtx-3080-ti-gaming-oc-12gb-gddr6x-pci-express-4-0-graphics-card/6501085.p?skuId=6501085"
driverPath = "C:/Program Files/Google/Chrome/Application/chrome.exe"

# Email configuration
emailAddress = "zachajohnson2004@gmail.com"
emailPassword = "password"
recipientEmail = "zachajohnson2004@gmail.com"

driver = webdriver.Chrome(executable_path=driverPath)

driver.get(refreshUrl)

# Add to cart
def add_to_cart():
    try:
        add_to_cart_button = driver.find_element_by_xpath("//button[contains(text(), 'Add to Cart')]")
        add_to_cart_button.click()
        print("Added to cart!")

        send_email("Added to Cart", "The item has been added to your cart successfully.")
    except Exception as e:
        print(f"Error adding to cart: {e}")

# Email notification
def send_email(subject, message):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(emailAddress, emailPassword)

        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = emailAddress
        msg['To'] = recipientEmail

        server.sendmail(emailAddress, recipientEmail, msg.as_string())
        server.quit()
        print("Email notification sent!")
    except Exception as e:
        print(f"Error sending email notification: {e}")

add_to_cart()

while True:
    driver.refresh()

    time.sleep(5)

    add_to_cart()
driver.quit()
