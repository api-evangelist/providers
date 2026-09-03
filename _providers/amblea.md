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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amblea-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.amblea.fr/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/amblerhq
- group: start
  title: ''
  type: Login
  url: https://app.amblea.fr/log-in
created: '2026-07-17'
description: Amblea is a French mission-driven ("entreprise à mission") healthcare-logistics platform that centralizes and optimizes patient (medical / sanitary) transport across the French health system. Formed in 2023 from the merger of Ambler (founded 2018) and Sanilea (2013), it operates a marketplace connecting healthcare establishments (hospitals, clinics, EHPADs, day-care centers) with licensed transport providers (ambulance companies and medical taxi services). The platform handles centralized booking and digital prescription management, shared-transport optimization (grouping patients per trip), real-time tracking, budget and contract management, and automated billing between facilities and transporters. Amblea reports 800+ healthcare establishments, 6,300 transport partner companies, and roughly 8,000 daily trips, making it one of France's largest healthcare-transport coordination platforms. It exposes no public developer API, documentation, or SDKs; access is via its web application
  and direct business arrangements.
image: https://www.amblea.fr/favicon.ico
layout: provider
modified: '2026-07-17'
name: Amblea
nav: Providers
network: true
overview: Amblea is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Patient Transport, Medical Transport, and Healthcare Logistics.
random_paper: 1
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 5.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amblea/refs/heads/main/screenshots/amblea-2026-07-25T200028.png
security:
- kind: domain-security
  name: Amblea Domain Security
  slug: amblea-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: amblea
tags:
- Company
- Healthcare
- Patient Transport
- Medical Transport
- Healthcare Logistics
- Marketplace
- France
website: https://www.amblea.fr/
---
