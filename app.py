# Важно!:
# Оваа скрипта е дадена само за едукативни и информативни цели.
# Употребата на оваа скрипта за автоматизирање на интеракциите на веб-страниците, како што е регистрацијата на Pazar3.mk, може да подлежи на условите за користење на веб-страницата.
# Со користење на оваа скрипта, вие потврдувате и се согласувате дека:
# 1. Вие сте единствено одговорни за вашите постапки и за сите последици што може да произлезат од користењето на оваа скрипта.
# 2. Разбирате дека автоматизираните интеракции со веб-локациите може да ги прекршат условите за користење на тие веб-локации.
# 3. Се согласувате да ја користите оваа скрипта одговорно и во согласност со важечките закони и прописи.
# 4. Креаторите и соработниците на оваа скрипта не се одговорни за каква било злоупотреба или незаконска употреба на оваа скрипта.
# Ве молиме користете ја оваа скрипта на ваш сопствен ризик и дискреција. Ако изберете да го користите, погрижете се да ги прегледате и почитувате условите за користење и политиките за приватност на веб-локациите со кои комуницирате.
# Warning: This project is not intended for any cyber disruption or illegal purposes. The author is not responsible for any misuse of this code.
#Автор на оваа скрипта е: Леонид Крстевски

import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def generate_temp_email():
    # Start a new Chrome session
    driver = webdriver.Chrome()

    # Navigate to temp-mail.io
    driver.get("https://temp-mail.io/")

    # Wait for the email address to be generated
    email_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'email'))
    )

    # Wait for a few seconds to let the email load completely
    time.sleep(5)

    # Copy the email address
    email_address = email_input.get_attribute("value")

    return driver, email_address


def check_for_activation_link(driver, temp_email):
    # Refresh the page to check for new emails
    driver.refresh()

    # Wait for a few seconds to let the page refresh
    time.sleep(5)

    # Check if there's an email with an activation link
    email_subjects = driver.find_elements(By.XPATH, '//div[@class="message__title"]/span[@class="message__subject new-message"]')
    for subject in email_subjects:
        if "Активирај ја твојата Pazar3 сметка" in subject.text:  # Assuming this is the activation email subject
            # Open the email
            subject.click()

            # Extract the activation link from the email body
            try:
                activation_link = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//a[contains(@href, "pazar3.mk")][contains(text(), "Активирај профил")]'))
                ).get_attribute("href")
                print("Activation Link:", activation_link)
                return activation_link
            except:
                print("Unable to extract activation link.")
                return None

    print("Activation link not found.")
    return None

# Save email, password, and activation link to a text file
def save_credentials(email, password, activation_link):
    with open("credentials.txt", "w") as file:
        file.write(f"Email: {email}\n")
        file.write(f"Password: {password}\n")
        file.write(f"Activation Link: {activation_link}\n")

# Generate temporary email
driver, temp_email = generate_temp_email()

# Start a new Chrome session for registration
registration_driver = webdriver.Chrome()

# Navigate to the registration page
registration_driver.get("https://www.pazar3.mk/smetka/kreiraj-smetka")

# Wait for the form to load
form = WebDriverWait(registration_driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "form")))

# Find the input fields and fill them with placeholder data
email_input = form.find_element(By.ID, 'Email')
email_input.clear()  # Clear any existing text
email_input.send_keys(temp_email)

password_input = form.find_element(By.ID, 'Password')
password_input.clear()
password_input.send_keys("placeholderpassword")

# Find the name input field and fill it with placeholder data
name_input = form.find_element(By.ID, 'Name')
name_input.clear()
name_input.send_keys("John Doe")

# Submit the form
submit_button = form.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
submit_button.click()

# Wait for the next page to load by waiting for a specific element to appear
try:
    WebDriverWait(registration_driver, 10).until(
        EC.presence_of_element_located((By.ID, "element_id_on_next_page"))
    )
except TimeoutException:
    print("Timed out waiting for page to load")

# Close the registration browser
registration_driver.quit()

# Continue with the rest of your code
# Wait for the activation email to arrive
start_time = time.time()
while time.time() - start_time < 120:  # Wait for 2 minutes
    activation_link = check_for_activation_link(driver, temp_email)
    if activation_link:
        save_credentials(temp_email, "placeholderpassword", activation_link)
        break
    time.sleep(10)  # Check for new emails every 10 seconds

# Close the temporary email browser
driver.quit()

if not activation_link:
    print("Activation link not found.")


# Важно!:
# Оваа скрипта е дадена само за едукативни и информативни цели.
# Употребата на оваа скрипта за автоматизирање на интеракциите на веб-страниците, како што е регистрацијата на Pazar3.mk, може да подлежи на условите за користење на веб-страницата.
# Со користење на оваа скрипта, вие потврдувате и се согласувате дека:
# 1. Вие сте единствено одговорни за вашите постапки и за сите последици што може да произлезат од користењето на оваа скрипта.
# 2. Разбирате дека автоматизираните интеракции со веб-локациите може да ги прекршат условите за користење на тие веб-локации.
# 3. Се согласувате да ја користите оваа скрипта одговорно и во согласност со важечките закони и прописи.
# 4. Креаторите и соработниците на оваа скрипта не се одговорни за каква било злоупотреба или незаконска употреба на оваа скрипта.
# Ве молиме користете ја оваа скрипта на ваш сопствен ризик и дискреција. Ако изберете да го користите, погрижете се да ги прегледате и почитувате условите за користење и политиките за приватност на веб-локациите со кои комуницирате.
# Warning: This project is not intended for any cyber disruption or illegal purposes. The author is not responsible for any misuse of this code.
#Автор на оваа скрипта е: Леонид Крстевски
