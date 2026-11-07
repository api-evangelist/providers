---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
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
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 23.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Compute Comparison Agentic Access
  operation_count: 6
  slug: compute-comparison-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- description: Real-time LLM inference pricing across 33+ providers and 274+ models.
  name: LLM Pricing API
  slug: llm-pricing-api
- baseURL: https://computecomparison.com/api/v1
  baseurl_source: declared
  description: The Prices API from Compute Comparison — 4 operation(s) for prices.
  name: Compute Comparison Prices API
  slug: compute-comparison-prices-api
- baseURL: https://computecomparison.com/api/v1
  baseurl_source: declared
  description: The Status API from Compute Comparison — 1 operation(s) for status.
  name: Compute Comparison Status API
  slug: compute-comparison-status-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/compute-comparison/agentic-access/compute-comparison-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/compute-comparison-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/compute-comparison/rate-limits/compute-comparison-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/compute-comparison-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/compute-comparison/rules/compute-comparison-rules.yml
  title: ''
  type: Spectral
  url: rules/compute-comparison-rules.yml
- group: design
  href: https://artifacts.apis.io/compute-comparison/json-ld/compute-comparison-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/compute-comparison-context.jsonld
- group: design
  href: https://artifacts.apis.io/compute-comparison/vocabulary/compute-comparison-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/compute-comparison-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/compute-comparison/data-model/compute-comparison-data-model.yml
  title: ''
  type: DataModel
  url: data-model/compute-comparison-data-model.yml
- group: design
  href: https://artifacts.apis.io/compute-comparison/conventions/compute-comparison-conventions.yml
  title: ''
  type: Conventions
  url: conventions/compute-comparison-conventions.yml
- group: auth
  href: https://artifacts.apis.io/compute-comparison/authentication/compute-comparison-authentication.yml
  title: ''
  type: Authentication
  url: authentication/compute-comparison-authentication.yml
- group: design
  href: https://artifacts.apis.io/compute-comparison/conformance/compute-comparison-conformance.yml
  title: ''
  type: Conformance
  url: conformance/compute-comparison-conformance.yml
- group: agent
  href: https://artifacts.apis.io/compute-comparison/llms/compute-comparison-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/compute-comparison-llms.txt
- group: agent
  href: https://artifacts.apis.io/compute-comparison/well-known/compute-comparison-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/compute-comparison-well-known.yml
- group: other
  href: https://artifacts.apis.io/compute-comparison/hosts/compute-comparison-hosts.yml
  title: ''
  type: Hosts
  url: hosts/compute-comparison-hosts.yml
- group: other
  href: https://artifacts.apis.io/compute-comparison/vendors/compute-comparison-vendors.yml
  title: ''
  type: Vendors
  url: vendors/compute-comparison-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://computecomparison.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://computecomparison.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://computecomparison.com/press
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/computecomparison
- group: auth
  href: https://artifacts.apis.io/compute-comparison/security/compute-comparison-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/compute-comparison-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://computecomparison.com
- group: docs
  title: ''
  type: Documentation
  url: https://computecomparison.com/api-docs
- group: commercial
  title: ''
  type: Pricing
  url: https://computecomparison.com/tco-calculator
created: '2026-10-30'
description: Compute Comparison provides real-time price comparison tools for GPU cloud compute and LLM inference services, aggregating live hourly pricing across dozens of providers, offering calculators, historical charts, and decision‑support features to help developers and businesses choose optimal compute resources.
image: https://computecomparison.com/airo-assets/images/og-image
json_schemas:
- name: PriceMeta
  property_count: 5
  slug: compute-comparison-price-meta
- name: ProviderPriceResult
  property_count: 8
  slug: compute-comparison-provider-price-result
jsonld:
- class_count: 2
  name: Compute Comparison Context
  property_count: 13
  slug: compute-comparison-context
layout: provider
modified: '2026-10-30'
name: Compute Comparison
nav: Providers
network: true
overview: 'Compute Comparison publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including Prices API, Status API, and 1 more. Tagged areas include Company, GPU, LLM, Cloud, and Pricing.


  The Compute Comparison catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Compute Comparison''s developer surface includes authentication, documentation, pricing, and 18 more developer resources.'
random_paper: 21
rate_limits:
- limit_count: 1
  name: Compute Comparison Rate Limits
  slug: compute-comparison-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Compute Comparison API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: compute-comparison-rules
scopes:
- name: Compute Comparison Scopes
  scope_count: 0
  slug: compute-comparison-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 36.0
  coverage:
    artifact_dirs: 27
    catalog_earned: 67.8
    catalog_earned_first_party: 8.0
    catalog_gap: 47.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.1
  facets:
    access_clarity: 15.8
    contract_governance: 22.0
    contract_quality: 60.5
    developer_ergonomics: 16.7
    discoverability: 67.0
    operational_transparency: 23.7
  previous_composite: 41.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/compute-comparison/compute-comparison-2026-11-03T125027.png
security:
- kind: authentication
  name: Compute Comparison Authentication
  slug: compute-comparison-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Compute Comparison Domain Security
  slug: compute-comparison-domain-security
  summary_line: TLSv1.3 · DMARC
slug: compute-comparison
tags:
- Company
- GPU
- LLM
- Cloud
- Pricing
- Comparison
website: https://computecomparison.com
---
