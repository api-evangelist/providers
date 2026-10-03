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
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: Employee benefits API
  name: Beni API
  slug: beni-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beni/refs/heads/main/hosts/beni-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beni-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beni/refs/heads/main/vendors/beni-vendors.yml
  title: ''
  type: Vendors
  url: vendors/beni-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.beniglobal.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.beniglobal.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.beniglobal.com/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beni/refs/heads/main/security/beni-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beni-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.beniglobal.com
coverage:
  checked: '2026-09-27'
  detail: The API documentation site returns HTML shells for spec URLs, providing no machine‑readable contract.
  evidence:
  - status: 200
    url: https://www.beniglobal.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-27'
description: Beni is a global employee benefits consulting and solutions provider, offering technology-driven services that deliver below-market renewals, strategic benefits solutions, and innovative health plans. The company focuses on real relationships and best-in-class technology to help employers manage fiduciary risk and improve employee satisfaction across multiple industries.
image: https://www.beniglobal.com/opengraph-image?e87fe144f66314f5
layout: provider
modified: '2026-09-27'
name: Beni
nav: Providers
network: true
overview: Beni publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Employee Benefits, Consulting, Technology, Health, and Solutions.
random_paper: 18
score:
  band: minimal
  composite: 9.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Beni Domain Security
  slug: beni-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: beni
tags:
- Employee Benefits
- Consulting
- Technology
- Health
- Solutions
website: https://www.beniglobal.com
---
