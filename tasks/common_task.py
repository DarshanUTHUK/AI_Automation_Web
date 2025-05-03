from browser_use.agent.views import ActionResult
from browser_use.browser.context import BrowserContext
from utils.controller_instance import ControllerInstance
from testdata.testdata import TestDataModel


class CommonTask:

    contro = ControllerInstance()
    controller = contro.controller()

    task = ('Open Chrome browser along with website url'
                'Wait for the next steps prompt')

    @controller.action("Open Chrome browser along with website url", param_model=TestDataModel)
    async def open_website(params: TestDataModel, browser: BrowserContext):
        page = await browser.get_current_page()
        params.url = "https://parabank.parasoft.com/parabank/index.htm"
        await page.goto(params.url)
        current_url = await page.url
        page_text = await page.get_by_text("Parabank").get_attribute("title")
        return ActionResult(extracted_content=f"Browser opened and Nagivated to the Url {current_url} and attribute value is {page_text}")

