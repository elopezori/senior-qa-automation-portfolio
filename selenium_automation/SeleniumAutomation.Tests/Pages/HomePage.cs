using OpenQA.Selenium;

namespace SeleniumAutomation.Tests.Pages;

public class HomePage
{
    private readonly IWebDriver _driver;

    private const string Url = "https://the-internet.herokuapp.com/";

    public HomePage(IWebDriver driver)
    {
        _driver = driver;
    }

    public void Navigate()
    {
        _driver.Navigate().GoToUrl(Url);
    }

    public string GetPageTitle()
    {
        return _driver.Title;
    }
}