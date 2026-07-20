# 📋 AWS DCO 교육용 샘플 로그 분석 리포트

본 리포트는 데이터 센터 운영(Data Center Operations) 직무 이해를 돕기 위해 작성된 교육용 가상 분석 보고서입니다.

## 1. 분석 개요
| 항목 | 분석 결과 |
| :--- | :--- |
| **전체 로그 줄 수** | 11개 |
| **주의/경고 로그 수 (WARNING/CRITICAL)** | 7개 |
| **주요 장애 이벤트 수 (점검 대상)** | 7개 |

## 2. 심각도별(Severity) 분포
로그 내 위험 수준별 발생 현황입니다.

| 심각도 | 발생 건수 | 비율 |
| :--- | :---: | :---: |
| INFO | 4개 | 36.4% |
| WARNING | 4개 | 36.4% |
| CRITICAL | 3개 | 27.3% |

## 3. 이벤트 유형별 발생 분포
어떤 종류의 상태 변화 및 에러가 많이 발생했는지 확인합니다.

| 이벤트명 | 발생 건수 |
| :--- | :---: |
| LINK_DOWN | 3개 |
| CRC_ERROR | 2개 |
| TICKET_ESCALATED | 2개 |
| LINK_UP | 1개 |
| HARDWARE_HEALTH | 1개 |
| TEMP_OK | 1개 |
| BGP_ESTABLISHED | 1개 |

## 4. WARNING 및 CRITICAL 로그 상세 리스트
데이터 센터에서 수동 또는 자동 모니터링 대응이 필요할 수 있는 경고/심각 로그 목록입니다.

| 번호 | 일시 | 장비명 | 심각도 | 이벤트 | 메시지 |
| :---: | :--- | :--- | :---: | :--- | :--- |
| 1 | 2026-07-19 10:15:30 | SVR-102 | **WARNING** | CRC_ERROR | High bit error rate detected on copper transceiver port 4 |
| 2 | 2026-07-19 10:20:12 | RTR-01 | **CRITICAL** | LINK_DOWN | Fiber backbone path redundant connection failure |
| 3 | 2026-07-19 10:45:00 | SW-02 | **WARNING** | LINK_DOWN | Secondary inter-cabinet link intermittent flap detected |
| 4 | 2026-07-19 11:12:40 | SW-01 | **CRITICAL** | TICKET_ESCALATED | Ticket #92019 auto-opened for persistent link down state on primary route |
| 5 | 2026-07-19 11:30:22 | SVR-102 | **WARNING** | CRC_ERROR | Port 4 CRC error count exceeded threshold 50/sec |
| 6 | 2026-07-19 12:05:10 | SW-02 | **WARNING** | LINK_DOWN | Core transceiver temperature exceeded threshold warning limit |
| 7 | 2026-07-19 12:15:00 | SW-02 | **CRITICAL** | TICKET_ESCALATED | Ticket #92044 generated for SW-02 link stability issue |

## 5. 주요 점검 대상 이벤트 요약
데이터 센터 인프라 운영진이 즉각 확인해야 하는 대표적인 에러 패턴(`CRC_ERROR`, `LINK_DOWN`, `TICKET_ESCALATED`)에 대한 상세 점검 요약입니다.

### 1. [CRC_ERROR] - 장비: SVR-102
- **발생 시각:** `2026-07-19 10:15:30`
- **위험 단계:** `WARNING`
- **현상 및 메시지:** High bit error rate detected on copper transceiver port 4
- **가이드라인 (교육용):** 물리적 회선 연결부(케이블, 트랜시버)에 비트 에러가 발생한 상황입니다. 먼지 유입 여부 점검이나 트랜시버 재장착이 필요할 수 있습니다.

### 2. [LINK_DOWN] - 장비: RTR-01
- **발생 시각:** `2026-07-19 10:20:12`
- **위험 단계:** `CRITICAL`
- **현상 및 메시지:** Fiber backbone path redundant connection failure
- **가이드라인 (교육용):** 포트의 연결이 끊어졌거나 통신 신호가 유실되었습니다. 상하위 장비 상태와 포트 LED 상태를 점검해야 합니다.

### 3. [LINK_DOWN] - 장비: SW-02
- **발생 시각:** `2026-07-19 10:45:00`
- **위험 단계:** `WARNING`
- **현상 및 메시지:** Secondary inter-cabinet link intermittent flap detected
- **가이드라인 (교육용):** 포트의 연결이 끊어졌거나 통신 신호가 유실되었습니다. 상하위 장비 상태와 포트 LED 상태를 점검해야 합니다.

### 4. [TICKET_ESCALATED] - 장비: SW-01
- **발생 시각:** `2026-07-19 11:12:40`
- **위험 단계:** `CRITICAL`
- **현상 및 메시지:** Ticket #92019 auto-opened for persistent link down state on primary route
- **가이드라인 (교육용):** 장애 상황이 지속되어 티켓 관리 시스템으로 자동 이관되었습니다. 긴급 현장 엔지니어 배정 및 점검이 권장됩니다.

### 5. [CRC_ERROR] - 장비: SVR-102
- **발생 시각:** `2026-07-19 11:30:22`
- **위험 단계:** `WARNING`
- **현상 및 메시지:** Port 4 CRC error count exceeded threshold 50/sec
- **가이드라인 (교육용):** 물리적 회선 연결부(케이블, 트랜시버)에 비트 에러가 발생한 상황입니다. 먼지 유입 여부 점검이나 트랜시버 재장착이 필요할 수 있습니다.

### 6. [LINK_DOWN] - 장비: SW-02
- **발생 시각:** `2026-07-19 12:05:10`
- **위험 단계:** `WARNING`
- **현상 및 메시지:** Core transceiver temperature exceeded threshold warning limit
- **가이드라인 (교육용):** 포트의 연결이 끊어졌거나 통신 신호가 유실되었습니다. 상하위 장비 상태와 포트 LED 상태를 점검해야 합니다.

### 7. [TICKET_ESCALATED] - 장비: SW-02
- **발생 시각:** `2026-07-19 12:15:00`
- **위험 단계:** `CRITICAL`
- **현상 및 메시지:** Ticket #92044 generated for SW-02 link stability issue
- **가이드라인 (교육용):** 장애 상황이 지속되어 티켓 관리 시스템으로 자동 이관되었습니다. 긴급 현장 엔지니어 배정 및 점검이 권장됩니다.


---
*본 분석 보고서는 Python 스크립트(`dco_analyzer.py`)에 의해 자동 생성되었습니다.*
