from collection.datalists import list_tags
from collection.datalists import list_content
from collection.datalists import list_content2
from collection.datalists import list_imagename
from collection.datalists import list_imagename2
from common.common import make_tags
#import common.common

import random
import requests
import time


# 종합운동장 위도/경도 : 37.5140929,127.07495340000002
# 1. 포스트 글 배열
# 2. 포스트 이미지 파일명
# 3. 데이터 조합해서 보내기(프로시져 호출)
# 4. 프로시저 = 포스트 등록 및 포스트&지역 정보 등록
# 5. 데이터 등록 수 별 시간 체크

# =============================
# Table : locationInfo 정보
# locationNo => 자동생성(2341617)
# code : R07A25 (종합운동장/체육관/강당)
# businessName : 잠실종합운동장
# 지번(oldAddress) : 서울특별시 송파구 잠실동 10
# 도로명(newAddress) : 서울특별시 송파구 올림픽로 25 서울종합운동장
# 위도(latitude) : 37.5140929
# 경도(longitude) : 127.072851
# =============================
# Table : post
# postNo = 자동생성
# userNo = 1~1000까지 중 랜덤
# viewsCnt = 0
# likeCnt = 0
# commentCnt = 0
# -content : 포스트내용 배열로 작성하여 랜덤 혹은 반복 = 강다니엘 관련
# -image : 이미지 파일명 배열로 작성하여 랜던 혹은 반복 (예 : /jajang.jpg)
# kakaoLink :
# postDate : 작성일시
# -tag : 형태소 분석으로 추출
# 위도(latitude) : 37.5140929
# 경도(longitude) : 127.072851
# poststatus : 0
# posttype : 0
# poentype : 0
# -----------------------------
# Table : postlocation
# postlocationNo = 자동생성
# postNo : 새로 생성할 포스트 번호
# locationNo : 2341617
# =============================


#====================================================================
# int userNo;
#     int locationNo;
#     String content;
#     String image;
#     String kakaoLink;
#     String tag;
#     double latitude;
#     double longitude;
#     int posttype;
#     int opentype;


def requestPost(paramSet):
    repeatCnt = paramSet[0]
    sleepInterval = paramSet[1]
    dataType = paramSet[2]

    # 상수
    locationNo = 2341617
    kakaoLink = ''
    latitude = 37.5140929
    longitude = 127.072851
    posttype = 0
    opentype = 0

    list_ctt = list_content
    list_img = list_imagename
    img_path = "/post/kang/"
    if(dataType == "twice"):
        list_ctt = list_content2
        list_img = list_imagename2
        img_path = "/post/twice/"

    userids = [u for u in range(2, 1001)]
    contents = [c for c in list_ctt]
    images = [i for i in list_img]
    # tagsList = list_tags(dataType)
    # tags = [t for t in tagsList]


    cnt = 0
    random.seed()

    while cnt < repeatCnt:
        param = ''

        userNo = random.choice(userids)
        content = random.choice(contents)
        image = random.choice(images)
        tag = make_tags(content)
        #tag = list_tags(dataType)

        params = {'userNo':userNo, 'locationNo':locationNo, 'content':content,
                    'image': img_path + image, 'kakaoLink':kakaoLink,
                    'tag':tag, 'latitude':latitude, 'longitude':longitude,
                    'posttype':posttype, 'opentype':opentype}
        url = 'http://192.168.1.204:3000/posting/write/'

        response = requests.post(url = url, data=params)
        print(response.json)
        print(params)
        time.sleep(sleepInterval)

        cnt += 1
        # print("┏ " + str(cnt) + " == " + content)
        # print("┠ " + str(cnt) + " == " + random.choice(image))
        # print("┗ " + str(cnt) + " == " + make_tags(content))



# 메인
if __name__=='__main__':

    print("################## START #######################")
    print("------------------")

    execSet = (170, 0, "twice")
    execSet2 = (10, 0, "kang")

    requestPost(execSet2)

    print("------------------")
    print("################## END #######################")





