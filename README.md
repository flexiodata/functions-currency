# Currency Conversion Google Sheets & Excel Spreadsheet Add on

This Foreign Exchange Currency Conversion utility uses rates published by the European Central Bank and available through the [Foreign Exchange Rates API](https://exchangeratesapi.io/). This Currency Conversion spreadsheet integration for Google Sheets and Microsoft Excel enables you to convert currencies as well as list currency rates. This add-on will enable you to integrate on-demand, refreshable currency conversion without leaving your spreadsheet.

For example, with this Excel and Google Sheets add-on you can:

* Convert a currency amount to another currency, at current rate or rate based on a historic date.
* List foreign exchange rates for a basket of different currencies, at the current rates or based on a historic date.

Here are some examples:

```
=FLEX("YOUR_TEAM_NAME/currency-converter", 100, "EUR", "USD", "2018-12-31")
114.5
```

```
=FLEX("YOUR_TEAM_NAME/currency-rates", "EUR", "2018-12-31")
currency	amount
AUD	1.622
BGN	1.9558
BRL	4.444
CAD	1.5605
CHF	1.1269
CNY	7.8751
CZK	25.724
DKK	7.4673
GBP	0.89453
HKD	8.9675
HRK	7.4125
HUF	320.98
IDR	16500
ILS	4.2972
INR	79.7298
ISK	133.2
JPY	125.85
KRW	1277.93
MXN	22.4921
MYR	4.7317
NOK	9.9483
NZD	1.7056
PHP	60.113
PLN	4.3014
RON	4.6635
RUB	79.7153
SEK	10.2548
SGD	1.5591
THB	37.052
TRY	6.0588
USD	1.145
ZAR	16.4594
```

## Prerequisites

The Currency Spreadsheet Functions are powered by [Flex.io](https://www.flex.io). To use these functions, you'll need:

* A [Flex.io account](https://www.flex.io/app/signup) to run the functions
* A [Flex.io Add-on](https://www.flex.io/add-ons) for Microsoft Excel or Google Sheets to use the functions in your spreadsheet

## Installing the Functions

Once you've signed up for Flex.io and have the Flex.io Add-on installed, you're ready to install the function pack.

You can install these functions directly by mounting this repository in Flex.io:

1. [Sign in](https://www.flex.io/app/signin) to Flex.io
2. In the Functions area, click the "New" button in the upper-left and select "Function Mount" from the list
3. In the function mount dialog, select "GitHub", then authenticate with your GitHub account
4. In the respository URL box, enter the name of this repository, which is "flexiodata/functions-currency"
5. Click "Create Function Mount"

If you prefer, you can also install these using the [Flex.io Currency Integration](https://www.flex.io/integrations/currency).

## Using the Functions

Once you've installed the function pack, you're ready to use the functions.

1. Open Microsoft Excel or Google Sheets
2. Open the Flex.io Add-in:
   - In Microsoft Excel, select Home->Flex.io
   - In Google Sheets, select Add-ons->Flex.io
3. In the Flex.io side bar, log in to Flex.io and you’ll see the functions you have installed
4. For any function, click on the “details” in the function list to open a help dialog with some examples you can try at the bottom
5. Simply copy/paste the function into a cell, then edit the formula with a value you want to use

## Documentation

Here are some additional resources:

* [Currency Function Documentation.](https://www.flex.io/integrations/currency#functions-and-syntax) Here, you'll find a list of the functions available, their syntax and parameters, as well as examples for how to use them.
* [Flex.io Add-ons.](https://www.flex.io/add-ons) Here, you'll find more information about the Flex.io Add-ons for Microsoft Excel and Google Sheets, including how to install them and use them.
* [Flex.io Integrations.](https://www.flex.io/integrations) Here, you'll find out more information about other spreadsheet function packs available.

## Help

If you have question or would like more information, please feel free to live chat with us at our [website](https://www.flex.io) or [contact us](https://www.flex.io/about#contact-us) via email.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

