using OpenQA.Selenium;
using OpenQA.Selenium.Support.UI;
using SeleniumAutomation.Tests.Settings;

namespace SeleniumAutomation.Tests.Pages;

public class HomePage
{
    private readonly IWebDriver _driver;
    private readonly WebDriverWait _wait;

    public HomePage(IWebDriver driver, WebDriverWait wait)
    {
        _driver = driver;
        _wait = wait;
    }

    public void Navigate()
    {
        _driver.Navigate().GoToUrl(TestSettings.BaseUrl);

        _wait.Until(driver =>
            ((IJavaScriptExecutor)driver)
            .ExecuteScript("return document.readyState")
            ?.ToString() == "complete");
    }

    public string GetPageTitle()
    {
        return _wait.Until(driver =>
        {
            var title = driver.Title;
            return !string.IsNullOrWhiteSpace(title) ? title : null;
        })!;
    }
}