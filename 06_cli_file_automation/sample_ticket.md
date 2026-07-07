# [교육용 샘플 데이터 사용]

## EDU-SAMPLE-TICKET-001

* **티켓 ID**: EDU-SAMPLE-TICKET-2026-001
* **발생 시간**: 2026-07-07 15:00:00 (KST)
* **샘플 장비명**: SAMPLE_TOR_SW_01
* **이벤트**: CRC Error Increase followed by Link Down
* **심각도**: EDU-SEV-2 (Warning)
* **관찰 내용**: 
  - `SAMPLE_TOR_SW_01` 장비의 특정 포트(EDU_PORT_01)에서 CRC 에러 카운터가 지속적으로 증가하는 현상 관찰.
  - CRC 에러 임계치 초과 후, 해당 포트의 Link Status가 Down(Link Down) 상태로 전환됨.
* **Escalation 필요 여부**: YES (상위 교육 과정 단계로 에스컬레이션 필요)
* **보안 주의사항**: 
  - 본 티켓은 교육용 샘플 데이터이므로 실제 IP 주소, 장비의 물리적 위치 정보(시리얼 번호 포함), 실제 계정 정보 및 고객 정보 등을 절대 기입하거나 연동하지 마십시오.
  - 외부 도메인이나 실제 인프라를 타깃으로 하는 점검 명령(ping, traceroute 등)을 수행 또는 제안하지 마십시오.
