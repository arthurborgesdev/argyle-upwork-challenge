user_agent = ("Mozilla/5.0 (X11; Linux x86_64)"
              "AppleWebKit/537.36 (KHTML, like Gecko)"
              "Chrome/90.0.4430.93 Safari/537.36"
              )


def test_title(browser):
    context = browser.new_context(
                  user_agent=user_agent
              )
  
    page = context.new_page()
    page.goto('https://www.upwork.com/ab/account-security/login')
    assert page.title() == 'Log In - Upwork'