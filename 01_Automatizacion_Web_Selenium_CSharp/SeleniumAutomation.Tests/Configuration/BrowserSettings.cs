namespace SeleniumAutomation.Tests.Configuration;

public static class BrowserSettings
{
    // Activa o desactiva los navegadores
    public static bool RunChrome = true;
    public static bool RunEdge = true;
    public static bool RunFirefox = true;

    // Orden de ejecución
    public static IEnumerable<string> EnabledBrowsers
    {
        get
        {
            if (RunChrome)
                yield return "Chrome";

            if (RunEdge)
                yield return "Edge";

            if (RunFirefox)
                yield return "Firefox";
        }
    }
}