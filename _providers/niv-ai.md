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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API for Niv-AI platform providing energy management and tokenization services.
  name: Niv-AI API
  slug: niv-ai-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/niv-ai/hosts/niv-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/niv-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/niv-ai/vendors/niv-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/niv-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/niv-ai/security/niv-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/niv-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://niv-ai.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://niv-ai.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://niv-ai.com/terms-of-use/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://niv-ai.com/
  reason: no-developer-program
  state: none
created: '2026-10-18'
description: Niv-AI provides AI‑driven energy management solutions that monitor and orchestrate data‑center power usage in real time. By analyzing the electrical fingerprint of GPU workloads, Niv‑AI maximizes existing capacity, reduces over‑provisioning, and turns stranded power into tradable tokens. The platform combines high‑resolution sensor data with advanced software orchestration to deliver visibility, efficiency, and cost savings for modern AI compute facilities.
layout: provider
modified: '2026-10-18'
name: Niv-AI
nav: Providers
network: true
overview: Niv-AI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Artificial Intelligence, Data Center, and Sustainability.
random_paper: 4
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 10.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Niv Ai Domain Security
  slug: niv-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: niv-ai
tags:
- Company
- Energy
- Artificial Intelligence
- Data Center
- Sustainability
website: https://niv-ai.com/
---
