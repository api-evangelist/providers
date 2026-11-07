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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
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
  score: 5.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Buyvignettepass Com Agentic Access
  operation_count: 3
  slug: buyvignettepass-com-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- description: API for checking required motorway vignettes and pricing across European countries.
  name: Buy Vignette Pass API
  slug: buy-vignette-pass-api
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/buyvignettepass-com/agentic-access/buyvignettepass-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/buyvignettepass-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/buyvignettepass-com/rules/buyvignettepass-com-rules.yml
  title: ''
  type: Spectral
  url: rules/buyvignettepass-com-rules.yml
- group: design
  href: https://artifacts.apis.io/buyvignettepass-com/errors/buyvignettepass-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/buyvignettepass-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/buyvignettepass-com/conformance/buyvignettepass-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/buyvignettepass-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/buyvignettepass-com/llms/buyvignettepass-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/buyvignettepass-com-llms.txt
- group: other
  href: https://artifacts.apis.io/buyvignettepass-com/hosts/buyvignettepass-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/buyvignettepass-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/buyvignettepass-com/vendors/buyvignettepass-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/buyvignettepass-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/buyvignettepass-com/security/buyvignettepass-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/buyvignettepass-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://buyvignettepass.com/
- group: docs
  title: ''
  type: Documentation
  url: https://buyvignettepass.com/en/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://buyvignettepass.com/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://buyvignettepass.com/privacy.html
created: '2026-11-03'
description: Buy Vignette Pass offers an online service for purchasing vignette (toll) passes across several European countries including Austria, Czechia, Slovakia, Hungary, Slovenia, Romania, Bulgaria, and Switzerland. The platform provides route checking, price comparison, and a streamlined checkout process, enabling drivers to obtain the necessary toll permits before traveling. It integrates with mapping services and supports multiple languages, aiming to simplify cross‑border travel for both residents and tourists.
image: https://buyvignettepass.com/og-image.png
layout: provider
modified: '2026-11-03'
name: Buy Vignette Pass
nav: Providers
network: true
overview: 'Buy Vignette Pass is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Toll, Europe, Travel, and Payments.


  The Buy Vignette Pass catalog on APIs.io includes 1 Spectral governance ruleset.


  Buy Vignette Pass'' developer surface includes documentation and 11 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 73
  extends:
  - spectral:oas
  name: Buy Vignette Pass API Rules
  rule_count: 32
  severity_counts:
    error: 30
    hint: 0
    info: 1
    warn: 1
  slug: buyvignettepass-com-rules
score:
  band: minimal
  composite: 10.9
  coverage:
    artifact_dirs: 13
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 13.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Buyvignettepass Com Domain Security
  slug: buyvignettepass-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: buyvignettepass-com
tags:
- Company
- Toll
- Europe
- Travel
- Payments
website: https://buyvignettepass.com/
---
