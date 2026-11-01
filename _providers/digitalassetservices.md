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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API documentation not publicly available; website provides tokenized asset services.
  name: Digital Asset Services API
  slug: digital-asset-services-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/digitalassetservices/hosts/digitalassetservices-hosts.yml
  title: ''
  type: Hosts
  url: hosts/digitalassetservices-hosts.yml
- group: auth
  href: https://artifacts.apis.io/digitalassetservices/security/digitalassetservices-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/digitalassetservices-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.digitalassetservices.ca
coverage:
  checked: '2026-10-23'
  detail: Website renders content via JavaScript, preventing machine‑readable API discovery.
  evidence:
  - status: 200
    url: https://www.digitalassetservices.ca
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-23'
description: Digital Asset Services (DAS) is a financial‑technology firm founded in 2020 that bridges traditional finance and the digital economy through tokenized real‑world assets (RWAs). It offers tokenized investments, education, wealth‑planning, and decentralized digital utility tokens, aiming to provide accessible, secure, and liquid investment opportunities via blockchain technology. The company focuses on financial independence and education for a broad audience.
image: https://www.digitalassetservices.ca/static/images/social-preview.png
layout: provider
modified: '2026-10-23'
name: Digitalassetservices
nav: Providers
network: true
overview: Digitalassetservices is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Tokenization, WealthEducation, and Blockchain.
random_paper: 10
score:
  band: minimal
  composite: 4.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Digitalassetservices Domain Security
  slug: digitalassetservices-domain-security
  summary_line: TLSv1.3 · DMARC
slug: digitalassetservices
tags:
- Company
- Fintech
- Tokenization
- WealthEducation
- Blockchain
website: https://www.digitalassetservices.ca
---
