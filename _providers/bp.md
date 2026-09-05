---
access_model:
  confidence: high
  label: Custom / business relationship — no public plans or pricing published
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - https://developer.fleet.bp.com/DE/apis
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 40.1
  scored_at: '2026-09-04'
api_count: 7
apis:
- description: The bp API Marketplace is a white-labelled RapidAPI Enterprise Hub developer portal for BP's digital APIs. It provides API discovery, a testing playground, documentation, usage monitoring, error and l
  name: BP API Marketplace
  slug: bp-api-marketplace
- baseURL: https://api.fleet.bp.com/authentication/v1.0/
  baseurl_source: declared
  description: Token endpoint for the bp Open Fleet platform. POST /token exchanges a client_id and client_secret for a bearer access_token used by every other Open Fleet API. Credentials are bound to a single envir
  name: bp Open Fleet Authentication API
  slug: bp-fleet-authentication
- baseURL: https://api.fleet.bp.com/{apiPrefix}/v1/
  baseurl_source: declared
  description: 'Fuel-card management for bp and Aral fleet customers. Currently exposes a single read operation, GET /cards, returning the latest card updates filtered by authority, parent account, card status and a '
  name: bp Open Fleet Card Management API
  slug: bp-fleet-card-management
- baseURL: https://api.fleet.bp.com/{apiPrefix}/v1.0/
  baseurl_source: declared
  description: 'Real-time access to fleet invoice data. GET /invoices retrieves and searches invoices with cost breakdowns, payment statuses, due dates and applicable discounts, filtered by authority, parent account '
  name: bp Open Fleet Invoice Management API
  slug: bp-fleet-invoice-management
- baseURL: https://api.fleet.bp.com/{apiPrefix}/v1.0/
  baseurl_source: declared
  description: Direct access to fleet fuel transaction data. GET /transactions returns full transaction detail including product breakdowns, site location, driver and vehicle information, discounts, taxes and invoic
  name: bp Open Fleet Transaction Management API
  slug: bp-fleet-transaction-management
- baseURL: https://api.fleet.bp.com/{apiPrefix}/v1.0/
  baseurl_source: declared
  description: 'Comprehensive bp and Aral retail site data. GET /sites returns address, contact details, retail site features such as ATM and car wash, operating hours and holiday schedules, site amenities, fuel and '
  name: bp Open Fleet Retail Site Information API
  slug: bp-fleet-retail-site-information
- baseURL: https://api.fleet.bp.com/{apiPrefix}/v1/
  baseurl_source: declared
  description: Digital fuel authorization at bp and Aral stations. Drivers authorize a fuel card directly from the vehicle, avoiding the till; the card is linked to a driver, vehicle or onboard computer and only the
  name: bp Open Fleet Aral AppConnect (Pay@Pump) API
  slug: bp-fleet-aral-appconnect
artifact_total: 14
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bp-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bp
- group: company
  title: ''
  type: Website
  url: https://www.bp.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.bp.com/hub
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.bp.com/en/global/corporate/investors.html
- group: other
  title: ''
  type: Sustainability
  url: https://www.bp.com/en/global/corporate/sustainability.html
- group: start
  title: ''
  type: Portal
  url: https://developer.fleet.bp.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.fleet.bp.com/DE/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.fleet.bp.com/DE/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://developer.bp.com/bp%20API%20Marketplace%20User%20Guide.pdf
- group: operate
  title: ''
  type: Support
  url: https://developer.fleet.bp.com/DE/support
- group: operate
  title: ''
  type: StatusPage
  url: https://developer.fleet.bp.com/DE/api-status
- group: start
  title: ''
  type: Login
  url: https://api.developer.bp.com/auth
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bp.com/legal-notice
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bp.com/en/global/privacy/global-products-and-services-notices.html
- group: auth
  title: ''
  type: Security
  url: https://bp.responsibledisclosure.com/hc/en-us
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bp-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bp-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bp-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bp-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bp-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bp-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bp-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bp-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/bp-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bp-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/bp-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bp-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/bp-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bp-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bp-finops.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/bp-mcp.yml
- group: other
  title: ''
  type: RAML
  url: raml/bp-anypoint-statistics-service.raml
created: '2025-03-01'
description: BP (British Petroleum) is one of the world's largest integrated energy companies, operating in over 70 countries across oil and gas exploration, production, refining, distribution, marketing, petrochemicals, power generation and renewable energy. BP runs two distinct public API surfaces. The bp Open Fleet Developer Portal (developer.fleet.bp.com) publishes six machine-readable OpenAPI 3.0.1 contracts covering fleet-card management, invoicing, fuel transactions, retail site information and Aral AppConnect pay-at-pump authorization, secured with OAuth2 client credentials against api.fleet.bp.com and a matching sandbox. The bp API Marketplace (developer.bp.com) is a white-labelled RapidAPI Enterprise Hub whose catalogue sits behind a login. Access to both is aimed at existing B2B fleet and mobility customers rather than public self-serve signup.
finops:
- name: Bp Finops
  service_category: API
  slug: bp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bp.png
layout: provider
modified: '2026-09-04'
name: BP
nav: Providers
network: true
overview: 'BP publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Open Fleet Authentication API, Open Fleet Card Management API, Open Fleet Invoice Management API, and 3 more. Tagged areas include Energy, Oil, Gas, Renewables, and Developer Platform.


  BP''s developer surface includes developer portal, API reference, getting-started guide, documentation, support, authentication, sandbox, and 28 more developer resources.'
plans:
- name: Bp Plans Pricing
  plan_count: 0
  slug: bp-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 6
  name: Bp Rate Limits
  slug: bp-rate-limits
scopes:
- name: Bp Scopes
  scope_count: 0
  slug: bp-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 49.9
  coverage:
    artifact_dirs: 22
    catalog_earned: 50.0
    catalog_earned_first_party: 12.0
    catalog_gap: 65.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 41.1
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 4.5
    contract_quality: 35.7
    developer_ergonomics: 54.2
    discoverability: 64.8
    governance: 4.5
    operational_transparency: 60.5
  previous_composite: 8.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 64.9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/bp/refs/heads/main/screenshots/bp-2026-07-25T203719.png
security:
- kind: authentication
  name: Bp Authentication
  slug: bp-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Bp Domain Security
  slug: bp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bp Vulnerability Disclosure
  slug: bp-vulnerability-disclosure
  summary_line: disclosure policy published
slug: bp
tags:
- Energy
- Oil
- Gas
- Renewables
- Developer Platform
- Fleet
- Fuel Cards
- Mobility
- Retail Fuel
- EV Charging
website: https://www.bp.com
---
