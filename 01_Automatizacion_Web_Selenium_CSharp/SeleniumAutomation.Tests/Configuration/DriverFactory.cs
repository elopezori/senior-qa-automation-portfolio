using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.Edge;
using OpenQA.Selenium.Firefox;
using SeleniumAutomation.Tests.Settings;

namespace SeleniumAutomation.Tests.Configuration;

public static class DriverFactory
{
    public static IWebDriver CreateDriver(string browser)
    {
        IWebDriver driver = browser.ToLowerInvariant() switch
        {
            "chrome" => CreateChromeDriver(),
            "firefox" => CreateFirefoxDriver(),
            "edge" => CreateEdgeDriver(),

            _ => throw new NotSupportedException(
                $"Browser '{browser}' is not supported."
            )
        };

        try
        {
            if (!TestSettings.Headless)
            {
                driver.Manage().Window.Maximize();
            }

            return driver;
        }
        catch
        {
            try
            {
                driver.Quit();
            }
            finally
            {
                driver.Dispose();
            }

            throw;
        }
    }

    private static IWebDriver CreateChromeDriver()
    {
        var options = new ChromeOptions();

        if (TestSettings.Headless)
            options.AddArgument("--headless=new");

        return new ChromeDriver(options);
    }

    private static IWebDriver CreateFirefoxDriver()
    {
        var options = new FirefoxOptions();

        if (TestSettings.Headless)
            options.AddArgument("--headless");

        return new FirefoxDriver(options);
    }

    private static IWebDriver CreateEdgeDriver()
    {
        var options = new EdgeOptions();

        if (TestSettings.Headless)
            options.AddArgument("--headless=new");

        return new EdgeDriver(options);
    }
}