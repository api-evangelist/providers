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
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: The RALS (Remote Automated Laboratory Systems) platform provides point-of-care device management and data integration capabilities. RALS connects point-of-care testing devices to laboratory informatio
  name: RALS Point-of-Care Data Management API
  slug: rals-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alere-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/alere-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alere-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/alere-conformance.yml
- group: company
  title: ''
  type: Website
  url: https://www.alere.com
- group: company
  title: ''
  type: Website
  url: https://www.globalpointofcare.abbott/us/en/index.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/alere-informatics-inc.
description: Alere Inc. was a global manufacturer of rapid point-of-care diagnostic tests, founded in 1991 and headquartered in Waltham, Massachusetts. The company operated three business units focused on cardiometabolic, infectious disease, and toxicology testing. Alere's product portfolio included the Alere i platform for rapid molecular diagnostics, the Alere CD4 analyser for HIV management, and the RALS point-of-care data management system for laboratory connectivity. Alere Informatics offered web-based solutions including RALS-Freedom, AegisPOC, and RALS-Web3 for point-of-care device management and data integration with laboratory information systems. Abbott Laboratories acquired Alere on October 3, 2017 for $5.3 billion, and the company now operates as Abbott Rapid Diagnostics.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/alere.png
layout: provider
modified: '2026-06-20'
name: alere
nav: Providers
network: true
overview: alere publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Diagnostics, Point Of Care, Healthcare, Laboratory, and Medical Devices.
random_paper: 17
score:
  band: minimal
  composite: 6.8
  delta: -1.6
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 70.4
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 8.4
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alere/refs/heads/main/screenshots/alere-2026-07-25T195556.png
security:
- kind: domain-security
  name: Alere Domain Security
  slug: alere-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: alere
tags:
- Diagnostics
- Point Of Care
- Healthcare
- Laboratory
- Medical Devices
- HL7
website: https://www.alere.com
---
