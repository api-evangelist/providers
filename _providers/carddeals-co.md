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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Carddeals Co Agentic Access
  operation_count: 3
  slug: carddeals-co-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- baseURL: https://catalog.carddeals.co
  baseurl_source: declared
  description: The Gift-card deals API from CardDeals — 3 operation(s) for gift-card deals.
  name: CardDeals Gift-card deals API
  slug: carddeals-co-gift-card-deals-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/carddeals-co/agentic-access/carddeals-co-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/carddeals-co-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/carddeals-co/rules/carddeals-co-rules.yml
  title: ''
  type: Spectral
  url: rules/carddeals-co-rules.yml
- group: design
  href: https://artifacts.apis.io/carddeals-co/json-ld/carddeals-co-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/carddeals-co-context.jsonld
- group: design
  href: https://artifacts.apis.io/carddeals-co/vocabulary/carddeals-co-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/carddeals-co-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/carddeals-co/data-model/carddeals-co-data-model.yml
  title: ''
  type: DataModel
  url: data-model/carddeals-co-data-model.yml
- group: auth
  href: https://artifacts.apis.io/carddeals-co/security/carddeals-co-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/carddeals-co-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/carddeals-co/errors/carddeals-co-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/carddeals-co-problem-types.yml
- group: design
  href: https://artifacts.apis.io/carddeals-co/conformance/carddeals-co-conformance.yml
  title: ''
  type: Conformance
  url: conformance/carddeals-co-conformance.yml
- group: agent
  href: https://artifacts.apis.io/carddeals-co/llms/carddeals-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/carddeals-co-llms.txt
- group: auth
  href: https://artifacts.apis.io/carddeals-co/well-known/carddeals-co-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/carddeals-co-security.txt
- group: agent
  href: https://artifacts.apis.io/carddeals-co/well-known/carddeals-co-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/carddeals-co-well-known.yml
- group: other
  href: https://artifacts.apis.io/carddeals-co/hosts/carddeals-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carddeals-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/carddeals-co/vendors/carddeals-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/carddeals-co-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://carddeals.co/login
- group: auth
  href: https://artifacts.apis.io/carddeals-co/security/carddeals-co-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/carddeals-co-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/carddeals-co/security/carddeals-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carddeals-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://carddeals.co/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://carddeals.co/mcp
- group: docs
  title: ''
  type: Documentation
  url: https://carddeals.co/mcp
- group: docs
  title: ''
  type: APIReference
  url: https://catalog.carddeals.co/openapi.json
- group: company
  title: ''
  type: Blog
  url: https://carddeals.co/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://carddeals.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://carddeals.co/privacy
created: '2026-11-03'
description: CardDeals is a gift‑card comparison platform that aggregates discounted gift‑card offers from verified resale providers. It helps shoppers save up to 25 % on purchases across categories such as groceries, electronics, travel, and more. By presenting real‑time price data and deals from over 700 top brands, CardDeals enables users to find the best value and purchase gift cards instantly.
image: https://carddeals.co/og.png
jsonld:
- class_count: 6
  name: Carddeals Co Context
  property_count: 37
  slug: carddeals-co-context
layout: provider
modified: '2026-11-03'
name: CardDeals
nav: Providers
network: true
overview: 'CardDeals publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Gift-card deals API. Tagged areas include Company, Gift Cards, Comparison, Discounts, and E-Commerce.


  The CardDeals catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CardDeals'' developer surface includes documentation, API reference, engineering blog, and 20 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: CardDeals API Rules
  rule_count: 48
  severity_counts:
    error: 46
    hint: 0
    info: 1
    warn: 1
  slug: carddeals-co-rules
score:
  band: thin
  composite: 29.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 48.8
    catalog_earned_first_party: 0.0
    catalog_gap: 66.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 52.8
    developer_ergonomics: 14.3
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Carddeals Co Domain Security
  slug: carddeals-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Carddeals Co Vulnerability Disclosure
  slug: carddeals-co-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: carddeals-co
tags:
- Company
- Gift Cards
- Comparison
- Discounts
- E-Commerce
- Real-Time
website: https://carddeals.co/
---
