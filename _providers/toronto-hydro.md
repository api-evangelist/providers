---
access_model:
  confidence: low
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: Toronto Hydro's Green Button Download My Data (DMD) implementation, also required by O. Reg. 633/21 and built to NAESB REQ.21 ESPI v3.3. A Toronto Hydro customer signs in to their own account and down
  name: Toronto Hydro Green Button Download My Data
  slug: toronto-hydro-green-button-download-my-data
- baseURL: https://sandbox.greenbuttonalliance.org:8443/DataCustodian
  baseurl_source: spec
  description: Application Information endpoints
  name: Toronto Hydro Application Information API
  slug: toronto-hydro-applicationinformation-api
- baseURL: https://sandbox.greenbuttonalliance.org:8443/DataCustodian
  baseurl_source: spec
  description: Authorization endpoints
  name: Toronto Hydro Authorization API
  slug: toronto-hydro-authorization-api
- baseURL: https://sandbox.greenbuttonalliance.org:8443/DataCustodian
  baseurl_source: spec
  description: Batch data transfer endpoints
  name: Toronto Hydro Batch API
  slug: toronto-hydro-batch-api
- baseURL: https://sandbox.greenbuttonalliance.org:8443/DataCustodian
  baseurl_source: spec
  description: Usage Point endpoints
  name: Toronto Hydro Usage Point API
  slug: toronto-hydro-usagepoint-api
artifact_total: 9
collections:
- collection_type: open
  name: Green Button API Documentation
  slug: open-toronto-hydro-green-button-espi
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/toronto-hydro-green-button-espi-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/toronto-hydro-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/toronto-hydro-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/toronto-hydro-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/toronto-hydro-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/toronto-hydro-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/toronto-hydro-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/toronto-hydro-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/toronto-hydro-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/toronto-hydro-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/toronto-hydro-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/toronto-hydro-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.torontohydro.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.torontohydro.com/for-home/green-button
- group: start
  title: ''
  type: DeveloperPortal
  url: https://torontoonboarding.savagedata.com/
- group: other
  title: ''
  type: Registration
  url: https://torontoonboarding.savagedata.com/
- group: start
  title: ''
  type: SignUp
  url: https://torontoonboarding.savagedata.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.torontohydro.com/documents/d/guest/green-button-connect-my-data-customer-guide
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.torontohydro.com/green-button/third-party-terms
- group: commercial
  title: ''
  type: TermsOfUse
  url: https://www.torontohydro.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.torontohydro.com/privacy-policy
- group: commercial
  title: ''
  type: Legal
  url: https://www.torontohydro.com/conditions-of-service
- group: operate
  title: ''
  type: StatusPage
  url: https://outagemap.torontohydro.com/
- group: operate
  title: ''
  type: Support
  url: https://www.torontohydro.com/contact-us
- group: operate
  title: ''
  type: FAQ
  url: https://www.torontohydro.com/frequently-asked-questions
- group: company
  title: ''
  type: Blog
  url: https://www.torontohydro.com/newsroom
- group: other
  title: ''
  type: Regulations
  url: https://www.torontohydro.com/regulatory-information
- group: company
  title: ''
  type: LinkedIn
  url: https://ca.linkedin.com/company/toronto-hydro
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/torontohydro
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/TorontoHydro/
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/torontohydro/
- group: learn
  title: ''
  type: Youtube
  url: https://www.youtube.com/user/TorontoHydro
created: '2026-07-27'
description: Toronto Hydro is the municipally owned local electricity distribution company (LDC) for the City of Toronto, delivering power to roughly 800,000 residential and business customers across Canada's largest city. It sits in the wires-and-meters layer of Ontario's electricity value chain — it does not generate power and it does not run the wholesale market (that is IESO) — so the only customer-facing data it owns is smart-meter consumption, billing and account data. Its API posture is a clean example of a mandate that produced an implementation but not a developer product — Ontario's O. Reg. 633/21 under the Electricity Act, 1998 compelled rate-regulated electricity and gas utilities to offer Green Button Download My Data and Connect My Data conforming to NAESB REQ.21 ESPI v3.3 by 1 November 2023, and Toronto Hydro runs both — customer-facing Download My Data and Connect My Data pages behind its account login, a published third-party terms-and-conditions document, and a live third-party
  onboarding portal operated by its platform vendor Savage Data Systems. But there is no developer.torontohydro.com, no docs. or api. subdomain, no published base URI, no OpenAPI, and no self-serve keys. Consumer data is available only to companies that apply, pass a connectivity test and sign the third-party terms; market and grid data are not published openly at all. Mandated, implemented, and completely gated.
image: https://www.torontohydro.com/favicon.ico
layout: provider
modified: '2026-07-27'
name: Toronto Hydro
nav: Providers
network: true
overview: 'Toronto Hydro publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Application Information API, Authorization API, Batch API, and 1 more. Tagged areas include Energy, Canada, Utilities, Electricity, and Smart Metering.


  Toronto Hydro''s developer surface includes authentication, documentation, signup flow, getting-started guide, legal docs, support, FAQ, and 26 more developer resources.'
random_paper: 19
scopes:
- name: Toronto Hydro Scopes
  scope_count: 0
  slug: toronto-hydro-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 30.9
  coverage:
    artifact_dirs: 17
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 11.1
    developer_ergonomics: 42.3
    discoverability: 59.3
    governance: 4.5
    operational_transparency: 15.8
  previous_composite: 30.9
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 56.8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/toronto-hydro/refs/heads/main/screenshots/toronto-hydro-2026-09-02T163937.png
security:
- kind: authentication
  name: Toronto Hydro Authentication
  slug: toronto-hydro-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Toronto Hydro Domain Security
  slug: toronto-hydro-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: toronto-hydro
tags:
- Energy
- Canada
- Utilities
- Electricity
- Smart Metering
- Green Button
- Grid
- Ontario
- Consumer Data
- Electricity Distribution
website: https://www.torontohydro.com/
---
