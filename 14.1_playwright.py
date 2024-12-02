import os
import warnings
os.environ['KPM_DUPLICATE_LIB_OK'] = 'True'
warnings.filterwarnings('ignore')

from langchain_community.agent_toolkits import PlayWrightBrowserToolkit
from langchain_community.tools.playwright.utils import (
    create_async_playwright_browser,  # A synchronous browser is available, though it isn't compatible with jupyter.\n",	  },
)
import nest_asyncio
import asyncio



def main():
    nest_asyncio.apply()
    async_browser = create_async_playwright_browser()
    toolkit = PlayWrightBrowserToolkit.from_browser(async_browser=async_browser)
    tools = toolkit.get_tools()

    tools_by_name = {tool.name: tool for tool in tools}
    navigate_tool = tools_by_name["navigate_browser"]
    get_elements_tool = tools_by_name["get_elements"]
    

if __name__ == "__main__":
    main()