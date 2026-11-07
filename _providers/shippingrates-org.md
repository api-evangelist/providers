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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Public API for freight rate calculations, shipping intelligence, and rate comparisons.
  name: ShippingRates API
  slug: shippingrates-api
- baseURL: https://api.shippingrates.org
  baseurl_source: declared
  description: 'shippingrates-org API as documented publicly: 7 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: shippingrates-org API
  slug: shippingrates-org-api
artifact_total: 4
common:
- group: design
  href: https://artifacts.apis.io/shippingrates-org/rules/shippingrates-org-rules.yml
  title: ''
  type: Spectral
  url: rules/shippingrates-org-rules.yml
- group: design
  href: https://artifacts.apis.io/shippingrates-org/vocabulary/shippingrates-org-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/shippingrates-org-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/shippingrates-org/conformance/shippingrates-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/shippingrates-org-conformance.yml
- group: agent
  href: https://artifacts.apis.io/shippingrates-org/llms/shippingrates-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/shippingrates-org-llms.txt
- group: other
  href: https://artifacts.apis.io/shippingrates-org/hosts/shippingrates-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/shippingrates-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/shippingrates-org/vendors/shippingrates-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/shippingrates-org-vendors.yml
- group: auth
  href: https://artifacts.apis.io/shippingrates-org/security/shippingrates-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/shippingrates-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://shippingrates.org/
- group: docs
  title: ''
  type: Documentation
  url: https://shippingrates.org/docs
- group: docs
  title: ''
  type: APIReference
  url: https://shippingrates.org/docs/interactive
- group: company
  title: ''
  type: Blog
  url: https://shippingrates.org/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://shippingrates.org/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://shippingrates.org/privacy
coverage:
  checked: '2026-10-31'
  detail: Docs are public HTML but no OpenAPI, AsyncAPI, GraphQL, or other machine-readable spec was found.
  evidence:
  - status: 410
    url: https://api.shippingrates.org/openapi.json
  - status: 404
    url: https://shippingrates.org/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: ShippingRates provides a freight rate API, quote builder, and shipping intelligence platform. It offers tools for calculating shipping costs, historical carrier rates, detention, local charges, and demurrage. The service includes a public API for freight data, rate comparisons, and landed cost calculations, targeting logistics agents and developers seeking shipping rate automation.
image: https://shippingrates.org/assets/showcase-social.svg
layout: provider
modified: '2026-10-31'
name: shippingrates-org
nav: Providers
network: true
overview: 'shippingrates-org is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Shipping, Freight, Logistics, and Rates.


  The shippingrates-org catalog on APIs.io includes 1 Spectral governance ruleset.


  shippingrates-org''s developer surface includes documentation, API reference, engineering blog, and 10 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: shippingrates-org API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: shippingrates-org-rules
score:
  band: emerging
  composite: 14.1
  coverage:
    artifact_dirs: 14
    catalog_earned: 32.8
    catalog_earned_first_party: 0.0
    catalog_gap: 82.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.5
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 10.7
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 19.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/shippingrates-org/shippingrates-org-2026-11-03T143122.png
security:
- kind: domain-security
  name: Shippingrates Org Domain Security
  slug: shippingrates-org-domain-security
  summary_line: TLSv1.3 · DMARC
slug: shippingrates-org
tags:
- Shipping
- Freight
- Logistics
- Rates
website: https://shippingrates.org/
---
