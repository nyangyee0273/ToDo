# FastAPi에서 URL 주소를 모아 관리할 수 있는 도구를 불러온다.
from fastapi import APIRouter

# router는 여러 기능(API 주소들)을 모아서 저장해주는 상자(모음집) 같은 역할을 한다.
router = APIRouter()

# 아래는 /tasks 라는 주소에 접속했을 때 실행될 기능(함수)을 만든다.


# /tasks 주소에 GET 방식으로 접근하면 이 함수가 실행된다.
# (예: 할 일 목록 전체 보기 기능)
@router.get("/tasks")
async def list_tasks():
    pass  # 아직 기능은 만들지 않았음. 나중에 여기에 코드를 넣을 예정


# /tasks 주소에 POST 방식으로 접근하면 이 함수가 실행된다.
# (예: 새로운 할 일을 추가하는 기능)
@router.post("/tasks")
async def create_task():
    pass


# /tasks/3 같은 주소에 DELETE 방식으로 접근하면 이 함수가 실행된다.
# (예; 3번 할 일을 삭제하는 기능)
@router.delete("/task/{task_id}")
async def delete_task():
    pass
