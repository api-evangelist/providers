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
    agentic_commerce: false
    auth_clarity: false
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
  score: 0.0
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Heineken operates an internal API portal under its HEIWAY platform used for B2B and partner integrations (distributors, on-trade customers, and internal systems). The portal is reached via developer.h
  name: Heineken HEIWAY API Portal
  slug: heineken-heiway-api-portal
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/heineken-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/heineken-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/The-Heineken-Company
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/heineken
- group: company
  title: ''
  type: Website
  url: https://www.theheinekencompany.com/
- group: start
  title: ''
  type: Portal
  url: https://developer.heineken.com/
- group: company
  title: ''
  type: Blog
  url: https://www.theheinekencompany.com/newsroom
created: '2026-05-05'
description: A Dutch multinational brewing company and one of the world's largest beer producers. Operates over 165 breweries across 70 countries producing iconic brands including Heineken, Amstel, Tecate, and Dos Equis. Maintains an internal HEIWAY API portal (api-portal.production.az.heiway.com) used for partner, distributor, and on-trade B2B integrations; access is gated and not openly published.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/heineken.png
layout: provider
modified: '2026-05-16'
name: Heineken
nav: Providers
network: true
overview: 'Heineken publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Beverages, Consumer Goods, Manufacturing, and B2B Integration.


  Heineken''s developer surface includes developer portal, engineering blog, and 5 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 7.7
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 7.7
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/heineken/refs/heads/main/screenshots/heineken-2026-06-20T182617.png
security:
- kind: domain-security
  name: Heineken Domain Security
  slug: heineken-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Heineken Vulnerability Disclosure
  slug: heineken-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: heineken
tags:
- Beverages
- Consumer Goods
- Manufacturing
- B2B Integration
website: https://www.theheinekencompany.com/
---
