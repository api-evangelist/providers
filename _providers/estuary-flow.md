---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-12'
api_count: 4
apis:
- description: REST/JSON API backing the Estuary Flow web dashboard and flowctl CLI. Manages captures, collections, materializations, derivations, drafts, publications, tenants, and role grants. Authenticated with a
  name: Estuary Flow Agent API
  slug: agent-api
- description: OpenMetrics-compatible endpoint that exposes per-task pipeline metrics for captures, materializations, and derivations. Designed to be scraped by Prometheus or other OpenMetrics-aware observability sy
  name: Estuary Flow OpenMetrics API
  slug: openmetrics-api
- description: 'Command-line tool for authoring, drafting, testing, and publishing Flow catalogs (captures, collections, derivations, materializations). Wraps the Flow agent API and integrates with local development '
  name: flowctl CLI
  slug: flowctl-cli
- description: Open-source library of source and destination connectors for SaaS apps, databases, message queues, warehouses, lakehouses, and file systems. Connectors run inside the Flow runtime and are configured a
  name: Estuary Flow Connectors
  slug: connectors
artifact_total: 8
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/estuary/flow/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/estuary/flow/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/estuary/flow/blob/master/CONTRIBUTING.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/estuary-flow-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://estuary.dev
- group: start
  title: ''
  type: Portal
  url: https://docs.estuary.dev
- group: docs
  title: ''
  type: Documentation
  url: https://docs.estuary.dev
- group: start
  title: ''
  type: Signup
  url: https://dashboard.estuary.dev/register
- group: start
  title: ''
  type: Login
  url: https://dashboard.estuary.dev
- group: other
  title: ''
  type: Dashboard
  url: https://dashboard.estuary.dev
- group: commercial
  title: ''
  type: Pricing
  url: https://estuary.dev/pricing/
- group: company
  title: ''
  type: Blog
  url: https://estuary.dev/blog/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/estuary
- group: other
  title: ''
  type: Repository
  url: https://github.com/estuary/flow
- group: build
  title: ''
  type: CLI
  url: https://docs.estuary.dev/concepts/flowctl/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://estuary.dev/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://estuary.dev/privacy/
- group: operate
  title: ''
  type: Support
  url: https://estuary.dev/contact-us/
- group: operate
  title: ''
  type: Community
  url: https://go.estuary.dev/slack
- group: agent
  title: ''
  type: LlmsText
  url: https://estuary.dev/llms.txt
created: '2026-05-23'
description: Estuary Flow is a real-time data movement and transformation platform combining streaming infrastructure, a runtime, and an open-source ecosystem of connectors. It supports change data capture (CDC), SaaS integration, database replication, streaming lakehouse, and real-time analytics pipelines. Users build pipelines as captures, collections, derivations, and materializations - manageable from the web dashboard, the flowctl CLI, and a REST/agent API.
finops:
- name: Estuary Flow Finops
  service_category: API
  slug: estuary-flow-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/estuary-flow.png
layout: provider
modified: '2026-05-23'
name: Estuary Flow
nav: Providers
network: true
overview: 'Estuary Flow publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Data, Streaming, Change Data Capture, CDC, and ETL.


  Estuary Flow''s developer surface includes developer portal, documentation, signup flow, pricing, engineering blog, GitHub presence, CLI, and 13 more developer resources.'
plans:
- name: Estuary Flow Plans Pricing
  plan_count: 1
  slug: estuary-flow-plans-pricing
random_paper: 66
rate_limits:
- limit_count: 2
  name: Estuary Flow Rate Limits
  slug: estuary-flow-rate-limits
score:
  band: thin
  composite: 34.4
  delta: 0.0
  facets:
    commercial_clarity: 73.7
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 34.4
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/estuary-flow/refs/heads/main/screenshots/estuary-flow-2026-06-20T180830.png
security:
- kind: domain-security
  name: Estuary Flow Domain Security
  slug: estuary-flow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: estuary-flow
tags:
- Data
- Streaming
- Change Data Capture
- CDC
- ETL
- ELT
- Real-Time
- Data Pipelines
- Connectors
- Lakehouse
website: https://estuary.dev
---
