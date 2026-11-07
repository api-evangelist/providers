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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Buyrecord App Agentic Access
  operation_count: 9
  slug: buyrecord-app-agentic-access
  summary_line: 9 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.buyrecord.app
  baseurl_source: declared
  description: The Keys API from BuyRecord — 1 operation(s) for keys.
  name: BuyRecord Keys API
  slug: buyrecord-app-keys-api
- baseURL: https://api.buyrecord.app
  baseurl_source: declared
  description: The Merchants API from BuyRecord — 1 operation(s) for merchants.
  name: BuyRecord Merchants API
  slug: buyrecord-app-merchants-api
- baseURL: https://api.buyrecord.app
  baseurl_source: declared
  description: The Outcomes API from BuyRecord — 1 operation(s) for outcomes.
  name: BuyRecord Outcomes API
  slug: buyrecord-app-outcomes-api
- baseURL: https://api.buyrecord.app
  baseurl_source: declared
  description: The Products API from BuyRecord — 3 operation(s) for products.
  name: BuyRecord Products API
  slug: buyrecord-app-products-api
- baseURL: https://api.buyrecord.app
  baseurl_source: declared
  description: The Stays API from BuyRecord — 3 operation(s) for stays.
  name: BuyRecord Stays API
  slug: buyrecord-app-stays-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/buyrecord-app/agentic-access/buyrecord-app-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/buyrecord-app-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/buyrecord-app/rules/buyrecord-app-rules.yml
  title: ''
  type: Spectral
  url: rules/buyrecord-app-rules.yml
- group: design
  href: https://artifacts.apis.io/buyrecord-app/json-ld/buyrecord-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/buyrecord-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/buyrecord-app/vocabulary/buyrecord-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/buyrecord-app-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/buyrecord-app/data-model/buyrecord-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/buyrecord-app-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://buyrecord.app/security.html
- group: design
  href: https://artifacts.apis.io/buyrecord-app/errors/buyrecord-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/buyrecord-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/buyrecord-app/conformance/buyrecord-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/buyrecord-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/buyrecord-app/llms/buyrecord-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/buyrecord-app-llms.txt
- group: auth
  href: https://artifacts.apis.io/buyrecord-app/well-known/buyrecord-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/buyrecord-app-security.txt
- group: auth
  href: https://artifacts.apis.io/buyrecord-app/well-known/buyrecord-app-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/buyrecord-app-api-security.txt
- group: agent
  href: https://artifacts.apis.io/buyrecord-app/well-known/buyrecord-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/buyrecord-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/buyrecord-app/hosts/buyrecord-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/buyrecord-app-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://buyrecord.app/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://buyrecord.app/privacy.html
- group: auth
  href: https://artifacts.apis.io/buyrecord-app/authentication/buyrecord-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/buyrecord-app-authentication.yml
- group: auth
  href: https://artifacts.apis.io/buyrecord-app/security/buyrecord-app-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/buyrecord-app-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/buyrecord-app/security/buyrecord-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/buyrecord-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://buyrecord.app/
- group: docs
  title: ''
  type: Documentation
  url: https://api.buyrecord.app/docs
created: '2026-11-03'
description: BuyRecord provides AI shopping agents with verified purchase outcome data, indicating whether a product was kept or returned. The service aggregates real purchase records tied to proof of purchase, offering a REST API and MCP server for agents to read before buying and report back after. This enables transparent, data‑driven decisions for e‑commerce and AI‑driven recommendation systems, improving trust and reducing returns.
image: https://buyrecord.app/img/og.png
json_schemas:
- name: IssuedKey
  property_count: 4
  slug: buyrecord-app-issued-key
- name: MerchantProfile
  property_count: 10
  slug: buyrecord-app-merchant-profile
- name: OutcomeSubmission
  property_count: 5
  slug: buyrecord-app-outcome-submission
- name: ProductDetails
  property_count: 21
  slug: buyrecord-app-product-details
- name: StayOutcomes
  property_count: 8
  slug: buyrecord-app-stay-outcomes
- name: StaySubmission
  property_count: 7
  slug: buyrecord-app-stay-submission
jsonld:
- class_count: 31
  name: Buyrecord App Context
  property_count: 98
  slug: buyrecord-app-context
layout: provider
modified: '2026-11-03'
name: BuyRecord
nav: Providers
network: true
overview: 'BuyRecord publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Keys API, Merchants API, Outcomes API, and 2 more. Tagged areas include Artificial Intelligence, E-Commerce, Data, Shopping, and Analytics.


  The BuyRecord catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BuyRecord''s developer surface includes authentication, documentation, and 18 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 88
  extends:
  - spectral:oas
  name: BuyRecord API Rules
  rule_count: 47
  severity_counts:
    error: 45
    hint: 0
    info: 1
    warn: 1
  slug: buyrecord-app-rules
score:
  band: thin
  composite: 31.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 57.7
    developer_ergonomics: 16.7
    discoverability: 66.1
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
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
- kind: authentication
  name: Buyrecord App Authentication
  slug: buyrecord-app-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Buyrecord App Domain Security
  slug: buyrecord-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Buyrecord App Vulnerability Disclosure
  slug: buyrecord-app-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: buyrecord-app
tags:
- Artificial Intelligence
- E-Commerce
- Data
- Shopping
- Analytics
website: https://buyrecord.app/
---
