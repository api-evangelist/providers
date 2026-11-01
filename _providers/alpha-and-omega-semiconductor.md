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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/alpha-and-omega-semiconductor/hosts/alpha-and-omega-semiconductor-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alpha-and-omega-semiconductor-hosts.yml
- group: other
  href: https://artifacts.apis.io/alpha-and-omega-semiconductor/vendors/alpha-and-omega-semiconductor-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alpha-and-omega-semiconductor-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aosmd.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aosmd.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.aosmd.com/newsroom
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.aosmd.com/
- group: auth
  href: https://artifacts.apis.io/alpha-and-omega-semiconductor/security/alpha-and-omega-semiconductor-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alpha-and-omega-semiconductor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aosmd.com/
coverage:
  checked: '2026-10-24'
  detail: The provider's website serves HTML shells for OpenAPI URLs, preventing machine-readable spec retrieval.
  evidence:
  - status: 200
    url: https://www.aosmd.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-23'
description: Alpha & Omega Semiconductor Limited (AOS) designs, develops, and globally supplies a broad range of power semiconductor products, including Power MOSFETs, IGBTs, IPMs, and Power ICs. The company serves automotive, industrial, and consumer markets with high-efficiency solutions, emphasizing innovation, reliability, and performance across its extensive product portfolio.
image: https://www.aosmd.com/themes/custom/aos/logo.png
layout: provider
modified: '2026-10-23'
name: Alpha & Omega Semiconductor
nav: Providers
network: true
overview: Alpha & Omega Semiconductor is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductor, Manufacturing, Technology, and Hardware.
random_paper: 8
score:
  band: minimal
  composite: 10.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Alpha And Omega Semiconductor Domain Security
  slug: alpha-and-omega-semiconductor-domain-security
  summary_line: TLSv1.3 · DMARC
slug: alpha-and-omega-semiconductor
tags:
- Company
- Semiconductor
- Manufacturing
- Technology
- Hardware
website: https://www.aosmd.com/
---
