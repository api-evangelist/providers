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
api_count: 1
apis:
- description: MCP (Microservice Control Protocol) server for Duck Tax providing API access.
  name: Duck Tax MCP
  slug: duck-tax-mcp
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/ducktax-com/security/ducktax-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/ducktax-com-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/ducktax-com/conformance/ducktax-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ducktax-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ducktax-com/llms/ducktax-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ducktax-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/ducktax-com/well-known/ducktax-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ducktax-com-security.txt
- group: agent
  href: https://artifacts.apis.io/ducktax-com/well-known/ducktax-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ducktax-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/ducktax-com/hosts/ducktax-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ducktax-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/ducktax-com/vendors/ducktax-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ducktax-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/ducktax-com/security/ducktax-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ducktax-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ducktax-com/security/ducktax-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ducktax-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ducktax.com/
- group: docs
  title: ''
  type: Documentation
  url: https://ducktax.com/docs/mcp
- group: docs
  title: ''
  type: APIReference
  url: https://ducktax.com/docs/mcp
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ducktax.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ducktax.com/tos
- group: commercial
  title: ''
  type: Pricing
  url: https://ducktax.com/
coverage:
  checked: '2026-11-06'
  detail: MCP documentation is served as a JavaScript-rendered HTML page with no machine-readable spec.
  evidence:
  - status: 200
    url: https://ducktax.com/docs/mcp
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-06'
description: Duck Tax provides a free online checker for UK micro-entity company accounts. Users can input their financial figures to generate an FRS 105 balance sheet, identify errors, and ensure compliance before filing. The service is offered by Spark Games Ltd and aims to simplify small business accounting with a zero‑cost tool.
image: https://ducktax.com/opengraph-image?48421b6213f07c99
layout: provider
modified: '2026-11-06'
name: Duck Tax
nav: Providers
network: true
overview: 'Duck Tax is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Accounting, United Kingdom, and Micro-entity.


  Duck Tax''s developer surface includes documentation, API reference, pricing, and 12 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 19.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ducktax Com Domain Security
  slug: ducktax-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ducktax Com Vulnerability Disclosure
  slug: ducktax-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ducktax-com
tags:
- Finance
- Accounting
- United Kingdom
- Micro-entity
website: https://ducktax.com/
---
