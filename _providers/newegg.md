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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Seller integration API for the Newegg marketplaces covering item, order, shipping-label, RMA, datafeed, report, seller, and SBN management. Requests and responses are JSON or XML, authenticated with p
  name: Newegg Marketplace API
  slug: newegg-marketplace-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/newegg-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.newegg.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.newegg.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.newegg.com/newegg_marketplace_api/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.newegg.com/newegg_marketplace_api/newegg-developers-quick-guide/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Newegg
- group: operate
  title: ''
  type: StatusPage
  url: https://developer.newegg.com/status/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.newegg.com/whats-new/
- group: operate
  title: ''
  type: HelpCenter
  url: https://kb.newegg.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.newegg.com/sellers/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kb.newegg.com/knowledge-base/privacy-policy-newegg/
- group: auth
  title: ''
  type: Security
  url: https://kb.newegg.com/knowledge-base/newegg-vulnerability-disclosure-policy/
- group: auth
  title: ''
  type: Authentication
  url: authentication/newegg-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/newegg-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/newegg-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/newegg-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/newegg-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/newegg-changelog.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/newegg-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/newegg-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/newegg-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/newegg-llms.txt
created: '2026-07-17'
description: Newegg is a leading global online retailer of computer hardware, consumer electronics, and technology products, operating the Newegg.com (US), NeweggBusiness.com (B2B), and Newegg.ca (Canada) marketplaces. For third-party sellers Newegg exposes the Newegg Marketplace API, an API-key-authenticated, REST-style interface (JSON or XML) covering item management, order management, shipping-label services, RMA/returns, datafeed batch processing, reports, seller management, and Shipped By Newegg (SBN) fulfillment. First-party .NET and Java SDKs, a developer portal, service-status page, and dated release notes support the integration.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/newegg.png
layout: provider
modified: '2026-07-20'
name: Newegg
nav: Providers
network: true
overview: 'Newegg publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, E-Commerce, Marketplace, and Retail.


  Newegg''s developer surface includes documentation, getting-started guide, changelog, signup flow, authentication, and 17 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 29.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 44.7
  previous_composite: 29.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/newegg/refs/heads/main/screenshots/newegg-2026-08-07T185106.png
security:
- kind: authentication
  name: Newegg Authentication
  slug: newegg-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Newegg Domain Security
  slug: newegg-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Newegg Vulnerability Disclosure
  slug: newegg-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: newegg
tags:
- Company
- Consumer
- E-Commerce
- Marketplace
- Retail
- Electronics
- Sellers
- Order Management
- Fulfillment
website: http://www.newegg.com/
---
