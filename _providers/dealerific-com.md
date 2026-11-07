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
    agent_card: conformant
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
  score: 8.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Dealerific Com Agentic Access
  operation_count: 2
  slug: dealerific-com-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- description: Public read-only endpoints for retrieving curated consumer deals and coupon codes.
  name: Dealerific Public API
  slug: dealerific-public-api
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/dealerific-com/agentic-access/dealerific-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dealerific-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/dealerific-com/rules/dealerific-com-rules.yml
  title: ''
  type: Spectral
  url: rules/dealerific-com-rules.yml
- group: design
  href: https://artifacts.apis.io/dealerific-com/errors/dealerific-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dealerific-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dealerific-com/conformance/dealerific-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dealerific-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dealerific-com/llms/dealerific-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dealerific-com-llms.txt
- group: other
  href: https://artifacts.apis.io/dealerific-com/a2a/dealerific-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/dealerific-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/dealerific-com/well-known/dealerific-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dealerific-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dealerific-com/hosts/dealerific-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dealerific-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dealerific-com/vendors/dealerific-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dealerific-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dealerific.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dealerific.com/privacy
- group: start
  title: ''
  type: Login
  url: https://dealerific.com/signin
- group: docs
  title: ''
  type: Documentation
  url: https://dealerific.com/guides
- group: start
  title: ''
  type: GettingStarted
  url: https://www.dealerific.com/c/keyboards-setup
- group: auth
  href: https://artifacts.apis.io/dealerific-com/security/dealerific-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dealerific-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dealerific.com/
created: '2026-11-05'
description: 'dealerific-com is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://www.dealerific.com/og/default.png
layout: provider
modified: '2026-11-05'
name: dealerific-com
nav: Providers
network: true
overview: 'dealerific-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Deals, Coupons, Price Drops, Daily Email, and Shopping.


  The dealerific-com catalog on APIs.io includes 1 Spectral governance ruleset.


  dealerific-com''s developer surface includes documentation, getting-started guide, and 14 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 66
  extends:
  - spectral:oas
  name: dealerific-com API Rules
  rule_count: 25
  severity_counts:
    error: 23
    hint: 0
    info: 1
    warn: 1
  slug: dealerific-com-rules
score:
  band: emerging
  composite: 21.2
  coverage:
    artifact_dirs: 14
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 31.8
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dealerific Com Domain Security
  slug: dealerific-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: dealerific-com
tags:
- Deals
- Coupons
- Price Drops
- Daily Email
- Shopping
- Discounts
- Retail
website: https://dealerific.com/
---
