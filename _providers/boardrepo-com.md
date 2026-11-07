---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Developer API for BoardRepo providing access to board data and markdown representations.
  name: BoardRepo API
  slug: boardrepo-api
- description: 'BoardRepo API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: BoardRepo API
  slug: boardrepo-com-api
artifact_total: 7
common:
- group: design
  href: https://artifacts.apis.io/boardrepo-com/rules/boardrepo-com-rules.yml
  title: ''
  type: Spectral
  url: rules/boardrepo-com-rules.yml
- group: design
  href: https://artifacts.apis.io/boardrepo-com/vocabulary/boardrepo-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/boardrepo-com-vocabulary.yml
- group: auth
  title: ''
  type: Compliance
  url: https://boardrepo.com/security
- group: auth
  href: https://artifacts.apis.io/boardrepo-com/authentication/boardrepo-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/boardrepo-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/boardrepo-com/conformance/boardrepo-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/boardrepo-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/boardrepo-com/llms/boardrepo-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/boardrepo-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/boardrepo-com/well-known/boardrepo-com-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/boardrepo-com-status-security.txt
- group: auth
  href: https://artifacts.apis.io/boardrepo-com/well-known/boardrepo-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/boardrepo-com-security.txt
- group: agent
  href: https://artifacts.apis.io/boardrepo-com/well-known/boardrepo-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/boardrepo-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/boardrepo-com/hosts/boardrepo-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boardrepo-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/boardrepo-com/vendors/boardrepo-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/boardrepo-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://boardrepo.com/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.boardrepo.com/
- group: auth
  title: ''
  type: Security
  url: https://boardrepo.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://boardrepo.com/privacy
- group: start
  title: ''
  type: Login
  url: https://boardrepo.com/signin
- group: docs
  title: ''
  type: Documentation
  url: https://boardrepo.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://boardrepo.com/connect
- group: auth
  href: https://artifacts.apis.io/boardrepo-com/security/boardrepo-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/boardrepo-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/boardrepo-com/security/boardrepo-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/boardrepo-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/boardrepo-com/security/boardrepo-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boardrepo-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://boardrepo.com/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://boardrepo.com/mcp
  - status: 200
    url: https://boardrepo.com/
  reason: partner-login
  state: gated
created: '2026-11-02'
description: BoardRepo is a platform for sharing and reviewing KiCad hardware projects. Users can upload schematics and PCB designs, inspect them directly in the browser, and collaborate with teams. The service offers free core features, integrates with KiCad, and provides AI‑assistant support for design inspection.
image: https://boardrepo.com/opengraph-image.jpg
layout: provider
modified: '2026-11-02'
name: BoardRepo
nav: Providers
network: true
overview: 'BoardRepo is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Hardware, KiCad, Collaboration, Open Source, and Design.


  The BoardRepo catalog on APIs.io includes 1 Spectral governance ruleset.


  BoardRepo''s developer surface includes authentication, documentation, getting-started guide, and 19 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 61
  extends:
  - spectral:oas
  name: BoardRepo API Rules
  rule_count: 20
  severity_counts:
    error: 18
    hint: 0
    info: 1
    warn: 1
  slug: boardrepo-com-rules
score:
  band: emerging
  composite: 24.8
  coverage:
    artifact_dirs: 14
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 28.9
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 22.6
    discoverability: 57.1
    operational_transparency: 13.2
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Boardrepo Com Authentication
  slug: boardrepo-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Boardrepo Com Domain Security
  slug: boardrepo-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Boardrepo Com Vulnerability Disclosure
  slug: boardrepo-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Boardrepo Com Trust Center
  slug: boardrepo-com-trust-center
  summary_line: SOC 2, ISO 27001
slug: boardrepo-com
tags:
- Hardware
- KiCad
- Collaboration
- Open Source
- Design
website: https://boardrepo.com/
---
