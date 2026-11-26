using NUnit.Framework;
using SeleniumAutomation.Tests.Configuration;
using SeleniumAutomation.Tests.Pages;

namespace SeleniumAutomation.Tests.Tests;

public class HomePageTests : BaseTest
{
    [Test]
    public void HomePage_ShouldDisplayCorrectTitle()
    {
        // Arrange
        var homePage = new HomePage(Driver);

        // Act
        homePage.Navigate();
        var pageTitle = homePage.GetPageTitle();

        // Assert
        Assert.That(pageTitle, Is.EqualTo("The Internet"));
    }
}