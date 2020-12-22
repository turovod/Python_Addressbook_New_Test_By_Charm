import re


def test_phone_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)

    assert contact_from_home_page.homephone == clear(contact_from_edit_page.homephone)
    assert contact_from_home_page.mobilephone == clear(contact_from_edit_page.mobilephone)
    assert contact_from_home_page.fax == clear(contact_from_edit_page.fax)
    assert contact_from_home_page.workphone == clear(contact_from_edit_page.workphone)


def test_phone_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)

    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.fax == contact_from_edit_page.fax
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone


def test_phone_on_home_page_stable(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)

    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_from_home_page(contact_from_edit_page)


# regex: replace unnecessary characters with an empty string
def clear(s):
    return re.sub("[() -qwertyuiopasdfghjkl:xcvbnm,./MNBVCXZASDFGHJKL;'POIUYTREWQ]", "", s)


def merge_phones_like_on_from_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone,  contact.workphone, contact.mobilephone, contact.fax]))))
