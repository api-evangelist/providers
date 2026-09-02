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
api_count: 1
apis:
- description: World Data
  name: World Bank
  slug: world-bank
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/world-bank-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://blogs.worldbank.org/en
- group: company
  title: ''
  type: Website
  url: https://datahelpdesk.worldbank.org/knowledgebase/topics/125589
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: World Data
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/world-bank.png
layout: provider
modified: '2026-05-28'
name: World Bank
nav: Providers
network: true
overview: 'World Bank publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Science And Math and Public APIs.


  World Bank''s developer surface includes engineering blog and 3 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 8.1
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
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/world-bank/refs/heads/main/screenshots/world-bank-2026-06-20T201614.png
security:
- kind: domain-security
  name: World Bank Domain Security
  slug: world-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: world-bank
tags:
- Science And Math
- Public APIs
website: https://datahelpdesk.worldbank.org/knowledgebase/topics/125589
---
