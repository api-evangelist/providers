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
- description: Coople API documentation
  name: Coople API
  slug: coople-api
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coople/refs/heads/main/well-known/coople-clarity-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/coople-clarity-security.txt
- group: auth
  title: ''
  type: Security
  url: https://clarity.com/vdp
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/coople/refs/heads/main/llms/coople-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/coople-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coople/refs/heads/main/well-known/coople-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/coople-help-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/coople/refs/heads/main/well-known/coople-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/coople-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coople/refs/heads/main/hosts/coople-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coople-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coople/refs/heads/main/vendors/coople-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coople-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.coople.com/en/
- group: start
  title: ''
  type: Login
  url: https://www.coople.com/ch/sign-in
- group: docs
  title: ''
  type: Documentation
  url: https://help.coople.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coople/refs/heads/main/security/coople-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/coople-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coople/refs/heads/main/security/coople-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coople-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.coople.com/ch
coverage:
  checked: '2026-10-11'
  detail: Help center pages contain API documentation but no machine‑readable OpenAPI, GraphQL, AsyncAPI, gRPC, or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://help.coople.com/en/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-10'
description: Coople is a technology-driven workforce solutions provider that connects businesses with flexible, skilled talent across various sectors such as healthcare, retail, logistics, hospitality, and office environments. Their platform enables companies to quickly find, hire, and manage temporary staff, offering services like payrolling, workforce planning, and compliance support. Coople leverages a smart digital platform to streamline recruitment, onboarding, and workforce management, helping businesses adapt to fluctuating labor needs while providing workers with flexible job opportunities.
layout: provider
modified: '2026-10-10'
name: Coople
nav: Providers
network: true
overview: 'Coople is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Workforce, Staffing, Technology, Platform, and FlexibleWork.


  Coople''s developer surface includes support, documentation, and 11 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 12.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 60.7
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Coople Domain Security
  slug: coople-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Coople Vulnerability Disclosure
  slug: coople-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: coople
tags:
- Workforce
- Staffing
- Technology
- Platform
- FlexibleWork
website: https://www.coople.com/ch
---
