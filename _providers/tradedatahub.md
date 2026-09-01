---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.2
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Free, unauthenticated REST discovery API for contractor/trade-business datasets, with paid CSV retrieval via x402 (testnet-only). Includes coverage stats, inventory discovery, dataset listings, pricin
  name: TradeDataHub Public API
  slug: tradedatahub-public-api
artifact_total: 15
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tradedatahub-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.tradedatahub.net/developers/
- group: operate
  title: ''
  type: Support
  url: https://www.tradedatahub.net/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tradedatahub.net/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tradedatahub.net/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tradedatahub.net/faq/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tradedatahub-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/tradedatahub-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tradedatahub-rate-limits.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tradedatahub-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tradedatahub-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tradedatahub-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tradedatahub-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tradedatahub-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tradedatahub-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/tradedatahub-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/tradedatahub-packages.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/tradedatahub-openapi-overlay.yaml
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
created: '2026-08-29'
description: A marketplace API for downloadable CSV datasets of verified U.S. contractor and trade-business listings. Offers a free, unauthenticated REST discovery API under /api/v1/ (coverage, states, trades, cities, datasets, previews, pricing) plus paid dataset retrieval via x402 (testnet-only, Base Sepolia). Backed by an OpenAPI 3.1.0 contract and llms.txt/llms-full.txt agent guides.
examples:
- key_count: 3
  name: Tradedatahub Cities Texas Response
  slug: tradedatahub-cities-texas-response
- key_count: 9
  name: Tradedatahub Coverage Response
  slug: tradedatahub-coverage-response
- key_count: 12
  name: Tradedatahub Dataset Detail Response
  slug: tradedatahub-dataset-detail-response
- key_count: 3
  name: Tradedatahub Datasets Response
  slug: tradedatahub-datasets-response
- key_count: 2
  name: Tradedatahub Error 404 Response
  slug: tradedatahub-error-404-response
- key_count: 7
  name: Tradedatahub Preview Response
  slug: tradedatahub-preview-response
- key_count: 12
  name: Tradedatahub Price Response
  slug: tradedatahub-price-response
- key_count: 2
  name: Tradedatahub States Response
  slug: tradedatahub-states-response
- key_count: 2
  name: Tradedatahub Teaser Response
  slug: tradedatahub-teaser-response
- key_count: 2
  name: Tradedatahub Trades Response
  slug: tradedatahub-trades-response
layout: provider
modified: '2026-08-29'
name: TradeDataHub Public API
nav: Providers
network: true
overview: 'TradeDataHub Public API publishes 1 API on the [APIs.io](https://apis.io/) network: TradeDataHub Public API. Tagged areas include contractor data, B2B Data, Business Listings, Datasets, and CSV.


  TradeDataHub Public API''s developer surface includes support, pricing, authentication, sandbox, code examples, and 15 more developer resources.'
plans:
- name: Tradedatahub Plans Pricing
  plan_count: 4
  slug: tradedatahub-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Tradedatahub Rate Limits
  slug: tradedatahub-rate-limits
score:
  band: developing
  composite: 40.4
  coverage:
    artifact_dirs: 18
    catalog_gap: 68.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 33.3
    developer_ergonomics: 50.0
    discoverability: 72.2
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 40.4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Tradedatahub Authentication
  slug: tradedatahub-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Tradedatahub Domain Security
  slug: tradedatahub-domain-security
  summary_line: TLSv1.3 · HSTS
slug: tradedatahub
tags:
- contractor data
- B2B Data
- Business Listings
- Datasets
- CSV
- Lead Generation
- Sales Intelligence
- x402
- agent-native
- llms-txt
- OpenAPI
website: https://www.tradedatahub.net/developers/
---
