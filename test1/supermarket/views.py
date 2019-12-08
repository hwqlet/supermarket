import json
from time import *
from django.contrib.sessions.models import Session
from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
import datetime
import time
from django.urls import reverse
from django.urls import resolve

from .models import *
from django.conf import settings
from .forms import *
import os

# Create your views here.


def home(request):
    """系统主页面"""
    img_back = settings.BASE_DIR+'/static/home/home_back.jpg'
    img_back = os.path.join(img_back).replace('\\', '/')
    return render(request, 'supermarket/sup_home.html', {'img_home_back': img_back})


def login(request):
    """统一登录界面"""
    # 登录界面没有用模型表单或者表单，而是自建表单
    return render(request, 'supermarket/sup_login.html')


def login_sub(request):
    """登录提交处理"""
    # 不能与urls中的name属性同名，所以我改成了login_sub
    """登录处理"""
    # POST一定得大写
    if request.method == 'POST':
        if request.is_ajax():
            username = request.POST.get('username', None)
            password = request.POST.get('password', None)
            # Session.
            current_user = user.objects.get(username=username)
            if current_user.xiaofei > 10000 and current_user.user_vip is not None:
                current_user.user_vip.vip_level = 5
                current_user.user_vip.save()
                current_user.save()
            elif current_user.xiaofei > 8000 and current_user.user_vip is not None:
                current_user.user_vip.vip_level = 4
                current_user.user_vip.save()
                current_user.save()
            elif current_user.xiaofei > 3000 and current_user.user_vip is not None:
                current_user.user_vip.vip_level = 3
                current_user.user_vip.save()
                current_user.save()
            elif current_user.xiaofei > 1000 and current_user.user_vip is not None:
                current_user.vip_level = 2
                current_user.user_vip.save()
                current_user.save()
            elif current_user.xiaofei > 100 and current_user.user_vip is not None:
                current_user.user_vip.vip_level = 1
                current_user.user_vip.save()
                current_user.save()
            elif current_user.xiaofei > 0 and current_user.user_vip is not None:
                current_user.user_vip.vip_level = 0
                current_user.user_vip.save()
                current_user.save()
            dict_query = user.objects.all()
            for u in dict_query:
                # print(u.username+' '+u.password)
                # print(username+' '+password)
                # 这些都有执行到
                # print('111')
                if username == u.username and password == u.password:
                    # print('222')这里有执行到，说明是前端或者下一条语句有问题
                    # 因为是传数据到前端的js中，所以要用json.dumps，否则用模板就行了
                    return HttpResponse(json.dumps({'result': '成功', 'userid': username}))
                    # 本来想在后端进行跳转，但是要改的很多，就在前端进行跳转吧
            return HttpResponse(json.dumps({'result': "用户名或密码错误"}))
    else:
        return HttpResponse(request, u'未提交数据')
    
    
def register(request):
    """返回注册界面"""
    # print(request.POST.get('username', 'hwq'))没有传东西过来
    if request.method == "POST":
        form_submit = register_form(request.POST)
        # dict_new = form_submit.cleaned_data
        print(form_submit['password'])
        if form_submit.is_valid():
            print('clean')
            dict_new = form_submit.cleaned_data
            print(dict_new['username'])

            # print(user.objects.filter(username=dict_new['username']))
        # print('hwq')
        # print(form_submit['username'])# 测试没有错了，nice
            for u in user.objects.filter(username=dict_new['username']):
                if u is None:
                    break
                else:
                    return HttpResponse('用户已存在')
            user_register = user()
            user_register.username = dict_new['username']
            user_register.password = dict_new['password']
            user_register.shenfenzheng = dict_new['shenfenzheng']
            user_register.user_phone = dict_new['user_phone']
            # print('111')
            user_register.save()
            return redirect(reverse('manager_login'))
        else:
            return HttpResponse('表单无效')
    # 刚开是加载的时候要生成这个表单，如下
    form = register_form()
    # print('222')这里有访问到，符合逻辑
    return render(request, 'supermarket/sup_register.html', {"form": form})


def register_result(request):
    """暂时用不上"""
    pass


def change_pass(request):
    """返回忘记密码的处理界面"""
    return render(request, 'supermarket/forget.html')


def change_pass_result(request):
    """修改密码处理"""
    if request.is_ajax():
        change_user = request.POST.get('username', None)
        change_shenfen = request.POST.get('shenfenzheng', None)
        new_password = request.POST.get('mima', None)
        # print(change_shenfen)
        dict_query = user.objects.all()
        # print('111')
        for u in dict_query:
            # print('111')这里都没进来
            # print(u.username+' '+u.password)
            if u.username == change_user and u.shenfenzheng == change_shenfen:
                u.password = new_password
                u.save()
                return HttpResponse(json.dumps({'result': '修改密码成功'}))
        return HttpResponse(json.dumps({'result': '不存在此用户'}))
    return HttpResponse(json.dumps({'result': '修改界面'}))


def user_index(request):
    """返回用户的根界面"""
    return render(request, 'supermarket/user_index.html')


def user_info(request):
    """用户信息查看界面"""
    # print(request.POST.get('hidden_username', 'none'))测试没有问题
    if request.method == 'POST':
        # print('hwq')
        username_hidden = request.POST.get('hidden_username', '空')
        password_hidden = request.POST.get('hidden_password', "空")
        user_hidden = user.objects.get(username=username_hidden, password=password_hidden)
        user_dict = model_to_dict(user_hidden)
        backto_fore_username = user_dict['username']
        backto_fore_password = user_dict['password']
        backto_fore_shenfenzheng = user_dict['shenfenzheng']
        backto_fore_user_phone = user_dict['user_phone']
        return render(request, 'supermarket/user_info.html', {'username': backto_fore_username,
                                                              'password': backto_fore_password,
                                                              'shenfenzheng': backto_fore_shenfenzheng,
                                                              'user_phone': backto_fore_user_phone})
    else:
        return HttpResponse('错误')


def user_purchase(request):
    """用户购买界面"""
    # todo 选购界面
    if request.method == 'GET':
        """页面加载的时候上架商品"""
        shangjia_goods = shangpin_online.objects.filter()
        shangpin_dict = dict()
        i = 1
        for shangjia_good in shangjia_goods:
            shangpin = model_to_dict(shangjia_good)
            shangpin_dict.update({i: shangpin})
            # 里面有中文,所以dumps要设置ensure_ascii
            i += 1
        # print(shangpin_dict)
        dic = json.dumps(shangpin_dict, ensure_ascii=False)
        print(dic)
        return render(request, 'supermarket/user_purchase.html', shangpin_dict)
        # return HttpResponse(json.dumps({'data': dic}, ensure_ascii=False))

    if request.method == 'POST':
        if request.is_ajax():
            shangpinming = request.POST.get('shangpinming', 'none')
            print(shangpinming)
            changjia = request.POST.get('changjia', 'none')
            print(changjia)
            goods = shangpin_online.objects.get(shangpinming_shangpin_online=shangpinming, changjia_shangpin_online=changjia)
            # 获取到这个queryset对象
            id_set = shangpin_id_set.objects.filter(shangpinming_set_id=goods.id, is_sold='待售')
            yuliang = len(id_set)
            goods_to_fore = model_to_dict(goods)
            goods_to_fore.update({'yuliang': yuliang})
            data = {}
            data.update(goods_to_fore)
            # print(data.keys())
            # print(data.values()) # 外键的值有些问题
            # print(yuliang) # 查询没有问题
            # return HttpResponse(request, json.dumps({'yuliang': str(yuliang)}))
            # 不能有request
            print(goods_to_fore)
            return HttpResponse(json.dumps(goods_to_fore))
        return HttpResponse(json.dumps({'yuliang': 'ajax请求异常'}))


def user_initial(request):
    if request.method == 'POST':
        if request.is_ajax():
            # 获取所有商品
            all_shangpin = shangpin_online.objects.filter()
            all_li = []
            for x in all_shangpin:
                all_li.append(x.id)
            # print(all_li)
            id_set = {}
            for i, x in zip(range(len(all_li)), all_li):
                xx = shangpin_id_set.objects.filter(shangpinming_set_id=x, is_sold='待售')
                id_set.update({i+1: len(xx)})
            # print(id_set)
            return HttpResponse(json.dumps(id_set))
        return HttpResponse(json.dumps({'result': 'ajax请求错误'}))
    return HttpResponse(json.dumps({'result': 'post未请求'}))


def user_extra(request):
    if request.method == 'POST':
        if request.is_ajax():
            shangjia_goods = shangpin_online.objects.filter()
            shangpin_dict = dict()
            length = len(shangjia_goods)
            for i, shangjia_good in zip(range(length), shangjia_goods):
                shangpin = model_to_dict(shangjia_good)
                shangpin_dict.update({i+1: shangpin})
            # 原始的商品字典
            print(shangpin_dict)
            return HttpResponse(json.dumps(shangpin_dict))
        return HttpResponse(json.dumps({'result': 'ajax请求出错'}))
    return HttpResponse(json.dumps({'result': 'post未请求'}))


def change_info(request):
    """修改信息"""
    if request.method == 'POST':
        if request.is_ajax():
            username = request.POST.get('username', 'none')
            password = request.POST.get('password', 'none')
            shenfenzheng = request.POST.get('shenfenzheng', 'none')
            phone = request.POST.get('phone', 'none')
            user_change = user.objects.get(username=username)
            user_change.password = password
            user_change.shenfenzheng = shenfenzheng
            user_change.user_phone = phone
            user_change.save()
            return HttpResponse(json.dumps({'result': '修改信息成功'}))
        else:
            return HttpResponse('Ajax异常')
    else:
        return HttpResponse('表单未提交')


def user_dingdan(request):
    """订单处理视图"""
    # todo 订单怎么解析
    if request.method == 'POST':
        if request.is_ajax():
            # todo 将前端返回的用户下单情况生成订单回馈到前端
            user_buy = request.POST.get('user', 'none')
            # 这个为什么收不到?
            thing = request.POST.get('things', 'none')
            print(user_buy+'   '+thing)
            t = json.loads(thing)
            dingdan = {}
            print(len(t))
            i = 1
            for x in t:
                dic = {}
                if x is not None:
                    print(type(x[0]), type(x[1]))
                    shangpin = shangpin_online.objects.filter(id=x[0])
                    print(shangpin)
                    # 虽然前端已经规定了下拉框的商品数量，但是如果有另外一个用户在期间下了单的话
                    # 就需要重新查一下库存
                    # 但是感觉性能很差
                    id_set = shangpin_id_set.objects.filter(shangpinming_set_id=x[0], is_sold='待售')
                    if len(id_set) < int(x[1]):
                        # 库存不足时直接不进行下一步，节约性能，让用户重新下单
                        return HttpResponse(json.dumps({'result': str(shangpin_online.shangpinming_shangpin_online)+'下单失败,库存不足'}))
                    # Queryset是个结果集，再怎么着也得加个下标
                    dic.update({'商品名': shangpin[0].shangpinming_shangpin_online, '厂家': shangpin[0].changjia_shangpin_online,
                                '单价': shangpin[0].danjia, '数量': int(x[1]), '用户': user_buy})
                    dingdan.update({i: dic})
                    i += 1
            return HttpResponse(json.dumps(dingdan, ensure_ascii=False))
        return HttpResponse(json.dumps({'result': 'ajax请求异常'}))
    return HttpResponse(json.dumps({'result': 'post未请求'}))


def user_buy(request):
    if request.method == 'POST':
        if request.is_ajax():
            final_things = request.POST.get('thing', 'none')
            clean_data = json.loads(final_things)
            print(clean_data)
            # print(type(clean_data['1']['数量']))测试为int
            # print(type(clean_data))测试为字典类型
            for x in clean_data.keys():
                thing = clean_data.get(x)
                for y in range(thing['数量']):
                    thing_id = shangpin_online.objects.get(shangpinming_shangpin_online=thing['商品名'],
                                                       changjia_shangpin_online=thing['厂家'])
                    tru_thing = shangpin_id_set.objects.filter(shangpinming_set_id=thing_id.id, is_sold='待售')
                    # print(tru_thing[0].shangpin_id)# 测试没有问题
                    truth = shangpin_id_set.objects.get(shangpin_id=tru_thing[0].shangpin_id)
                    truth.is_sold = '已售'

                    truth.save()
                    print(truth.is_sold)
                # print(thing['商品名'])测试没有问题
            sum = 0
            shangpin_set = ''
            yonghu = ''
            for x in clean_data.keys():
                thing = clean_data.get(x)
                shangpin_set += str(thing)
                sum += thing['单价']*thing['数量']
            dingdan_buy = dingdan()
            dingdan_buy.dingdan_id = 'dingdan_' + str(datetime.datetime.now())
            dingdan_buy.digndan_time = strftime("%Y-%m-%d %H:%M:%S", localtime())
            dingdan_buy.shangpin_set_dingdan = shangpin_set
            dingdan_buy.zongjia_dingdan = sum

            for i in range(len(user.objects.all())):
                # 这里可以用硬编码
                thing = clean_data.get('1')
                print('thing:', thing)
                username = user.objects.all()[i].username
                # print(thing['用户'], username)
                # print(thing['用户'] == username)
                if thing['用户'] == username:
                    # print(111)
                    dingdan_buy.yonghu = user.objects.all()[i]
                    user_ = user.objects.all()[i]
                    user_.xiaofei += sum
                    print(user_.xiaofei)
                    user_.save()
                    print(user_)
                    print(user_.xiaofei)
                    print(sum)
                    break
                i += 1
            str_zhangdan = "zhangdan_" + str(datetime.datetime.now().year)\
                                    + "_" + str(datetime.datetime.now().month)\
                                    + "_" + str(datetime.datetime.now().day)
            print(str_zhangdan)
            for i in range(len(zhangdan.objects.all())):
                zhangdan_id = zhangdan.objects.all()[i].zhangdan_id
                # print(zhangdan_id)
                if zhangdan_id == str_zhangdan:
                    # print('222')
                    dingdan_buy.zhangdan = zhangdan.objects.all()[i]
                    dingdan_buy.save()
                    break
                i += 1
            return HttpResponse(json.dumps({'result': 'succeed'}))
        return HttpResponse(json.dumps({'result': 'Ajax请求异常'}))
    # 下面是get请求的响应
    # todo 缺货管理要做
    else:
        return render(request, 'supermarket/user_buy.html', {'result': '恭喜你，购买成功了！！！'})


def electricity_del(request):
    if request.method == 'POST':
        if request.is_ajax():
            gongshi = request.POST.get('gongshi', 'none')
            print(gongshi)
            original = gongshi.strip().split(' ')
            print(original)
            electric_set = electrical.objects.filter()
            tag_set = []
            for xx in electric_set:
                tag_set.append(xx.elec_id)
            # print(tag_set)
            if original[0] == 'A':
                I_A_set = []
                for electric in electric_set:
                    i_a_in = electric.I_A_in
                    I_A_set.append(i_a_in)
                # print(I_A_set)
                if original[1] == '+' and original[2] == 'B':
                    I_B_set = []
                    result = {}
                    for electric in electric_set:
                        i_b_in = electric.I_B_in
                        I_B_set.append(i_b_in)
                    # print(I_B_set)
                    for tag, x, y in zip(tag_set, I_A_set, I_B_set):
                        # print(tag, x, y)
                        result.update({tag: x+y})
                    return HttpResponse(json.dumps({'result': str(result)}))
    return render(request, 'supermarket/user_purchase_test.html')


def manager_login(request):
    if request.method == "GET":
        return render(request, 'supermarket/manager_login.html', {'result': '职员登录界面'})
    elif request.method == 'POST':
        employee_account = request.POST.get('account', 'none')
        employee_password = request.POST.get('password', 'none')
        print(employee_account, employee_password)
        # 测试没有问题
        employee = Employee.objects.filter(employee_account=employee_account,
                                            employee_password=employee_password)
        if len(employee) == 0:
            return redirect(reverse('manager_login'))
        # print(employee[0].jingli, type(employee[0].authority))测试没有问题
        dic = dict()
        if employee[0].authority == '15':
            # print('111')
            for i in jingli.objects.all():
                # print('222')
                if i.employee_status == employee[0]:
                    # print('333')问题不大
                    supermarket = liansuodian.objects.filter(jingli=i)
                    for x, j in zip(range(len(supermarket)), supermarket):
                        dic.update({x: j.liansuodian_id})
                    dic.update({'result': 'succeed'})

            if len(employee) == 1:
                # 应用session,存在服务端的数据
                request.session['result'] = 'succeed'
                request.session['1'] = dic.get(1)
                request.session['2'] = dic.get(2)
                # return redirect(reverse('employee_index'))
                return redirect(reverse('employee_index'))
                # 可以直接返回渲染的网页的模板
                # return render(request, 'supermarket/employee_index.html', dic)
            else:
                return HttpResponse(json.dumps({'result': 'failed'}))
        else:
            return HttpResponse(json.dumps({'result': 'ajax请求异常'}))
    else:
        return HttpResponse(json.dumps({'result': 'post未请求'}))


def middle_request(request):
    """中间请求"""
    if request.method == 'POST':
        if request.is_ajax():
            account = request.POST.get('account', 'none')
            password = request.POST.get('password', 'none')
            print(account, password)
            employee = Employee.objects.filter(employee_account=account,
                                               employee_password=password)
            dic = dict()
            if employee[0].authority in ['15', '7', '3']:
                # print('111')
                for i in jingli.objects.all():
                    # print('222')
                    if i.employee_status == employee[0]:
                        # print('333')问题不大
                        supermarket = liansuodian.objects.filter(jingli=i)
                        for x, j in zip(range(len(supermarket)), supermarket):
                            # 这里的x不需要进行字符串化
                            # 传个长度过去更好构建select
                            dic.update({x: j.liansuodian_id})
                        dic.update({'result': 'succeed'})
                        dic.update({'len': len(supermarket)})
                        list_time = []
                        for x in zhangdan.objects.all():
                            tm = str(x.shijian_zhangdan)
                            list_time.append(tm)
                        dic.update({'time': list_time})
                        dic.update({'authority': employee[0].authority})
            return HttpResponse(json.dumps(dic))


def employee_index(request):
    if request.method == "POST":
        return HttpResponse(json.dumps)
    return render(request, 'supermarket/employee_index.html')


def search(request):
    # todo 做成图表的形式吧
    if request.method == 'POST':
        t_start = request.POST.get('time_start', 'none')
        t_end = request.POST.get('time_end', 'none')
        liansuodian_search = request.POST.get('liansuodian_search', 'none')
        liansuodian_father = liansuodian.objects.get(liansuodian_id=liansuodian_search)
        print(t_start, t_end, liansuodian_search)
        # 可以用反向查询
        # search_dingdan = zhangdan.objects.filter(liansuodian=liansuodian_search)
        # 因为字符串与Date类型不一致
        t_datetime_start = time.strptime(t_start, '%Y-%m-%d')
        year, month, day = t_datetime_start[:3]
        t_datetime_start = datetime.date(year, month, day)
        print(t_datetime_start)

        print(type(t_datetime_start))
        t_datetime_end = time.strptime(t_end, '%Y-%m-%d')
        year, month, day = t_datetime_end[:3]
        t_datetime_end = datetime.date(year, month, day)
        print(t_datetime_end)
        # zhangdan_ = liansuodian_father.zhangdans.all()[2]
        # print(t_datetime_start == zhangdan_.shijian_zhangdan)测试没有问题
        print(liansuodian_father.liansuodian_id)
        # zhangdan_ = zhangdan.objects.all()[0]
        # print(type(zhangdan_.shijian_zhangdan))测试没有问题，反向查询不能用filter，get等方法
        search_dingdan_start = liansuodian_father.zhangdans.all()
        search_dingdan_end = liansuodian_father.zhangdans.all()
        zhangdan_list = []
        for x in search_dingdan_start:
            if t_datetime_start > t_datetime_end:
                return HttpResponse(json.dumps({'result': '时间跨度有误'}))
            if x.shijian_zhangdan >= t_datetime_start and x.shijian_zhangdan <= t_datetime_end:
                zhangdan_list.append(x)
        print(zhangdan_list)
        temp_zhangdan_start = ''
        temp_zhangdan_end = ''
        for x in search_dingdan_start:
            if x.shijian_zhangdan == t_datetime_start:
                temp_zhangdan_start = x
                break
        for x in search_dingdan_end:
            if x .shijian_zhangdan == t_datetime_end:
                temp_zhangdan_end = x
                break
        temp_dingdan = temp_zhangdan_start.dingdans.all()
        print(temp_dingdan)
        # print(temp_dingdan_end)
        dic = dict()
        time_list = []
        sum_list = []
        for x in zhangdan_list:
            sum = 0
            for y in x.dingdans.all():
                sum += y.zongjia_dingdan
            x.xiaoshoue = sum
            sum_list.append(sum)
            print(sum)
            time_list.append(str(x.shijian_zhangdan))
            x.save()

        dic.update({'result': '查账成功', 'time': time_list, 'sum': sum_list})
        print('dic', dic)
        # todo 数据获取要做 有结束时间，还得有层循环
        return HttpResponse(json.dumps(dic))
    return HttpResponse(json.dumps({'result': 'post未请求'}))


def gen_zhangdan(request):
    if request.method == 'POST':
        if request.is_ajax():
            zhangdan_gen = zhangdan()
            str_zhangdan = 'zhangdan_'
            str_zhangdan += str(datetime.datetime.now().year) + '_' +\
                            str(datetime.datetime.now().month) + '_' +\
                            str(datetime.datetime.now().day)
            print(str_zhangdan)
            zhangdan_gen.zhangdan_id = str_zhangdan
            zhangdan_gen.shijian_zhangdan = strftime('%Y-%m-%d', localtime())
            # todo 加载这个界面时应该要把登录信息上传过来然后生成这个经理管理
            # todo 的连锁店同时判断她有没有权限
            liansuodian_put = request.POST.get('liansuodian', 'none')
            # print(liansuodian_put)
            related_liansuodian = ''
            for i in liansuodian.objects.all():
                print(i.liansuodian_id)
                if i.liansuodian_id == liansuodian_put:
                    print('111')
                    related_liansuodian = i
                    break
            zhangdan_gen.liansuodian = related_liansuodian
            try:
                zhangdan_gen.save()
                return HttpResponse(json.dumps({'result': '生成账单成功'}))
            except Exception as e:
                print(e)
    # todo ojbk了


def salary(request):
    """工资查询"""
    if request.method == 'POST':
        if request.is_ajax():
            account = request.POST.get('account_salary', 'none')
            print(account)
            employee = Employee.objects.get(employee_account=account)
            # print(employee.gongzis.all())测试成功
            dic = dict()
            gongzi = []
            sum = 0
            for x in employee.gongzis.all():
                gongzi.append(x.jichugongzi)
                sum += x.jichugongzi
                gongzi.append(x.jixiao)
                sum += x.jixiao
                gongzi.append(x.chuqin)
                sum += x.chuqin
                gongzi.append(x.weigui)
                sum -= x.weigui
                gongzi.append(x.shuijin)
                sum -= x.shuijin
                dic.update({account+' '+str(x.shijian): gongzi, 'sum': sum})
            dic.update({'result': 'succeed'})
            return HttpResponse(json.dumps(dic))
        return HttpResponse(json.dumps({'result': 'failed'}))
    return HttpResponse(json.dumps({'result': 'post未请求'}))


def test(request):
    """测试专用"""
    return render(request, 'supermarket/test.html')
