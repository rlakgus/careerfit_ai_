#backend/routers/jobs.py
from fastapi import APIRouter
from typing import List
router = APIRouter()

#목업 데이터 : 3일차에 실제 CSV데이터로 교체한다.
MOCK_JOBS = [
    {
        "id": 1,
        "company": "네이버클라우드",
        "title": "AI 엔지니어",
        "required_skills": ["Python", "PyTorch", "Machine Learning"],
        "preferred_skills": ["Docker", "AWS"],
        "description": "AI 모델을 설계하고 학습하여 다양한 서비스에 적용합니다. 데이터 전처리와 모델 성능 개선을 통해 서비스 품질을 향상시키는 업무를 수행합니다.",
        "deadline": "2026-08-31"
    },
    {
        "id": 2,
        "company": "카카오",
        "title": "AI 엔지니어",
        "required_skills": ["Python", "TensorFlow", "Deep Learning"],
        "preferred_skills": ["NLP", "FastAPI"],
        "description": "자연어 처리 및 생성형 AI 모델을 개발하고 운영합니다. 다양한 AI 서비스를 위한 모델 개발과 API 연동 업무를 담당합니다.",
        "deadline": "2026-08-31"
    },
    {
        "id": 3,
        "company": "LG AI연구원",
        "title": "AI 엔지니어",
        "required_skills": ["Python", "PyTorch", "Computer Vision"],
        "preferred_skills": ["Linux", "Git"],
        "description": "컴퓨터 비전 기반 AI 모델을 연구하고 개발합니다. 대규모 데이터셋을 활용하여 모델을 학습시키고 성능을 최적화하는 업무를 수행합니다.",
        "deadline": "2026-08-31"
    }
]



@router.get("/jobs", tags=["Jobs"])

def get_jobs():

    """

    취업 공고 목록을 반환하는 엔드포인트.

    현재는 목업 데이터를 반환하며, 3일차에 실제 데이터로 교체한다.

    """

    return {

        "count": len(MOCK_JOBS),

        "jobs": MOCK_JOBS

    }



@router.get("/jobs/{job_id}", tags=["Jobs"])

def get_job_by_id(job_id: int):

    """

    특정 공고의 상세 정보를 반환한다.

    """

    for job in MOCK_JOBS:

        if job["id"] == job_id:

            return job

    # 찾지 못한 경우

    from fastapi import HTTPException

    raise HTTPException(status_code=404, detail=f"공고 ID {job_id}를 찾을 수 없습니다.")
    
