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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.7
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: Current version of the Enverus Developer API (formerly Drillinginfo Direct Access). Read-only JSON access to energy datasets — wells, well-origins, wellbores, production, completions, permits, rigs, c
  name: Enverus Developer API (v3)
  slug: enverus-developer-api-v3
- description: Legacy Direct Access Version 2 of the Enverus / Drillinginfo API. Read-only JSON dataset access authenticated with client_id, client_secret and an API key exchanged for a bearer token. Superseded by t
  name: Enverus Direct Access API (v2, legacy)
  slug: enverus-direct-access-api-v2-legacy
artifact_total: 5
common:
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/drillinginfo-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/drillinginfo-mcp.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.enverus.com/blog/marketview-by-enverus-trading-and-risk-solutions-is-now-soc-1-type-1-certified/
- group: design
  title: ''
  type: Conformance
  url: conformance/drillinginfo-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/drillinginfo-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/drillinginfo-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/drillinginfo-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/drillinginfo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/drillinginfo-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/drillinginfo-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.drillinginfo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://app.enverus.com/direct/#/api/explorer/v3/gettingStarted
- group: docs
  title: ''
  type: APIReference
  url: https://app.enverus.com/direct/#/api/explorer/v3/gettingStarted
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.enverus.com/courses/direct-access-developer-api
- group: start
  title: ''
  type: SignUp
  url: https://app.enverus.com/provisioning/directaccess
- group: start
  title: ''
  type: Login
  url: https://rseg.auth0.com/login
- group: operate
  title: ''
  type: Support
  url: https://www.enverus.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://www.enverus.com/blog/
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
  url: https://github.com/enverus-ea
- group: company
  title: ''
  type: Website
  url: https://www.enverus.com/
created: '2026-07-17'
description: Drillinginfo (now Enverus) is an Austin, Texas energy-technology company that provides AI-powered analytics and the most comprehensive dataset across oil and gas, power, renewables, and financial markets. Its Direct Access / Developer API (rebranded from Drillinginfo Direct Access to the Enverus Developer API) gives subscribers programmatic, read-only access to well, production, completion, permit, rig, wellbore, lease, and producing-entity datasets for import into data warehouses and internal applications. The API is token-authenticated (secret key in v3, client credentials plus API key in v2), returns JSON, and paginates via RFC 5988 Link headers. An official Python client (enverus-developer-api) handles authentication, token management, pagination, and retries. Enverus serves over 8,000 companies across the energy value chain.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/drillinginfo.png
layout: provider
mcp_servers:
- description: ''
  name: drillinginfo-mcp.yml
  slug: drillinginfo-mcpyml
modified: '2026-07-18'
name: Drillinginfo
nav: Providers
network: true
overview: 'Drillinginfo publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Oil and Gas, Data, and Analytics.


  Drillinginfo''s developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, support, engineering blog, and 15 more developer resources.'
random_paper: 17
score:
  band: thin
  composite: 31.9
  delta: 0.1
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 60.9
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 31.8
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 40.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/drillinginfo/refs/heads/main/screenshots/drillinginfo-2026-07-25T212404.png
security:
- kind: authentication
  name: Drillinginfo Authentication
  slug: drillinginfo-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Drillinginfo Domain Security
  slug: drillinginfo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: drillinginfo
tags:
- Company
- Energy
- Oil and Gas
- Data
- Analytics
- Geospatial
- Developer API
- Well Data
- Production Data
- Energy Intelligence
website: https://www.enverus.com/
---
