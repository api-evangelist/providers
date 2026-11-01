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
    error_semantics: derived
    event_surface_described: false
    idempotency: derived
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.8
  scored_at: '2026-10-31'
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
artifact_total: 15
common:
- group: other
  href: https://artifacts.apis.io/bybe/capabilities/bybe-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/bybe-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/bybe/overlays/bybe-api-overlay.yaml
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
  href: https://artifacts.apis.io/bybe/authentication/bybe-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bybe-authentication.yml
- group: agent
  href: https://artifacts.apis.io/bybe/agentic-access/bybe-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bybe-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/bybe/security/bybe-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bybe-domain-security.yml
- group: design
  href: https://artifacts.apis.io/bybe/conventions/bybe-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bybe-conventions.yml
- group: design
  href: https://artifacts.apis.io/bybe/conventions/bybe-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/bybe-conventions.yml
- group: design
  href: https://artifacts.apis.io/bybe/errors/bybe-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bybe-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bybe/lifecycle/bybe-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/bybe-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/bybe/conformance/bybe-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bybe-conformance.yml
- group: design
  href: https://artifacts.apis.io/bybe/data-model/bybe-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bybe-data-model.yml
- group: build
  href: https://artifacts.apis.io/bybe/packages/bybe-packages.yml
  title: ''
  type: Packages
  url: packages/bybe-packages.yml
- group: commercial
  href: https://artifacts.apis.io/bybe/plans/bybe-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bybe-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/bybe/rate-limits/bybe-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bybe-rate-limits.yml
- group: start
  href: https://artifacts.apis.io/bybe/sandbox/bybe-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/bybe-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/bybe/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/bybe/llms/bybe-llms.txt
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
overview: 'BYBE publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Clips API, Consumers API, Manufacturers API, and 4 more. Tagged areas include Company, Alcohol, Beverages, Promotions, and Rebates.


  BYBE''s developer surface includes documentation, API reference, getting-started guide, pricing, support, authentication, sandbox, and 22 more developer resources.'
plans:
- name: Bybe Plans Pricing
  plan_count: 2
  slug: bybe-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Bybe Rate Limits
  slug: bybe-rate-limits
score:
  band: developing
  composite: 47.4
  coverage:
    artifact_dirs: 22
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 65.8
    contract_governance: 4.5
    contract_quality: 44.6
    developer_ergonomics: 63.7
    discoverability: 66.1
    operational_transparency: 21.1
  previous_composite: 47.4
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
    score: 22.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/bybe/bybe-2026-07-25T204132.png
security:
- kind: authentication
  name: Bybe Authentication
  slug: bybe-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bybe Domain Security
  slug: bybe-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Clip a BYBE offer for a shopper
  slug: bybe-clip-an-offer
- name: Submit purchases to BYBE and pay a shopper back
  slug: bybe-submit-redemption
- name: Sync the BYBE product and manufacturer catalog
  slug: bybe-sync-catalog
slug: bybe
tags:
- Company
- Alcohol
- Beverages
- Promotions
- Rebates
- Marketing
- Retail
- Consumer Packaged Goods
- Loyalty
- Payments
- Disbursements
- Compliance
website: https://bybe.com/
---
