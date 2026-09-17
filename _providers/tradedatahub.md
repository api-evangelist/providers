---
access_model:
  confidence: high
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.5
  scored_at: '2026-09-16'
api_count: 1
apis:
- baseURL: https://www.tradedatahub.net
  baseurl_source: declared
  description: x402 TESTNET paid retrieval. Mainnet is NOT enabled.
  name: TradeDataHub Public API Commerce API
  slug: tradedatahub-commerce-api
- baseURL: https://www.tradedatahub.net
  baseurl_source: declared
  description: Dataset metadata, pricing, masked previews.
  name: TradeDataHub Public API Datasets API
  slug: tradedatahub-datasets-api
- baseURL: https://www.tradedatahub.net
  baseurl_source: declared
  description: Zero-knowledge inventory discovery (coverage, states, trades, cities).
  name: TradeDataHub Public API Discovery API
  slug: tradedatahub-discovery-api
artifact_total: 17
common:
- group: company
  title: ''
  type: Website
  url: https://www.tradedatahub.net/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tradedatahub/refs/heads/main/security/tradedatahub-domain-security.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/tradedatahub/refs/heads/main/llms/tradedatahub-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tradedatahub-llms.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/tradedatahub/refs/heads/main/plans/tradedatahub-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tradedatahub-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/tradedatahub/refs/heads/main/rate-limits/tradedatahub-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tradedatahub-rate-limits.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tradedatahub/refs/heads/main/authentication/tradedatahub-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tradedatahub-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tradedatahub/refs/heads/main/errors/tradedatahub-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tradedatahub-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tradedatahub/refs/heads/main/conventions/tradedatahub-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tradedatahub-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tradedatahub/refs/heads/main/lifecycle/tradedatahub-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/tradedatahub-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tradedatahub/refs/heads/main/conformance/tradedatahub-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tradedatahub-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tradedatahub/refs/heads/main/data-model/tradedatahub-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tradedatahub-data-model.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/tradedatahub/refs/heads/main/sandbox/tradedatahub-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/tradedatahub-sandbox.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tradedatahub/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/tradedatahub/refs/heads/main/packages/tradedatahub-packages.yml
  title: ''
  type: Packages
  url: packages/tradedatahub-packages.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tradedatahub/refs/heads/main/overlays/tradedatahub-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/tradedatahub-openapi-overlay.yaml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/tradedatahub/refs/heads/main/examples/_index.yml
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
overview: 'TradeDataHub Public API publishes 3 APIs on the [APIs.io](https://apis.io/) network: Commerce API, Datasets API, and Discovery API. Tagged areas include contractor data, B2B Data, Business Listings, Datasets, and CSV.


  TradeDataHub Public API''s developer surface includes support, pricing, authentication, sandbox, code examples, and 16 more developer resources.'
plans:
- name: Tradedatahub Plans Pricing
  plan_count: 4
  slug: tradedatahub-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Tradedatahub Rate Limits
  slug: tradedatahub-rate-limits
score:
  band: developing
  composite: 42.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 47.0
    catalog_earned_first_party: 12.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.7
  facets:
    access_clarity: 63.2
    contract_governance: 4.5
    contract_quality: 50.8
    developer_ergonomics: 44.6
    discoverability: 72.2
    operational_transparency: 0.0
  previous_composite: 39.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/tradedatahub/refs/heads/main/screenshots/tradedatahub-2026-09-02T164042.png
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
website: https://www.tradedatahub.net/
---
