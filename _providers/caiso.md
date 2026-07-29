---
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
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: The Open Access Same-time Information System (OASIS) Download API — CAISO's public wholesale market data interface. Two servlets, SingleZip and GroupZip, accept a queryname or groupid plus a UTC datet
  name: CAISO OASIS Download API
  slug: caiso-oasis-download-api
- description: 'The CSV feeds behind CAISO''s public Today''s Outlook dashboard. Anonymous GET requests to https://www.caiso.com/outlook/current/{report}.csv return the current operating day at five-minute resolution, '
  name: CAISO Today's Outlook Data Feeds
  slug: caiso-todays-outlook-data-feeds
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/caiso-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.caiso.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.caiso.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.caiso.com/systems-applications/developer-portal
- group: start
  title: ''
  type: SignUp
  url: https://developer.caiso.com/_login/developersignup.aspx
- group: auth
  title: ''
  type: Authentication
  url: https://www.caiso.com/systems-applications/requesting-access-certificates
- group: start
  title: ''
  type: Portal
  url: https://www.caiso.com/systems-applications/portals-applications
- group: operate
  title: ''
  type: Support
  url: https://caiso.my.site.com/custsvccomm/s/knowledge-articles
- group: docs
  title: ''
  type: Documentation
  url: https://www.caiso.com/library/business-practice-manuals
- group: company
  title: ''
  type: Blog
  url: https://www.caiso.com/about/news
- group: company
  title: ''
  type: Blog
  url: https://www.caiso.com/about/news/energy-matters-blog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.caiso.com/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://www.caiso.com/documents/oasisapispecification.pdf
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.caiso.com/privacy-terms-of-use#api-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.caiso.com/privacy-terms-of-use
- group: operate
  title: ''
  type: Roadmap
  url: https://www.caiso.com/systems-applications/release-planning
- group: auth
  title: ''
  type: Authentication
  url: authentication/caiso-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/caiso-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/caiso-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/caiso-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/caiso-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/caiso-changelog.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/caiso-oasis-query-names.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/caiso-conformance.yml
- group: build
  title: ''
  type: Examples
  url: examples/caiso-oasis-examples.yml
- group: build
  title: ''
  type: Packages
  url: packages/caiso-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/caiso-llms.txt
created: '2026-07-27'
description: 'The California Independent System Operator (CAISO) is the non-profit public benefit corporation that operates the high-voltage transmission grid serving roughly 80 percent of California plus a portion of Nevada, and runs the wholesale day-ahead and real-time electricity markets, the Western Energy Imbalance Market (WEIM), and the Extended Day-Ahead Market (EDAM). As a system and market operator in the United States it sits at the wholesale layer of the energy value chain — upstream of the investor-owned utilities that bill retail customers, and therefore it holds no retail customer accounts and publishes no consumer usage data. Its API posture is a clean split: market data is genuinely open and consumer data does not exist. The OASIS Download API at https://oasis.caiso.com/oasisapi serves locational marginal prices, demand and renewables forecasts, ancillary services, transmission and nodal reference data as zipped CSV or CIM XML to anonymous callers with no key, no account
  and no registration — CAISO states in writing that every system it operates except OASIS requires a company User Access Administrator to grant access. The Today''s Outlook telemetry feeds under https://www.caiso.com/outlook publish five-minute fuel mix, demand, net demand and CO2 as plain CSV, also anonymously. Everything else — market submission, dispatch, settlements and the participant portals — is behind PKI client certificates and UAA-sponsored accounts, and even the OASIS reference documentation on the developer site requires a signup reviewed against a corporate email domain and a written justification. No Green Button, ESPI, or Consumer Data Right surface exists here and none is expected to; the obligation CAISO answers to is FERC''s open-access transparency regime, not a consumer data right. No OpenAPI, AsyncAPI, or other machine-readable contract is published for any of it.'
image: https://www.caiso.com/apple-touch-icon.png
layout: provider
modified: '2026-07-27'
name: California ISO
nav: Providers
network: true
overview: 'California ISO publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, United States, Electricity, Energy Markets, and Grid.


  California ISO''s developer surface includes documentation, signup flow, authentication, developer portal, support, engineering blog, getting-started guide, and 20 more developer resources.'
random_paper: 47
rate_limits:
- limit_count: 3
  name: Caiso Rate Limits
  slug: caiso-rate-limits
score:
  band: thin
  composite: 34.3
  delta: -3.6
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 52.2
    discoverability: 87.0
    governance: 13.5
    operational_transparency: 52.6
  previous_composite: 37.9
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 33.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Caiso Authentication
  slug: caiso-authentication
  summary_line: none/mutualTLS · 2 schemes
- kind: domain-security
  name: Caiso Domain Security
  slug: caiso-domain-security
  summary_line: TLSv1.3 · DMARC
slug: caiso
tags:
- Energy
- United States
- Electricity
- Energy Markets
- Grid
- Renewables
- System Operator
- Market Data
- California
website: https://www.caiso.com/
---
