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
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 12.9
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Tenant-scoped REST API for the Gatekeeper contract and vendor management platform. Exposes vendors, contracts, employees, custom data, files, events, and workflows. The base URL and interactive docume
  name: Gatekeeper REST API
  slug: rest-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gatekeeper-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gatekeeper-vclm
- group: company
  title: ''
  type: Website
  url: https://www.gatekeeperhq.com
- group: docs
  title: ''
  type: Documentation
  url: https://knowledge.gatekeeperhq.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.gatekeeperhq.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://www.gatekeeperhq.com/demo
- group: operate
  title: ''
  type: Support
  url: https://knowledge.gatekeeperhq.com
- group: learn
  title: ''
  type: Academy
  url: https://academy.gatekeeperhq.com
- group: company
  title: ''
  type: Blog
  url: https://www.gatekeeperhq.com/blog/rss.xml
created: '2026-05-11'
description: Gatekeeper is a SaaS contract lifecycle management (CLM) and vendor management platform that helps procurement, legal, and finance teams capture, approve, store, and renew supplier contracts with workflow automation, e-signature, spend analytics, and risk monitoring. The Gatekeeper REST API exposes vendors, contracts, employees, custom data records, files, workflows, and events so customers can integrate Gatekeeper with ERP, HRIS, and finance systems. API access is per-tenant and authenticated with a tenant-specific API key.
graphqls:
- description: This conceptual GraphQL schema models the Gatekeeper contract lifecycle management (CLM) and vendor management platform. Gatekeeper provides procurement, legal, and finance teams with tools to capture
  name: Gatekeeper GraphQL Schema
  slug: gatekeeper-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gatekeeper.png
layout: provider
modified: '2026-05-11'
name: Gatekeeper
nav: Providers
network: true
overview: 'Gatekeeper publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Contract Management, Contract Lifecycle Management, Vendor Management, Procurement, and Supplier Management.


  Gatekeeper''s developer surface includes documentation, pricing, signup flow, support, academy / training, engineering blog, and 3 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 25.3
  coverage:
    artifact_dirs: 4
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 41.5
    developer_ergonomics: 16.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 25.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gatekeeper/refs/heads/main/screenshots/gatekeeper-2026-06-20T181653.png
security:
- kind: domain-security
  name: Gatekeeper Domain Security
  slug: gatekeeper-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gatekeeper
tags:
- Contract Management
- Contract Lifecycle Management
- Vendor Management
- Procurement
- Supplier Management
- Legal Tech
- Risk Management
- E-Signature
website: https://www.gatekeeperhq.com
---
