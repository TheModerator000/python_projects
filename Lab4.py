"""
Created by: Jbrose1

Date: 2-16-22

"""


with open("RawData_TabDelimitted.txt") as dataTabDelim:
    content = dataTabDelim.readlines()


with open('exported_parsed_data.csv','w') as outputfile:
    outputfile.write('Campus, Department, Unit, Year, Month, Day\n')
    for line in content:
        lineData = line.split('\t')

        campusDepartUnit = lineData[0].split('|')

        campus = campusDepartUnit[0].strip()

        if len(campusDepartUnit) == 2:
            department = campusDepartUnit[1].strip()
            unit = ''
        elif len(campusDepartUnit) == 1:
            department = ''.strip( )
            unit = ''
        else:
            department = campusDepartUnit[1]
            unit = campusDepartUnit[2]

        createdTimeStampArray = lineData[1].split('-')
        strYear = createdTimeStampArray[0]
        strMonth = createdTimeStampArray[1]
        strDay = createdTimeStampArray[2][0:2]



        outputfile.write(('{},{},{},{},{},{} \n').format(campus, department, unit, strYear, strMonth, strDay))
