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
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: REST booking API for searching experiences, retrieving options and availability, and assembling and confirming booking orders. Authenticated with an X-API-Key header; versioned in the URI path (/v2).
  name: Turneo v2 API
  slug: turneo-v2-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.turneo.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.turneo.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://www.turneo.com/developers/guides
- group: docs
  title: ''
  type: APIReference
  url: https://www.turneo.com/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://www.turneo.com/developers/guides/getting-started
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.turneo.com
- group: company
  title: ''
  type: Blog
  url: https://www.turneo.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.turneo.com/partner-terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.turneo.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://app.turneo.co
- group: auth
  title: ''
  type: Authentication
  url: authentication/turneo-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/turneo-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/turneo-components.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/turneo-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/turneo-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/turneo-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/turneo-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/turneo-domain-security.yml
created: '2026-07-17'
description: Turneo is an operating system for hotel experiences and services, backed by Bessemer Venture Partners. It digitizes the activities, spa & wellness, dining, rentals, transfers, and tickets a hotel offers, makes them bookable across guest touchpoints, and deploys AI agents to automate the operations behind them. Hotels and partners integrate through the Turneo v2 REST API (https://api.turneo.co, API-key authenticated) to search experiences, retrieve options and availability, and assemble and confirm booking orders, and through embeddable Turneo Elements widgets that add browse-and-book surfaces (with Apple Pay) directly to a partner website. It also plugs into existing tools such as Bokun, OPERA Cloud, apaleo, MEWS, and REGIONDO.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/turneo.png
layout: provider
modified: '2026-07-21'
name: Turneo
nav: Providers
network: true
overview: 'Turneo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketplaces, Travel, Hospitality, and Hotels.


  Turneo''s developer surface includes documentation, API reference, getting-started guide, engineering blog, authentication, and 13 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 24.5
  coverage:
    artifact_dirs: 10
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 24.5
  provenance:
    mcp: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/turneo/refs/heads/main/screenshots/turneo-2026-09-02T164536.png
security:
- kind: authentication
  name: Turneo Authentication
  slug: turneo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Turneo Domain Security
  slug: turneo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: turneo
tags:
- Company
- Marketplaces
- Travel
- Hospitality
- Hotels
- Experience
- Booking
- Activities
- Tours
website: https://www.turneo.com/
---
