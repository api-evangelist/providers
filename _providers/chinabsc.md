---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chinabsc-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/chinabsc-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.bsc1.cn/BSCTelmed/frontend/index
- group: start
  title: ''
  type: Login
  url: https://www.bsc1.cn/BSCManage/manage/system/toIndex
- group: company
  title: ''
  type: Blog
  url: https://www.bsc1.cn/BSCTelmed/frontend/news/news2?colid=CCE08408038E46A2A3C52A16140FA7DA
created: '2026-07-17'
description: Beijing Lanweitong Technology Co., Ltd. (北京蓝卫通科技有限公司), branded BSC, operates one of China's longest-running telemedicine networks — the 蓝卫通远程医学服务平台 (Lanweitong Remote Medical Service Platform). Founded in 1998 and headquartered in Beijing, the company connects thousands of member hospitals and clinics to specialist physicians at Grade-A tertiary hospitals for remote consultation (远程会诊), remote outpatient clinics, multidisciplinary MDT consultations, remote imaging and DICOM cloud reading, remote ECG, remote pathology, remote ultrasound, remote ward rounds, and continuing medical education. The platform is delivered as hospital-facing web applications (BSCTelmed, DicomCloud, BSCEcg, BSCUltrasound, BSCEdu) plus a mobile app, and is sold to health systems and medical alliances (医联体) rather than exposed as a public developer API. The company reports 19 patents and 199 software copyrights and has been recognized as a national-level "little giant" specialized enterprise. It was surfaced
  in the API Evangelist network as a Qiming Venture Partners portfolio company. Its original domain chinabsc.com is still registered but no longer resolves; the live platform runs on bsc1.cn / bscm.cn.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chinabsc.png
layout: provider
modified: '2026-07-20'
name: Beijing Lanweitong Technology (蓝卫通 / BSC)
nav: Providers
network: true
overview: 'Beijing Lanweitong Technology (蓝卫通 / BSC) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Telemedicine, Remote Consultation, and Medical Imaging.


  Beijing Lanweitong Technology (蓝卫通 / BSC)''s developer surface includes engineering blog and 4 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 5.9
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chinabsc/refs/heads/main/screenshots/chinabsc-2026-07-25T205230.png
security:
- kind: domain-security
  name: Chinabsc Domain Security
  slug: chinabsc-domain-security
  summary_line: TLSv1.2 · DNSSEC
slug: chinabsc
tags:
- Company
- Healthcare
- Telemedicine
- Remote Consultation
- Medical Imaging
- DICOM
- Hospitals
- China
website: https://www.bsc1.cn/BSCTelmed/frontend/index
---
