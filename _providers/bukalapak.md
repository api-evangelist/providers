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
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Bukalapak's public REST API for marketplace resources such as products and the authenticated user profile, secured with OAuth2 (client_credentials and resource-owner password grants) issued by account
  name: Bukalapak REST API
  slug: bukalapak-rest-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://bukalapak.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bukalapak
- group: auth
  title: ''
  type: Authentication
  url: authentication/bukalapak-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/bukalapak-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/bukalapak-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bukalapak-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bukalapak-llms.txt
created: '2026-07-17'
description: 'Bukalapak is one of Indonesia''s largest online marketplaces and all-commerce platforms, connecting millions of individual sellers, small warungs (kiosks), and buyers across the archipelago, alongside virtual products, financial services, and online-to-offline retail. Originally added to the API Evangelist network as a portfolio-lead stub (backed by 500 Global), this profile has been enriched from Bukalapak''s real public developer surface: a public REST API at api.bukalapak.com secured with OAuth2 via accounts.bukalapak.com, a first-party JavaScript SDK (bukalapak.js), and a large public GitHub organization. No OpenAPI/Swagger specification is currently published by the provider, so the captured artifacts (authentication, packages, domain security) are sourced from first-party repositories and live domain probes rather than derived from a spec.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bukalapak.png
layout: provider
modified: '2026-07-18'
name: Bukalapak
nav: Providers
network: true
overview: 'Bukalapak publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Marketplace, Retail, and Indonesia.


  Bukalapak''s developer surface includes authentication and 6 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 9.7
  coverage:
    artifact_dirs: 4
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 9.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Bukalapak Authentication
  slug: bukalapak-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Bukalapak Domain Security
  slug: bukalapak-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bukalapak
tags:
- Company
- E-Commerce
- Marketplace
- Retail
- Indonesia
- Southeast Asia
- Payments
- Authentication
website: https://bukalapak.com
---
