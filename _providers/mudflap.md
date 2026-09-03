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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
  score: 10.8
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: OAuth 2.0 / OpenID Connect protected API surface serving Mudflap's partner, fleet, and merchant dashboards. Discovered via the published RFC 8414 authorization-server metadata; no public OpenAPI refer
  name: Mudflap Partner API
  slug: mudflap-partner-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://mudflapinc.com
- group: start
  title: ''
  type: Portal
  url: https://partner.mudflapinc.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.mudflapinc.com/app/how-it-works
- group: operate
  title: ''
  type: Support
  url: https://www.mudflapinc.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mudflapinc.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mudflapinc.com/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mudflap-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mudflap-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mudflap-authentication.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: authentication/mudflap-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/mudflap-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mudflap-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mudflap-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mudflap-domain-security.yml
created: '2026-07-17'
description: Mudflap is a fintech company operating a diesel fuel-discount network for truckers, owner-operators, and fleets. Its mobile app delivers instant cost-plus diesel discounts (up to $1.00/gallon) at 3,600+ truck stops using a driver's existing debit or credit card, and its Mudflap Fuel Card extends fleet credit terms, driver spend controls, and fraud protection across 70,000+ fuel stops nationwide, managed through a fleet dashboard. Mudflap reports $1B+ saved by 515,000+ active drivers and is recommended by 94% of owner-operators and fleets. It also runs a truck-stop merchant program and a Geotab telematics integration. Mudflap is backed by Matrix Partners. The company exposes an OAuth 2.0 / OpenID Connect authorization server at api.mudflapinc.com for its partner, fleet, and merchant surfaces; no public developer OpenAPI is published.
image: https://cdn.prod.website-files.com/663e75126ab14bc3a56a0e08/66bfbffec2941b37b6c31a3c_og-brand.png
layout: provider
modified: '2026-07-20'
name: Mudflap
nav: Providers
network: true
overview: 'Mudflap publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Fuel, Trucking, and Payments.


  Mudflap''s developer surface includes developer portal, getting-started guide, support, authentication, and 10 more developer resources.'
random_paper: 10
scopes:
- name: Mudflap Scopes
  scope_count: 3
  slug: mudflap-scopes
  summary_line: 3 scopes · authorizationCode/password
score:
  band: emerging
  composite: 24.9
  coverage:
    artifact_dirs: 8
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 24.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 54.7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mudflap/refs/heads/main/screenshots/mudflap-2026-08-07T184427.png
security:
- kind: authentication
  name: Mudflap Authentication
  slug: mudflap-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Mudflap Domain Security
  slug: mudflap-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mudflap
tags:
- Company
- Fintech
- Fuel
- Trucking
- Payments
- Fleet Management
- Logistics
- Fuel Card
website: https://mudflapinc.com
---
