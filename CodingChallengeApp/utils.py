from collections import OrderedDict
from django.core.files.base import ContentFile
from django.db.transaction import atomic
from django.template.loader import get_template
import pdfkit
import bs4

from PruebaTecnicaUD.settings import WKHTML2PDF


# Éste método se encarga de generar el resultado del problema de HanckerRank llamado Most Common
@atomic
def count_str(counter, str_list, max_num):
    str_list.sort()
    aux_dict = {}
    second = 0
    third = 0
    for s, n in counter.items():
        if n == max_num:
            if n not in aux_dict:
                aux_dict[n] = [s]
            else:
                aux_dict[n].append(s)
        elif second < n or second == n:
            if third < n < second:
                third = second
            if second != n:
                second = n
            if n not in aux_dict:
                aux_dict[n] = [s]
            else:
                aux_dict[n].append(s)
        elif third < n or third == n:
            if third != n:
                third = n
            if n not in aux_dict:
                aux_dict[n] = [s]
            else:
                aux_dict[n].append(s)

    result = aux_dict[max_num]
    len_result = len(result)
    if len_result < 3:
        second_list = aux_dict[second]
        if len_result == 1:
            if len(second_list) > 1:
                second_list.sort()
                second_list = second_list[:2]
                result += second_list
            else:
                result += second_list
                aux_dict[third].sort()
                result += aux_dict[third][0]
        else:
            result += second_list[0]
    elif len_result > 3 or len_result == 3:
        result.sort()
        result = result[:3]
    res = OrderedDict()
    for r in result:
        res[r] = counter[r]
    return res


# Éste método se genera el XML con los resultados y se agrega a la base de datos
def set_xml(context_dict, res):
    soup = bs4.BeautifulSoup('<result>', 'html.parser')
    result_xml = soup.find('result')
    result_xml.append(soup.new_tag('input'))
    result_xml.find('input').append(context_dict['input'])
    if 'success_count' in context_dict:
        result_xml['status'] = 'SUCCESS'
        result_xml.append(soup.new_tag('mostCommonChar', ocurrences=res.first_count))
        result_xml.find('mostCommonChar').append(res.first)
        result_xml.append(soup.new_tag('secondMostCommonChar', ocurrences=res.second_count))
        result_xml.find('secondMostCommonChar').append(res.second)
        result_xml.append(soup.new_tag('thirdMostCommonChar', ocurrences=res.third_count))
        result_xml.find('thirdMostCommonChar').append(res.third)
    else:
        result_xml['status'] = 'ERROR'
        result_xml.append(soup.new_tag('errorMsg'))
        result_xml.find('errorMsg').append(context_dict['error_message'])
    res.xml.save('xml_res.xml', ContentFile(str(result_xml)), False)


# Én este método se genera el PDF con los resultados y se agrega a la base de datos
def save_pdf(context_dict, res):
    template = get_template('CodingChallengeApp/index.html')
    html = template.render(context_dict)
    config = pdfkit.configuration(wkhtmltopdf=WKHTML2PDF)
    pdf = pdfkit.from_string(html, False, configuration=config)
    res.pdf.save('pdf_res.pdf', ContentFile(pdf))
    return html
