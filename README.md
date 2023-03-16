# oui2json

> An organizationally unique identifier (OUI) is a 24-bit number that uniquely identifies a vendor, manufacturer, or other organization.
> ...
> In MAC addresses, the OUI is combined with a 24-bit number (assigned by the assignee of the OUI) to form the address. The first three octets of the address are the OUI. (From Wikipedia)

Convert `oui.txt` to `oui.json`.

# Usage

1. Download `oui.txt` from [IEEE Standards](https://standards-oui.ieee.org/oui/oui.txt).

2. Copy `oui.txt` to the same directory as `oui2json.py`.

3. Run script: `python oui2json.py`


# Preview

**oui.txt**

```
OUI/MA-L                Organization                                 
company_id              Organization                                 
                        Address                                      

00-00-00   (hex)		XEROX CORPORATION
000000     (base 16)	XEROX CORPORATION
				        M/S 105-50C
				        WEBSTER  NY  14580
				        US

68-7F-74   (hex)		Cisco-Linksys, LLC
687F74     (base 16)	Cisco-Linksys, LLC
				        121 Theory Drive
				        Irvine  California  92612
				        US

68-7F-F0   (hex)		TP-Link Corporation Limited
687FF0     (base 16)	TP-Link Corporation Limited
				        Room 901,9/F.New East Ocean Centre, 9 Science Museum Road
				        Tsim Sha Tsui  Kowloon  999077
				        HK
...
```

**out.json**
```json
{
    "00:00:00": "XEROX CORPORATION",
    ...
    "68:7F:74": "Cisco-Linksys, LLC",
    "68:7F:F0": "TP-Link Corporation Limited",
    "68:81:E0": "HUAWEI TECHNOLOGIES CO.,LTD",
    "68:82:F2": "grandcentrix GmbH",
    "68:83:1A": "Pandora Mobility Corporation",
    "68:83:CB": "Apple, Inc.",
    ...
    "FC:FF:AA": "IEEE Registration Authority"
}
```