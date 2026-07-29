---
access_model:
  confidence: high
  label: Free · Application and approval required
  onboarding: unknown
  pricing: free
  public: false
  source:
  - documentation
  - terms
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Hydro One's Green Button Connect My Data implementation, mandated by Ontario Regulation 633/21. A registered third-party vendor obtains an OAuth 2.0 authorization code after the customer authenticates
  name: Hydro One Green Button Connect My Data (CMD)
  slug: hydro-one-green-button-connect-my-data
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hydro-one-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hydro-one-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/hydro-one-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hydro-one-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hydro-one-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hydro-one-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/hydro-one-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hydro-one-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.hydroone.com/
- group: company
  title: ''
  type: About
  url: https://www.hydroone.com/about
- group: docs
  title: ''
  type: Documentation
  url: https://www.hydroone.com/saving-money-and-energy/green-button
- group: start
  title: ''
  type: GettingStarted
  url: https://www.hydroone.com/saving-money-and-energy/green-button/third-party-apps
- group: start
  title: ''
  type: SignUp
  url: https://www.hydroone.com/saving-money-and-energy/green-button/third-party-onboarding-form
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hydroone.com/saving-money-and-energy/green-button/third-party-terms-and-conditions
- group: commercial
  title: ''
  type: TermsOfUse
  url: https://www.hydroone.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hydroone.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.hydroone.com/contact
- group: company
  title: ''
  type: News
  url: https://www.hydroone.com/newsroom
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hydro-one
- group: other
  title: ''
  type: Regulator
  url: https://www.oeb.ca/consumer-information-and-protection/green-button
created: '2026-07-27'
description: 'Hydro One Limited (TSX: H) is Canada''s largest electricity transmission and distribution service provider, transmitting and distributing electricity across Ontario — the province the company describes as "home to 38 per cent of Canada''s population." It sits in the regulated wires tier of the value chain: it owns and operates the provincial transmission grid and a rural/regional distribution network serving roughly 1.5 million customers, while the Ontario market itself is operated by the IESO and rates are set by the Ontario Energy Board. Its API posture is defined entirely by regulation, not by product. Ontario Regulation 633/21 (Energy Data, under the Electricity Act, 1998) compels Ontario electricity and natural gas distributors to implement Green Button Download My Data (DMD) and Connect My Data (CMD) and to have those implementations certified by the Green Button Alliance. Hydro One publishes DMD as an authenticated XML export inside My Account, runs a live Green Button
  CMD OAuth 2.0 authorization surface at www.hydroone.com/green-button-cmd-home, and operates a published third-party vendor onboarding form and terms and conditions — but the CMD resource base URI, client credentials, and test accounts are issued privately during onboarding and are not published anywhere. There is no developer subdomain, no OpenAPI or Swagger definition, and no self-serve signup. The split is the finding: consumer energy data is available through a real, standards-based, mandated API that a developer can only reach by application and 90-day connectivity testing, while open grid and market data is entirely absent — Hydro One publishes no open data portal and no documented public system or outage API, leaving Ontario market data to the IESO.'
image: https://www.hydroone.com/Style%20Library/H1/images/logo.svg
layout: provider
modified: '2026-07-27'
name: Hydro One
nav: Providers
network: true
overview: 'Hydro One publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Canada, Utilities, Electricity, and Grid.


  Hydro One''s developer surface includes authentication, sandbox, documentation, getting-started guide, signup flow, support, product news, and 13 more developer resources.'
random_paper: 70
scopes:
- name: Hydro One Scopes
  scope_count: 0
  slug: hydro-one-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 29.2
  delta: 6.1
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 41.3
    discoverability: 77.8
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 23.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 56.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
security:
- kind: authentication
  name: Hydro One Authentication
  slug: hydro-one-authentication
  summary_line: oauth2/mutualTLS · 2 schemes
- kind: domain-security
  name: Hydro One Domain Security
  slug: hydro-one-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hydro-one
tags:
- Energy
- Canada
- Utilities
- Electricity
- Grid
- Smart Metering
- Green Button
- Energy Data
- Transmission
- Distribution
website: https://www.hydroone.com/
---
