import os

OUT_DIR = r'./output'
XML_FILENAME = 'Report.xml'

#serializes JSON to XML
def json2xml(json_obj, line_padding=""):
    result_list = list()

    json_obj_type = type(json_obj)

    if json_obj_type is list:
        for sub_elem in json_obj:
            result_list.append(json2xml(sub_elem, line_padding))

        return "\n".join(result_list)

    if json_obj_type is dict:
        for tag_name in json_obj:
            sub_obj = json_obj[tag_name]
            result_list.append("%s<%s>" % (line_padding, tag_name))
            result_list.append(json2xml(sub_obj, "\t" + line_padding))
            result_list.append("%s</%s>" % (line_padding, tag_name))

        return "\n".join(result_list)

    return "%s%s" % (line_padding, json_obj)

#writes an XML file of the Suade report
def json2xml_file(json_obj, line_padding=""):
    the_xml = json2xml(json_obj)
    try:
        dirFile = os.path.join(OUT_DIR,XML_FILENAME)
        with open(dirFile,'w+') as f:
            f.write(the_xml)
    except IOError as e:
        print(e)
