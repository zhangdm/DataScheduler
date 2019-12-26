#!/usr/bin/env python                                                               
# -*- coding: utf-8 -*-                                                             


import commands
import sys
from datetime import datetime, timedelta


def is_valid_date(date_time):
    """判断是否是一个有效的日期字符串"""
    result = False
    try:
        datetime.strptime(date_time, "%Y-%m-%d")
        result = True
    except Exception as e:
        print ("'{0}' is not valid date, Exception: {1}".format(date_time, e))
        exit(1)
    print ("result =", result)
    return result


if __name__ == '__main__':
    _arg_date = sys.argv[2]
    if not is_valid_date(_arg_date) or len(sys.argv) != 3:
        print ('参数错误  like [ python %s xxx.hql 2017-08-09]' % (__file__))
        exit(1)
    
    _op_date = datetime.strptime(_arg_date,'%Y-%m-%d')
    
    # 配置环境变量
    _hivevar = dict()
    # 配置数据库目录
    _hivevar['DM']   = 'dm'
    _hivevar['DWM']  = 'dwm'
    _hivevar['TMP']  = 'tmp'
    _hivevar['UG']   = 'usergroups'

    _hivevar['OP_DATE']   = _arg_date
    _hivevar['OP_DATE_S'] = datetime.strftime(_op_date, '%Y%m%d')
    _hivevar["YEAR"]      = datetime.strftime(_op_date, '%Y')
    _hivevar['MONTH']     = datetime.strftime(_op_date, '%m')
    _hivevar['DAY']       = datetime.strftime(_op_date, '%d')
    _hivevar['AGO_1D']    = datetime.strftime(_op_date + timedelta(days=-1), '%Y-%m-%d')
    _hivevar['AGO_2D']    = datetime.strftime(_op_date + timedelta(days=-2), '%Y-%m-%d')
    _hivevar['AGO_3D']    = datetime.strftime(_op_date + timedelta(days=-3), '%Y-%m-%d')
    _hivevar['AGO_4D']    = datetime.strftime(_op_date + timedelta(days=-4), '%Y-%m-%d')
    _hivevar['AGO_5D']    = datetime.strftime(_op_date + timedelta(days=-5), '%Y-%m-%d')
    _hivevar['AGO_6D']    = datetime.strftime(_op_date + timedelta(days=-6), '%Y-%m-%d')
    _hivevar['AGO_7D']    = datetime.strftime(_op_date + timedelta(days=-7), '%Y-%m-%d')
    _hivevar['AGO_8D']    = datetime.strftime(_op_date + timedelta(days=-8), '%Y-%m-%d')
    _hivevar['AGO_9D']    = datetime.strftime(_op_date + timedelta(days=-9), '%Y-%m-%d')
    _hivevar['AGO_10D']   = datetime.strftime(_op_date + timedelta(days=-10), '%Y-%m-%d')
    _hivevar['AGO_11D']   = datetime.strftime(_op_date + timedelta(days=-11), '%Y-%m-%d')
    _hivevar['AGO_12D']   = datetime.strftime(_op_date + timedelta(days=-12), '%Y-%m-%d')
    _hivevar['AGO_13D']   = datetime.strftime(_op_date + timedelta(days=-13), '%Y-%m-%d')
    _hivevar['AGO_14D']   = datetime.strftime(_op_date + timedelta(days=-14), '%Y-%m-%d')
    _hivevar['AGO_15D']   = datetime.strftime(_op_date + timedelta(days=-15), '%Y-%m-%d')
    _hivevar['AGO_16D']   = datetime.strftime(_op_date + timedelta(days=-16), '%Y-%m-%d')
    _hivevar['AGO_17D']   = datetime.strftime(_op_date + timedelta(days=-17), '%Y-%m-%d')
    _hivevar['AGO_18D']   = datetime.strftime(_op_date + timedelta(days=-18), '%Y-%m-%d')
    _hivevar['AGO_19D']   = datetime.strftime(_op_date + timedelta(days=-19), '%Y-%m-%d')
    _hivevar['AGO_20D']   = datetime.strftime(_op_date + timedelta(days=-20), '%Y-%m-%d')
    _hivevar['AGO_21D']   = datetime.strftime(_op_date + timedelta(days=-21), '%Y-%m-%d')
    _hivevar['AGO_22D']   = datetime.strftime(_op_date + timedelta(days=-22), '%Y-%m-%d')
    _hivevar['AGO_23D']   = datetime.strftime(_op_date + timedelta(days=-23), '%Y-%m-%d')
    _hivevar['AGO_24D']   = datetime.strftime(_op_date + timedelta(days=-24), '%Y-%m-%d')
    _hivevar['AGO_25D']   = datetime.strftime(_op_date + timedelta(days=-25), '%Y-%m-%d')
    _hivevar['AGO_26D']   = datetime.strftime(_op_date + timedelta(days=-26), '%Y-%m-%d')
    _hivevar['AGO_27D']   = datetime.strftime(_op_date + timedelta(days=-27), '%Y-%m-%d')
    _hivevar['AGO_28D']   = datetime.strftime(_op_date + timedelta(days=-28), '%Y-%m-%d')
    _hivevar['AGO_29D']   = datetime.strftime(_op_date + timedelta(days=-29), '%Y-%m-%d')
    _hivevar['AGO_30D']   = datetime.strftime(_op_date + timedelta(days=-30), '%Y-%m-%d')
    _hivevar['AGO_31D']   = datetime.strftime(_op_date + timedelta(days=-31), '%Y-%m-%d')
    _hivevar['AGO_32D']   = datetime.strftime(_op_date + timedelta(days=-32), '%Y-%m-%d')
    _hivevar['AGO_33D']   = datetime.strftime(_op_date + timedelta(days=-33), '%Y-%m-%d')
    _hivevar['AGO_34D']   = datetime.strftime(_op_date + timedelta(days=-34), '%Y-%m-%d')
    _hivevar['AGO_35D']   = datetime.strftime(_op_date + timedelta(days=-35), '%Y-%m-%d')
    _hivevar['AGO_36D']   = datetime.strftime(_op_date + timedelta(days=-36), '%Y-%m-%d')
    _hivevar['AGO_37D']   = datetime.strftime(_op_date + timedelta(days=-37), '%Y-%m-%d')
    _hivevar['AGO_38D']   = datetime.strftime(_op_date + timedelta(days=-38), '%Y-%m-%d')
    _hivevar['AGO_39D']   = datetime.strftime(_op_date + timedelta(days=-39), '%Y-%m-%d')
    _hivevar['AGO_40D']   = datetime.strftime(_op_date + timedelta(days=-40), '%Y-%m-%d')
    _hivevar['AGO_41D']   = datetime.strftime(_op_date + timedelta(days=-41), '%Y-%m-%d')
    _hivevar['AGO_42D']   = datetime.strftime(_op_date + timedelta(days=-42), '%Y-%m-%d')
    _hivevar['AGO_43D']   = datetime.strftime(_op_date + timedelta(days=-43), '%Y-%m-%d')
    _hivevar['AGO_44D']   = datetime.strftime(_op_date + timedelta(days=-44), '%Y-%m-%d')
    _hivevar['AGO_45D']   = datetime.strftime(_op_date + timedelta(days=-45), '%Y-%m-%d')
    _hivevar['AGO_50D']   = datetime.strftime(_op_date + timedelta(days=-50), '%Y-%m-%d')
    _hivevar['AGO_60D']   = datetime.strftime(_op_date + timedelta(days=-60), '%Y-%m-%d')
    _hivevar['AGO_70D']   = datetime.strftime(_op_date + timedelta(days=-70), '%Y-%m-%d')
    _hivevar['AGO_80D']   = datetime.strftime(_op_date + timedelta(days=-80), '%Y-%m-%d')
    _hivevar['AGO_90D']   = datetime.strftime(_op_date + timedelta(days=-90), '%Y-%m-%d')
    _hivevar['AGO_1Y']    = datetime.strftime(_op_date + timedelta(days=-365), '%Y-%m-%d')
    
    #前1个月 格式： 2017-01
    _op_1mon_date = datetime.strftime(_op_date.replace(day=1) + timedelta(days=0), '%Y-%m-%d')
    _hivevar['AGO_1M'] = _op_1mon_date[0:7]
    #前2个月 格式： 2017-01
    _op_2mon_tmp = datetime.strptime(_op_1mon_date, '%Y-%m-%d')
    _op_2mon_date = datetime.strftime(_op_2mon_tmp.replace(day=1) + timedelta(days=-1), '%Y-%m-%d')
    _hivevar['AGO_2M'] = _op_2mon_date[0:7]
    #前3个月 格式： 2017-01
    _op_3mon_tmp = datetime.strptime(_op_2mon_date, '%Y-%m-%d')
    _op_3mon_date = datetime.strftime(_op_3mon_tmp.replace(day=1) + timedelta(days=-1), '%Y-%m-%d')
    _hivevar['AGO_3M'] = _op_3mon_date[0:7]  
    #前4个月 格式： 2017-01
    _op_4mon_tmp = datetime.strptime(_op_3mon_date, '%Y-%m-%d')
    _op_4mon_date = datetime.strftime(_op_4mon_tmp.replace(day=1) + timedelta(days=-1), '%Y-%m-%d')
    _hivevar['AGO_4M'] = _op_4mon_date[0:7]  
    
    _prefix = "h2cmd --verbose"
    _varStr = ''
    for _key in _hivevar.keys():
        _varStr = '%s --hivevar %s=%s ' % (_varStr, _key, _hivevar[_key])
    
    cmd = '%s %s -f %s ' % (_prefix, _varStr, sys.argv[1])
    
    print ('command [%s]' % cmd)
    s, log = commands.getstatusoutput(cmd)
    print (log)
    if log.__contains__("FAILED"):
        if log.__contains__("AlreadyExistsException"):
            exit(0)
        else:
            exit(1)
    if log.__contains__("Error"):
        exit(1)
    if log.__contains__("Exception"):
        exit(1)
