
using Microsoft.Playwright;
using NUnit.Framework;
using System.Threading.Tasks;

namespace QAAutomation.Tests;

public class Tests
{
    private IPlaywright _playwright = null!;
    private IBrowser _browser = null!;
    private IPage _page = null!;

    [SetUp]
    public async Task Setup()
    {
        _playwright = await Playwright.CreateAsync();

        _browser = await _playwright.Chromium.LaunchAsync(
            new BrowserTypeLaunchOptions
            {
                Headless = false
            });

        _page = await _browser.NewPageAsync();
    }

    [Test]
    public async Task LoginPage_ShouldDisplayCorrectTitle()
    {
        await _page.GotoAsync("https://www.saucedemo.com/");

        var title = await _page.TitleAsync();

        Assert.That(title, Is.EqualTo("Swag Labs"));
    }

    [TearDown]
    public async Task TearDown()
    {
        if (_browser != null)
            await _browser.CloseAsync();

        _playwright?.Dispose();
    }
}