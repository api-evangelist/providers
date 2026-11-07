---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 5.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Aeroz Io Agentic Access
  operation_count: 3
  slug: aeroz-io-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 1
apis:
- description: Physical-to-digital authentication platform API.
  name: Aeroz Platform API
  slug: aeroz-platform-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/aeroz-io/agentic-access/aeroz-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aeroz-io-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/aeroz-io/rules/aeroz-io-rules.yml
  title: ''
  type: Spectral
  url: rules/aeroz-io-rules.yml
- group: auth
  href: https://artifacts.apis.io/aeroz-io/security/aeroz-io-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/aeroz-io-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/aeroz-io/conformance/aeroz-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aeroz-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aeroz-io/llms/aeroz-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aeroz-io-llms.txt
- group: other
  href: https://artifacts.apis.io/aeroz-io/a2a/aeroz-io-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/aeroz-io-a2a.yml
- group: auth
  href: https://artifacts.apis.io/aeroz-io/well-known/aeroz-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aeroz-io-security.txt
- group: auth
  href: https://artifacts.apis.io/aeroz-io/well-known/aeroz-io-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aeroz-io-app-security.txt
- group: auth
  href: https://artifacts.apis.io/aeroz-io/well-known/aeroz-io-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aeroz-io-api-security.txt
- group: agent
  href: https://artifacts.apis.io/aeroz-io/well-known/aeroz-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aeroz-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/aeroz-io/hosts/aeroz-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aeroz-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/aeroz-io/vendors/aeroz-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aeroz-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aeroz.io/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aeroz.io/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://aeroz.io/blog
- group: auth
  href: https://artifacts.apis.io/aeroz-io/authentication/aeroz-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aeroz-io-authentication.yml
- group: auth
  href: https://artifacts.apis.io/aeroz-io/security/aeroz-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aeroz-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/aeroz-io/security/aeroz-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aeroz-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aeroz.io/
- group: docs
  title: ''
  type: Documentation
  url: https://api.aeroz.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.aeroz.io/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://aeroz.io/platform
- group: operate
  title: ''
  type: Support
  url: https://aeroz.io/contact?intent=call
created: '2026-10-31'
description: Aeroz provides supply chain traceability and product authentication solutions for regulated goods. Their platform uses NFC/UHF chips and GS1 2D codes to give each unit a unique identity, recording custody events via GS1 EPCIS 2.0. It supports compliance with DSCSA, EU Digital Product Passport, battery regulations, and other global standards, offering a secure, end‑to‑end digital product passport and connected packaging.
image: https://aeroz.io/assets/img/wh/chip-macro.webp
layout: provider
modified: '2026-10-31'
name: Aeroz
nav: Providers
network: true
overview: 'Aeroz is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Supply Chain, Traceability, Authentication, and Compliance.


  The Aeroz catalog on APIs.io includes 1 Spectral governance ruleset.


  Aeroz''s developer surface includes engineering blog, authentication, documentation, API reference, getting-started guide, support, and 17 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 48
  extends:
  - spectral:oas
  name: Aeroz API Rules
  rule_count: 7
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 1
  slug: aeroz-io-rules
score:
  band: emerging
  composite: 19.9
  coverage:
    artifact_dirs: 13
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.3
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 29.8
    discoverability: 66.1
    operational_transparency: 10.5
  previous_composite: 26.2
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aeroz Io Authentication
  slug: aeroz-io-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Aeroz Io Domain Security
  slug: aeroz-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Aeroz Io Vulnerability Disclosure
  slug: aeroz-io-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: aeroz-io
tags:
- Company
- Supply Chain
- Traceability
- Authentication
- Compliance
- NFC
website: https://aeroz.io/
---
