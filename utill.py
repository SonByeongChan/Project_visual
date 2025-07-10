# 모듈로딩 --------------------------------------------------------
from matplotlib import font_manager, rc



# ------------------------------------------------------------
#  함수기능 : 시각화 시 폰트 설정
#  한수이름: setHangulFont
#  매개변수 : fonth_path
#  반환값   : 없음
# ------------------------------------------------------------

def setHangulFont(font_path):
    
    # 설정할 한글 폰트 이름 추출
    font_name = font_manager.FontProperties(fname=font_path).get_name()

    # 한글 폰트 확인
    rc('font', family=font_name)
    



















