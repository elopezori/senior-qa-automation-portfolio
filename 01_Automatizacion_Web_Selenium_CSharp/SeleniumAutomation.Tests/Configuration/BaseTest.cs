using Allure.Net.Commons;
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
        var browser = TestContext.CurrentContext.Test.Arguments
            .FirstOrDefault()?.ToString()
            ?? TestSettings.Browser;

        Driver = DriverFactory.CreateDriver(browser);

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
                try
                {
                    var screenshot = ((ITakesScreenshot)Driver).GetScreenshot();

                    var screenshotDirectory = Path.Combine(
                        TestContext.CurrentContext.WorkDirectory,
                        "TestResults",
                        "Screenshots"
                    );

                    Directory.CreateDirectory(screenshotDirectory);

                    var safeTestName = string.Concat(
                        TestContext.CurrentContext.Test.Name.Select(
                        c => Path.GetInvalidFileNameChars().Contains(c) ? '_' : c
                        )
                    );

                    var fileName =
                        $"{safeTestName}_{DateTime.Now:yyyyMMdd_HHmmss}.png";

                    var filePath = Path.Combine(
                        screenshotDirectory,
                        fileName
                    );

                    // Guardar captura en disco
                    screenshot.SaveAsFile(filePath);

                    // Adjuntar captura al resultado de NUnit
                    TestContext.AddTestAttachment(filePath);

                    // Adjuntar captura al resultado de Allure
                    AllureApi.AddAttachment(
                        "Screenshot",
                        "image/png",
                        screenshot.AsByteArray,
                        "png"
                    );

                    TestContext.Progress.WriteLine(
                        $"Screenshot saved: {filePath}"
                    );
                }
                catch (Exception ex)
                {
                    TestContext.Progress.WriteLine(
                        $"Could not save or attach screenshot: {ex.Message}"
                    );
                }
            }
        }
        finally
        {
            if (Driver != null)
            {
                try
                {
                    Driver.Quit();
                }
                finally
                {
                    Driver.Dispose();
                }
            }
        }
    }
}