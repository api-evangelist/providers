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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.oracle.com/cx/marketing/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/datafox-domain-security.yml
created: '2026-07-17'
description: 'DataFox was a San Francisco company-intelligence and sales-prospecting startup, backed by GV among others, that used machine learning to collect and score signals about private and public companies (funding rounds, hiring, news, growth signals) and delivered them to sales and marketing teams through a web application, CRM integrations, and a company-data API. Oracle acquired DataFox and folded its company-and-signals data into the Oracle Cloud CX / Oracle Fusion Marketing stack. The independent product has been fully retired: as of this profile the datafox.com apex and www hosts are served from Oracle infrastructure and every path under www.datafox.com issues a blanket HTTP 301 to Oracle marketing pages, while api.datafox.com and app.datafox.com resolve to a parked Oracle address that accepts no connections. There is no surviving DataFox developer portal, documentation, API reference, or specification to harvest, so this profile is retained as a historical/acquired company
  record rather than an active API provider.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/datafox.png
layout: provider
modified: '2026-07-20'
name: DataFox
nav: Providers
network: true
overview: DataFox is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Company Data, Sales Intelligence, and Data Enrichment.
random_paper: 8
score:
  band: minimal
  composite: 5.0
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
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 5.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/datafox/refs/heads/main/screenshots/datafox-2026-07-25T211315.png
security:
- kind: domain-security
  name: Datafox Domain Security
  slug: datafox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: datafox
tags:
- Company
- Enterprise
- Company Data
- Sales Intelligence
- Data Enrichment
- Machine Learning
- Acquired
- Oracle
website: https://www.oracle.com/cx/marketing/
---
