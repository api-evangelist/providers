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
  href: https://raw.githubusercontent.com/api-evangelist/securitas/refs/heads/main/hosts/securitas-hosts.yml
  title: ''
  type: Hosts
  url: hosts/securitas-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/securitas/refs/heads/main/vendors/securitas-vendors.yml
  title: ''
  type: Vendors
  url: vendors/securitas-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.securitas.com/esc
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.securitas.com/en/about-us/privacy-notice/
- group: company
  title: ''
  type: Newsroom
  url: https://www.securitas.com/en/newsroom/
- group: company
  title: ''
  type: Blog
  url: https://www.securitas.com/en/newsroom/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/securitas/refs/heads/main/security/securitas-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/securitas-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://securitas.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.securitas.com/en/security-services/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.securitas.com/en/
- group: company
  title: ''
  type: AboutUs
  url: https://www.securitas.com/en/about-us/
coverage:
  checked: '2026-10-15'
  detail: The provider's documentation pages are public HTML with no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL specifications.
  evidence:
  - status: 0
    url: https://api.securitas.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-14'
description: Securitas Group is a global security services provider offering a wide range of solutions including guarding, electronic security, risk intelligence, and consulting. With operations in over 50 countries, they serve commercial, industrial, and governmental clients, focusing on safety, protection, and innovative security technology.
image: https://www.securitas.com/globalassets/images/2023/10/26/helsiki_230612_2711-181821c5b541914bd8958dec324d3e29f4594.jpg
layout: provider
modified: '2026-10-14'
name: Securitas
nav: Providers
network: true
overview: 'Securitas is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Security, Services, Global, Guarding, and Technology.


  Securitas'' developer surface includes support, engineering blog, documentation, and 8 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 11.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Securitas Domain Security
  slug: securitas-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: securitas
tags:
- Security
- Services
- Global
- Guarding
- Technology
website: https://securitas.com/
---
