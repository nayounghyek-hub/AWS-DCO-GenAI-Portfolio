# -*- coding: utf-8 -*-
"""
DCO(Data Center Operations) 교육용 샘플 로그 분석기
비전공자 및 Python 입문자를 위해 한 줄씩 상세히 설명된 친절한 코드입니다.

[로그 포맷]
날짜/시간 | 장비명 | 심각도(Severity) | 이벤트 유형 | 세부 메시지
예: 2026-07-19 10:15:30 | SVR-102 | WARNING | CRC_ERROR | High bit error rate...
"""

# 외부 패키지 설치 없이 Python에 기본 내장된 라이브러리만 사용합니다.
import os
from collections import Counter, defaultdict

def analyze_dco_logs(file_path="sample_dco_log.txt", output_path="incident_summary.md"):
    print("=" * 60)
    print(f"[{file_path}] 파일 분석을 시작합니다...")
    print("=" * 60)

    # 0. 파일 존재 여부 확인
    if not os.path.exists(file_path):
        print(f"오류: '{file_path}' 파일을 찾을 수 없습니다.")
        print("현재 디렉토리에 로그 파일이 있는지 확인해 주세요.")
        return

    # 분석에 필요한 변수들을 준비합니다.
    total_lines = 0               # 1. 전체 로그 줄 수
    severity_counter = Counter()  # 2. 심각도별 개수 저장용
    event_counter = Counter()     # 3. 이벤트별 개수 저장용
    
    warning_critical_logs = []    # 4. WARNING 또는 CRITICAL 로그 목록 저장용
    major_events_summary = []     # 5. CRC_ERROR, LINK_DOWN, TICKET_ESCALATED 로그 저장용

    # 1. 파일 열기 및 줄별 분석 시작
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()  # 줄 끝의 줄바꿈 문자(\\n)나 공백을 제거합니다.
            if not line:         # 빈 줄은 무시하고 넘어갑니다.
                continue
            
            total_lines += 1     # 유효한 로그가 발견될 때마다 줄 수를 1씩 더합니다.
            
            # '|' 기호를 기준으로 로그를 분할합니다.
            # split(" | ")을 통해 각각의 요소를 깔끔하게 나눌 수 있습니다.
            parts = [part.strip() for part in line.split("|")]
            
            # 로그 형식이 올바른지 체크합니다 (형식: 시간 | 장비 | 심각도 | 이벤트 | 메시지) -> 총 5개 영역
            if len(parts) >= 5:
                timestamp = parts[0]
                device = parts[1]
                severity = parts[2]
                event = parts[3]
                message = parts[4]
            else:
                # 형식이 다를 경우 유연하게 대처합니다.
                continue

            # 2. 심각도 집계
            severity_counter[severity] += 1

            # 3. 이벤트 집계
            event_counter[event] += 1

            # 4. WARNING 또는 CRITICAL 로그 추출
            if severity in ["WARNING", "CRITICAL"]:
                warning_critical_logs.append({
                    "timestamp": timestamp,
                    "device": device,
                    "severity": severity,
                    "event": event,
                    "message": message,
                    "original": line
                })

            # 5. 주요 이벤트(CRC_ERROR, LINK_DOWN, TICKET_ESCALATED) 요약 추출
            if event in ["CRC_ERROR", "LINK_DOWN", "TICKET_ESCALATED"]:
                major_events_summary.append({
                    "timestamp": timestamp,
                    "device": device,
                    "severity": severity,
                    "event": event,
                    "message": message
                })

    # 콘솔에 분석 결과 출력하기
    print(f"\n1. 전체 로그 수: 총 {total_lines}개")
    
    print("\n2. 심각도별(Severity) 로그 수:")
    for sev, count in severity_counter.items():
        print(f"   - {sev}: {count}개")

    print("\n3. 이벤트별(Event) 발생 횟수:")
    for ev, count in event_counter.items():
        print(f"   - {ev}: {count}개")

    print(f"\n4. WARNING/CRITICAL 단계 로그: 총 {len(warning_critical_logs)}개")
    for idx, log in enumerate(warning_critical_logs, 1):
        print(f"   [{idx}] [{log['severity']}] {log['timestamp']} | {log['device']} | {log['event']} -> {log['message']}")

    print(f"\n5. 주요 점검 대상 이벤트(CRC_ERROR, LINK_DOWN, TICKET_ESCALATED) 목록: 총 {len(major_events_summary)}개")
    for idx, log in enumerate(major_events_summary, 1):
        print(f"   [{idx}] {log['timestamp']} | 장비: {log['device']} | 이벤트: {log['event']} | 메시지: {log['message']}")

    # 6. 결과를 Markdown 파일(incident_summary.md)로 저장하기
    try:
        with open(output_path, "w", encoding="utf-8") as out_file:
            out_file.write("# 📋 AWS DCO 교육용 샘플 로그 분석 리포트\n\n")
            out_file.write("본 리포트는 데이터 센터 운영(Data Center Operations) 직무 이해를 돕기 위해 작성된 교육용 가상 분석 보고서입니다.\n\n")
            
            # 기본 요약 정보 표
            out_file.write("## 1. 분석 개요\n")
            out_file.write("| 항목 | 분석 결과 |\n")
            out_file.write("| :--- | :--- |\n")
            out_file.write(f"| **전체 로그 줄 수** | {total_lines}개 |\n")
            out_file.write(f"| **주의/경고 로그 수 (WARNING/CRITICAL)** | {len(warning_critical_logs)}개 |\n")
            out_file.write(f"| **주요 장애 이벤트 수 (점검 대상)** | {len(major_events_summary)}개 |\n\n")

            # 심각도 분포
            out_file.write("## 2. 심각도별(Severity) 분포\n")
            out_file.write("로그 내 위험 수준별 발생 현황입니다.\n\n")
            out_file.write("| 심각도 | 발생 건수 | 비율 |\n")
            out_file.write("| :--- | :---: | :---: |\n")
            for sev, count in severity_counter.most_common():
                ratio = (count / total_lines) * 100 if total_lines > 0 else 0
                out_file.write(f"| {sev} | {count}개 | {ratio:.1f}% |\n")
            out_file.write("\n")

            # 이벤트별 발생 분포
            out_file.write("## 3. 이벤트 유형별 발생 분포\n")
            out_file.write("어떤 종류의 상태 변화 및 에러가 많이 발생했는지 확인합니다.\n\n")
            out_file.write("| 이벤트명 | 발생 건수 |\n")
            out_file.write("| :--- | :---: |\n")
            for ev, count in event_counter.most_common():
                out_file.write(f"| {ev} | {count}개 |\n")
            out_file.write("\n")

            # WARNING 또는 CRITICAL 상세 목록
            out_file.write("## 4. WARNING 및 CRITICAL 로그 상세 리스트\n")
            out_file.write("데이터 센터에서 수동 또는 자동 모니터링 대응이 필요할 수 있는 경고/심각 로그 목록입니다.\n\n")
            out_file.write("| 번호 | 일시 | 장비명 | 심각도 | 이벤트 | 메시지 |\n")
            out_file.write("| :---: | :--- | :--- | :---: | :--- | :--- |\n")
            for idx, log in enumerate(warning_critical_logs, 1):
                out_file.write(f"| {idx} | {log['timestamp']} | {log['device']} | **{log['severity']}** | {log['event']} | {log['message']} |\n")
            out_file.write("\n")

            # 주요 이벤트 요약
            out_file.write("## 5. 주요 점검 대상 이벤트 요약\n")
            out_file.write("데이터 센터 인프라 운영진이 즉각 확인해야 하는 대표적인 에러 패턴(`CRC_ERROR`, `LINK_DOWN`, `TICKET_ESCALATED`)에 대한 상세 점검 요약입니다.\n\n")
            for idx, log in enumerate(major_events_summary, 1):
                out_file.write(f"### {idx}. [{log['event']}] - 장비: {log['device']}\n")
                out_file.write(f"- **발생 시각:** `{log['timestamp']}`\n")
                out_file.write(f"- **위험 단계:** `{log['severity']}`\n")
                out_file.write(f"- **현상 및 메시지:** {log['message']}\n")
                
                # 분석적인 해설 가이드 추가 (교육용)
                guide = ""
                if log['event'] == "CRC_ERROR":
                    guide = "물리적 회선 연결부(케이블, 트랜시버)에 비트 에러가 발생한 상황입니다. 먼지 유입 여부 점검이나 트랜시버 재장착이 필요할 수 있습니다."
                elif log['event'] == "LINK_DOWN":
                    guide = "포트의 연결이 끊어졌거나 통신 신호가 유실되었습니다. 상하위 장비 상태와 포트 LED 상태를 점검해야 합니다."
                elif log['event'] == "TICKET_ESCALATED":
                    guide = "장애 상황이 지속되어 티켓 관리 시스템으로 자동 이관되었습니다. 긴급 현장 엔지니어 배정 및 점검이 권장됩니다."
                
                out_file.write(f"- **가이드라인 (교육용):** {guide}\n\n")

            out_file.write("\n---\n")
            out_file.write("*본 분석 보고서는 Python 스크립트(`dco_analyzer.py`)에 의해 자동 생성되었습니다.*\n")
        
        print("\n" + "=" * 60)
        print(f"분석 결과가 '{output_path}' 파일로 성공적으로 저장되었습니다!")
        print("=" * 60)
        
    except Exception as e:
        print(f"오류: 보고서 저장 중 에러가 발생했습니다. {e}")

# 스크립트 직접 실행 시 실행하는 블록
if __name__ == "__main__":
    analyze_dco_logs()
