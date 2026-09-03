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
  url: security/ciitizen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.citizen.health/
created: '2026-07-17'
description: Ciitizen is a digital health company that helps patients collect, organize, and control their own medical records. Founded by Anil Sethi and backed by a16z, Ciitizen built patient-directed tools for aggregating records across providers under HIPAA right-of-access, originally with a focus on cancer patients. The team and technology now operate as Citizen Health (citizen.health), which turns a patient's medical records into instant answers through an AI Advocate built for rare disease patients and caregivers and used by 100+ patient advocacy groups. Ciitizen exposes no public developer API, developer portal, or machine-readable API artifacts at this time; this profile captures the company identity and its live web presence.
image: https://cdn.prod.website-files.com/6658cacd8ca3f5b6f07af2d5/699d46365751cf062e71736e_Open%20Graph%20with%20Phone%20and%20Recording.png
layout: provider
modified: '2026-07-18'
name: Ciitizen
nav: Providers
network: true
overview: Ciitizen is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Health Records, Patient Data, and Rare Disease.
random_paper: 2
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ciitizen/refs/heads/main/screenshots/ciitizen-2026-07-25T205354.png
security:
- kind: domain-security
  name: Ciitizen Domain Security
  slug: ciitizen-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ciitizen
tags:
- Company
- Healthcare
- Health Records
- Patient Data
- Rare Disease
- Digital Health
- Interoperability
- Artificial Intelligence
website: https://www.citizen.health/
---
