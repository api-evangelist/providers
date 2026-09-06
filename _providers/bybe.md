---
access_model:
  confidence: high
  label: Public docs, gated credentials
  onboarding: unknown
  pricing: unknown
  public: true
  source:
  - https://api.bybe.io/v1/swagger.yaml
  - https://bybe.com/pricing
  - https://developer.bybe.io/
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Bybe Agentic Access
  operation_count: 16
  slug: bybe-agentic-access
  summary_line: 16 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.bybe.io
  baseurl_source: declared
  description: A clip represents a consumer's intent to redeem an offer.
  name: BYBE Clips API
  slug: bybe-clips-api
- baseURL: https://api.bybe.io
  baseurl_source: declared
  description: A consumer purchases products and clips/redeems offers.
  name: BYBE Consumers API
  slug: bybe-consumers-api
- baseURL: https://api.bybe.io
  baseurl_source: declared
  description: A manufacturer represents a company or organization that produces alcoholic beverages.
  name: BYBE Manufacturers API
  slug: bybe-manufacturers-api
- baseURL: https://api.bybe.io
  baseurl_source: declared
  description: An offer is created and funded by a manufacturer (brand).
  name: BYBE Offers API
  slug: bybe-offers-api
- baseURL: https://api.bybe.io
  baseurl_source: declared
  description: A product is produced by a manufacturer and is featured in offers.
  name: BYBE Products API
  slug: bybe-products-api
- baseURL: https://api.bybe.io
  baseurl_source: declared
  description: Redemptions are created to disburse money to a consumer for their specific purchases.
  name: BYBE Redemptions API
  slug: bybe-redemptions-api
- baseURL: https://api.bybe.io
  baseurl_source: declared
  description: A store represents a specific retail location of a retailer.
  name: BYBE Stores API
  slug: bybe-stores-api
artifact_total: 12
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/bybe-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/bybe-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://bybe.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.bybe.io/
- group: docs
  title: ''
  type: Documentation
  url: https://bybe.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://docs.bybe.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://bybe.com/developers
- group: start
  title: ''
  type: Login
  url: https://dashboard.bybe.io/users/sign_in
- group: commercial
  title: ''
  type: Pricing
  url: https://bybe.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bybe.com/terms-and-conditions.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bybe.com/privacy-policy.html
- group: operate
  title: ''
  type: Support
  url: mailto:support@bybe.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BYBE-INC
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bybe.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/bybe-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bybe-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bybe-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bybe-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/bybe-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bybe-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bybe-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bybe-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bybe-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/bybe-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/bybe-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bybe-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/bybe-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bybe-llms.txt
created: '2026-07-17'
description: BYBE, Inc. is a promotion platform for the beer, wine, and spirits industry, connecting alcohol beverage brands, retailers, and consumers through digital cash-back rebates. Brands fund offers in the BYBE dashboard; retailers embed those offers in their own apps, sites and loyalty programs, and BYBE handles US state-by-state alcohol promotion compliance, redemption validation, clearing and consumer payout. BYBE publishes a real OpenAPI 3.0.1 contract for its Retail API at api.bybe.io covering manufacturers, products, offers, clips, consumers, stores and redemption disbursements, with HTTP Basic authentication and a documented SFTP CSV batch alternative for retailers that cannot call the API in real time. Backed by Techstars and Rev1 Ventures, BYBE was acquired by Swiftly in March 2024 and continues to operate under its own brand and domains.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bybe.png
layout: provider
modified: '2026-08-13'
name: BYBE
nav: Providers
network: true
overview: 'BYBE publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Clips API, Consumers API, Manufacturers API, and 4 more. Tagged areas include Company, Alcohol, Beverages, Promotions, and Rebates.


  BYBE''s developer surface includes documentation, API reference, getting-started guide, pricing, support, authentication, sandbox, and 22 more developer resources.'
plans:
- name: Bybe Plans Pricing
  plan_count: 2
  slug: bybe-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Bybe Rate Limits
  slug: bybe-rate-limits
score:
  band: thin
  composite: 34.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 46.8
    developer_ergonomics: 42.3
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 34.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bybe/refs/heads/main/screenshots/bybe-2026-07-25T204132.png
security:
- kind: authentication
  name: Bybe Authentication
  slug: bybe-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bybe Domain Security
  slug: bybe-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bybe
tags:
- Company
- Alcohol
- Beverages
- Promotions
- Rebates
- Marketing
- Retail
- CPG
- Loyalty
- Payments
- Disbursements
- Compliance
website: https://bybe.com/
---
