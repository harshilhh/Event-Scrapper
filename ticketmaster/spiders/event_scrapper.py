import scrapy

class EventSpider(scrapy.Spider):
    name = 'Get_Events'
    custom_settings = {
        'PLAYWRIGHT_BROWSER_TYPE': 'chromium',
        'PLAYWRIGHT_LAUNCH_OPTIONS': {
            'headless': True,
            'timeout': 1800000, 
        },
        'PLAYWRIGHT_DEFAULT_NAVIGATION_TIMEOUT': 1800000 
    }

    def start_requests(self):
        urls = ['https://www.ticketmaster.com/the-rock-orchestra-by-candlelight-saginaw-michigan-02-23-2025/event/080060FFBB554D0F',
                'https://www.ticketmaster.com/leanne-morgan-just-getting-started-saginaw-michigan-05-16-2025/event/0800612AEE6F4C9C',
                'https://www.ticketmaster.com/pretty-woman-the-musical-touring-saginaw-michigan-04-28-2025/event/080060C4BD212E02',
                'https://www.ticketmaster.com/clint-black-35th-anniversary-of-killin-saginaw-michigan-02-27-2025/event/08006131DE71384D',
                'https://www.ticketmaster.com/saginaw-spirit-vs-guelph-storm-saginaw-michigan-01-18-2025/event/080060EEB9A6249B'
                ]

        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "en-US,en;q=0.9",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
            "referer": "https://www.ticketmaster.com/the-rock-orchestra-by-candlelight-saginaw-michigan-02-23-2025/event/080060FFBB554D0F",
            "upgrade-insecure-requests": "1",
        }

        cookies = {'eps_sid': '849b00f4e610e3d45de78c48500f668e5d204c6c', 'LANGUAGE': 'en-us', 'NDMA': '200', 'SID': 'vsf0JDMWAutVJVA3TNnWoYBKrI2HjxtxnHBmcSxtsefQAVfVhrq77GQ-BtuNzHU0hSlL5sBmqdtuCADo', 'TMUO': 'west_NQskogAws3OB22OPHDpBD/O2LxGfSkjXvK497xAIOg8=', '_gid': 'GA1.2.1569225154.1736656420', 'TM_PIXEL': '{"_dvs":"0:m5t4e6oy:tuRTmFFrhS3S5eZYiXCl5DxlE7UF4dyu","_dvp":"0:m5t4e6oy:TRmnYt3ME6SpDx_Fhf_lXOZtf_amAEJE"}', '_dvp': '0:m5t4e6oy:TRmnYt3ME6SpDx_Fhf_lXOZtf_amAEJE', 'OptanonAlertBoxClosed': '2025-01-12T04:39:55.298Z', 'OptanonGroups': ',C0001,C0003,C0002,C0004,', '_au_1d': 'AU1D0200001736656796CUWH3UQJ420M', '_gcl_au': '1.1.934991941.1736656796', 'mt.v': '2.884540712.1736656796610', 'mt.pc': '2.1', 'mt.g.2f013145': '2.884540712.1736656796610', '_fbp': 'fb.1.1736656797254.327813109739998221', '_tt_enable_cookie': '1', '_ttp': 'hhZ9BQ_JDWoP-eD9NRWaoGxSK39.tt.1', '_cs_c': '0', '__qca': 'P0-2077010208-1736656798615', 'BID': 'uUSm7ARBxRqV9UFvvVbaPlqOumNKbRmni3mKzbKRYBLOzPeIW_st3JyS2F9vIUWGBrqn4z8Zownyjmr2', 'seerid': 'a2b019cc-5761-44f5-832d-734001ae95d7', 'lightstep_guid%2Fco2.sdk': '48261c6c47161816', 'lightstep_session_id': '73b9970618641e5b', '_scid': 'xGzsuwxXG8gmJFLyYaeOQd9xqDdhaNbz', '_ScCbts': '%5B%5D', '_sctr': '1%7C1736620200000', '_hjSessionUser_2908124': 'eyJpZCI6IjE1NGYzZjIwLWNjYTctNWIzZi1hY2Q1LTc2NGJmMjAzNzYxMyIsImNyZWF0ZWQiOjE3MzY2NTcwNTQzNzAsImV4aXN0aW5nIjpmYWxzZX0=', '_ga_75XNXGG1ZD': 'GS1.1.1736657054.1.1.1736657204.47.0.0', 'ARTIST': '805992', 'VENUE': '237572', 'AMCVS_A65F776A5245B01B0A490D44%40AdobeOrg': '1', 'AMCV_A65F776A5245B01B0A490D44%40AdobeOrg': '1687686476%7CMCIDTS%7C20101%7CMCMID%7C30735075579747716200587301278960918768%7CMCAAMLH-1737262039%7C12%7CMCAAMB-1737262039%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1736664439s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C3.0.0', 's_cc': 'true', '_ga_N8YFCZLYSZ': 'GS1.1.1736657242.1.0.1736657242.60.0.1046855206', '_pn': 'eyJzdWIiOnsidWRyIjowLCJpZCI6IkZaWlJ2SlNFRmFrS203bTdVSm9qZEhmaDNvZXVEOWxVIiwic3MiOjJ9LCJsdWEiOjE3MzY2NTc0NDA5NzZ9', '_dvs': '0:m5t4e6oy:tuRTmFFrhS3S5eZYiXCl5DxlE7UF4dyu', 'seerses': 'e', 'tmpt': '0:081e2034f6000000:1736666651:4d67ee42:dd4dac40bd9e7255caaff410975ad1c3:230b2049eb93fc75249748733dd3d78bad6c613506aafb776e2aaa0acc4e6710', '_ga': 'GA1.1.26801149.1736656419', '_ga_C1T806G4DF': 'GS1.1.1736666645.3.1.1736666655.50.0.0', '_ga_H1KKSGW33X': 'GS1.1.1736666645.3.1.1736666655.50.0.0', '_scid_r': '1ezsuwxXG8gmJFLyYaeOQd9xqDdhaNbzLJ-biA', '_cs_cvars': '%7B%221%22%3A%5B%22Page%20Name%22%2C%22TM_US%3A%20CCP%20EDP%3A%20RS%3A%20Offsale%22%5D%2C%222%22%3A%5B%22Page%20Type%22%2C%22CCP%20EDP%3A%20Offsale%22%5D%2C%223%22%3A%5B%22Modules%20Available%22%2C%22EDP_Rse%22%5D%2C%224%22%3A%5B%22Platform%22%2C%22ccp-edp%22%5D%2C%225%22%3A%5B%22Login%20Status%22%2C%22Not%20Logged%20In%22%5D%2C%226%22%3A%5B%22Major%20Category%22%2C%22Music%22%5D%2C%227%22%3A%5B%22Minor%20Category%22%2C%22Rock%22%5D%2C%228%22%3A%5B%22Artist%20ID%22%2C%222967647%22%5D%2C%229%22%3A%5B%22Artist%20Name%22%2C%22The%20Rock%20Orchestra%20By%20Candlelight%22%5D%2C%2210%22%3A%5B%22Venue%20ID%22%2C%2265965%22%5D%2C%2211%22%3A%5B%22Event%20ID%22%2C%22080060FFBB554D0F%22%5D%2C%2212%22%3A%5B%22Event%20Date%22%2C%222%2F23%2F2025%22%5D%2C%2213%22%3A%5B%22EDP%20Page%20Type%22%2C%22CCP%20EDP%3A%20SIM%22%5D%2C%2214%22%3A%5B%22Event%20Type%22%2C%22STANDARD%22%5D%7D', '_cs_id': 'd5086f42-fa3d-acc4-dc67-38015305d428.1736656798.2.1736666656.1736666338.1723134244.1770820798319.1', 'OptanonConsent': 'isGpcEnabled=0&datestamp=Sun+Jan+12+2025+12%3A54%3A16+GMT%2B0530+(India+Standard+Time)&version=202408.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=e208c9a9-0530-4134-839b-0409092f706a&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&AwaitingReconsent=false&intType=1&geolocation=IN%3BGJ', '_uetsid': '4664a2d0d09f11efb61c05b263c09b56|re1w9f|2|fsi|0|1838', '__gads': 'ID=7d6d76f5457f06f6:T=1736656899:RT=1736666656:S=ALNI_MY3355EAwd5hNtUkDn9VCr88-gIIw', '__eoi': 'ID=f8d191793d9effb8:T=1736656899:RT=1736666656:S=AA-AfjY9Km2L3G7FlUcBHOmJ-T-V', '_uetvid': '4664cc50d09f11ef92d6618c47e03e54|w65m9c|1736666657554|1|1|bat.bing.com/p/insights/c/i', '_cs_s': '5.5.1.1736669610865'}
        for single_url in urls:
            yield scrapy.Request(
                single_url,
                headers=headers,
                cookies=cookies,
                meta=dict(
                    playwright=True,
                    playwright_include_page=True
                )
            )

    async def parse(self, response):
        try:
            event_name=response.css("h1.sc-1eku3jf-14.ghwxrG::text").get()
            date_time=response.css("span.sc-1eku3jf-16.dCPMfd span::text").get().encode('ascii', 'ignore').decode()
            venue_name=response.css("a.sc-1akkrr6-1.dvPJxG::text").get()
            venue_url=response.css("a.sc-1akkrr6-1.dvPJxG::attr(href)").get()

            yield{
                "Event Url":response.url,
                "Event Name":event_name,
                "Event Date Time": date_time,
                "Venue Name":venue_name,
                "Venue Url":venue_url
            }
        except Exception as e:
            self.logger.error(f"Error processing {response.url}: {e}")


