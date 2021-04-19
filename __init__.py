import json
import asyncio
import sys
import io
from PIL import Image
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from .. import chara
imgpath = os.path.join(os.path.dirname(__file__), 'pic.png')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
chrome_options =Options()
chrome_options.add_argument('--headless')
#chrome_options.add_argument(r"user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data")
browser = webdriver.Chrome(options=chrome_options)
browser.set_window_size(width=1170,height=855)
browser.get('') #填url
browser.delete_all_cookies()
browser.add_cookie({"name":"wps_sid","value":""}) #填cookie
browser.add_cookie({"name":"csrf","value":""})
browser.add_cookie({"name":"visitorid","value":""})
browser.add_cookie({"name":"wpsua","value":""})
browser.add_cookie({"name":"lang","value":"zh-CN"})
browser.add_cookie({"name":"appcdn","value":"qn.cache.wpscdn.cn"})
browser.add_cookie({"name":"weboffice_cdn","value":"10"})
browser.get('')
time.sleep(2)
ActionChains(browser).send_keys(Keys.DOWN).perform()
ActionChains(browser).key_down(Keys.CONTROL).send_keys('f').key_up(Keys.CONTROL).perform()
time.sleep(1)
browser.find_element_by_xpath('//div[@class="component-icon-btn set-btn"]').click()
time.sleep(1)
browser.find_element_by_xpath("//div[contains(text(),'单元格匹配') and @class='checkbox-text']").click()
time.sleep(1)
browser.find_element_by_xpath('//input[@placeholder="输入查询内容"]').clear()
browser.find_element_by_xpath('//input[@placeholder="输入查询内容"]').send_keys('序号')
ActionChains(browser).send_keys(Keys.ENTER).perform()
time.sleep(1)
browser.find_element_by_xpath('//input[@placeholder="输入查询内容"]').clear()
browser.find_element_by_xpath('//input[@placeholder="输入查询内容"]').send_keys('定位点')
ActionChains(browser).send_keys(Keys.ENTER).perform()
browser.find_element_by_xpath('//i[@class="icons icons-16 icons-16-close"]').click()
time.sleep(5)
def load_config(path):
    try:
        with open(path,'r',encoding='utf8') as f:
            config = json.load(f)
            return config
    except:
        return {}
namedict = load_config(os.path.join(os.path.dirname(__file__),f"name.json"))
weidaodict = load_config(os.path.join(os.path.dirname(__file__),f"weidao.json"))
lastchallenge = {}
fanhui = {}
from hoshino import Service, priv
sv = Service('排刀表',manage_priv=priv.SUPERUSER,enable_on_default=False, visible = False) 
def sendkeys(name,boss_num,keys):
    ActionChains(browser).key_down(Keys.CONTROL).send_keys('f').key_up(Keys.CONTROL).perform()
    time.sleep(2)
    browser.find_element_by_xpath('//input[@placeholder="输入查询内容"]').clear()
    browser.find_element_by_xpath('//input[@placeholder="输入查询内容"]').send_keys(str(name))
    time.sleep(1)
    ActionChains(browser).send_keys(Keys.ENTER).perform()
    time.sleep(2)
    ActionChains(browser).send_keys(Keys.ENTER).perform()
    browser.find_element_by_xpath('//i[@class="icons icons-16 icons-16-close"]').click()
    browser.find_element_by_xpath('//textarea[@class="edit-box formula-bar"]').click()
    for i in range(boss_num): #定位到boss格
        ActionChains(browser).send_keys(Keys.TAB).perform()
    if check_txt() == False:
        ActionChains(browser).key_down(Keys.CONTROL).send_keys('f').key_up(Keys.CONTROL).perform()
        time.sleep(1)
        browser.find_element_by_xpath('//input[@placeholder="输入查询内容"]').clear()
        browser.find_element_by_xpath('//input[@placeholder="输入查询内容"]').send_keys('定位点')
        ActionChains(browser).send_keys(Keys.ENTER).perform()
        browser.find_element_by_xpath('//i[@class="icons icons-16 icons-16-close"]').click()
        return False
    if check_color() == False:
        ActionChains(browser).key_down(Keys.CONTROL).send_keys('f').key_up(Keys.CONTROL).perform()
        time.sleep(1)
        browser.find_element_by_xpath('//input[@placeholder="输入查询内容"]').clear()
        browser.find_element_by_xpath('//input[@placeholder="输入查询内容"]').send_keys('定位点')
        ActionChains(browser).send_keys(Keys.ENTER).perform()
        browser.find_element_by_xpath('//i[@class="icons icons-16 icons-16-close"]').click()
        return False
    time.sleep(1)
    color = get_color()
    if keys == '✔':
        browser.find_elements_by_xpath("//div[@class='right-btn']")[2].click() #背景色
        time.sleep(1)
        browser.find_element_by_xpath("//span[@style='background-color: rgb(0, 32, 96);']").click()
        time.sleep(1)
        browser.find_elements_by_xpath("//div[@class='right-btn']")[0].click() #字体色
        time.sleep(1)
        browser.find_element_by_xpath("//span[@style='background-color: rgb(255, 255, 255);']").click()
    elif keys == '尾刀':
        browser.find_elements_by_xpath("//div[@class='right-btn']")[2].click()
        time.sleep(1)
        browser.find_element_by_xpath("//span[@style='background-color: rgb(0, 176, 240);']").click()
        time.sleep(1)
        browser.find_elements_by_xpath("//div[@class='right-btn']")[0].click()
        time.sleep(1)
        browser.find_element_by_xpath("//span[@style='background-color: rgb(255, 255, 255);']").click()      
    time.sleep(1)
    ActionChains(browser).key_down(Keys.CONTROL).send_keys('f').key_up(Keys.CONTROL).perform()
    time.sleep(1)
    browser.find_element_by_xpath('//input[@placeholder="输入查询内容"]').clear()
    browser.find_element_by_xpath('//input[@placeholder="输入查询内容"]').send_keys('定位点')
    ActionChains(browser).send_keys(Keys.ENTER).perform()
    browser.find_element_by_xpath('//i[@class="icons icons-16 icons-16-close"]').click()
    return color
def backkeys(name,keys,delet=False):
    ActionChains(browser).key_down(Keys.CONTROL).send_keys('f').key_up(Keys.CONTROL).perform()
    time.sleep(2)
    browser.find_element_by_xpath('//input[@placeholder="输入查询内容"]').clear()
    browser.find_element_by_xpath('//input[@placeholder="输入查询内容"]').send_keys(str(name))
    time.sleep(1)
    ActionChains(browser).send_keys(Keys.ENTER).perform()
    time.sleep(2)
    ActionChains(browser).send_keys(Keys.ENTER).perform()
    browser.find_element_by_xpath('//i[@class="icons icons-16 icons-16-close"]').click()
    if keys == 'sl':
        ActionChains(browser).key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(Keys.SHIFT).perform()
        ActionChains(browser).key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(Keys.SHIFT).perform()
        ActionChains(browser).key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(Keys.SHIFT).perform()
        time.sleep(1)
    elif keys.isdigit():
        ActionChains(browser).key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(Keys.SHIFT).perform()  
        keys = int(keys)
        if keys >= 60:
            sec_ = str(keys - 60)
            min_ = '1'
            if len(sec_) == 1:
                sec_ = '0' + sec_
            keys = min_ + ':' + sec_
        else:
            if keys < 10:
                keys = '0:0' + str(keys)
            else:
                keys = '0:' + str(keys)
    else :
        ActionChains(browser).key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(Keys.SHIFT).perform()
        ActionChains(browser).key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(Keys.SHIFT).perform()
    
    browser.find_element_by_xpath('//textarea[@class="edit-box formula-bar"]').click()
    ActionChains(browser).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
    ActionChains(browser).send_keys(Keys.BACKSPACE).perform()
    if not delet :
        #time.sleep(1)
    
        browser.find_element_by_xpath('//textarea[@class="edit-box formula-bar"]').send_keys(str(keys))
    ActionChains(browser).send_keys(Keys.ENTER).perform()
    time.sleep(1)
    ActionChains(browser).key_down(Keys.CONTROL).send_keys('f').key_up(Keys.CONTROL).perform()
    time.sleep(1)
    browser.find_element_by_xpath('//input[@placeholder="输入查询内容"]').clear()
    browser.find_element_by_xpath('//input[@placeholder="输入查询内容"]').send_keys('定位点')
    ActionChains(browser).send_keys(Keys.ENTER).perform()
    browser.find_element_by_xpath('//i[@class="icons icons-16 icons-16-close"]').click()
def cancelkeys(name,boss_num,color:list): #有误
    bd_color = color[0]
    tx_color = color[1]
    ActionChains(browser).key_down(Keys.CONTROL).send_keys('f').key_up(Keys.CONTROL).perform()
    time.sleep(2)
    browser.find_element_by_xpath('//input[@placeholder="输入查询内容"]').clear()
    browser.find_element_by_xpath('//input[@placeholder="输入查询内容"]').send_keys(str(name))
    time.sleep(1)
    ActionChains(browser).send_keys(Keys.ENTER).perform()
    time.sleep(2)
    ActionChains(browser).send_keys(Keys.ENTER).perform()
    browser.find_element_by_xpath('//i[@class="icons icons-16 icons-16-close"]').click()
    browser.find_element_by_xpath('//textarea[@class="edit-box formula-bar"]').click()
    for i in range(boss_num):
        ActionChains(browser).send_keys(Keys.TAB).perform()
    browser.find_elements_by_xpath("//div[@class='right-btn']")[2].click() #背景色
    time.sleep(1)
    browser.find_element_by_xpath(f"//span[@style='{bd_color}']").click()
    time.sleep(1)
    browser.find_elements_by_xpath("//div[@class='right-btn']")[0].click() #字体色
    time.sleep(1)
    browser.find_element_by_xpath(f"//span[@style='{tx_color}']").click()
    time.sleep(1)
    ActionChains(browser).key_down(Keys.CONTROL).send_keys('f').key_up(Keys.CONTROL).perform()
    time.sleep(1)
    browser.find_element_by_xpath('//input[@placeholder="输入查询内容"]').clear()
    browser.find_element_by_xpath('//input[@placeholder="输入查询内容"]').send_keys('定位点')
    ActionChains(browser).send_keys(Keys.ENTER).perform()
    browser.find_element_by_xpath('//i[@class="icons icons-16 icons-16-close"]').click()
def get_color():
    color = []
    browser.find_elements_by_xpath("//div[@class='right-btn']")[2].click()
    time.sleep(1)
    bd_color = browser.find_element_by_xpath("//span[@class='color-item selected']").get_attribute('style') #背景色
    browser.find_elements_by_xpath("//div[@class='right-btn']")[0].click()
    time.sleep(1)
    try:
        tx_color = browser.find_element_by_xpath("//span[@class='color-item selected']").get_attribute('style')  #字体色
    except:
        tx_color = browser.find_element_by_xpath("//span[@class='color-item white selected']").get_attribute('style')
    color.append(bd_color)
    color.append(tx_color)
    return color

def check_txt():
    txt = browser.find_element_by_xpath('//textarea[@class="edit-box formula-bar"]').text
    if txt == '':
        return False
    else:
        return True

def check_color():
    browser.find_elements_by_xpath("//div[@class='right-btn']")[2].click()
    time.sleep(1)
    try:
        color =  browser.find_element_by_xpath("//span[@class='color-item selected']").get_attribute('style') #背景色
    except:
        color =  browser.find_element_by_xpath("//span[@class='color-item white selected']").get_attribute('style')
    browser.find_elements_by_xpath("//div[@class='right-btn']")[2].click()
    if color == 'background-color: rgb(0, 32, 96);':
        return False

def change_sheet(sheet):
    try:
        browser.find_elements_by_xpath(f"//span[@class='sheet-name']")[int(sheet)-1].click()
        return True
    except:
        return False

def reset():
    browser.find_element_by_xpath("//div[@class='zoom-value']").click()
    time.sleep(1)
    txt = browser.find_element_by_xpath("//div[@class='zoom-value selected']").text
    if txt == '100%':
        browser.find_element_by_xpath("//div[@class='zoom-value selected']").click()
    else:
        browser.find_element_by_xpath("//div[@class='panel-item only-text' and contains(text(),'100%')]").click()
    time.sleep(1)
    ActionChains(browser).send_keys(Keys.DOWN).perform()
    ActionChains(browser).key_down(Keys.CONTROL).send_keys('f').key_up(Keys.CONTROL).perform()
    browser.find_element_by_xpath('//input[@placeholder="输入查询内容"]').clear()
    browser.find_element_by_xpath('//input[@placeholder="输入查询内容"]').send_keys('序号')
    ActionChains(browser).send_keys(Keys.ENTER).perform()
    time.sleep(1)
    browser.find_element_by_xpath('//input[@placeholder="输入查询内容"]').clear()
    browser.find_element_by_xpath('//input[@placeholder="输入查询内容"]').send_keys('定位点')
    ActionChains(browser).send_keys(Keys.ENTER).perform()
    browser.find_element_by_xpath('//i[@class="icons icons-16 icons-16-close"]').click()
    
@sv.on_rex(r'^报刀 ?(?:\d+)(([,，])(\d+))')
async def chudao(bot,ev):
    global weidaodict
    global fanhui
    global lastchallenge
    match = ev.match
    for m in ev.message:
        if m.type == 'at' and m.data['qq'] != 'all':
            qq = m.data['qq']
            break
        else:
            qq = ev.user_id
        #print(m.type)
    #print(qq)
    name = namedict.get(str(qq))
    lastchallenge = {}
    if qq in weidaodict.keys():
        backkeys(name,keys='1',delet=True)
        boss_num = weidaodict[qq]['boss_num']
        fanhui = weidaodict.pop(qq)
        with open(os.path.join(os.path.dirname(__file__),f"weidao.json"), "w", encoding='utf-8') as f:
            f.write(json.dumps(weidaodict, indent=4, ensure_ascii=False))
        lastchallenge['keys'] = '尾刀'
    else:
        boss_num = int(match.group(3))
        lastchallenge['keys'] = '✔'
        fanhui = {}

    lastchallenge['color'] = sendkeys(name,boss_num,keys='✔')
    if lastchallenge['color'] == False:
        lastchallenge.clear()
        await bot.send(ev,'更新排刀表出错')
        await bot.send(ev,'您没有排这一刀或者已出，请检查尾数是否正确',at_sender=True)
        return
    lastchallenge['qq'] = qq
    lastchallenge['boss_num'] = boss_num   
    await bot.send(ev,f'已更新排刀表')
    
@sv.on_fullmatch(('出刀情况','排刀表'))
async def cdqk(bot,ev):
    browser.save_screenshot(imgpath)
    img = Image.open(imgpath)
    cropped = img.crop((33, 136, 1020, 790))
    cropped.save(imgpath)
    await bot.send(ev,f'[CQ:image,file=file:///{imgpath}]')
    
@sv.on_rex(r'^尾刀 ?(([,，])(\d+))')
async def weidao(bot,ev):
    global weidaodict
    global lastchallenge
    match = ev.match
    for m in ev.message:
        if m.type == 'at' and m.data['qq'] != 'all':
            qq = m.data['qq']
            break
        else:
            qq = ev.user_id
        #print(m.type)
    #print(qq)
    name = namedict.get(str(qq))
    boss_num = int(match.group(3))
    #print(boss_num)
    lastchallenge={}

    lastchallenge['color'] =sendkeys(name,boss_num,keys=f'尾刀')
    if lastchallenge['color'] == False:
        lastchallenge.clear()
        await bot.send(ev,'更新排刀表出错')
        await bot.send(ev,'您没有排这一刀或者已出，请检查尾数是否正确',at_sender=True)
        return
    lastchallenge['qq'] = qq
    lastchallenge['boss_num'] = boss_num
    lastchallenge['keys'] = '尾刀'
    print(str(weidaodict))
    weidaodict[qq] = {}
    weidaodict[qq]['name'] = name
    weidaodict[qq]['boss_num'] = boss_num
    with open(os.path.join(os.path.dirname(__file__),f"weidao.json"), "w", encoding='utf-8') as f:
        f.write(json.dumps(weidaodict, indent=4, ensure_ascii=False))
    await bot.send(ev,f'已更新排刀表，请报您的补偿时间，格式：补偿[数字]s')

@sv.on_fullmatch(('撤销报刀','撤销出刀'))
async def cancel(bot,ev):
    global lastchallenge
    global fanhui
    global weidaodict
    qq = lastchallenge['qq']
    boss_num = lastchallenge['boss_num']
    keys = lastchallenge['keys']
    color = lastchallenge['color']
    name = namedict.get(str(qq))
    if fanhui:
        await bot.send(ev,str(lastchallenge))
        cancelkeys(name,boss_num,color)
        weidaodict.update(fanhui)
        with open(os.path.join(os.path.dirname(__file__),f"weidao.json"), "w", encoding='utf-8') as f:
            f.write(json.dumps(weidaodict, indent=4, ensure_ascii=False))    
        fanhui = {}
    else:
        cancelkeys(name,boss_num,color)
    lastchallenge.clear()
    await bot.send(ev,f'已更新排刀表')

@sv.on_fullmatch(('重载尾刀'))
async def reload_weidao(bot,ev):
    global weidaodict
    weidaodict = load_config(os.path.join(os.path.dirname(__file__),f"weidao.json"))
    await bot.send(ev,'已重载')
    
'''@sv.on_prefix(('取消sl','取消SL','取消sL','取消Sl'))
async def sl(bot,ev):
    for m in ev.message:
        if m.type == 'at' and m.data['qq'] != 'all':
            qq = m.data['qq']
            break
        else:
            qq = ev.user_id
    name = namedict.get(str(qq))
    backkeys(name,keys='sl',delet=True)
    
@sv.on_prefix(('sl','SL','sL','Sl'))
async def unsl(bot,ev):
    if '?' in ev['raw_message'] or '？' in ev['raw_message']:
        return
    for m in ev.message:
        if m.type == 'at' and m.data['qq'] != 'all':
            qq = m.data['qq']
            break
        else:
            qq = ev.user_id
    name = namedict.get(str(qq))
    backkeys(name,keys='sl')'''
import re
@sv.on_message('group')
async def test(bot,ev):
    msg = ev['raw_message']
    if re.match(r'^尾刀 ?(\[CQ:at,qq=(\d+)\])? ?$',msg) or re.match(r'^报刀 ?(\d+) ?(\[CQ:at,qq=(\d+)\])? ?$',msg):
        await asyncio.sleep(1)
        await bot.send(ev,'撤销')
    if re.match(r'^取消[Ss][Ll] ?(\[CQ:at,qq=(\d+)\])? ?$',msg):
        match = re.match(r'^取消[Ss][Ll] ?(\[CQ:at,qq=(\d+)\])? ?$',msg)
        if match.group(2):
            qq = match.group(2)
        else:
            qq = ev.user_id
        name = namedict.get(str(qq))
        backkeys(name,keys='sl',delet=True)
    if re.match(r'^[Ss][Ll] ?(\[CQ:at,qq=(\d+)\])? ?$',msg):
        match = re.match(r'^[Ss][Ll] ?(\[CQ:at,qq=(\d+)\])? ?$',msg)
        if match.group(2):
            qq = match.group(2)
        else:
            qq = ev.user_id
        name = namedict.get(str(qq))
        backkeys(name,keys='sl')
        
@sv.on_prefix(('锁'))
async def lock(bot,ev):
    nickname = ev.message.extract_plain_text().strip()
    if len(nickname) > 3:
        return
    id_ = chara.name2id(nickname)
    confi = 100
    guess = False
    if id_ == chara.UNKNOWN:
        id_, guess_name, confi = chara.guess_id(nickname)
        guess = True
    c = chara.fromid(id_)
    for m in ev.message:
        if m.type == 'at' and m.data['qq'] != 'all':
            qq = m.data['qq']
            break
        else:
            qq = ev.user_id
    name = namedict.get(str(qq))    
    
    msg = ''
    if guess:
        #lmt.start_cd(uid, 120)
        msg = f'兰德索尔似乎没有叫"{nickname}"的人...'
        await bot.finish(ev, msg)
       # msg = f'\n您有{confi}%的可能在找{guess_name} '

    backkeys(name,keys=nickname)
    if confi == 100:
        msg += f'您锁了角色： {c.name}，已更新排刀表'
        await bot.send(ev, msg, at_sender=True)
        
@sv.on_prefix(('取消锁'))
async def unlock(bot,ev):
    nickname = ev.message.extract_plain_text().strip()
    if len(nickname) > 3:
        return
    msg = ''
    if nickname != '人':
        id_ = chara.name2id(nickname)
        confi = 100
        guess = False
        if id_ == chara.UNKNOWN:
            id_, guess_name, confi = chara.guess_id(nickname)
            guess = True
        c = chara.fromid(id_)
        for m in ev.message:
            if m.type == 'at' and m.data['qq'] != 'all':
                qq = m.data['qq']
                break
            else:
                qq = ev.user_id
        name = namedict.get(str(qq))    
        backkeys(name,keys=c.name,delet=True)       
        if guess:
            #lmt.start_cd(uid, 120)
            msg = f'兰德索尔似乎没有叫"{nickname}"的人...'
            await bot.finish(ev, msg)
            msg = f'\n您有{confi}%的可能在找{guess_name} '

        if confi == 100:
            msg += f'您解锁了角色： {c.name}，已更新排刀表'
    else :
        backkeys(name,keys='取消',delet=True)
        msg += f'您解锁了角色： 已更新排刀表'
    await bot.send(ev, msg, at_sender=True)

@sv.on_rex((r'^补偿(\d+)s'))
async def con_time(bot,ev):
    match = ev.match
    time = match.group(1)
    for m in ev.message:
        if m.type == 'at' and m.data['qq'] != 'all':
            qq = m.data['qq']
            break
        else:
            qq = ev.user_id
    name = namedict.get(str(qq))    
    backkeys(name,keys=time)
    await bot.send(ev,f'已更新排刀表')

@sv.on_rex((r'^补偿(\d+)[:：](\d+)'))
async def _con_time(bot,ev):
    match = ev.match
    min_ = match.group(1)
    sec_ = match.group(2)
    for m in ev.message:
        if m.type == 'at' and m.data['qq'] != 'all':
            qq = m.data['qq']
            break
        else:
            qq = ev.user_id
    name = namedict.get(str(qq))    
    time = str(int(min_)*60+int(sec_))
    backkeys(name,keys=time)
    await bot.send(ev,f'已更新排刀表')

@sv.on_prefix(('切换sheet','切换表'))
async def ce_sheet(bot,ev):
    sheet = ev.message.extract_plain_text().strip()
    if sheet.isdigit() == False:
        await bot.finish(ev,'请输入正确的数字，例如切换sheet1')
    a = change_sheet(sheet)
    if a == True:
        await bot.send(ev,'已切换')
    else:
        await bot.send(ev,'未找到表名')

@sv.on_fullmatch(('重置分辨率'))
async def rt(bot,ev):
    reset()
    browser.save_screenshot(imgpath)
    img = Image.open(imgpath)
    cropped = img.crop((33, 136, 1020, 790))
    cropped.save(imgpath)    
    await bot.send(ev,f'已重置[CQ:image,file=file:///{imgpath}]')
