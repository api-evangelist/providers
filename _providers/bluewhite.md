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
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bluewhite/refs/heads/main/well-known/bluewhite-clarity-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bluewhite-clarity-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bluewhite/refs/heads/main/well-known/bluewhite-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bluewhite-well-known.yml
- group: auth
  title: ''
  type: Security
  url: https://clarity.com/vdp
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bluewhite/refs/heads/main/hosts/bluewhite-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bluewhite-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bluewhite/refs/heads/main/vendors/bluewhite-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bluewhite-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bluewhite.ai/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bluewhite.ai/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.bluewhite.ai/press
- group: company
  title: ''
  type: Blog
  url: https://www.bluewhite.ai/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bluewhite/refs/heads/main/security/bluewhite-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bluewhite-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bluewhite/refs/heads/main/security/bluewhite-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bluewhite-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bluewhite.ai/
coverage:
  checked: '2026-09-29'
  detail: No public developer program or API documentation is provided; attempts to fetch OpenAPI spec returned 404.
  evidence:
  - status: 404
    url: https://www.bluewhite.ai/openapi.json
  reason: no-developer-program
  state: none
created: '2026-09-29'
description: Bluewhite is an AI‑powered autonomy company delivering off‑road autonomous solutions for critical defense missions. Their platform automates high‑risk, labor‑intensive operations such as combat logistics, route clearance, and border security, enabling frontline units to operate safely and efficiently. With over 100,000 autonomous operating hours and a modular, interoperable stack, Bluewhite provides scalable, software‑driven autonomy for defense forces worldwide.
layout: provider
modified: '2026-09-29'
name: Bluewhite
nav: Providers
network: true
overview: 'Bluewhite is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Autonomy, Defense, and Robotics.


  Bluewhite''s developer surface includes engineering blog and 11 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 46.4
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bluewhite Domain Security
  slug: bluewhite-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Bluewhite Vulnerability Disclosure
  slug: bluewhite-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bluewhite
tags:
- Company
- Artificial Intelligence
- Autonomy
- Defense
- Robotics
website: https://www.bluewhite.ai/
---
