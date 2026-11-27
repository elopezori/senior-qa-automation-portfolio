using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using SeleniumAutomation.Tests.Settings;

namespace SeleniumAutomation.Tests.Configuration;

public static class DriverFactory
{
    public static IWebDriver CreateDriver()
    {
        if (TestSettings.Browser.Equals("Chrome", StringComparison.OrdinalIgnoreCase))
        {
            var options = new ChromeOptions();

            options.AddArgument("--start-maximized");

            if (TestSettings.Headless)
            {
                options.AddArgument("--headless=new");
            }

            return new ChromeDriver(options);
        }

        throw new NotSupportedException(
            $"Browser '{TestSettings.Browser}' is not supported.");
    }
}