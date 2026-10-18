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
api_count: 1
apis:
- description: MOIA provides mobility services; public API documentation is hosted on their help site but no machine‑readable contract was found.
  name: MOIA API
  slug: moia-api
artifact_total: 3
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moia/refs/heads/main/vendors/moia-vendors.yml
  title: ''
  type: Vendors
  url: vendors/moia-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/moia/refs/heads/main/security/moia-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/moia-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/moia/refs/heads/main/well-known/moia-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/moia-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/moia/refs/heads/main/well-known/moia-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/moia-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moia/refs/heads/main/hosts/moia-hosts.yml
  title: ''
  type: Hosts
  url: hosts/moia-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.moia.io/en-US/terms
- group: operate
  title: ''
  type: Support
  url: https://help.moia.io/hc/de
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.moia.io/en-US/privacy-statement
- group: company
  title: ''
  type: Newsroom
  url: https://www.moia.io/en-US/news
- group: docs
  title: ''
  type: Documentation
  url: https://help.moia.io/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/moia/refs/heads/main/security/moia-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/moia-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/moia/refs/heads/main/security/moia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/moia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.moia.io
coverage:
  checked: '2026-10-13'
  detail: The help.moia.io documentation site provides only HTML pages without an OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://help.moia.io/hc/de
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: MOIA America is an autonomous mobility solutions provider that develops and operates self‑driving vehicle services for cities and businesses. Based in Belmont, California, MOIA offers a turnkey platform combining autonomous vehicle technology, mobility‑as‑a‑service software, and operational support to expand transportation access, improve community connectivity, and advance sustainable urban mobility. The company conducts on‑road testing in multiple U.S. markets, including Los Angeles, Austin, and Orlando, and partners with municipalities to shape the future of mobility.
image: https://www.moia.io/dist/assets/images/sharing-image.jpg
layout: provider
modified: '2026-10-13'
name: MOIA
nav: Providers
network: true
overview: 'MOIA is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Autonomous Mobility, Ridepooling, Transportation, Cities, and Software.


  MOIA''s developer surface includes support, documentation, and 11 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 15.0
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
    developer_ergonomics: 14.3
    discoverability: 58.9
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Moia Domain Security
  slug: moia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Moia Vulnerability Disclosure
  slug: moia-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: moia
tags:
- Autonomous Mobility
- Ridepooling
- Transportation
- Cities
- Software
website: https://www.moia.io
---
