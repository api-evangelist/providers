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
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/asignio/refs/heads/main/llms/asignio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/asignio-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/asignio/refs/heads/main/hosts/asignio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/asignio-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/asignio/refs/heads/main/vendors/asignio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/asignio-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/asignio/refs/heads/main/security/asignio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/asignio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.web.asignio.com/
- group: company
  title: ''
  type: Blog
  url: https://www.web.asignio.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.web.asignio.com/pricing
- group: company
  title: ''
  type: About
  url: https://www.web.asignio.com/about
- group: operate
  title: ''
  type: Contact
  url: https://www.web.asignio.com/contact
coverage:
  checked: 2026-09-26
  detail: No machine‑readable OpenAPI or other contract discovered; API endpoints return 404 and documentation appears to be rendered via Wix without downloadable specs.
  evidence:
  - status: 404
    url: https://api.asignio.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: Asignio provides biometric authentication solutions that replace passwords with user‑drawn signatures, facial and voice biometrics. Their platform combats phishing, ransomware and deep‑fake attacks by verifying identity through AI‑driven behavioral markers, live selfie checks and multi‑modal biometrics, offering a password‑less, fraud‑resistant sign‑in experience for web and mobile applications.
layout: provider
modified: '2026-09-26'
name: Asignio
nav: Providers
network: true
overview: 'Asignio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biometric, Authentication, Security, Identity, and Fraud Prevention.


  Asignio''s developer surface includes engineering blog, pricing, and 7 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 6.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 51.8
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Asignio Domain Security
  slug: asignio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: asignio
tags:
- Biometric
- Authentication
- Security
- Identity
- Fraud Prevention
website: https://www.web.asignio.com/
---
