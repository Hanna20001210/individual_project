import re
import codecs
import pandas as pd

f = open("MarketDataLog_20220215_23615.log", "rb")
byte_f = f.read()
f.close()

hex_f = byte_f.hex()
extract_result = re.findall(r'1b3542.*?0d0a', hex_f)

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
cal_flag = []
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

for data in extract_result :
    if(data[38:78] == "54584f31373330304e3220202020202020202020"):
        for i in range(int(data[90:92])):
            data_type.append(data[2:6])
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
            cal_flag.append(hex_to_string(data[88:90]))
            no_md_entries.append(int(data[90:92]))
            md_entry_type.append(hex_to_string(data[92+24*i:94+24*i]))
            sign.append(hex_to_string(data[94+24*i:96+24*i]))
            md_entry_px.append(int(data[96+24*i:106+24*i]))
            md_entry_size.append(int(data[106+24*i:114+24*i]))
            md_entry_level.append(int(data[114+24*i:116+24*i]))
            d = {
                'data': data,
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
                'md_entry_type':md_entry_type,
                'sign':sign,
                'md_entry_px':md_entry_px,
                'md_entry_size':md_entry_size,
                'md_entry_level':md_entry_level
                }

df = pd.DataFrame(data=d)

df.to_csv("output_I083.csv")
