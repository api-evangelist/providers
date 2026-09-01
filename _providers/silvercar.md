---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.4
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'Versioned (mob-api-v4) REST API for Dealerware fleet-management and courtesy/loaner mobility workflows: contracts, reservations, contactless check-in, customers, drivers, employees, dealerships, fleet'
  name: Dealerware Partner Integration API
  slug: dealerware-partner-integration-api
artifact_total: 4
asyncapis:
- description: ''
  name: Silvercar Webhooks
  slug: silvercar-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/silvercar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://silvercar.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.dealerware.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.dealerware.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.dealerware.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.dealerware.com/docs/quickstart-guide
- group: auth
  title: ''
  type: Authentication
  url: authentication/silvercar-authentication.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.dealerware.com/docs/deprecation-1
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/silvercar-webhooks.yml
- group: operate
  title: ''
  type: Support
  url: https://developer.dealerware.com/docs/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dealerware.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dealerware.com/privacy-policy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/silvercar-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/silvercar-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/silvercar-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/silvercar-lifecycle.yml
created: '2026-07-17'
description: Silvercar began as an Austin, Texas premium car-rental startup (all-silver Audi fleet) and was a Slow Ventures portfolio company. After Audi acquired it, the team pivoted the technology into Dealerware, a dealership fleet-management and courtesy/loaner-mobility SaaS platform. silvercar.com now 301-redirects to dealerware.com, and the company's public developer surface is the Dealerware Partner Integration API — a versioned (v4) REST API on a ReadMe developer hub at developer.dealerware.com covering contracts, reservations, customers, dealerships, fleets, vehicles, drivers, employees, payments, reporting, and webhooks. Authentication is OAuth 2.0 machine-to-machine (client_credentials) via Auth0, returning RS256-signed JWT bearer tokens.
image: https://files.readme.io/ce942b596bb59005caaba879dd9e42d25b4fd618aa4444310d4148fdb273781c-small-dw_darkmode.png
layout: provider
modified: '2026-07-21'
name: silvercar
nav: Providers
network: true
overview: 'silvercar publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automotive, Car Rental, Fleet Management, and Mobility.


  The silvercar catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  silvercar''s developer surface includes documentation, API reference, getting-started guide, authentication, support, and 11 more developer resources.'
random_paper: 5
score:
  band: thin
  composite: 30.7
  coverage:
    artifact_dirs: 8
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 42.7
    developer_ergonomics: 33.3
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 11.8
  previous_composite: 30.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Silvercar Authentication
  slug: silvercar-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Silvercar Domain Security
  slug: silvercar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: silvercar
tags:
- Company
- Automotive
- Car Rental
- Fleet Management
- Mobility
- Dealership
- Rentals
- Software-as-a-Service
website: https://silvercar.com
---
