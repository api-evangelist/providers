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
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: API for Auger platform
  name: Auger API
  slug: auger-api
artifact_total: 3
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/auger/refs/heads/main/hosts/auger-hosts.yml
  title: ''
  type: Hosts
  url: hosts/auger-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/auger/refs/heads/main/vendors/auger-vendors.yml
  title: ''
  type: Vendors
  url: vendors/auger-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.auger.com/
- group: auth
  title: ''
  type: Security
  url: https://auger.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://auger.com/privacy-notice/
- group: company
  title: ''
  type: Newsroom
  url: https://auger.com/about/newsroom/
- group: other
  title: ''
  type: Leadership
  url: https://auger.com/about/team/kim-peevy/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/auger/refs/heads/main/security/auger-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/auger-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/auger/refs/heads/main/security/auger-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/auger-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://auger.com
coverage:
  checked: 2026-09-26
  detail: No OpenAPI or other machine-readable contract found on any probed host.
  evidence:
  - status: timeout
    url: https://api.auger.com/openapi.json
  - status: 404
    url: https://auger.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Auger provides an operating system for supply chain finance, ingesting raw operational streams such as ERPs, spreadsheets, and legacy APIs to unlock trapped working capital. The platform automates coordination, reduces lead times, and offers AI‑driven insights to help enterprises accelerate execution and capture billions of dollars in value.
image: https://auger.com/wp-content/uploads/2026/01/Social-512.png
layout: provider
modified: '2026-09-26'
name: Auger
nav: Providers
network: true
overview: Auger publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Supply Chain, Finance, Automation, and Artificial Intelligence.
random_paper: 4
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 60.7
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Auger Domain Security
  slug: auger-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Auger Vulnerability Disclosure
  slug: auger-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: auger
tags:
- Company
- Supply Chain
- Finance
- Automation
- Artificial Intelligence
website: https://auger.com
---
