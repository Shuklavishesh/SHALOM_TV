import pytest
from pages.page import Page


@pytest.mark.usefixtures("driver")
class TestNavigation:

    def validate_section_content(self, home, driver, section_name):
        print(f"\n=== Validating Section: {section_name} ===")

        # Section Headings
        headings = home.get_section_headings()
        if headings:
            for h in headings:
                print(f"Section Heading: {h.text}")
                assert h.is_displayed()
        else:
            print(" No section headings found")

        # Thumbnails
        thumbs = home.get_video_thumbnails()
        if thumbs:
            for t in thumbs:
                src = t.get_attribute("src")
                if not t.is_displayed():
                    print(f" Hidden thumbnail: {src}")
                else:
                    print(f"Visible thumbnail: {src}")
                assert t.is_displayed(), f"Thumbnail not visible: {src}"
        else:
            print(" No thumbnails found")

        # Play Buttons + Video check
        play_buttons = home.get_play_buttons()
        if play_buttons:
            for idx, p in enumerate(play_buttons, start=1):
                assert p.is_displayed(), f"Play button {idx} not visible"
                print(f"Clicking Play button {idx}")
                p.click()
                driver.implicitly_wait(3)

                videos = home.get_videos()
                if videos:
                    print(f" Video {idx} loaded successfully")
                else:
                    print(f" Video {idx} did NOT load after clicking play")
        else:
            print(" No play buttons found")

    def test_navigation_and_content(self, driver):
        home = Page(driver) 

        # Home
        home.go_to_home()
        assert "shalom" in driver.title.lower()
        self.validate_section_content(home, driver, "Home")

        # Radio
        home.go_to_radio()
        assert "radio" in driver.current_url.lower()
        self.validate_section_content(home, driver, "Radio")

        # Kids
        home.go_to_kids()
        assert "kids" in driver.current_url.lower()
        self.validate_section_content(home, driver, "Kids")

        # Publication
        home.go_to_publication()
        assert "publication" in driver.current_url.lower()
        self.validate_section_content(home, driver, "Publication")

        # TV Schedule
        home.go_to_tv_schedule()
        assert "schedule" in driver.current_url.lower()
        self.validate_section_content(home, driver, "TV Schedule")

        # Prayer
        home.go_to_prayer()
        assert "prayer" in driver.current_url.lower()
        self.validate_section_content(home, driver, "Prayer") 
        
