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
  url: security/alkemics-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/alkemics-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/alkemics-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alkemics-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/alkemics
- group: company
  title: ''
  type: Website
  url: https://www.alkemics.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.supplierxm.salsify.com/reference
- group: other
  title: ''
  type: Company
  url: https://www.salsify.com/
coverage:
  checked: '2026-08-17'
  detail: Alkemics was fully absorbed by Salsify in October 2020 — alkemics.com and docs.alkemics.com now answer only HTTP 301 to salsify.com and docs.supplierxm.salsify.com, and api.alkemics.com returns NXDOMAIN, so there is no Alkemics-owned host left to serve a contract.
  evidence:
  - status: 301
    url: https://www.alkemics.com/
  - status: 301
    url: https://docs.alkemics.com/openapi.json
  - status: 0
    url: https://api.alkemics.com/
  - status: 301
    url: https://www.alkemics.com/.well-known/agent-card.json
  - status: 200
    url: https://github.com/alkemics
  reason: defunct
  state: none
created: '2026-07-17'
description: Alkemics was a French SaaS company founded in 2011 in Paris that operated a collaborative commerce platform connecting consumer packaged goods (CPG) brands and retailers to share, enrich, and distribute product content and data across the FMCG/grocery supply chain. Backed by investors including Partech, Cathay Innovation, and Serena, Alkemics was acquired by Salsify (a US product experience management company) in October 2020. The product now lives on as "SupplierXM by Salsify"; alkemics.com and docs.alkemics.com redirect to Salsify, and the successor developer documentation is hosted at docs.supplierxm.salsify.com. This company profile is preserved in the API Evangelist network with an honest acquisition/successor record. No independent Alkemics-owned API surface remains.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/alkemics.png
layout: provider
modified: '2026-08-17'
name: Alkemics
nav: Providers
network: true
overview: 'Alkemics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Applicative Saas, Product Content, Product Information Management, and CPG.


  Alkemics'' developer surface includes documentation and 7 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 8.3
  coverage:
    artifact_dirs: 6
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
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 8.3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alkemics/refs/heads/main/screenshots/alkemics-2026-07-25T195632.png
security:
- kind: domain-security
  name: Alkemics Domain Security
  slug: alkemics-domain-security
  summary_line: TLSv1.3 · HSTS
slug: alkemics
tags:
- Company
- Applicative Saas
- Product Content
- Product Information Management
- CPG
- Retail
- E-Commerce
- Data Syndication
- Acquired
website: https://www.alkemics.com/
---
