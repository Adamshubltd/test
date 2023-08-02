import xml.etree.ElementTree as ET

data = '''<person>
    <student>
        <name>Adams</name>
        <age type="int"> 25</age>
    </student>

    <student>
        <name>John</name>
        <age type="int">19</age>
    </student>

    <student>
        <name>Peter</name>
        <age type="int">32</age>
    </student>
  <student>
        <name>Huss</name>
        <age type="int">20</age>
    </student>

    <student>
        <name>Lizy</name>
        <age type="int">17</age>
    </student>

      


        </person>'''

tree = ET.fromstring(data)

ls = tree.findall('student')

if len(ls) > 3:
    for st in ls:
        print(st.find('name').text, '\t', st.find('age').text)
else:
    print('The lenght is shorter')
    



