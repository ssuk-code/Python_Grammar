# 패키지의 서브 패키지의 모듈의 함수만 가져오고 싶을 때
from mymath.stats.average import data_mean

# 패키지의 서브 패키지의 모듈을 가져오고 싶을 때
from mymath.stats import average
import mymath.stats.average

# 패키지의 서브패키지 모두를 가져오고 싶을 때
from mymath import stats
import mymath.stats

# mymath __init__ 안에 아무것도 없기 때문에 모듈들을 가져올 수 없음
import mymath