using NUnit.Framework;
using OpenQA.Selenium;
using OpenQA.Selenium.Support.UI;
using SeleniumAutomation.Tests.Settings;

namespace SeleniumAutomation.Tests.Configuration;

public class BaseTest
{
    protected IWebDriver Driver = null!;
    protected WebDriverWait Wait = null!;

    [SetUp]
    public void SetUp()
    {
        Driver = DriverFactory.CreateDriver();

        Wait = new WebDriverWait(
            Driver,
            TimeSpan.FromSeconds(TestSettings.DefaultTimeoutInSeconds)
        );
    }

    [TearDown]
    public void TearDown()
    {
        try
        {
            if (Driver != null &&
                TestContext.CurrentContext.Result.Outcome.Status
                    == NUnit.Framework.Interfaces.TestStatus.Failed)
            {
                var screenshot = ((ITakesScreenshot)Driver).GetScreenshot();

                var screenshotDirectory = Path.Combine(
                    TestContext.CurrentContext.WorkDirectory,
                    "TestResults",
                    "Screenshots"
                );

                Directory.CreateDirectory(screenshotDirectory);

                var fileName = $"{TestContext.CurrentContext.Test.Name}_{DateTime.Now:yyyyMMdd_HHmmss}.png";

                var filePath = Path.Combine(screenshotDirectory, fileName);

                screenshot.SaveAsFile(filePath);

                TestContext.AddTestAttachment(filePath);
            }
        }
        finally
        {
            Driver?.Quit();
            Driver?.Dispose();
        }
    }
}