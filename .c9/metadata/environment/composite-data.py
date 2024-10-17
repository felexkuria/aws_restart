{"filter":false,"title":"composite-data.py","tooltip":"/composite-data.py","undoManager":{"mark":64,"position":64,"stack":[[{"start":{"row":0,"column":0},"end":{"row":1,"column":11},"action":"insert","lines":["import csv","import copy"],"id":16}],[{"start":{"row":1,"column":11},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":17}],[{"start":{"row":2,"column":0},"end":{"row":11,"column":1},"action":"insert","lines":["myVehicle = {","    \"vin\" : \"<empty>\",","    \"make\" : \"<empty>\" ,","    \"model\" : \"<empty>\" ,","    \"year\" : 0,","    \"range\" : 0,","    \"topSpeed\" : 0,","    \"zeroSixty\" : 0.0,","    \"mileage\" : 0","}"],"id":18}],[{"start":{"row":11,"column":1},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":19}],[{"start":{"row":12,"column":0},"end":{"row":13,"column":38},"action":"insert","lines":["for key, value in myVehicle.items():","    print(\"{} : {}\".format(key,value))"],"id":20}],[{"start":{"row":13,"column":38},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":21},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"remove","lines":["    "],"id":22}],[{"start":{"row":14,"column":0},"end":{"row":34,"column":42},"action":"insert","lines":["with open('car_fleet.csv') as csvFile:","    csvReader = csv.reader(csvFile, delimiter=',')  ","    lineCount = 0  ","    for row in csvReader:","        if lineCount == 0:","            print(f'Column names are: {\", \".join(row)}')  ","            lineCount += 1  ","        else:  ","            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  ","            currentVehicle = copy.deepcopy(myVehicle)  ","            currentVehicle[\"vin\"] = row[0]  ","            currentVehicle[\"make\"] = row[1]  ","            currentVehicle[\"model\"] = row[2]  ","            currentVehicle[\"year\"] = row[3]  ","            currentVehicle[\"range\"] = row[4]  ","            currentVehicle[\"topSpeed\"] = row[5]  ","            currentVehicle[\"zeroSixty\"] = row[6]  ","            currentVehicle[\"mileage\"] = row[7]  ","            myInventoryList.append(currentVehicle)  ","            lineCount += 1  ","    print(f'Processed {lineCount} lines.')"],"id":23}],[{"start":{"row":11,"column":1},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":24}],[{"start":{"row":12,"column":0},"end":{"row":12,"column":20},"action":"insert","lines":["myInventoryList = []"],"id":25}],[{"start":{"row":35,"column":42},"end":{"row":36,"column":0},"action":"insert","lines":["",""],"id":26},{"start":{"row":36,"column":0},"end":{"row":36,"column":4},"action":"insert","lines":["    "]},{"start":{"row":36,"column":4},"end":{"row":37,"column":0},"action":"insert","lines":["",""]},{"start":{"row":37,"column":0},"end":{"row":37,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":37,"column":0},"end":{"row":37,"column":4},"action":"remove","lines":["    "],"id":27}],[{"start":{"row":37,"column":0},"end":{"row":37,"column":41},"action":"insert","lines":["currentVehicle = copy.deepcopy(myVehicle)"],"id":28}],[{"start":{"row":35,"column":42},"end":{"row":36,"column":0},"action":"insert","lines":["",""],"id":29},{"start":{"row":36,"column":0},"end":{"row":36,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":38,"column":41},"end":{"row":39,"column":0},"action":"insert","lines":["",""],"id":30}],[{"start":{"row":39,"column":0},"end":{"row":42,"column":22},"action":"insert","lines":["for myCarProperties in myInventoryList:","    for key, value in myCarProperties.items():","        print(\"{} : {}\".format(key,value))","        print(\"-----\")"],"id":31}],[{"start":{"row":42,"column":22},"end":{"row":43,"column":0},"action":"insert","lines":["",""],"id":32},{"start":{"row":43,"column":0},"end":{"row":43,"column":8},"action":"insert","lines":["        "]},{"start":{"row":43,"column":8},"end":{"row":44,"column":0},"action":"insert","lines":["",""]},{"start":{"row":44,"column":0},"end":{"row":44,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":44,"column":4},"end":{"row":44,"column":8},"action":"remove","lines":["    "],"id":33},{"start":{"row":44,"column":0},"end":{"row":44,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":44,"column":0},"end":{"row":44,"column":1},"action":"insert","lines":["u"],"id":34},{"start":{"row":44,"column":1},"end":{"row":44,"column":2},"action":"insert","lines":["s"]},{"start":{"row":44,"column":2},"end":{"row":44,"column":3},"action":"insert","lines":["e"]},{"start":{"row":44,"column":3},"end":{"row":44,"column":4},"action":"insert","lines":["r"]}],[{"start":{"row":44,"column":4},"end":{"row":44,"column":5},"action":"insert","lines":["R"],"id":35},{"start":{"row":44,"column":5},"end":{"row":44,"column":6},"action":"insert","lines":["e"]},{"start":{"row":44,"column":6},"end":{"row":44,"column":7},"action":"insert","lines":["p"]},{"start":{"row":44,"column":7},"end":{"row":44,"column":8},"action":"insert","lines":["l"]},{"start":{"row":44,"column":8},"end":{"row":44,"column":9},"action":"insert","lines":["y"]}],[{"start":{"row":44,"column":9},"end":{"row":44,"column":10},"action":"insert","lines":[" "],"id":36}],[{"start":{"row":44,"column":9},"end":{"row":44,"column":10},"action":"remove","lines":[" "],"id":37}],[{"start":{"row":44,"column":9},"end":{"row":44,"column":10},"action":"insert","lines":["="],"id":38}],[{"start":{"row":44,"column":10},"end":{"row":44,"column":11},"action":"insert","lines":["i"],"id":40},{"start":{"row":44,"column":11},"end":{"row":44,"column":12},"action":"insert","lines":["n"]},{"start":{"row":44,"column":12},"end":{"row":44,"column":13},"action":"insert","lines":["p"]}],[{"start":{"row":44,"column":10},"end":{"row":44,"column":13},"action":"remove","lines":["inp"],"id":41},{"start":{"row":44,"column":10},"end":{"row":44,"column":17},"action":"insert","lines":["input()"]}],[{"start":{"row":44,"column":16},"end":{"row":44,"column":67},"action":"insert","lines":["\"Do you need to ship a package? (Enter yes or no) \""],"id":42}],[{"start":{"row":44,"column":68},"end":{"row":45,"column":0},"action":"insert","lines":["",""],"id":43},{"start":{"row":45,"column":0},"end":{"row":45,"column":1},"action":"insert","lines":[" "]}],[{"start":{"row":45,"column":1},"end":{"row":45,"column":2},"action":"insert","lines":["i"],"id":44},{"start":{"row":45,"column":2},"end":{"row":45,"column":3},"action":"insert","lines":["f"]}],[{"start":{"row":45,"column":2},"end":{"row":45,"column":3},"action":"remove","lines":["f"],"id":45},{"start":{"row":45,"column":1},"end":{"row":45,"column":2},"action":"remove","lines":["i"]},{"start":{"row":45,"column":0},"end":{"row":45,"column":1},"action":"remove","lines":[" "]}],[{"start":{"row":45,"column":0},"end":{"row":45,"column":1},"action":"insert","lines":["i"],"id":46},{"start":{"row":45,"column":1},"end":{"row":45,"column":2},"action":"insert","lines":["f"]}],[{"start":{"row":45,"column":2},"end":{"row":45,"column":3},"action":"insert","lines":[" "],"id":47}],[{"start":{"row":45,"column":3},"end":{"row":45,"column":4},"action":"insert","lines":["u"],"id":48},{"start":{"row":45,"column":4},"end":{"row":45,"column":5},"action":"insert","lines":["s"]}],[{"start":{"row":45,"column":3},"end":{"row":45,"column":5},"action":"remove","lines":["us"],"id":49},{"start":{"row":45,"column":3},"end":{"row":45,"column":12},"action":"insert","lines":["userReply"]}],[{"start":{"row":45,"column":12},"end":{"row":45,"column":13},"action":"insert","lines":["="],"id":50},{"start":{"row":45,"column":13},"end":{"row":45,"column":14},"action":"insert","lines":["y"]},{"start":{"row":45,"column":14},"end":{"row":45,"column":15},"action":"insert","lines":["e"]}],[{"start":{"row":45,"column":15},"end":{"row":45,"column":16},"action":"insert","lines":["s"],"id":51},{"start":{"row":45,"column":16},"end":{"row":45,"column":17},"action":"insert","lines":[":"]}],[{"start":{"row":45,"column":17},"end":{"row":46,"column":0},"action":"insert","lines":["",""],"id":52},{"start":{"row":46,"column":0},"end":{"row":46,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":45,"column":13},"end":{"row":45,"column":14},"action":"insert","lines":["="],"id":53}],[{"start":{"row":45,"column":18},"end":{"row":46,"column":0},"action":"insert","lines":["",""],"id":54},{"start":{"row":46,"column":0},"end":{"row":46,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":46,"column":4},"end":{"row":46,"column":5},"action":"insert","lines":["p"],"id":55},{"start":{"row":46,"column":5},"end":{"row":46,"column":6},"action":"insert","lines":["r"]},{"start":{"row":46,"column":6},"end":{"row":46,"column":7},"action":"insert","lines":["i"]},{"start":{"row":46,"column":7},"end":{"row":46,"column":8},"action":"insert","lines":["n"]},{"start":{"row":46,"column":8},"end":{"row":46,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":46,"column":4},"end":{"row":46,"column":9},"action":"remove","lines":["print"],"id":56},{"start":{"row":46,"column":4},"end":{"row":46,"column":11},"action":"insert","lines":["print()"]}],[{"start":{"row":46,"column":10},"end":{"row":46,"column":46},"action":"insert","lines":["\"We can help you ship that package!\""],"id":59}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":2},"action":"insert","lines":["# "],"id":60},{"start":{"row":1,"column":0},"end":{"row":1,"column":2},"action":"insert","lines":["# "]},{"start":{"row":2,"column":0},"end":{"row":2,"column":2},"action":"insert","lines":["# "]},{"start":{"row":3,"column":0},"end":{"row":3,"column":2},"action":"insert","lines":["# "]},{"start":{"row":4,"column":0},"end":{"row":4,"column":2},"action":"insert","lines":["# "]},{"start":{"row":5,"column":0},"end":{"row":5,"column":2},"action":"insert","lines":["# "]},{"start":{"row":6,"column":0},"end":{"row":6,"column":2},"action":"insert","lines":["# "]},{"start":{"row":7,"column":0},"end":{"row":7,"column":2},"action":"insert","lines":["# "]},{"start":{"row":8,"column":0},"end":{"row":8,"column":2},"action":"insert","lines":["# "]},{"start":{"row":9,"column":0},"end":{"row":9,"column":2},"action":"insert","lines":["# "]},{"start":{"row":10,"column":0},"end":{"row":10,"column":2},"action":"insert","lines":["# "]},{"start":{"row":11,"column":0},"end":{"row":11,"column":2},"action":"insert","lines":["# "]},{"start":{"row":12,"column":0},"end":{"row":12,"column":2},"action":"insert","lines":["# "]},{"start":{"row":13,"column":0},"end":{"row":13,"column":2},"action":"insert","lines":["# "]},{"start":{"row":14,"column":0},"end":{"row":14,"column":2},"action":"insert","lines":["# "]},{"start":{"row":15,"column":0},"end":{"row":15,"column":2},"action":"insert","lines":["# "]},{"start":{"row":16,"column":0},"end":{"row":16,"column":2},"action":"insert","lines":["# "]},{"start":{"row":17,"column":0},"end":{"row":17,"column":2},"action":"insert","lines":["# "]},{"start":{"row":18,"column":0},"end":{"row":18,"column":2},"action":"insert","lines":["# "]},{"start":{"row":19,"column":0},"end":{"row":19,"column":2},"action":"insert","lines":["# "]},{"start":{"row":20,"column":0},"end":{"row":20,"column":2},"action":"insert","lines":["# "]},{"start":{"row":21,"column":0},"end":{"row":21,"column":2},"action":"insert","lines":["# "]},{"start":{"row":22,"column":0},"end":{"row":22,"column":2},"action":"insert","lines":["# "]},{"start":{"row":23,"column":0},"end":{"row":23,"column":2},"action":"insert","lines":["# "]},{"start":{"row":24,"column":0},"end":{"row":24,"column":2},"action":"insert","lines":["# "]},{"start":{"row":25,"column":0},"end":{"row":25,"column":2},"action":"insert","lines":["# "]},{"start":{"row":26,"column":0},"end":{"row":26,"column":2},"action":"insert","lines":["# "]},{"start":{"row":27,"column":0},"end":{"row":27,"column":2},"action":"insert","lines":["# "]},{"start":{"row":28,"column":0},"end":{"row":28,"column":2},"action":"insert","lines":["# "]},{"start":{"row":29,"column":0},"end":{"row":29,"column":2},"action":"insert","lines":["# "]},{"start":{"row":30,"column":0},"end":{"row":30,"column":2},"action":"insert","lines":["# "]},{"start":{"row":31,"column":0},"end":{"row":31,"column":2},"action":"insert","lines":["# "]},{"start":{"row":32,"column":0},"end":{"row":32,"column":2},"action":"insert","lines":["# "]},{"start":{"row":33,"column":0},"end":{"row":33,"column":2},"action":"insert","lines":["# "]},{"start":{"row":34,"column":0},"end":{"row":34,"column":2},"action":"insert","lines":["# "]},{"start":{"row":35,"column":0},"end":{"row":35,"column":2},"action":"insert","lines":["# "]},{"start":{"row":38,"column":0},"end":{"row":38,"column":2},"action":"insert","lines":["# "]},{"start":{"row":39,"column":0},"end":{"row":39,"column":2},"action":"insert","lines":["# "]},{"start":{"row":40,"column":0},"end":{"row":40,"column":2},"action":"insert","lines":["# "]},{"start":{"row":41,"column":0},"end":{"row":41,"column":2},"action":"insert","lines":["# "]},{"start":{"row":42,"column":0},"end":{"row":42,"column":2},"action":"insert","lines":["# "]}],[{"start":{"row":45,"column":14},"end":{"row":45,"column":17},"action":"remove","lines":["yes"],"id":61},{"start":{"row":45,"column":14},"end":{"row":45,"column":15},"action":"insert","lines":["\""]},{"start":{"row":45,"column":15},"end":{"row":45,"column":16},"action":"insert","lines":["\""]}],[{"start":{"row":45,"column":15},"end":{"row":45,"column":16},"action":"insert","lines":["y"],"id":62},{"start":{"row":45,"column":16},"end":{"row":45,"column":17},"action":"insert","lines":["e"]},{"start":{"row":45,"column":17},"end":{"row":45,"column":18},"action":"insert","lines":["s"]}],[{"start":{"row":46,"column":47},"end":{"row":47,"column":0},"action":"insert","lines":["",""],"id":63},{"start":{"row":47,"column":0},"end":{"row":47,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":47,"column":0},"end":{"row":47,"column":4},"action":"remove","lines":["    "],"id":64}],[{"start":{"row":47,"column":0},"end":{"row":47,"column":1},"action":"insert","lines":["e"],"id":65},{"start":{"row":47,"column":1},"end":{"row":47,"column":2},"action":"insert","lines":["l"]},{"start":{"row":47,"column":2},"end":{"row":47,"column":3},"action":"insert","lines":["s"]},{"start":{"row":47,"column":3},"end":{"row":47,"column":4},"action":"insert","lines":["e"]}],[{"start":{"row":47,"column":4},"end":{"row":47,"column":5},"action":"insert","lines":[" "],"id":66}],[{"start":{"row":47,"column":5},"end":{"row":47,"column":6},"action":"insert","lines":["u"],"id":67},{"start":{"row":47,"column":6},"end":{"row":47,"column":7},"action":"insert","lines":["e"]}],[{"start":{"row":47,"column":6},"end":{"row":47,"column":7},"action":"remove","lines":["e"],"id":68}],[{"start":{"row":47,"column":6},"end":{"row":47,"column":7},"action":"insert","lines":["s"],"id":69},{"start":{"row":47,"column":7},"end":{"row":47,"column":8},"action":"insert","lines":["e"]},{"start":{"row":47,"column":8},"end":{"row":47,"column":9},"action":"insert","lines":["r"]}],[{"start":{"row":47,"column":9},"end":{"row":47,"column":10},"action":"insert","lines":["R"],"id":70},{"start":{"row":47,"column":10},"end":{"row":47,"column":11},"action":"insert","lines":["e"]},{"start":{"row":47,"column":11},"end":{"row":47,"column":12},"action":"insert","lines":["p"]},{"start":{"row":47,"column":12},"end":{"row":47,"column":13},"action":"insert","lines":["l"]}],[{"start":{"row":47,"column":13},"end":{"row":47,"column":14},"action":"insert","lines":["y"],"id":71},{"start":{"row":47,"column":14},"end":{"row":47,"column":15},"action":"insert","lines":["="]}],[{"start":{"row":47,"column":15},"end":{"row":47,"column":16},"action":"insert","lines":["="],"id":72}],[{"start":{"row":47,"column":16},"end":{"row":47,"column":18},"action":"insert","lines":["\"\""],"id":73}],[{"start":{"row":47,"column":17},"end":{"row":47,"column":18},"action":"insert","lines":["n"],"id":74},{"start":{"row":47,"column":18},"end":{"row":47,"column":19},"action":"insert","lines":["o"]}],[{"start":{"row":47,"column":20},"end":{"row":47,"column":21},"action":"insert","lines":[";"],"id":75}],[{"start":{"row":47,"column":20},"end":{"row":47,"column":21},"action":"remove","lines":[";"],"id":76}],[{"start":{"row":47,"column":20},"end":{"row":47,"column":21},"action":"insert","lines":[":"],"id":77}],[{"start":{"row":47,"column":21},"end":{"row":48,"column":0},"action":"insert","lines":["",""],"id":78},{"start":{"row":48,"column":0},"end":{"row":48,"column":4},"action":"insert","lines":["    "]},{"start":{"row":48,"column":4},"end":{"row":48,"column":5},"action":"insert","lines":["p"]},{"start":{"row":48,"column":5},"end":{"row":48,"column":6},"action":"insert","lines":["r"]}],[{"start":{"row":48,"column":6},"end":{"row":48,"column":7},"action":"insert","lines":["i"],"id":79},{"start":{"row":48,"column":7},"end":{"row":48,"column":8},"action":"insert","lines":["n"]},{"start":{"row":48,"column":8},"end":{"row":48,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":48,"column":4},"end":{"row":48,"column":9},"action":"remove","lines":["print"],"id":80},{"start":{"row":48,"column":4},"end":{"row":48,"column":11},"action":"insert","lines":["print()"]}],[{"start":{"row":48,"column":10},"end":{"row":48,"column":12},"action":"insert","lines":["\"\""],"id":81}],[{"start":{"row":48,"column":11},"end":{"row":48,"column":71},"action":"insert","lines":["Please come back when you need to ship a package. Thank you."],"id":82}],[{"start":{"row":47,"column":5},"end":{"row":47,"column":20},"action":"remove","lines":["userReply==\"no\""],"id":83}]]},"ace":{"folds":[],"scrolltop":632.5,"scrollleft":0,"selection":{"start":{"row":47,"column":5},"end":{"row":47,"column":5},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":9,"state":"start","mode":"ace/mode/python"}},"timestamp":1729161501195,"hash":"4d761f06ba89c014f9aa0372f91500ae3f9296a6"}