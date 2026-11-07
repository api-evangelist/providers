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
    mcp_server: documented
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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API documentation and developer portal for disclose.io
  name: Disclose.io API
  slug: disclose-io-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Security
  url: https://disclose.io/security/
- group: agent
  href: https://artifacts.apis.io/disclose-io/llms/disclose-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/disclose-io-llms.txt
- group: auth
  href: https://artifacts.apis.io/disclose-io/well-known/disclose-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/disclose-io-security.txt
- group: auth
  href: https://artifacts.apis.io/disclose-io/well-known/disclose-io-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/disclose-io-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/disclose-io/well-known/disclose-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/disclose-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/disclose-io/hosts/disclose-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/disclose-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/disclose-io/vendors/disclose-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/disclose-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://disclose.io/framework/terms/
- group: company
  title: ''
  type: Blog
  url: https://blog.disclose.io/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.disclose.io/
- group: auth
  href: https://artifacts.apis.io/disclose-io/security/disclose-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/disclose-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/disclose-io/security/disclose-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/disclose-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://disclose.io/
coverage:
  checked: '2026-11-05'
  detail: Developer portal pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://dev.disclose.io/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-05'
description: The open, vendor-neutral infrastructure that powers vulnerability disclosure and security reporting. Safe, simple, and standardized for everyone. disclose.io provides tools to create policies, manage security.txt files, and host public directories of disclosure programs, enabling coordinated vulnerability reporting across the ecosystem.
image: https://disclose.io/uploads/og-image-1200x630.jpg
layout: provider
modified: '2026-11-05'
name: disclose.io
nav: Providers
network: true
overview: 'disclose.io is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Security, Vulnerability Disclosure, Open Source, Infrastructure, and Community.


  disclose.io''s developer surface includes engineering blog, documentation, and 11 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Disclose Io Domain Security
  slug: disclose-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Disclose Io Vulnerability Disclosure
  slug: disclose-io-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: disclose-io
tags:
- Security
- Vulnerability Disclosure
- Open Source
- Infrastructure
- Community
website: https://disclose.io/
---
