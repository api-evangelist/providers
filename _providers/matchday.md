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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/matchday-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://matchday.com
- group: start
  title: ''
  type: Portal
  url: https://matchday.com
created: '2026-07-17'
description: 'Matchday is a consumer mobile platform for collecting officially licensed digital football (soccer) player cards and building a squad, surfaced in the API Evangelist network as a portfolio company of Andreessen Horowitz (a16z). The product is a business-to-consumer collecting and squad-building experience delivered through its mobile apps and website at matchday.com. As of this enrichment pass, Matchday does not publish a public developer API, developer portal, OpenAPI specification, or documentation surface: probing api.matchday.com, docs.matchday.com, and developer.matchday.com returned no reachable developer hosts, and the marketing site is a single-page application. This profile therefore carries company identity plus a domain-security probe rather than API artifacts, and remains a lead to revisit if a public API surface is launched.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/matchday.png
layout: provider
modified: '2026-07-20'
name: Matchday
nav: Providers
network: true
overview: 'Matchday is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sports, Football, Soccer, and Collectibles.


  Matchday''s developer surface includes developer portal and 2 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 6.9
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/matchday/refs/heads/main/screenshots/matchday-2026-07-25T230346.png
security:
- kind: domain-security
  name: Matchday Domain Security
  slug: matchday-domain-security
  summary_line: TLSv1.3 · DMARC
slug: matchday
tags:
- Company
- Sports
- Football
- Soccer
- Collectibles
- Digital Collectibles
- Gaming
- Consumer
- Mobile
website: https://matchday.com
---
