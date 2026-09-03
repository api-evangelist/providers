---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-09-02'
api_count: 2
apis:
- description: Provides programmatic access to Bloomberg's financial market data including real-time and historical pricing, reference data, and analytics.
  name: Bloomberg Data API
  slug: bloomberg-data-api
- description: 'Desktop API for accessing Bloomberg Terminal functionality programmatically through Excel, custom applications, and third-party systems. No public baseURL is recorded because none exists: the BLPAPI D'
  name: Bloomberg Terminal Connect API
  slug: bloomberg-terminal-connect-api
artifact_total: 10
asyncapis:
- description: ''
  name: Bloomberg Applications Blpapi Events
  slug: bloomberg-applications-blpapi-events
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/bloomberg/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bloomberg-applications-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/bloomberg-applications-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bloomberg-applications-domain-security.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/bloomberg-applications-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bloomberg-applications-well-known.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.bloomberg.com/
- group: docs
  title: ''
  type: Documentation
  url: https://professional.bloomberg.com/support/documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://bloomberg.github.io/blpapi-docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://professional.bloomberg.com/support/api-library/
- group: operate
  title: ''
  type: Support
  url: https://professional.bloomberg.com/support/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bloomberg
- group: start
  title: ''
  type: SignUp
  url: https://service.blpprofessional.com/portal/product/ureg?referrer=bdev
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bloomberg.com/notices/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bloomberg.com/notices/privacy/
- group: operate
  title: ''
  type: Releases
  url: https://bloomberg.github.io/blpapi-docs/all_versions.html
- group: build
  title: ''
  type: Packages
  url: packages/bloomberg-applications-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/bloomberg-applications-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/bloomberg-applications-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bloomberg-applications-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bloomberg-applications-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bloomberg-applications-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bloomberg-applications-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bloomberg-applications-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bloomberg-applications-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/bloomberg-applications-changelog.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bloomberg-applications-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/bloomberg-applications-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bloomberg-applications-llms.txt
created: '2024-01-01'
description: Bloomberg's financial data and application API surface, covering the BLPAPI family (Desktop API, Server API and B-PIPE) reached through first-party C++, Java, C#/.NET and Python SDKs, and the Data License Hypermedia API served over HTTP at api.bloomberg.com/eap. The surface delivers real-time and historical pricing, reference data, intraday bars and ticks, and streaming market data subscriptions. BLPAPI is an asynchronous binary event protocol rather than a REST API, so it carries no HTTP status codes, rate-limit headers or idempotency keys; errors and quota exhaustion arrive as typed messages on the event queue. Bloomberg publishes no OpenAPI description, no public pricing and no self-service signup — data access is entitlement-gated and provisioned under contract — but the SDKs, their full version archive and the BLPAPI developer guides are downloadable without an account.
finops:
- name: Bloomberg Applications Finops
  service_category: API
  slug: bloomberg-applications-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bloomberg-applications.png
layout: provider
modified: '2026-08-27'
name: Bloomberg Applications
nav: Providers
network: true
overview: 'Bloomberg Applications publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Enterprise API, Financial Analytics, Financial-Services, Market Data, and Real-Time Data.


  The Bloomberg Applications catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Bloomberg Applications'' developer surface includes developer portal, documentation, API reference, getting-started guide, support, signup flow, CLI, and 22 more developer resources.'
plans:
- name: Bloomberg Applications Plans Pricing
  plan_count: 0
  slug: bloomberg-applications-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 6
  name: Bloomberg Applications Rate Limits
  slug: bloomberg-applications-rate-limits
scopes:
- name: Bloomberg Applications Scopes
  scope_count: 0
  slug: bloomberg-applications-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 54.5
  coverage:
    artifact_dirs: 18
    catalog_gap: 68.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 69.0
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 60.5
  previous_composite: 54.5
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 78.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bloomberg-applications/refs/heads/main/screenshots/bloomberg-applications-2026-06-20T173410.png
security:
- kind: authentication
  name: Bloomberg Applications Authentication
  slug: bloomberg-applications-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Bloomberg Applications Domain Security
  slug: bloomberg-applications-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bloomberg Applications Vulnerability Disclosure
  slug: bloomberg-applications-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bloomberg-applications
tags:
- Enterprise API
- Financial Analytics
- Financial-Services
- Market Data
- Real-Time Data
website: https://developer.bloomberg.com/
---
