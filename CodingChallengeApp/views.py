from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from CodingChallengeApp.utils import count_str, save_pdf, set_xml, send_email
from CodingChallengeApp.models import Result


def index(request):
    return render(request, 'CodingChallengeApp/index.html')


@csrf_exempt
def check_str_count(request):
    if request.method == 'POST':
        sti = request.POST.get('str-input', '')
        sti_len = len(sti)
        if 3 < sti_len <= 10000:
            if sti.isalpha():
                if sti.islower():
                    counter = {}
                    str_list = []
                    max_num = 1
                    for s in str(sti):
                        if s in counter:
                            counter[s] += 1
                            if counter[s] > max_num:
                                max_num = counter[s]
                        else:
                            counter[s] = 1
                            str_list.append(s)
                    if len(counter) >= 3:
                        success_count = count_str(counter, str_list, max_num)
                        res = Result(input=sti, success=True)
                        i = 0
                        for s, n in success_count.items():
                            if i == 0:
                                res.first = s
                                res.first_count = n
                            elif i == 1:
                                res.second = s
                                res.second_count = n
                            elif i == 2:
                                res.third = s
                                res.third_count = n
                            i += 1
                        context_dict = {'input': sti, 'success_count': success_count}
                        set_xml(context_dict, res)
                        # send_email(context_dict, res)
                        return HttpResponse(save_pdf(context_dict, res), status=200)
                    else:
                        error_msg = 'La cadena debe tener mínimo 3 caracteres diferentes'
                        res = Result(
                            input=sti,
                            success=False,
                            error_msg=error_msg
                        )
                        context_dict = {'error_message': error_msg, 'error': True, 'input': sti}
                        set_xml(context_dict, res)
                        # send_email(context_dict, res)
                        return HttpResponse(save_pdf(context_dict, res),status=200)
                else:
                    error_msg = 'La cadena debe estar compuesta de minúsculas únicamente'
                    res = Result(
                        input=sti,
                        success=False,
                        error_msg=error_msg
                    )
                    context_dict = {'error_message': error_msg, 'error': True, 'input': sti}
                    set_xml(context_dict, res)
                    # send_email(context_dict, res)
                    return HttpResponse(save_pdf(context_dict, res),status=200)
            else:
                error_msg = 'La cadena debe estar compuesta únicamente de letras'
                res = Result(
                    input=sti,
                    success=False,
                    error_msg=error_msg
                )
                context_dict = {'error_message': error_msg, 'error': True, 'input': sti}
                set_xml(context_dict, res)
                # send_email(context_dict, res)
                return HttpResponse(save_pdf(context_dict, res),status=200)
        else:
            error_msg = 'La cadena debe tener minimo 4 caracteres y máximo 10.000'
            res = Result(
                input=sti,
                success=False,
                error_msg=error_msg
            )
            context_dict = {'error_message': error_msg, 'error': True, 'input': sti}
            set_xml(context_dict, res)
            # send_email(context_dict, res)
            return HttpResponse(save_pdf(context_dict, res),status=200)
    else:
        return render(request, '_common/error.html', {'error_message': 'Method not allowed'}, status=405)
