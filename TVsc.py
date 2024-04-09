import pathlib
import gspread
import time
this_path = pathlib.Path(__file__)
json_path = pathlib.Path(this_path).parent /"flsc-415712-47f0e1c13822.json" #以json金鑰取得金鑰
account = gspread.service_account(json_path)
sheet = account.open("TVsc")
all = sheet.worksheet("All")
human = sheet.worksheet("human")

k = None
def fucku(lol):       #你要不要寫一下這個在幹嘛
    c = lol.acell("Q1").value
    lol.update('A'+c,all.acell("B2").value)
    lol.update('C'+c,all.acell("D2").value)
    lol.update('D'+c,int (all.acell("E2").value))
    lol.update("E"+c,int(all.acell("F2").value))
    lol.update('F'+c,all.acell("G2").value)
    lol.update('G'+c,all.acell("H2").value)
    lol.update('H'+c,int(all.acell("I2").value))
    lol.update('I'+c,int(all.acell("J2").value))
    lol.update('J'+c,int(all.acell("K2").value))
    lol.update('K'+c,int(all.acell("L2").value))
    lol.update('L'+c,all.acell("M2").value)
    lol.update('M'+c,all.acell("N2").value)
    lol.update('N'+c,all.acell("O2").value)
    lol.update('B'+c,all.acell("C2").value)
    lol.update('O'+c,all.acell("P2").value)
    lol.update('P'+c,all.acell("Q2").value)
    lol.update('Q1',int(c)+1)
while True:                               #用while true去卡
    k = all.acell("A2").value
    if k != None:                        #用if else直接跑過 去判斷隊伍
        fucku(sheet.worksheet(k))
        all.delete_row(2)
        time.sleep(20)
    else:
        print('沒比賽資料啦喜勒考')   #不是柳如風好帥嗎?#喜勒考
        time.sleep(5)
    print(0)