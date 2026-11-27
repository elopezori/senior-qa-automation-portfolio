using Allure.NUnit;
using Allure.Net.Commons;
using NUnit.Framework;
using SeleniumAutomation.Tests.Configuration;
using SeleniumAutomation.Tests.Pages;

namespace SeleniumAutomation.Tests.Tests;

[AllureNUnit]
public class HomePageTests : BaseTest
{
    [TestCaseSource(
        typeof(BrowserSettings),
        nameof(BrowserSettings.EnabledBrowsers)
    )]
    public void HomePage_ShouldDisplayCorrectTitle(string browser)
    {
        // Arrange
        AllureApi.AddLabel("browser", browser);
        AllureApi.AddFeature("Automatización Web");
        AllureApi.AddStory("Página principal");

        TestContext.Progress.WriteLine(
            $"Executing test with browser: {browser}"
        );

        var homePage = new HomePage(Driver, Wait);

        // Act
        homePage.Navigate();
        var pageTitle = homePage.GetPageTitle();

        // Assert
        Assert.That(pageTitle, Is.EqualTo(homePage.ExpectedTitle));
    }
}