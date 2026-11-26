using NUnit.Framework;
using OpenQA.Selenium;

namespace SeleniumAutomation.Tests.Configuration;

public class BaseTest
{
    protected IWebDriver Driver = null!;

    [SetUp]
    public void SetUp()
    {
        Driver = DriverFactory.CreateDriver();
    }

    [TearDown]
    public void TearDown()
    {
        Driver?.Quit();
        Driver?.Dispose();
    }
}