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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nextgentel-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nextgentel.no
- group: operate
  title: ''
  type: Support
  url: https://hjelp.nextgentel.no
created: '2026-07-17'
description: NextGenTel is one of Norway's established independent internet service providers, delivering fiber and DSL broadband, TV (via RiksTV), mobile telephony, and online security services to consumers and small businesses across Norway. Surfaced as a portfolio company of Northzone and added to the API Evangelist network. An enrichment pass (2026-07-20) found a consumer-facing marketing and self-service website (www.nextgentel.no) and a customer help center (hjelp.nextgentel.no), but no public developer portal, API documentation, OpenAPI specification, or programmatic API surface — this remains a consumer telecom company with no external API program.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nextgentel.png
layout: provider
modified: '2026-07-20'
name: Nextgentel
nav: Providers
network: true
overview: 'Nextgentel is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Telecommunications, Broadband, and Internet Service Provider.


  Nextgentel''s developer surface includes support and 2 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 2.8
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
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 2.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 8.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nextgentel/refs/heads/main/screenshots/nextgentel-2026-08-07T185208.png
security:
- kind: domain-security
  name: Nextgentel Domain Security
  slug: nextgentel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nextgentel
tags:
- Company
- Consumer
- Telecommunications
- Broadband
- Internet Service Provider
- ISP
- Norway
- Fiber
- Television
- Mobile
website: https://www.nextgentel.no
---
