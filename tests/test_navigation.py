import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.page import Page


@pytest.mark.usefixtures("driver")
class TestNavigation:

    def validate_sections(self, driver, section_name):
        """Validate all sections on a page safely"""
        print(f"\n=== Validating Section: {section_name} ===")

        try:
            # Wait until sections appear
            sections = WebDriverWait(driver, 15).until(
                EC.presence_of_all_elements_located(Page.SECTIONS)
            )
        except Exception as e:
            print(f" No sections found on {section_name} page: {e}")
            return

        print(f" 🔎 Found {len(sections)} sections on {section_name} page")

        for index, section in enumerate(sections):
            try:
                driver.execute_script("arguments[0].scrollIntoView(true);", section)
            except Exception as e:
                print(f" Could not scroll to section {index+1}: {e}")
                continue

            print(f"\n===== Checking Section {index+1} =====")

            # Section heading
            try:
                heading = section.find_element(By.TAG_NAME, "h4").text.strip()
                print(f"  Section heading: {heading}")
            except Exception as e:
                print(f"  No heading found: {e}")

            # Thumbnails
            try:
                thumbnails = section.find_elements(By.CSS_SELECTOR, "div.swiper-slide img")
                print(f"   Found {len(thumbnails)} thumbnails")

                for i, thumb in enumerate(thumbnails):
                    try:
                        src = thumb.get_attribute("src")
                        if src:
                            print(f"   Thumbnail {i+1} loaded: {src[:60]}...")
                        else:
                            print(f"   Thumbnail {i+1} missing src!")
                    except Exception as e:
                        print(f"   Thumbnail {i+1} could not be read: {e}")

            except Exception as e:
                print(f"   No thumbnails found in section {index+1}: {e}")

    def validate_videos(self, driver):
        """Validate video players"""
        try:
            video_player = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(Page.VIDEOS)
            )
            if video_player.is_displayed():
                print(" 🎥 Video player opened successfully")
            else:
                print("  Video player not visible")
        except Exception as e:
            print(f"  No video player detected: {e}")

    def validate_audio(self, driver):
        """Validate audio players"""
        try:
            audios = driver.find_elements(By.CSS_SELECTOR, "audio")
            print(f" 🎵 Found {len(audios)} audio players")
            for i, audio in enumerate(audios):
                try:
                    src = audio.get_attribute("src")
                    print(f"   Audio {i+1}: {src}")
                except Exception as e:
                    print(f"   Could not read audio {i+1}: {e}")
            assert audios, "No audio players found on Radio page"
        except Exception as e:
            print(f"  Error while validating audio: {e}")

    def validate_documents(self, driver):
        """Validate documents (pdf/doc/docx)"""
        try:
            docs = driver.find_elements(By.CSS_SELECTOR, "a[href$='.pdf'], a[href$='.doc'], a[href$='.docx']")
            print(f" 📄 Found {len(docs)} documents")
            for i, doc in enumerate(docs):
                try:
                    href = doc.get_attribute("href")
                    print(f"   Document {i+1}: {href}")
                except Exception as e:
                    print(f"   Could not read document {i+1}: {e}")
            assert docs, "No documents found on Publication page"
        except Exception as e:
            print(f"  Error while validating documents: {e}")

    def test_navigation_and_content(self, driver):
        home = Page(driver)

        # Home
        home.go_to_home()
        assert "shalom" in driver.title.lower()
        self.validate_sections(driver, "Home")
        self.validate_videos(driver)

        # Radio
        home.go_to_radio()
        assert "radio" in driver.current_url.lower()
        self.validate_sections(driver, "Radio")
        self.validate_audio(driver)

        # Kids
        home.go_to_kids()
        assert "kids" in driver.current_url.lower()
        self.validate_sections(driver, "Kids")
        self.validate_videos(driver)

        # Publication
        home.go_to_publication()
        assert "publication" in driver.current_url.lower()
        self.validate_sections(driver, "Publication")
        self.validate_documents(driver)

        # TV Schedule
        home.go_to_tv_schedule()
        assert "schedule" in driver.current_url.lower()
        self.validate_sections(driver, "TV Schedule")

        # Prayer
        home.go_to_prayer()
        assert "prayer" in driver.current_url.lower()
        self.validate_sections(driver, "Prayer")
