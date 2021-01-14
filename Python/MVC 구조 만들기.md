# MVC 구조 만들기

#### 만드는 순서

1. dao : 데이터베이스와 같다
2. entity : 사용할 객체 클래스
3. service : 비즈니스 로직, entity를 가지고 해야하는 task를 구현
4. controller : main 화면과 service를 연결해주는 역할, service를 실행시키기 위해서는 무조건 controller를 거치도록 구현
5. view : 스프링 프레임워크를 할 때는 view 폴더가 html 파일들을 보관했다. 그러나 해당 연습 프로젝트에서는 view에는 main에서 display할 때 사용하는 함수를 만들었다. 여기서는 main이 index.html과 비슷한 역할을 한다.





#### 주의할 점

main.py를 상위에 만들었고, 같은 위치에 controller, dao, entity, service, view 폴더를 만들었다.

그랬더니 main에서는 하위 폴더 내의 모듈을 import 하는데 문제가 없었지만, 하위 폴더 내부에 있는 파일들은 다른 하위 폴더 내부에 있든 파일의 모듈을 참조할 수 없었다.

즉, controller 폴더 내의 controller.py에서 service 폴더 내의 service.py를 인식하지 못하여 service 객체를 사용할 수 없었다.

이는 **package**로 인지하지 못해서라고 한다.



###### 해결 방법

각 하위 폴더 내부에 `__init__.py`라는 파일을 만들어 주었다.

폴더 안에 `__init__.py`가 존재해야 해당 폴더를 **package**로 인식하기 때문이다.

파이썬 상위 버전에서는 `__init__.py`가 없어도 패키지로 인식된다고 한다. 하지만, 하위 버전과의 호환을 위해 `__init__.py`를 만드는 습관을 들이는 게 좋을 것 같다.