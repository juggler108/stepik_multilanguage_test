

def test_guest_should_see_button_add_to_basket(browser):

    assert browser.find_elements(by="class name", value="btn-add-to-basket"), "The basket button is not founded!"
