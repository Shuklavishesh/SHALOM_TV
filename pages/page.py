from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    #  Navigation Locators
    HOME = (By.LINK_TEXT, "Home")
    RADIO = (By.LINK_TEXT, "Radio")        
    KIDS = (By.LINK_TEXT, "Kids")
    PUBLICATION = (By.LINK_TEXT, "Publication")
    TV_SCHEDULE = (By.LINK_TEXT, "TV Schedule")
    PRAYER = (By.LINK_TEXT, "Prayer")

    #  Content Locators
    SECTION_HEADING = (By.CSS_SELECTOR, "section.thumb_slider_section h4")
    VIDEO_THUMBNAILS = (By.CSS_SELECTOR, "section.thumb_slider_section .itemBox img:not(.video-play-button)")
    VIDEO_PLAY_BUTTONS = (By.CSS_SELECTOR, "section.thumb_slider_section img.video-play-button")
    VIDEOS = (By.CSS_SELECTOR, "video, iframe")

    #  Navigation methods
    def go_to_home(self):
        self.wait.until(EC.element_to_be_clickable(self.HOME)).click()

    def go_to_radio(self):
        self.wait.until(EC.element_to_be_clickable(self.RADIO)).click()   # Fixed

    def go_to_kids(self):
        self.wait.until(EC.element_to_be_clickable(self.KIDS)).click()

    def go_to_publication(self):
        self.wait.until(EC.element_to_be_clickable(self.PUBLICATION)).click()

    def go_to_tv_schedule(self):
        self.wait.until(EC.element_to_be_clickable(self.TV_SCHEDULE)).click()

    def go_to_prayer(self):
        self.wait.until(EC.element_to_be_clickable(self.PRAYER)).click()

    #  Content methods
    def get_section_headings(self):
        return self.driver.find_elements(*self.SECTION_HEADING)

    def get_video_thumbnails(self):
        return self.driver.find_elements(*self.VIDEO_THUMBNAILS)

    def get_play_buttons(self):
        return self.driver.find_elements(*self.VIDEO_PLAY_BUTTONS)

    def get_videos(self):
        return self.driver.find_elements(*self.VIDEOS)


