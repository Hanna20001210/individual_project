import re
import codecs
import pandas as pd

f = open("MarketDataLog_20220215_23615.log", "rb")
byte_f = f.read()
f.close()

hex_f = byte_f.hex()
#print(hex_f)
extract_result = re.findall(r'1b3541.*?0d0a', hex_f)

data_type = []
info_hr = []
info_min = []
info_sec = []
info_ms = []
info_us = []
channel_id = []
channel_seq = []
ver_no = []
body_len_list = []
prod_id = []
prod_msg_seq = []
#cal_flag = []
no_md_entries = []
md_update_action = []
md_entry_type = []
sign = []
md_entry_px = []
md_entry_size = []
md_entry_level = []

def hex_to_string(hex):
    if hex[:2] == '0x':
        hex = hex[2:]
    string_value = bytes.fromhex(hex).decode('utf-8')
    return string_value
#(data[2:6] == "3541") | 
for data in extract_result :
    #print(data, len(data))
    if(data[38:78] == "54584f31373330304e3220202020202020202020"):
        for i in range(int(data[88:90])):
            #print(i, data[94+26*i:96+26*i])
            data_type.append(data[2:6])
            #msg_type.append(message_type(data[2:6]))
            info_hr.append(int(data[6:8]))
            info_min.append(int(data[8:10]))
            info_sec.append(int(data[10:12]))
            info_ms.append(int(data[12:15]))
            info_us.append(int(data[15:18]))
            channel_id.append(int(data[18:22]))
            channel_seq.append(int(data[22:32]))
            ver_no.append(int(data[32:34]))
            body_len_list.append(int(data[34:38]))
            prod_id.append(hex_to_string(data[38:78]))
            prod_msg_seq.append(int(data[78:88]))
            no_md_entries.append(int(data[88:90]))
            md_update_action.append(hex_to_string(data[90+26*i:92+26*i]))
            md_entry_type.append(hex_to_string(data[92+26*i:94+26*i]))
            sign.append(hex_to_string(data[94+26*i:96+26*i]))
            md_entry_px.append(int(data[96+26*i:106+26*i]))
            md_entry_size.append(int(data[106+26*i:114+26*i]))
            md_entry_level.append(int(data[114+26*i:116+26*i]))

            #print(hex_to_string(data[90+25*i:92+25*i]), data[90+25*i:92+25*i])
            #print(hex_to_string(data[92+24*i:94+24*i]), data[92+24*i:94+24*i])
            #print(hex_to_string(data[94+24*i:96+24*i]), data[94+24*i:96+24*i])
            #print(int(data[96+24*i:106+24*i]), data[96+24*i:106+24*i])
            #print(int(data[106+24*i:114+24*i]), data[106+24*i:114+24*i])
            #print(int(data[114+24*i:116+24*i]), data[114+24*i:116+24*i])
            d = {
                'data': data,
                #'msg_type': msg_type,
                'hr': info_hr,
                'min': info_min,
                'sec': info_sec,
                'ms': info_ms,
                'us': info_us,
                'c-id': channel_id,
                'c_seq': channel_seq,
                'v_no': ver_no,
                'info in packet byte len_c': body_len_list,
                'prod_id': prod_id,
                'prod_msg_seq': prod_msg_seq,
                'no_md_entries':no_md_entries,
                'md_update_action':md_update_action,
                'md_entry_type':md_entry_type,
                'sign':sign,
                'md_entry_px':md_entry_px,
                'md_entry_size':md_entry_size,
                'md_entry_level':md_entry_level
                }

print(len(data_type))
print(len(info_hr))
print(len(info_min))
print(len(info_sec))
print(len(info_ms))
print(len(info_us))
print(len(channel_id ))
print(len(channel_seq))
print(len(ver_no ))
print(len(body_len_list ))
print(len(prod_id))
print(len(prod_msg_seq ))
#print(len(cal_flag))
print(len(no_md_entries ))
print(len(md_update_action ))
print(len(md_entry_type ))
print(len(sign ))
print(len(md_entry_px ))
print(len(md_entry_size))
print(len(md_entry_level))
df = pd.DataFrame(data=d)

df.to_csv("output_I081.csv")

#1b 3541 08 45 24 471 000 0002 0000246426 01 0052 54584f3137353030423220202020202020202020 0000000391 02 
#32 30 30 0000257000 00000000 03
#30 30 30 0000123000 00000001 05 9f0d0a
#1b35410845244710000002000024642601005254584f313735303042322020202020202020202000000003910232303000002570000000000003303030000012300000000001059f0d0a

#1b 3541 08 45 24 712 000 0002 0000246545 01 0156 54584f3138323030423220202020202020202020 0000000504 10
#32 30 30 0000007300 00000000 05
#30 30 30 0000006900 00000001 05
#32 30 30 0000007700 00000000 04
#30 30 30 0000006600 00000002 05
#32 30 30 0000007800 00000000 03
#30 30 30 0000006500 00000001 05
#32 30 30 0000008000 00000000 02
#30 30 30 0000005800 00000012 05
#32 30 30 0000008100 00000000 01
#30 30 30 0000005700 00000001 05
#0a0d0a