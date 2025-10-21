def funct() :
    file = open("periodic_table.txt")
    html = "<table>"
    lastPos = ""
    for line in file :
        name, rest = line.strip().split(" = ")
        elements = rest.split(", ")
        dic = dict(e.split(":") for e in elements)
        if(dic['position'] == '0') :
            html += "<tr>"
        if(lastPos != "" and int(dic['position']) != int(lastPos) + 1):
            difference = int(dic['position']) - int(lastPos)
            for x in range(difference - 1):
                html += "<td style=\"padding: 10px; min-width: 150px; height:150px\"></td>"
        html += "<td style=\"border: 1px solid black; padding: 10px; min-width: 150px; height:150px\"><h4>"
        html += name + "</h4><ul><li>No " + dic['number'] + "</li><li>"
        html += dic['small'].strip() + "</li><li>"
        html += dic['molar'] + "</li></td>"
        if (dic['position'] == '17') :
            html += "</tr>"
            lastPos = ""
        lastPos = dic['position']
    with open("periodic_table.html", "w", encoding='utf-8') as file:
        file.write(html)
    return 0

if __name__ == '__main__':
    funct()