---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: Partner-only integration surface advertised through the Carahsoft Developer Center covering accounts, quotes, orders, invoices, price lists, purchase orders, and resource distribution. Access requires
  name: Carahsoft Partner API
  slug: partner-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/carahsoft-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/carahsoft
- group: company
  title: ''
  type: Website
  url: https://www.carahsoft.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.carahsoft.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.carahsoft.com/
- group: other
  title: ''
  type: Contract Vehicles
  url: https://www.carahsoft.com/contracts
- group: operate
  title: ''
  type: Contact
  url: https://www.carahsoft.com/contact
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/carahsoft
created: '2026-05-11'
description: Carahsoft Technology Corp. is a master government IT solutions aggregator and distributor that resells software, cloud, and cybersecurity products from hundreds of technology vendors to U.S. federal, state, local, defense, intelligence, healthcare, and education customers across 220+ government contract vehicles. Carahsoft operates a partner-facing Developer Center that exposes partner integrations for accounts, quotes, orders, invoices, price lists, purchase orders, and resources; the underlying API is gated behind a partner account and is not a public REST API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/carahsoft.png
layout: provider
modified: '2026-05-11'
name: Carahsoft
nav: Providers
network: true
overview: 'Carahsoft publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Government IT, Public Sector, Reseller, Distributor, and Procurement.


  Carahsoft''s developer surface includes documentation and 7 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 10.2
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 10.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/carahsoft/refs/heads/main/screenshots/carahsoft-2026-06-20T173947.png
security:
- kind: domain-security
  name: Carahsoft Domain Security
  slug: carahsoft-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: carahsoft
tags:
- Government IT
- Public Sector
- Reseller
- Distributor
- Procurement
- Contract Vehicles
- Federal
- State and Local
website: https://www.carahsoft.com
---
