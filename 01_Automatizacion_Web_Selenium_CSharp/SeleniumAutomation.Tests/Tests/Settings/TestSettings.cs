namespace SeleniumAutomation.Tests.Settings;

public static class TestSettings
{
    public static string BaseUrl =>
        Environment.GetEnvironmentVariable("SELENIUM_BASE_URL")
        ?? "https://the-internet.herokuapp.com/";

    public static int DefaultTimeoutInSeconds =>
        int.TryParse(
            Environment.GetEnvironmentVariable("SELENIUM_TIMEOUT"),
            out var timeout
        ) && timeout > 0
            ? timeout
            : 10;

    public static bool Headless =>
        bool.TryParse(
            Environment.GetEnvironmentVariable("SELENIUM_HEADLESS"),
            out var headless
        ) && headless;

    public static string Browser =>
        Environment.GetEnvironmentVariable("SELENIUM_BROWSER")
        ?? "Chrome";
}
