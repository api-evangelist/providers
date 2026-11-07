---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Bidprowl Com Agentic Access
  operation_count: 12
  slug: bidprowl-com-agentic-access
  summary_line: 12 operations · 2 acting
api_count: 1
apis:
- baseURL: https://bidprowl.com
  baseurl_source: declared
  description: The Comps API from BidProwl — 2 operation(s) for comps.
  name: BidProwl Comps API
  slug: bidprowl-com-comps-api
- baseURL: https://bidprowl.com
  baseurl_source: declared
  description: The Export API from BidProwl — 1 operation(s) for export.
  name: BidProwl Export API
  slug: bidprowl-com-export-api
- baseURL: https://bidprowl.com
  baseurl_source: declared
  description: The Flip Score API from BidProwl — 1 operation(s) for flip score.
  name: BidProwl Flip Score API
  slug: bidprowl-com-flip-score-api
- baseURL: https://bidprowl.com
  baseurl_source: declared
  description: The Listings API from BidProwl — 2 operation(s) for listings.
  name: BidProwl Listings API
  slug: bidprowl-com-listings-api
- baseURL: https://bidprowl.com
  baseurl_source: declared
  description: The Sold API from BidProwl — 1 operation(s) for sold.
  name: BidProwl Sold API
  slug: bidprowl-com-sold-api
- baseURL: https://bidprowl.com
  baseurl_source: declared
  description: The Sources API from BidProwl — 1 operation(s) for sources.
  name: BidProwl Sources API
  slug: bidprowl-com-sources-api
- baseURL: https://bidprowl.com
  baseurl_source: declared
  description: The Usage API from BidProwl — 1 operation(s) for usage.
  name: BidProwl Usage API
  slug: bidprowl-com-usage-api
- baseURL: https://bidprowl.com
  baseurl_source: declared
  description: The Webhooks API from BidProwl — 2 operation(s) for webhooks.
  name: BidProwl Webhooks API
  slug: bidprowl-com-webhooks-api
artifact_total: 23
asyncapis:
- description: ''
  name: Bidprowl Com Webhooks
  slug: bidprowl-com-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/bidprowl-com/agentic-access/bidprowl-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bidprowl-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/bidprowl-com/plans/bidprowl-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bidprowl-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/bidprowl-com/rules/bidprowl-com-rules.yml
  title: ''
  type: Spectral
  url: rules/bidprowl-com-rules.yml
- group: design
  href: https://artifacts.apis.io/bidprowl-com/json-ld/bidprowl-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bidprowl-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/bidprowl-com/vocabulary/bidprowl-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bidprowl-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/bidprowl-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/bidprowl-com/asyncapi/bidprowl-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/bidprowl-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/bidprowl-com/data-model/bidprowl-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bidprowl-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/bidprowl-com/errors/bidprowl-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bidprowl-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bidprowl-com/conformance/bidprowl-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bidprowl-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bidprowl-com/llms/bidprowl-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bidprowl-com-llms.txt
- group: other
  href: https://artifacts.apis.io/bidprowl-com/hosts/bidprowl-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bidprowl-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bidprowl-com/vendors/bidprowl-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bidprowl-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bidprowl.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bidprowl.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://bidprowl.com/pricing
- group: start
  title: ''
  type: Login
  url: https://bidprowl.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://bidprowl.com/guides
- group: docs
  title: ''
  type: APIReference
  url: https://bidprowl.com/developers
- group: auth
  href: https://artifacts.apis.io/bidprowl-com/authentication/bidprowl-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bidprowl-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/bidprowl-com/security/bidprowl-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bidprowl-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bidprowl.com/
created: '2026-11-02'
description: BidProwl provides a searchable platform for government auction lots across the United States, aggregating data from over 27 sites including vehicles, equipment, and real estate. Users can browse, filter, and receive alerts for live auction items, view flip scores and sold prices, and access free tools to help evaluate and win government surplus auctions.
image: https://bidprowl.com/api/og?v=2&title=Government+Surplus+Auctions+in+One+Place&subtitle=Search+GSA,+GovDeals,+GovPlanet+and+more
json_schemas:
- name: Listing
  property_count: 26
  slug: bidprowl-com-listing
- name: SoldLot
  property_count: 11
  slug: bidprowl-com-sold-lot
- name: SoldStats
  property_count: 6
  slug: bidprowl-com-sold-stats
- name: Usage
  property_count: 10
  slug: bidprowl-com-usage
- name: WebhookFilters
  property_count: 8
  slug: bidprowl-com-webhook-filters
- name: Webhook
  property_count: 13
  slug: bidprowl-com-webhook
jsonld:
- class_count: 7
  name: Bidprowl Com Context
  property_count: 63
  slug: bidprowl-com-context
layout: provider
modified: '2026-11-02'
name: BidProwl
nav: Providers
network: true
overview: 'BidProwl publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Comps API, Export API, Flip Score API, and 5 more. Tagged areas include Government, Auctions, Marketplace, Data, and Search.


  The BidProwl catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  BidProwl''s developer surface includes pricing, documentation, API reference, authentication, and 18 more developer resources.'
plans:
- name: Bidprowl Com Plans Pricing
  plan_count: 4
  slug: bidprowl-com-plans-pricing
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: BidProwl API Rules
  rule_count: 53
  severity_counts:
    error: 51
    hint: 0
    info: 1
    warn: 1
  slug: bidprowl-com-rules
score:
  band: developing
  composite: 45.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 70.4
    developer_ergonomics: 26.7
    discoverability: 66.1
    operational_transparency: 7.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bidprowl Com Authentication
  slug: bidprowl-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bidprowl Com Domain Security
  slug: bidprowl-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: 'null'
  slug: bidprowl-com-null
- name: bidprowl-com
  slug: bidprowl-com
slug: bidprowl-com
tags:
- Government
- Auctions
- Marketplace
- Data
- Search
website: https://bidprowl.com/
---
