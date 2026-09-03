---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/inbrace-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://inbrace.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/inbrace_stock/
coverage:
  checked: '2026-08-23'
  detail: Swift Health Systems, Inc. (InBrace) ceased operations in April 2025 and every path on inbrace.com — apex, /.well-known/*, /openapi.json, /llms.txt, /docs, /api — now answers HTTP 301 into insmilebraces.com, the site of InSmile Braces, the separate company that bought the IP; the surviving portal host is a login-gated React app whose only backend is an internal /api/ path, so there is no InBrace-owned contract left to read.
  evidence:
  - status: 301
    url: https://inbrace.com/
  - status: 301
    url: https://inbrace.com/openapi.json
  - status: 301
    url: https://inbrace.com/.well-known/agent-card.json
  - status: 404
    url: https://www.insmilebraces.com/openapi.json
  - status: 404
    url: https://www.insmilebraces.com/llms.txt
  - status: 401
    url: https://portal.insmilebraces.com/openapi.json
  reason: defunct
  state: none
created: '2026-08-23'
description: InBrace was the lingual orthodontics brand of Swift Health Systems, Inc., an Irvine, California medical-device company co-founded in 2012 by orthodontists John Pham and Hongsheng Tong. Its patented INBRACE Smartwires were programmed from digital scans of a patient's teeth and bonded behind the teeth, moving teeth continuously without relying on patient compliance; the product reached market in 2016 and was sold to orthodontic practices through a doctor-facing case-submission portal at portal.inbrace.com rather than through any public developer program. The company raised roughly $70 million in total, including a $45 million Series C led by Vivo Capital with Novo Holdings and venBio Partners in 2019. InBrace ceased operations in April 2025, citing tightening capital markets and slower-than-expected adoption, leaving providers with cases mid-treatment. Its intellectual property, production equipment and manufacturing assets were acquired by orthodontist Dr. Scott Schwartz, who
  relaunched the technology in August 2025 as InSmile Braces — an independent company operated by Lorelli Technologies and explicitly separate from InBrace. As of this profile inbrace.com and portal.inbrace.com 301-redirect wholesale to insmilebraces.com, so no InBrace-origin content is served from any host. InBrace never published an API, SDK, developer portal or machine-readable specification, and none is served today.
layout: provider
modified: '2026-08-23'
name: InBrace
nav: Providers
network: true
overview: InBrace is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Orthodontics, Dental, Medical Devices, and Health.
random_paper: 10
score:
  band: minimal
  composite: 2.9
  coverage:
    artifact_dirs: 3
    catalog_gap: 90.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 2.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/inbrace/refs/heads/main/screenshots/inbrace-2026-09-02T145846.png
security:
- kind: domain-security
  name: Inbrace Domain Security
  slug: inbrace-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: inbrace
tags:
- Company
- Orthodontics
- Dental
- Medical Devices
- Health
- Lingual Braces
- Consumer Health
- Defunct
website: https://inbrace.com/
---
