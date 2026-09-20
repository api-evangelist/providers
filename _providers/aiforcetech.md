---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-19'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aiforcetech/refs/heads/main/security/aiforcetech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aiforcetech-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aiforcetech/refs/heads/main/llms/aiforcetech-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aiforcetech-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.aiforcetech.com/
coverage:
  checked: '2026-09-14'
  detail: AIForce Technology sells autonomous and electric farm machinery with an embedded self-driving stack, a companion mobile app and an internal telemetry cloud, but exposes no public developer program — aiforcetech.com is a five-section Chinese marketing site where /openapi.json, /swagger.json, /api-docs, /apis.json and /llms.txt all return a real 404, api./dev./developer./open./cloud.aiforcetech.com do not resolve, and the only other certificate-transparency hosts are an unconfigured default nginx (tbox.) and a 403 media host (v.).
  evidence:
  - status: 200
    url: https://www.aiforcetech.com/sitemap.xml
  - status: 404
    url: https://www.aiforcetech.com/openapi.json
  - status: 404
    url: https://www.aiforcetech.com/llms.txt
  - status: 404
    url: https://www.aiforcetech.com/.well-known/openid-configuration
  - status: 200
    url: https://tbox.aiforcetech.com/
  - status: 403
    url: https://v.aiforcetech.com/
  reason: no-developer-program
  state: none
created: '2026-09-14'
description: 'AIForce Technology (Beijing Zhongke Yuandongli Technology Co., Ltd. / 北京中科原动力科技有限公司) is a Beijing agricultural-robotics manufacturer incubated out of the Chinese Academy of Sciences Institute of Microelectronics, registered in 2018 and operating since July 2019, with Chinese Academy of Engineering academician Li Deyi as chief scientist. It builds autonomous and battery-electric farm machinery across four product lines: the Wantu (万途) electric intelligent tractors, the Zhiniu (智牛) unmanned agricultural machines, the Zhinong (智农) multi-function field robots, and the Zhiyun (智耘) unmanned-operation system that adds full-day autonomous tillage, planting, crop management and harvest to existing machinery in dry fields, paddies and greenhouses, paired with a mobile app and telemetry cloud for route setting and operation monitoring. It is a hardware company that sells machines and retrofit systems to farms, cooperatives and agricultural enterprises, backed by Vertex Ventures China,
  Chery and CCV among others, and named champion of PepsiCo''s Greenhouse Accelerator APAC edition for an AI-powered low-carbon automatic tractor. aiforcetech.com is a five-section Chinese marketing site with no developer program, API, SDK or machine-readable specification of any kind.'
layout: provider
modified: '2026-09-14'
name: AIForce Technology
nav: Providers
network: true
overview: AIForce Technology is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, Agricultural Machinery, Agricultural Robotics, and Robotics.
random_paper: 5
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 4
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 4.6
  schema_version: 0.22.0
  scored_at: '2026-09-19'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aiforcetech Domain Security
  slug: aiforcetech-domain-security
  summary_line: TLSv1.3
slug: aiforcetech
tags:
- Company
- Agriculture
- Agricultural Machinery
- Agricultural Robotics
- Robotics
- Artificial Intelligence
- Autonomous Vehicles
- Precision Agriculture
- Electric Vehicles
- China
website: https://www.aiforcetech.com/
---
