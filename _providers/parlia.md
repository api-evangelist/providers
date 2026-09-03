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
  url: security/parlia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://parlia.com/
- group: company
  title: ''
  type: About
  url: https://www.parlia.com/about
created: '2026-07-17'
description: Parlia is the "encyclopedia of opinion," a London-based collaborative content platform founded by Turi Munthe and J. Paul Neeley that maps the world's arguments and opinions the way Wikipedia maps facts. Launched in January 2020 from Somerset House Exchange, it lets a community document, compare, and debate perspectives across politics, technology, and culture in calm, descriptive language, and publishes the "On Opinion with Turi Munthe" podcast. Parlia is a consumer-facing web product; the enrichment pass found no public developer API, SDKs, or OpenAPI surface. It is tracked here as a Bloomberg Beta portfolio company.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/parlia.png
layout: provider
modified: '2026-07-20'
name: Parlia
nav: Providers
network: true
overview: Parlia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Opinion, Content, Media, and Debate.
random_paper: 3
score:
  band: minimal
  composite: 3.4
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
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 3.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/parlia/refs/heads/main/screenshots/parlia-2026-08-07T191447.png
security:
- kind: domain-security
  name: Parlia Domain Security
  slug: parlia-domain-security
  summary_line: TLSv1.3 · DMARC
slug: parlia
tags:
- Company
- Opinion
- Content
- Media
- Debate
- Knowledge Base
- Civic Technology
website: https://parlia.com/
---
