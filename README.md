# careerfit_ai_

# CareerFit AI 🚀

취업/공모전 데이터를 기반으로  
사용자의 전공과 스킬에 맞는 맞춤형 커리어 추천을 제공하는 AI 서비스입니다.

---

## 📌 프로젝트 개요

CareerFit AI는 채용 공고 데이터를 분석하고  
LLM(Gemini) + RAG 구조를 활용하여  
사용자 맞춤형 커리어 코칭을 제공하는 백엔드 중심 프로젝트입니다.

---

## 🧠 핵심 기능

### 1. 채용 데이터 분석
- CSV 기반 채용 공고 데이터 처리
- Pandas를 이용한 전처리 파이프라인 구성
- 결측치 처리 / 중복 제거 / 스킬 표준화

---

### 2. 데이터 저장 구조
- SQLite 기반 로컬 DB 저장
- jobs 테이블 생성 및 관리
- 분석용 데이터 구조화

---

### 3. RAG (Retrieval-Augmented Generation)
- ChromaDB 기반 벡터 검색 시스템 구축
- job 데이터를 문서 형태로 변환
- 사용자 질문 기반 유사 공고 검색

---

### 4. LLM 연동 (Gemini API)
- Google Gemini 2.5 Flash-Lite 사용
- 검색 결과 + 사용자 입력을 결합한 프롬프트 생성
- 커리어 코칭 답변 생성

---

### 5. Mock Mode 지원
- `MOCK_MODE=true` → API 없이 테스트 가능
- `MOCK_MODE=false` → 실제 Gemini API 호출

---

### 6. FastAPI 백엔드
- `/health` : 서버 상태 확인
- `/jobs` : 채용 데이터 조회
- `/analyze` : AI 기반 커리어 분석

---

## ⚙️ 기술 스택

- Python
- FastAPI
- Pandas
- SQLite
- ChromaDB
- Google Gemini API
- python-dotenv

---

## 📊 데이터 구조 (jobs.csv)

| 컬럼 | 설명 |
|------|------|
| id | 공고 ID |
| company | 회사명 |
| title | 직무 |
| required_skills | 필수 기술 |
| preferred_skills | 우대 기술 |
| description | 직무 설명 |
| job_type | 직무 카테고리 |

---

## 🔧 주요 구현 내용

### 📌 Day 2
- FastAPI 서버 구축
- API 구조 설계 (/health, /jobs, /analyze)
- Gemini API 연동 기반 구성
- Mock Mode 시스템 구현

---

### 📌 Day 3
- CSV 데이터 로딩 및 전처리 파이프라인 구축
- SQLite 저장 및 조회 기능 구현
- RAG 문서 변환 구조 설계
- LLM 서비스 구조 분리 (`services/llm_service.py`)
- Swagger 기반 API 테스트 완료

---

### 📌 Day 4
- ChromaDB 기반 벡터 검색 시스템 구축
- RAG 검색 결과 생성 기능 구현
- 검색 결과 + LLM 응답 연결 파이프라인 구현
- 의미 기반 직무 추천 시스템 완성

---

## 🧪 실행 방법

```bash
# 가상환경 활성화
.\backend\.venv\Scripts\Activate.ps1

# 서버 실행
uvicorn main:app --reload
