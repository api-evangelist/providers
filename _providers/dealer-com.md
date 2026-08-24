---
access_model:
  confidence: high
  label: Public docs, registration required
  onboarding: unknown
  pricing: unknown
  public: true
  source:
  - https://developer.inv.dealer.com/content/home.html
  - https://coxautoinc.mashery.com/member/register
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-24'
api_count: 7
apis:
- description: Dealership account information for dealers who have a relationship with Dealer.com. GET /accounts/search returns a filterable, paginated list; GET /accounts/id/{accountId} returns one account. Payload
  name: Dealer.com Accounts API
  slug: dealer-com-accounts-api
- description: Manufacturer and dealer incentive offers. GET /incentives returns a filterable, paginated list; GET /incentives/id/{uniqueId} returns one offer, keyed by a composite accountID_incentiveID. Each incent
  name: Dealer.com Incentives API
  slug: dealer-com-incentives-api
- description: 'Vehicle inventory available for sale at Dealer.com dealerships in the United States and Canada. GET /vehicles/search returns a filterable, paginated list; GET /vehicles/id/{uuid} returns one vehicle, '
  name: Dealer.com Vehicle API
  slug: dealer-com-vehicle-api
- description: Equipment and option data for vehicles in Dealer.com inventory, exposed as its own resource alongside the Vehicle API. GET /vehicles/equipment returns a paginated list and GET /vehicles/equipment/id/{
  name: Dealer.com Equipment API
  slug: dealer-com-equipment-api
- description: Vehicle price data for Dealer.com inventory, exposed as its own resource within the Inventory family alongside the Vehicle and Equipment APIs. Complements the twenty price fields already selectable on
  name: Dealer.com Price API
  slug: dealer-com-price-api
- description: 'Browser-side JavaScript API that lets Integrated Partner Program partners place and control experiences on Dealer.com dealer websites. A partner hosts one script on their own CDN; Dealer.com loads it '
  name: Dealer.com Website Integration API
  slug: dealer-com-website-integration-api
- description: Lead generation and management capability - pre-qualification, messaging, and customer-engagement tools that capture website leads and route them into dealer CRM and Cox Automotive systems (Dealertrac
  name: Dealer.com Leads API
  slug: dealer-com-leads-api
artifact_total: 13
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dealer-com-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/dealer-com-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dealer-com-domain-security.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/dealer-com-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/dealer-com-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dealer-com-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dealer-com-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dealer-com-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dealer-com-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://coxautoapi.statuspage.io
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/dealer-com-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dealer-com-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dealer-com-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/dealer-com-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/dealer-com-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/dealer-com-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dealer-com-llms.txt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dealer-com
- group: company
  title: ''
  type: Website
  url: https://www.dealer.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.inv.dealer.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.inv.dealer.com/content/accounts/accounts-home.html
- group: docs
  title: ''
  type: Documentation
  url: https://www.dealer.com/products/integrated-partner-program
- group: docs
  title: ''
  type: Documentation
  url: https://developer.coxautoinc.com/
- group: docs
  title: ''
  type: APIReference
  url: https://dealerdotcom.github.io/web-integration-api-docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.inv.dealer.com/content/home.html
- group: start
  title: ''
  type: SignUp
  url: https://coxautoinc.mashery.com/member/register
- group: operate
  title: ''
  type: Support
  url: https://www.dealer.com/support/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DealerDotCom
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dealer.com/company/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dealer.com/company/dealer-com-privacy-policy/
- group: commercial
  title: ''
  type: Plans
  url: plans/dealer-com-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dealer-com-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dealer-com-finops.yml
- group: other
  title: ''
  type: ProductPage
  url: https://www.dealer.com/integrations/
- group: company
  title: ''
  type: News
  url: https://www.dealer.com/company-news/data-integration-unlocks-website-personalization-press-release/
created: '2026-07-10'
description: Dealer.com, a Cox Automotive brand, builds automotive dealership websites, digital advertising, and digital marketing technology used by thousands of franchise and independent dealers across North America. It publishes two distinct developer surfaces. The Dealer Developer Portal at developer.inv.dealer.com documents a read-only REST family — Accounts, Incentives and Inventory (Vehicle, Equipment, Price) — authenticated with a single self-registered API key, with published quotas of 2 calls/second and 5,000 calls/day, offset pagination, sparse fieldsets via a repeatable select parameter, and HAL-style hypermedia links. The Website Integration API, documented in public git at github.com/DealerDotCom, is a browser-side JavaScript API that lets Integrated Partner Program partners subscribe to page and vehicle events and insert markup, CTAs and gallery content into named locations on dealer sites, with content-delivery authentication built on signed JWTs validated against a live
  JWK Set. Platform-level lead, deal and digital-retail data flows separately through the OAuth-gated Cox Automotive Integration Platform at developer.coxautoinc.com. Both Dealer.com surfaces are documented in public; the credentials, not the contracts, are what is gated. The published REST surface is decaying, though — the documented base host api.dealer.com no longer resolves, and the five Swagger documents the portal's own API Explorer loads have contained an AWS API Gateway error string since February 2020.
finops:
- name: Dealer Com Finops
  service_category: Automotive Digital Marketing and Websites
  slug: dealer-com-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dealer-com.png
layout: provider
modified: '2026-08-12'
name: Dealer.com
nav: Providers
network: true
overview: 'Dealer.com publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Automotive, Dealership, Digital Marketing, Website Platform, and Inventory.


  Dealer.com''s developer surface includes authentication, changelog, sandbox, documentation, API reference, getting-started guide, signup flow, and 28 more developer resources.'
plans:
- name: Dealer Com Plans Pricing
  plan_count: 3
  slug: dealer-com-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Dealer Com Rate Limits
  slug: dealer-com-rate-limits
score:
  band: developing
  composite: 44.8
  delta: 0.0
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 61.9
    discoverability: 72.2
    governance: 4.5
    operational_transparency: 76.3
  previous_composite: 44.8
  provenance:
    conformance: derived
    mcp: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dealer-com/refs/heads/main/screenshots/dealer-com-2026-07-25T211507.png
security:
- kind: authentication
  name: Dealer Com Authentication
  slug: dealer-com-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Dealer Com Domain Security
  slug: dealer-com-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Dealer Com Vulnerability Disclosure
  slug: dealer-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dealer-com
tags:
- Automotive
- Dealership
- Digital Marketing
- Website Platform
- Inventory
- Vehicle Data
- Incentives
- Leads
- Digital Advertising
- Cox Automotive
- Partner Program
website: https://www.dealer.com
---
