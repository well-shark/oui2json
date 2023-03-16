import json
import requests

def download_oui_txt():
    url = 'https://standards-oui.ieee.org/oui/oui.txt'
    # 下载 oui.txt
    r = requests.get(url, allow_redirects=True).content
    with open('oui.txt', 'wb') as f:
        f.write(r)
    
    

def main(oui_path:str, json_path:str):
    ''' oui.txt to oui.json
    '''
    ouis = {}
    with open(oui_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if '(hex)' not in line:
                continue
            line = line.split('(hex)')
            oui = line[0].strip().replace('-', ':')
            company = line[1].strip()
            ouis[oui] = company
    
    with open(json_path, 'w') as f:
        json.dump(ouis, f, indent=4, sort_keys=True)

if __name__ == '__main__':
    download_oui_txt()
    main('oui.txt', 'oui.json')