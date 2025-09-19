from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
    
    # Navigation Locators
    
    HOME = (By.LINK_TEXT, "Home")
    RADIO = (By.LINK_TEXT, "Radio")
    KIDS = (By.LINK_TEXT, "Kids")
    PUBLICATION = (By.LINK_TEXT, "Publication")
    TV_SCHEDULE = (By.LINK_TEXT, "TV Schedule")
    PRAYER = (By.LINK_TEXT, "Prayer")

   
    # Content Locators
   
    SECTIONS = (By.CSS_SELECTOR, "section.thumb_slider_section")  # Section blocks
    SECTION_HEADING = (By.CSS_SELECTOR, "section.thumb_slider_section h4")
    VIDEO_THUMBNAILS = (By.CSS_SELECTOR, "div.swiper-slide img")  # carousel thumbnails
    VIDEO_PLAY_BUTTONS = (By.CSS_SELECTOR, "button.MuiIconButton-root svg[data-testid='PlayArrowIcon']")
    VIDEOS = (By.CSS_SELECTOR, "video[src^='blob:'], iframe")  # fixed iframe locator

    # Radio (Audio) locators
    AUDIOS = (By.CSS_SELECTOR, "audio")

    # Publication (Document) locators
    DOCUMENTS = (By.CSS_SELECTOR, "a[href$='.pdf'], a[href$='.doc'], a[href$='.docx']")

    
    # Navigation Methods
   
    def go_to_home(self):
        self.wait.until(EC.element_to_be_clickable(self.HOME)).click()

    def go_to_radio(self):
        self.wait.until(EC.element_to_be_clickable(self.RADIO)).click()

    def go_to_kids(self):
        self.wait.until(EC.element_to_be_clickable(self.KIDS)).click()

    def go_to_publication(self):
        self.wait.until(EC.element_to_be_clickable(self.PUBLICATION)).click()

    def go_to_tv_schedule(self):
        self.wait.until(EC.element_to_be_clickable(self.TV_SCHEDULE)).click()

    def go_to_prayer(self):
        self.wait.until(EC.element_to_be_clickable(self.PRAYER)).click()

    
    # Helper Methods
    
    def get_sections(self):
        return self.wait.until(EC.presence_of_all_elements_located(self.SECTIONS))

    def get_videos(self):
        return self.driver.find_elements(*self.VIDEOS)

    def get_audios(self):
        return self.driver.find_elements(*self.AUDIOS)

    def get_documents(self):
        return self.driver.find_elements(*self.DOCUMENTS)
ents(*self.VIDEOS)


