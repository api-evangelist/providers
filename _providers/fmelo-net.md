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
    mcp_tool_quality: na
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
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/fmelo-net/security/fmelo-net-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/fmelo-net-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/fmelo-net/well-known/fmelo-net-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/fmelo-net-security.txt
- group: auth
  href: https://artifacts.apis.io/fmelo-net/well-known/fmelo-net-folio-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/fmelo-net-folio-security.txt
- group: auth
  href: https://artifacts.apis.io/fmelo-net/well-known/fmelo-net-desk9-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/fmelo-net-desk9-security.txt
- group: auth
  href: https://artifacts.apis.io/fmelo-net/well-known/fmelo-net-cognita-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/fmelo-net-cognita-security.txt
- group: auth
  href: https://artifacts.apis.io/fmelo-net/well-known/fmelo-net-astur-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/fmelo-net-astur-security.txt
- group: agent
  href: https://artifacts.apis.io/fmelo-net/well-known/fmelo-net-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fmelo-net-well-known.yml
- group: other
  href: https://artifacts.apis.io/fmelo-net/hosts/fmelo-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fmelo-net-hosts.yml
- group: other
  href: https://artifacts.apis.io/fmelo-net/vendors/fmelo-net-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fmelo-net-vendors.yml
- group: auth
  href: https://artifacts.apis.io/fmelo-net/security/fmelo-net-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/fmelo-net-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/fmelo-net/security/fmelo-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fmelo-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fmelo.net/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://cognita.fmelo.net/mcp
  - status: 200
    url: https://fmelo.net/
  reason: no-developer-program
  state: none
created: '2026-10-30'
description: 'fmelo-net is a technology-focused company that provides networking solutions and API services. It was initially identified through the API Evangelist harvest backlog (source: mcp-registry) and added as a stub for comprehensive profiling. The company aims to deliver robust, scalable APIs for developers, emphasizing security, performance, and ease of integration across various platforms.'
image: https://fmelo.net/profile.jpg
layout: provider
modified: '2026-10-30'
name: fmelo-net
nav: Providers
network: true
overview: fmelo-net is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Networking, Developer Tools, and Security.
random_paper: 15
score:
  band: minimal
  composite: 4.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 39.3
    operational_transparency: 10.5
  previous_composite: 5.7
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/fmelo-net/fmelo-net-2026-11-03T132210.png
security:
- kind: domain-security
  name: Fmelo Net Domain Security
  slug: fmelo-net-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Fmelo Net Vulnerability Disclosure
  slug: fmelo-net-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: fmelo-net
tags:
- Company
- Networking
- Developer Tools
- Security
website: https://fmelo.net/
---
