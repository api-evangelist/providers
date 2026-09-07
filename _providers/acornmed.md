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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-06'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acornmed-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/acornmed-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/acornmed-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/acornmed-rate-limits.yml
- group: company
  title: ''
  type: Website
  url: https://en.acornmed.com/
- group: company
  title: ''
  type: About
  url: https://en.acornmed.com/about/index.html
- group: operate
  title: ''
  type: Support
  url: https://en.acornmed.com/SupportContactUs/index.html
- group: company
  title: ''
  type: Blog
  url: https://www.acornmed.com/news
- group: company
  title: ''
  type: Partners
  url: https://en.acornmed.com/Partnering/index.html
coverage:
  checked: '2026-09-06'
  detail: 'AcornMed sells CAP/ISO 15189 laboratory testing and IVD products, not software: its English and Chinese sites carry only Home/About/Tests/Partnering/Support navigation, the one page named /dev-service is 药企研发合作 (pharma R&D services) rather than a developer platform, and no api., docs., developer. or open. subdomain resolves in DNS.'
  evidence:
  - status: 200
    url: https://en.acornmed.com/
  - status: 200
    url: https://www.acornmed.com/dev-service
  - status: 302
    url: https://en.acornmed.com/openapi.json
  - status: 404
    url: https://www.acornmed.com/openapi.json
  - status: 404
    url: https://acornmed.com/.well-known/agent-card.json
  - status: 404
    url: https://acornmed.com/apis.json
  reason: not-a-software-company
  state: none
created: '2026-09-06'
description: 'AcornMed Biotechnology Co., Ltd. (金橡医学) is a Beijing-headquartered precision-oncology company founded in 2018, with subsidiaries in Tianjin and Qingdao. It develops and operates next-generation-sequencing (NGS) diagnostics for solid tumors and hematologic malignancies — the AcornUI urine-based series for bladder, ureteral and renal-pelvic cancer rule-out and recurrence monitoring, AcornUPro-SEEK for prostate cancer screening, AcornOne 808 for solid tumors and AcornHema 521 for blood cancers — alongside CAP/ISO 15189 central-laboratory testing, companion-diagnostic co-development and real-world-data services for pharmaceutical partners. AcornMed is a clinical laboratory and IVD developer: it sells testing services to hospitals, physicians and pharma sponsors and publishes no public developer program, API, or machine-readable contract of any kind.'
image: https://en.acornmed.com/uploads/20240808/64de09767d8debd0f5ac3fc159834a0c.png
layout: provider
modified: '2026-09-06'
name: Acornmed
nav: Providers
network: true
overview: 'Acornmed is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Life Sciences, and Biotechnology.


  Acornmed''s developer surface includes support, engineering blog, and 7 more developer resources.'
plans:
- name: Acornmed Plans Pricing
  plan_count: 0
  slug: acornmed-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Acornmed Rate Limits
  slug: acornmed-rate-limits
score:
  band: minimal
  composite: 4.7
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.19.0
  scored_at: '2026-09-06'
security:
- kind: domain-security
  name: Acornmed Domain Security
  slug: acornmed-domain-security
  summary_line: TLSv1.3 · HSTS
slug: acornmed
tags:
- Company
- Health
- Healthcare
- Life Sciences
- Biotechnology
- Genomics
- Diagnostics
- Oncology
- Precision Medicine
- Clinical Laboratory
- China
website: https://en.acornmed.com/
---
