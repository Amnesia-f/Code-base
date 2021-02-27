id_name = {"01001":"小张",
           "01005":"小王",
           "01008":"小林",
           "01015":"小李",
           "01020":"小孔",
           "01035":"小何"}
name_id = {}
for id,name in id_name.items():
    name_id[name] = id
print("小李的学号:",name_id["小李"])
