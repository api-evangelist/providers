---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 9
  human_in_the_loop: 1
  name: Estuary Agentic Access
  operation_count: 22
  slug: estuary-agentic-access
  summary_line: 22 operations · 9 acting · 1 human-in-the-loop
api_count: 8
apis:
- description: The Auth API from Estuary — 5 operation(s) for auth.
  name: Estuary Auth API
  slug: estuary-auth-api
- description: The Captures API from Estuary — 2 operation(s) for captures.
  name: Estuary Captures API
  slug: estuary-captures-api
- description: The Collections API from Estuary — 3 operation(s) for collections.
  name: Estuary Collections API
  slug: estuary-collections-api
- description: The Connectors API from Estuary — 3 operation(s) for connectors.
  name: Estuary Connectors API
  slug: estuary-connectors-api
- description: The Drafts API from Estuary — 3 operation(s) for drafts.
  name: Estuary Drafts API
  slug: estuary-drafts-api
- description: The Materializations API from Estuary — 2 operation(s) for materializations.
  name: Estuary Materializations API
  slug: estuary-materializations-api
- description: The Publications API from Estuary — 1 operation(s) for publications.
  name: Estuary Publications API
  slug: estuary-publications-api
- description: The Tenants API from Estuary — 3 operation(s) for tenants.
  name: Estuary Tenants API
  slug: estuary-tenants-api
artifact_total: 15
collections:
- collection_type: open
  name: Estuary Flow Control Plane API
  slug: open-estuary
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/estuary-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/estuary-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/estuary-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/estuary
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/estuary-tech
- group: company
  title: ''
  type: Website
  url: https://estuary.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.estuary.dev
- group: commercial
  title: ''
  type: Plans
  url: plans/estuary-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/estuary-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/estuary-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://estuary.dev/blog/rss.xml
created: '2026-07-01'
description: Estuary builds Estuary Flow, a real-time data movement platform for streaming ETL and change data capture (CDC). Flow captures data from databases, warehouses, and SaaS systems into durable collections and materializes those collections back out to destinations. The Flow control plane exposes a Supabase/PostgREST-based REST API (Bearer refresh/access tokens) covering captures, materializations, collections, catalog drafts and publications, connectors, and tenants/billing, while the data plane is driven declaratively via the flowctl CLI and a Gitops model.
finops:
- name: Estuary Finops
  service_category: Analytics
  slug: estuary-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/estuary.png
layout: provider
modified: '2026-07-01'
name: Estuary
nav: Providers
network: true
overview: 'Estuary publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Captures API, Collections API, and 5 more. Tagged areas include Data Integration, Streaming ETL, Change Data Capture, CDC, and Real-Time Data.


  Estuary''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Estuary Plans Pricing
  plan_count: 3
  slug: estuary-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Estuary Rate Limits
  slug: estuary-rate-limits
score:
  band: thin
  composite: 37.4
  delta: -2.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 51.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/estuary/refs/heads/main/screenshots/estuary-2026-07-25T213644.png
security:
- kind: authentication
  name: Estuary Authentication
  slug: estuary-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Estuary Domain Security
  slug: estuary-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: estuary
tags:
- Data Integration
- Streaming ETL
- Change Data Capture
- CDC
- Real-Time Data
- Data Pipelines
website: https://estuary.dev/
---
