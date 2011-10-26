from selenium import selenium
import unittest, time, re

class example_test(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://code.google.com/")
        self.selenium.start()
    
    def test_example_test(self):
        sel = self.selenium
        sel.open("/p/selenium/source/checkout")
        sel.addLocationStrategy("asdf", "qwe")
        sel.addLocationStrategyAndWait("sdfg", "wer")
        sel.allowNativeXpath("true")
        sel.allowNativeXpathAndWait("false")
        sel.altKeyDown()
        sel.altKeyUpAndWait()
        sel.assertAlert()
        sel.assertAlertPresent()
        sel.assertTextPresent("Perl WebDriver bindings")
        sel.assertNotAlert()
        sel.assertNotWhetherThisWindowMatchWindowExpression("qwe", "tgb")
        sel.verifyElementPresent("//td[@id='wikicontent']/h2[2]")
        sel.assignId("css=#rfv", "rfvv")
        sel.captureEntirePageScreenshotAndWait("asdf.png", "background=#CCFFDD")
        sel.check("css=#qay")
        sel.chooseOkOnNextConfirmationAndWait()
        sel.clickAndWait("css=#zhn")
        sel.close()
        sel.contextMenuAtAndWait("css=#edc", "-10,20")
        sel.createCookieAndWait("name=value", "path=/path/, max_age=60, domain=.foo.com")
        sel.deleteAllVisibleCookies()
        sel.deselectPopUp()
        sel.doubleClickAndWait("css=#qwe")
        sel.dragAndDrop("css=#rte", "+70,-300")
        sel.echo("Hallo Echo!")
        sel.fireEvent("css=#ert", "blur")
        sel.focus("css=#qwe")
        sel.goBackAndWait()
        sel.highlight("css=#dsf")
        sel.ignoreAttributesWithoutValue("true")
        sel.keyDown("css=#ed", "w")
        sel.openWindow("http://seleniumhq.com", "selhq")
        sel.open("http://asdf.com")
        time.sleep(1)
        sel.refreshAndWait()
        sel.removeScript("qay")
        sel.selectFrame("css=#f1")
        sel.setBrowserLogLevel("debug")
        sel.setMouseSpeed("200")
        sel.setSpeed("1")
        sel.setTimeout("20")
        sel.shiftKeyDown()
        var1 = "sdfg"
        sel.storeAllButtons()
        sel.submitAndWait("css=#form1")
        sel.typeKeys("css=#er", "asdf")
        sel.useXpathLibrary("ajaxslt")
        sel.verifyAlertPresent()
        sel.verifyAttribute("//div@id")
        sel.verifyNotBodyText()
        sel.verifyOrdered("css=#id1", "css=#id2")
        sel.waitForAlert()
        sel.waitForCssCount("css=table")
        sel.waitForNotAttribute("foo@bar")
        sel.waitForPageToLoad("30")
        sel.windowMaximize()
        sel.windowFocus()
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
