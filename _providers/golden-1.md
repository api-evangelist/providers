---
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
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/golden-1-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.golden1.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/golden-1-credit-union
created: '2026-07-23'
description: Golden 1 Credit Union is a state-chartered, member-owned not-for-profit financial cooperative headquartered in Sacramento, California, and is one of the largest credit unions in the United States, serving roughly 1.1 million members across California with approximately 20 billion dollars in assets. Founded in 1933 and open to all Californians, it offers consumer checking, savings, credit cards, auto and home loans, and digital banking, and holds the naming rights to Golden 1 Center in Sacramento. Like most US credit unions, Golden 1 publishes NO public developer portal and NO first-party public API; its digital banking runs on a core-provider platform, and consumer-permissioned account data is reachable only indirectly through third-party data aggregators (Plaid, MX, Finicity, Akoya) rather than a documented first-party open-finance API. US open finance is voluntary and fragmented, and this institution's public API surface is honestly empty as of this record.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Golden 1 Credit Union
nav: Providers
network: true
overview: Golden 1 Credit Union is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Banking, Credit Union, United States, and Consumer Finance.
random_paper: 13
score:
  band: minimal
  composite: 1.5
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
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 1.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/golden-1/refs/heads/main/screenshots/golden-1-2026-07-25T220025.png
security:
- kind: domain-security
  name: Golden 1 Domain Security
  slug: golden-1-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: golden-1
tags:
- Financial-Services
- Banking
- Credit Union
- United States
- Consumer Finance
- Open Finance
- Data Aggregation
website: https://www.golden1.com/
---
