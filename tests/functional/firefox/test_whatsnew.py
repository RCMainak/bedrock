# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from selenium.common.exceptions import TimeoutException
from pages.firefox.whatsnew import FirefoxWhatsNewPage


@pytest.mark.skip_if_not_firefox(reason='Whatsnew pages are shown to Firefox only.')
@pytest.mark.nondestructive
def test_send_to_device_success(base_url, selenium):
    page = FirefoxWhatsNewPage(selenium, base_url).open()
    assert not page.is_qr_code_displayed
    send_to_device = page.send_to_device
    send_to_device.type_email('success@example.com')
    send_to_device.click_send()
    assert send_to_device.send_successful


@pytest.mark.skip_if_not_firefox(reason='Whatsnew pages are shown to Firefox only.')
@pytest.mark.nondestructive
def test_send_to_device_fails_when_missing_required_fields(base_url, selenium):
    page = FirefoxWhatsNewPage(selenium, base_url).open()
    with pytest.raises(TimeoutException):
        page.send_to_device.click_send()


@pytest.mark.skip_if_not_firefox(reason='Whatsnew pages are shown to Firefox only.')
@pytest.mark.nondestructive
def test_firefox_rocket_send_yourself(base_url, selenium):
    page = FirefoxWhatsNewPage(selenium, base_url, locale='id').open()
    assert page.send_yourself.is_displayed
    send_yourself = page.send_yourself
    send_yourself.type_email('success@example.com')
    send_yourself.click_send()
    assert send_yourself.send_successful
