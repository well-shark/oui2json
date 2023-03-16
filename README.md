# oui2json

> From Wikipedia:
> 
> An organizationally unique identifier (OUI) is a 24-bit number that uniquely identifies a vendor, manufacturer, or other organization.
> 
> OUIs are purchased from the Institute of Electrical and Electronics Engineers (IEEE) Registration Authority by the assignee (IEEE term for the vendor, manufacturer, or other organization). Only assignment from MA-L registry assigns new OUI. They are used to uniquely identify a particular piece of equipment through derived identifiers such as MAC addresses, Subnetwork Access Protocol protocol identifiers, World Wide Names for Fibre Channel devices or vendor blocks in EDID.
> 
> In MAC addresses, the OUI is combined with a 24-bit number (assigned by the assignee of the OUI) to form the address. The first three octets of the address are the OUI.

Convert `oui.txt` to `oui.json`.

## Usage

1. Download `oui.txt` from [IEEE Standards](https://standards-oui.ieee.org/oui/oui.txt).

2. Copy `oui.txt` to the same directory as `oui2json.py`.

3. Run script: `python oui2json.py`


# Preview

**oui.txt**

```
OUI/MA-L                Organization                                 
company_id              Organization                                 
                        Address                                      

FC-59-C0   (hex)		Arista Networks
FC59C0     (base 16)	Arista Networks
				        5453 Great America Parkway
				        Santa Clara  CA  95054
				        US

64-1B-2F   (hex)		Samsung Electronics Co.,Ltd
641B2F     (base 16)	Samsung Electronics Co.,Ltd
				        #94-1, Imsoo-Dong
				        Gumi  Gyeongbuk  730-350
				        KR

00-16-F6   (hex)		Nevion
0016F6     (base 16)	Nevion
				        Lysaker Torg 5 
				        Lysaker    NO-1366
				        NO
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