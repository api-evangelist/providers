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
  url: security/vendease-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vendease.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Vendease
- group: docs
  title: ''
  type: Documentation
  url: https://vendease.github.io/vendease-docs/
- group: build
  title: ''
  type: Packages
  url: packages/vendease-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vendease-llms.txt
created: '2026-07-17'
description: Vendease is a Nigerian B2B food procurement platform (founded 2020, Y Combinator W21, backed by Partech Africa and TLcom) that helps restaurants, hotels, and other food businesses buy fresh and processed food supplies, offering Buy Now, Pay Later financing, supplier consolidation, cold-chain logistics, and 24-hour delivery in Lagos. Vendease publishes no public developer API or SDKs; its procurement, payments, inventory, and tenant management service APIs are internal-only, though its engineering handover documentation is publicly available on GitHub.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vendease.png
layout: provider
modified: '2026-07-21'
name: Vendease
nav: Providers
network: true
overview: 'Vendease is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketplace, Food, Procurement, and Food Tech.


  Vendease''s developer surface includes documentation and 5 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 7.2
  coverage:
    artifact_dirs: 4
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
    operational_transparency: 2.6
  previous_composite: 7.2
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Vendease Domain Security
  slug: vendease-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: vendease
tags:
- Company
- Marketplace
- Food
- Procurement
- Food Tech
- BNPL
- Logistics
- Nigeria
- Africa
website: https://vendease.com/
---
