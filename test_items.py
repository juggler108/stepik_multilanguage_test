

def test_guest_should_see_button_add_to_basket(browser):
    basket_button = browser.find_element(by="class name", value="btn-add-to-basket")

    assert basket_button, "The basket button is not founded!"
