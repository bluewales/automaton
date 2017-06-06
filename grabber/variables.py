import datetime
from grabber.stock_grabber import StockGrabber


class Variables:

    def __init__(self):

        self.sg = StockGrabber()

        self.stock_details = [
            dict(name="Open", description="Opening price"),
            dict(name="High", description="High price"),
            dict(name="Low", description="Low price"),
            dict(name="Close", description="Close price"),
            dict(name="Volume", description="Trade volume")
        ]

        self.stocks = [
            dict(ticker="AAL", name="American Airlines Group, Inc."),
            dict(ticker="AAPL", name="Apple Inc."),
            dict(ticker="ADBE", name="Adobe Systems Incorporated"),
            dict(ticker="ADI", name="Analog Devices, Inc."),
            dict(ticker="ADP", name="Automatic Data Processing, Inc."),
            dict(ticker="ADSK", name="Autodesk, Inc."),
            dict(ticker="AKAM", name="Akamai Technologies, Inc."),
            dict(ticker="ALXN", name="Alexion Pharmaceuticals, Inc."),
            dict(ticker="AMAT", name="Applied Materials, Inc."),
            dict(ticker="AMGN", name="Amgen Inc."),
            dict(ticker="AMZN", name="Amazon.com, Inc."),
            dict(ticker="ATVI", name="Activision Blizzard, Inc"),
            dict(ticker="AVGO", name="Broadcom Limited"),
            dict(ticker="BIDU", name="Baidu, Inc."),
            dict(ticker="BIIB", name="Biogen Inc."),
            dict(ticker="BMRN", name="BioMarin Pharmaceutical Inc."),
            dict(ticker="CA", name="CA Inc."),
            dict(ticker="CELG", name="Celgene Corporation"),
            dict(ticker="CERN", name="Cerner Corporation"),
            dict(ticker="CHKP", name="Check Point Software Technologies Ltd."),
            dict(ticker="CHTR", name="Charter Communications, Inc."),
            dict(ticker="CMCSA", name="Comcast Corporation"),
            dict(ticker="COST", name="Costco Wholesale Corporation"),
            dict(ticker="CSCO", name="Cisco Systems, Inc."),
            dict(ticker="CSX", name="CSX Corporation"),
            dict(ticker="CTAS", name="Cintas Corporation"),
            dict(ticker="CTRP", name="Ctrip.com International, Ltd."),
            dict(ticker="CTSH", name="Cognizant Technology Solutions Corporation"),
            dict(ticker="CTXS", name="Citrix Systems, Inc."),
            dict(ticker="DISCA", name="Discovery Communications, Inc."),
            dict(ticker="DISCK", name="Discovery Communications, Inc."),
            dict(ticker="DISH", name="DISH Network Corporation"),
            dict(ticker="DLTR", name="Dollar Tree, Inc."),
            dict(ticker="EA", name="Electronic Arts Inc."),
            dict(ticker="EBAY", name="eBay Inc."),
            dict(ticker="ESRX", name="Express Scripts Holding Company"),
            dict(ticker="EXPE", name="Expedia, Inc."),
            dict(ticker="FAST", name="Fastenal Company"),
            dict(ticker="FB", name="Facebook, Inc."),
            dict(ticker="FISV", name="Fiserv, Inc."),
            dict(ticker="FOX", name="Twenty-First Century Fox, Inc."),
            dict(ticker="FOXA", name="Twenty-First Century Fox, Inc."),
            dict(ticker="GILD", name="Gilead Sciences, Inc."),
            dict(ticker="GOOG", name="Alphabet Inc."),
            dict(ticker="GOOGL", name="Alphabet Inc."),
            dict(ticker="HAS", name="Hasbro, Inc."),
            dict(ticker="HOLX", name="Hologic, Inc."),
            dict(ticker="HSIC", name="Henry Schein, Inc."),
            dict(ticker="IDXX", name="IDEXX Laboratories, Inc."),
            dict(ticker="ILMN", name="Illumina, Inc."),
            dict(ticker="INCY", name="Incyte Corporation"),
            dict(ticker="INTC", name="Intel Corporation"),
            dict(ticker="INTU", name="Intuit Inc."),
            dict(ticker="ISRG", name="Intuitive Surgical, Inc."),
            dict(ticker="JBHT", name="J.B. Hunt Transport Services, Inc."),
            dict(ticker="JD", name="JD.com, Inc."),
            dict(ticker="KHC", name="The Kraft Heinz Company"),
            dict(ticker="KLAC", name="KLA-Tencor Corporation"),
            dict(ticker="LBTYA", name="Liberty Global plc"),
            dict(ticker="LBTYK", name="Liberty Global plc"),
            dict(ticker="LILA", name="Liberty Global plc"),
            dict(ticker="LILAK", name="Liberty Global plc"),
            dict(ticker="LRCX", name="Lam Research Corporation"),
            dict(ticker="LVNTA", name="Liberty Interactive Corporation"),
            dict(ticker="MAR", name="Marriott International"),
            dict(ticker="MAT", name="Mattel, Inc."),
            dict(ticker="MCHP", name="Microchip Technology Incorporated"),
            dict(ticker="MDLZ", name="Mondelez International, Inc."),
            dict(ticker="MNST", name="Monster Beverage Corporation"),
            dict(ticker="MSFT", name="Microsoft Corporation"),
            dict(ticker="MU", name="Micron Technology, Inc."),
            dict(ticker="MXIM", name="Maxim Integrated Products, Inc."),
            dict(ticker="MYL", name="Mylan N.V."),
            dict(ticker="NCLH", name="Norwegian Cruise Line Holdings Ltd."),
            dict(ticker="NFLX", name="Netflix, Inc."),
            dict(ticker="NTES", name="NetEase, Inc."),
            dict(ticker="NVDA", name="NVIDIA Corporation"),
            dict(ticker="ORLY", name="O'Reilly Automotive, Inc."),
            dict(ticker="PAYX", name="Paychex, Inc."),
            dict(ticker="PCAR", name="PACCAR Inc."),
            dict(ticker="PCLN", name="The Priceline Group Inc."),
            dict(ticker="PYPL", name="PayPal Holdings, Inc."),
            dict(ticker="QCOM", name="QUALCOMM Incorporated"),
            dict(ticker="QVCA", name="Liberty Interactive Corporation"),
            dict(ticker="REGN", name="Regeneron Pharmaceuticals, Inc."),
            dict(ticker="ROST", name="Ross Stores, Inc."),
            dict(ticker="SBUX", name="Starbucks Corporation"),
            dict(ticker="SHPG", name="Shire plc"),
            dict(ticker="SIRI", name="Sirius XM Holdings Inc."),
            dict(ticker="STX", name="Seagate Technology PLC"),
            dict(ticker="SWKS", name="Skyworks Solutions, Inc."),
            dict(ticker="SYMC", name="Symantec Corporation"),
            dict(ticker="TMUS", name="T-Mobile US, Inc."),
            dict(ticker="TSCO", name="Tractor Supply Company"),
            dict(ticker="TSLA", name="Tesla, Inc."),
            dict(ticker="TXN", name="Texas Instruments Incorporated"),
            dict(ticker="ULTA", name="Ulta Beauty, Inc."),
            dict(ticker="VIAB", name="Viacom Inc."),
            dict(ticker="VOD", name="Vodafone Group Plc"),
            dict(ticker="VRSK", name="Verisk Analytics, Inc."),
            dict(ticker="VRTX", name="Vertex Pharmaceuticals Incorporated"),
            dict(ticker="WBA", name="Walgreens Boots Alliance, Inc."),
            dict(ticker="WDC", name="Western Digital Corporation"),
            dict(ticker="WYNN", name="Wynn Resorts, Limited"),
            dict(ticker="XLNX", name="Xilinx, Inc."),
            dict(ticker="XRAY", name="DENTSPLY SIRONA Inc."),
            dict(ticker="YHOO", name="Yahoo! Inc.")

        ]

        self.calendar_variables = [
            {
                'name': "day_of_week",
                'description': "day of the week, a number 1-7",
                'type': "calendar",
                'fetcher': lambda day: day.weekday()+1
            },
            {
                'name': "day",
                'description': "day part of the date",
                'type': "calendar",
                'fetcher': lambda day: day.day
            },
            {
                'name': "month",
                'description': "month part of the date",
                'type': "calendar",
                'fetcher': lambda day: day.month
            },
            {
                'name': "year",
                'description': "year part of the date",
                'type': "calendar",
                'fetcher': lambda day: day.year
            },
            {
                'name': "week_of_year",
                'description': "week number of the year",
                'type': "calendar",
                'fetcher': lambda day: day.isocalendar()[1]
            }
        ]

    def stock_variable_from_detail(self, stock, detail):
        return {
            'name':stock['ticker']+" "+detail['name'],
            'description':detail['description']+" of "+stock['name']+" stock",
            'type': "stock",
            'fetcher': lambda day: self.sg.fetch_stock_data(stock['ticker'], day, detail['name'])
        }

    def get_variable_list(self):

        for v in self.calendar_variables:
            yield v

        for s in self.stocks:
            for d in self.stock_details:
                yield self.stock_variable_from_detail(s,d)

