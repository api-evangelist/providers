---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
  - security
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.2
  scored_at: '2026-09-05'
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
random_paper: 2
rate_limits:
- limit_count: 3
  name: Caiso Rate Limits
  slug: caiso-rate-limits
score:
  band: thin
  composite: 38.1
  coverage:
    artifact_dirs: 15
    catalog_earned: 54.0
    catalog_earned_first_party: 17.0
    catalog_gap: 61.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 19.7
    contract_quality: 6.7
    developer_ergonomics: 57.1
    discoverability: 68.5
    governance: 19.7
    operational_transparency: 52.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 38.1
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 33.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/caiso/refs/heads/main/screenshots/caiso-2026-08-07T162911.png
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
