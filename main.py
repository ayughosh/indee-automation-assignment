from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class Indeedemo:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.webapge = "https://indeedemo-fyc.watch.indee.tv/"
        self.video_element = None
        self.action = ActionChains(self.driver)
        
    def open_website(self):
        print(f"Opening the website: {self.webapge}")
        self.driver.get(self.webapge)
    
    def enter_access_code(self):
        wait = WebDriverWait(self.driver, 10)
        print("Waiting for the access code input element to be located...")
        input_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#access-code")))
        print("Element located, entering the access code...")
        input_element.send_keys("WVMVHWBS")
        button_element = self.driver.find_element(By.CSS_SELECTOR, "button#sign-in-button")
        button_element.click()

    def enter_test_automation_project(self, timeout=10):
        div_selector = "div#indee-title-card-prj-01j912ej0rs3wwadvadhavpasx"
        try:
            wait = WebDriverWait(self.driver, timeout)
            print("Waiting for the main project element to be located...")
            element = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, div_selector)))
            print("Element located, clicking on it...")
            element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, div_selector)))
            element.click()
        except Exception as e:
            print(f"An error occurred: {e}")

    def show_details(self, total_time_to_show=5):
        anchor_selector = "a#detailsSection"
        try:
            wait = WebDriverWait(self.driver, total_time_to_show)
            print("Waiting for the 'Details' anchor to be located...")
            element = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, anchor_selector)))
            print("Element located, clicking on it...")
            element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, anchor_selector)))
            element.click()
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            print(f"Waiting for {total_time_to_show} seconds to show the details...")
            time.sleep(total_time_to_show)
        
    def return_to_videos(self):
        anchor_selector = "a#videosSection"
        try:
            wait = WebDriverWait(self.driver, 10)
            print("Waiting for the 'Videos' anchor to be located...")
            element = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, anchor_selector)))
            print("Element located, clicking on it...")
            element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, anchor_selector)))
            element.click()
        except Exception as e:
            print(f"An error occurred: {e}")

    def play_the_video(self, timeout=10):
        play_button_selector = ".play-section button"
        try:
            wait = WebDriverWait(self.driver, timeout)
            print("Waiting for the 'Play' button to be located...")
            element = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, play_button_selector)))
            print("Element located, clicking on it...")
            element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, play_button_selector)))
            element.click()    
        except Exception as e:
            print(f"An error occurred while trying to play the video: {e}")
    
    def locate_and_switch_to_iframe(self, iframe_id="video_player", timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            print("Waiting for the iframe element to be located...")
            iframe_element = wait.until(EC.presence_of_element_located((By.ID, iframe_id)))
            print("Element located, switching to the iframe...")
            self.driver.switch_to.frame(iframe_element)
        except Exception as e:
            print(f"An error occurred while trying to locate the iframe: {e}")
    
    def switch_to_default_content(self):
        self.driver.switch_to.default_content()
          
    def find_video_element(self, timeout=10):
        video_css_selector = "video.jw-video.jw-reset"
        wait = WebDriverWait(self.driver, timeout)
        try:
            self.locate_and_switch_to_iframe()
            print("Switched to the iframe, now looking for the video element...")
            self.video_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, video_css_selector)))
        except Exception as e:
            print(f"An error occurred while trying to find the video element: {e}")
            return None
    
    def pause_video_at(self, seconds=10):
        while True:
            elapsed_video_time = self.driver.execute_script("return arguments[0].currentTime", self.video_element)
            print(f"Elapsed video time: {elapsed_video_time}")
            if elapsed_video_time >= seconds:
                break
        self.driver.execute_script("arguments[0].pause()", self.video_element)
        print(f"Video paused at {elapsed_video_time}")
    
    def pause_video(self):
        self.driver.execute_script("arguments[0].pause()", self.video_element)
    
    def unpause_video(self):
        self.driver.execute_script("arguments[0].play()", self.video_element)
    
    def unpause_video_using_continue_watching(self):
        self.switch_to_default_content()
        continue_watching_button_xpath = '//*[@id="__nuxt"]/div/div/div[2]/dialog/div[2]/div[1]/div/div[1]/button'
        wait = WebDriverWait(self.driver, 10)
        try:
            print("Waiting for the 'Continue Watching' button to be located...")
            element = wait.until(EC.presence_of_all_elements_located((By.XPATH, continue_watching_button_xpath)))
            print("Element located, clicking on it...")
            element = wait.until(EC.element_to_be_clickable((By.XPATH, continue_watching_button_xpath)))
            element.click()
        except Exception as e:
            print(f"An error occurred while trying to click on the 'Continue Watching' button: {e}")
        finally:
            self.locate_and_switch_to_iframe()
    
    def set_volume(self, volume=0.5, time_between_steps=.5):
        volume_css_selector = '.jw-icon.jw-icon-tooltip.jw-icon-volume.jw-button-color.jw-reset.jw-full'
        wait = WebDriverWait(self.driver, 10)
        try:
            print("Waiting for the volume element to be located...")
            element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, volume_css_selector)))
            print("Element located, moving to it...")
            self.action.move_to_element(element).perform()
            time.sleep(time_between_steps)
            self.driver.execute_script(f"arguments[0].volume = {volume}", self.video_element)    
        except Exception as e:
            print(f"An error occurred while trying to click on the 'Settings' button: {e}")
            
    def change_resolution(self, resolution="720p", time_between_steps=.5):
        bottom_container_css_selector = '.jw-reset.jw-button-container'
        settings_xpath = '//*[@id="media-player"]/div[2]/div[13]/div[4]/div[2]/div[14]'
        xpath_720p_button = '//*[@id="jw-settings-submenu-quality"]/div/button[2]'
        xpath_480p_button = '//*[@id="jw-settings-submenu-quality"]/div/button[3]'
        xpath_360p_button = '//*[@id="jw-settings-submenu-quality"]/div/button[4]'
        
        wait = WebDriverWait(self.driver, 10)
        try:
            element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, bottom_container_css_selector)))
            self.action.move_to_element(element).perform()
            
            print("Waiting for the 'Settings' button to be located...")
            element = wait.until(EC.presence_of_all_elements_located((By.XPATH, settings_xpath)))
            print("Element located, clicking on it...")
            element = wait.until(EC.element_to_be_clickable((By.XPATH, settings_xpath)))
            element.click()
            time.sleep(time_between_steps)
            if resolution == "720p":
                print("Waiting for the '720p' button to be located...")
                element = wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath_720p_button)))
                print("Element located, clicking on it...")
                element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_720p_button)))
                element.click()
            elif resolution == "480p":
                print("Waiting for the '480p' button to be located...")
                element = wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath_480p_button)))
                print("Element located, clicking on it...")
                element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_480p_button)))
                element.click()
            elif resolution == "360p":
                print("Waiting for the '360p' button to be located...")
                element = wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath_360p_button)))
                print("Element located, clicking on it...")
                element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_360p_button)))
                element.click()
        except Exception as e:
            print(f"An error occurred while trying to click on the 'Settings' button: {e}")

    def exit_video(self):
        self.switch_to_default_content()
        back_button_xpath = '//*[@id="__nuxt"]/div/div/div[2]/dialog/div[1]/button'
        wait = WebDriverWait(self.driver, 10)
        try:
            print("Waiting for the 'Back' button to be located...")
            element = wait.until(EC.presence_of_all_elements_located((By.XPATH, back_button_xpath)))
            print("Element located, clicking on it...")
            element = wait.until(EC.element_to_be_clickable((By.XPATH, back_button_xpath)))
            element.click()
        except Exception as e:
            print(f"An error occurred while trying to click on the 'Back' button: {e}")

    def sign_out(self, time_between_steps=.5):
        sidebar_xpath_selector = '//*[@id="SideBar"]'
        sign_out_button_xpath = '//*[@id="signOutSideBar"]'
        element_selector = "#vid-01j912gbvdnr5er79gqeb8k30w"
        wait = WebDriverWait(self.driver, 10)
        try:
            print("Checking if page load is complete")
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, element_selector)))
            
            print("Page load complete, expanding sidebar")
            sidebar = wait.until(EC.presence_of_element_located((By.XPATH, sidebar_xpath_selector)))
            self.action.move_to_element(sidebar).perform()
            
            time.sleep(time_between_steps)
            print("Signing out!")
            signout = wait.until(EC.presence_of_element_located((By.XPATH, sign_out_button_xpath)))
            signout.click()
        except Exception as e:
            print(f"An error occurred while trying to click on the 'Sign Out' button: {e}")
    
if __name__ == "__main__":
    indeedemo = Indeedemo()
    indeedemo.open_website()
    time.sleep(1) # Just to see output 
    indeedemo.enter_access_code()
    time.sleep(1) # Just to see output
    indeedemo.enter_test_automation_project()
    time.sleep(1) # Just to see output
    indeedemo.show_details()
    time.sleep(1) # Just to see output
    indeedemo.return_to_videos()
    time.sleep(1) # Just to see output
    indeedemo.play_the_video()
    time.sleep(1) # Just to see output
    indeedemo.find_video_element()
    time.sleep(1) # Just to see output
    indeedemo.pause_video_at(10)
    time.sleep(2) # Just to see output
    indeedemo.unpause_video_using_continue_watching()
    time.sleep(2) # Just to see output
    indeedemo.set_volume(0.5, time_between_steps=1)
    time.sleep(1) # Just to see output
    indeedemo.change_resolution("480p", time_between_steps=1)
    time.sleep(1) # Just to see output
    indeedemo.change_resolution("720p", time_between_steps=1)
    time.sleep(1) # Just to see output
    indeedemo.pause_video()
    time.sleep(1) # Just to see output
    indeedemo.exit_video()
    time.sleep(1) # Just to see output
    indeedemo.sign_out(time_between_steps=1)
    time.sleep(1) # Wait for exit