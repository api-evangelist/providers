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
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Token-authenticated REST API (v2) for bulk programmatic access to Enverus' energy datasets — well origins, rigs, permits, producing entities, and production. Authenticate with an API key plus client c
  name: Enverus DirectAccess API
  slug: enverus-directaccess-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/enverus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.enverus.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.enverus.com/direct/
- group: docs
  title: ''
  type: Documentation
  url: https://app.enverus.com/direct/#/api/explorer/v2/gettingStarted
- group: start
  title: ''
  type: GettingStarted
  url: https://app.enverus.com/direct/#/api/explorer/v2/gettingStarted
- group: start
  title: ''
  type: Login
  url: https://login.auth.enverus.com/
- group: company
  title: ''
  type: Blog
  url: https://www.enverus.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.enverus.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.enverus.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.enverus.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/enverus
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/enverus-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/enverus-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/enverus-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/enverus-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/enverus-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/enverus-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/enverus-well-known.yml
created: '2026-07-17'
description: Enverus is an energy-dedicated SaaS company providing analytics, market intelligence, and workflow automation across the global energy value chain — oil and gas, power and renewables, minerals, midstream, trading and risk, and financial services. Its developer surface is the Enverus DirectAccess API (formerly Drillinginfo DirectAccess), a token-authenticated REST API that delivers bulk access to Enverus' energy datasets — well origins, rigs, permits, producing entities, production, and related upstream data — with server-side filter functions, field selection, and cursor-based pagination. Enverus serves 8,000+ companies and 35,000+ energy customers from its Austin, Texas headquarters.
image: https://www.enverus.com/wp-content/uploads/2024/08/enverus-og-logo-1553x1553-1.png
layout: provider
modified: '2026-07-19'
name: Enverus
nav: Providers
network: true
overview: 'Enverus publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Oil and Gas, Energy Data, and Analytics.


  Enverus'' developer surface includes documentation, getting-started guide, engineering blog, support, authentication, and 13 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 23.0
  coverage:
    artifact_dirs: 10
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 34.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 23.0
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 33.8
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/enverus/refs/heads/main/screenshots/enverus-2026-07-25T213445.png
security:
- kind: authentication
  name: Enverus Authentication
  slug: enverus-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Enverus Domain Security
  slug: enverus-domain-security
  summary_line: TLSv1.3 · DMARC
slug: enverus
tags:
- Company
- Energy
- Oil and Gas
- Energy Data
- Analytics
- Market Intelligence
- Well Data
- Software-as-a-Service
- Direct Access
- Trading and Risk
website: https://www.enverus.com/
---
