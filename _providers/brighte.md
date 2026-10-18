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
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brighte/refs/heads/main/hosts/brighte-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brighte-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brighte/refs/heads/main/vendors/brighte-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brighte-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.brighte.com.au/hc/en-gb
- group: auth
  title: ''
  type: Security
  url: https://brighte.com.au/support/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://brighte.com.au/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://brighte.com.au/media
- group: start
  title: ''
  type: Login
  url: https://brighte.com.au/login
- group: other
  title: ''
  type: Leadership
  url: https://brighte.com.au/about/team
- group: company
  title: ''
  type: Blog
  url: https://brighte.com.au/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brighte/refs/heads/main/security/brighte-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/brighte-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brighte/refs/heads/main/security/brighte-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brighte-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brighte.com.au
coverage:
  checked: '2026-10-06'
  detail: Brighte's website and known hosts provide no machine‑readable API specifications.
  evidence:
  - status: 200
    url: https://brighte.com.au
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-06'
description: Brighte provides financing solutions for Australian households and businesses to adopt solar panels, green loans, and energy-efficient home improvements. Their platform offers interest‑free payment plans, green loans, personal loans, and various government‑backed schemes to make sustainable energy affordable. By partnering with vendors and offering a portal for customers, Brighte aims to accelerate the transition to renewable energy across Australia, supporting both residential and commercial projects.
layout: provider
modified: '2026-10-06'
name: Brighte
nav: Providers
network: true
overview: 'Brighte is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Renewable Energy, Australia, and Solar.


  Brighte''s developer surface includes support, engineering blog, and 10 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 12.3
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 13.1
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brighte Domain Security
  slug: brighte-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Brighte Vulnerability Disclosure
  slug: brighte-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: brighte
tags:
- Company
- Finance
- Renewable Energy
- Australia
- Solar
website: https://brighte.com.au
---
