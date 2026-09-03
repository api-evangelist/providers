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
  url: security/infarm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://infarm.com/
created: '2026-07-17'
description: infarm (Indoor Urban Farming GmbH) is a Berlin-based vertical/indoor farming company, surfaced as a portfolio company of balderton-capital and added to the API Evangelist network. The company builds modular, cloud-connected growing systems for herbs, leafy greens, and produce placed in grocery stores and distribution hubs. This profile was enriched by the pipeline; infarm publishes no public developer API, OpenAPI, SDK, or documentation surface, and its website is bot-blocked (HTTP 403) to automated access, so only domain-level security posture could be probed. It remains a company/identity record rather than an API provider.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/infarm.png
layout: provider
modified: '2026-07-19'
name: infarm
nav: Providers
network: true
overview: infarm is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Vertical Farming, Agriculture, AgTech, and Food.
random_paper: 7
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 1
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
  previous_composite: 5.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: domain-security
  name: Infarm Domain Security
  slug: infarm-domain-security
  summary_line: TLSv1.3
slug: infarm
tags:
- Company
- Vertical Farming
- Agriculture
- AgTech
- Food
- Sustainability
website: https://infarm.com/
---
