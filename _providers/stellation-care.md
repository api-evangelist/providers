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
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/stellation-care/refs/heads/main/hosts/stellation-care-hosts.yml
  title: ''
  type: Hosts
  url: hosts/stellation-care-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/stellation-care/refs/heads/main/vendors/stellation-care-vendors.yml
  title: ''
  type: Vendors
  url: vendors/stellation-care-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/stellation-care/refs/heads/main/security/stellation-care-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stellation-care-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://stellationcare.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.stellationcare.com/privacy
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://stellationcare.com/
  reason: no-developer-program
  state: none
created: '2026-10-12'
description: Stellation Care provides AI‑augmented provider intelligence and engagement platforms for health plans and provider groups. Their platform combines advanced algorithms with nationwide Medicare and Medicaid claims data to identify high‑performing providers, optimize network strategies, and improve patient outcomes. Acquired by Skylight Health, they offer solutions for provider performance, network tiering, anomaly detection, and workflow automation.
layout: provider
modified: '2026-10-12'
name: Stellation Care
nav: Providers
network: true
overview: Stellation Care is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Artificial Intelligence, ProviderAnalytics, NetworkOptimization, and Medicare.
random_paper: 3
score:
  band: minimal
  composite: 5.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Stellation Care Domain Security
  slug: stellation-care-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: stellation-care
tags:
- Healthcare
- Artificial Intelligence
- ProviderAnalytics
- NetworkOptimization
- Medicare
- Medicaid
website: https://stellationcare.com/
---
