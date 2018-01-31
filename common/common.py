
import common.config
import datetime
import re
import sys
from konlpy.tag import Kkma


# 현재 일자/시간 추출
def current_time():

    now = datetime.datetime.now()
    current_time = now.strftime(common.config.currentTime_format)

    return current_time


# 에러 출력
def error_print(e, funcname, last_no, type):
    # 화면 출력
    if(re.findall("M", type) == 'M'):
        print("Except " + funcname + " [No:" + last_no + "]")
        print(e)
        print('ERROR =>> ', sys.exc_info())


# 형태소 분석(해시태그 추출)
def make_tags(words):
    result_tag = ""

    try:
        kkma = Kkma()
        nouns = kkma.nouns(words)

        for index, n in enumerate(nouns):
            if(index > 0):
                result_tag = result_tag + ", "
            result_tag = result_tag + ("#" + n)

    except Exception as e:
        error_print(e, "make_tags", "", "M")

    finally:
        return result_tag
