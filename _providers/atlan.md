---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-10'
api_count: 3
apis:
- description: The core REST API for the Atlan platform, providing programmatic access to all platform capabilities including asset management, data lineage, glossary terms, classifications, custom metadata, persona
  name: Atlan REST API
  slug: atlan-rest-api
- description: GraphQL interface for querying Atlan's knowledge graph, enabling flexible traversal of metadata relationships including asset lineage, classifications, tags, business glossary links, and governance po
  name: Atlan GraphQL API
  slug: atlan-graphql-api
- description: Real-time event webhooks that capture and deliver notifications when metadata changes occur within the Atlan platform, enabling downstream integrations, automation pipelines, and event-driven governan
  name: Atlan Webhooks API
  slug: atlan-webhooks-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/atlan-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/atlan-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://atlan.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.atlan.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/atlanhq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/atlan-hq/
- group: company
  title: ''
  type: Blog
  url: https://blog.atlan.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://atlan.com/data-catalog-pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.atlan.com/
- group: other
  title: ''
  type: X
  url: https://x.com/atlanhq
- group: commercial
  title: ''
  type: Plans
  url: plans/atlan-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/atlan-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/atlan-finops.yml
created: '2026-06-13'
description: Atlan is a data catalog and metadata management platform — the Context Layer for AI — that unifies metadata from 80+ business systems into a single knowledge graph. It provides REST and GraphQL APIs for managing data assets, lineage, classifications, glossary terms, and data governance workflows. Customers execute 10,000+ API calls per week powering automated documentation, metadata enrichment, and custom integrations across the modern data stack.
finops:
- name: Atlan Finops
  service_category: ''
  slug: atlan-finops
graphqls:
- description: Atlan exposes a tenant-scoped GraphQL API that provides flexible querying of the platform's knowledge graph — the unified metadata layer spanning 80+ data sources. Through GraphQL, clients can travers
  name: Atlan GraphQL API
  slug: atlan-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/atlan.png
jsonld:
- class_count: 7
  name: Atlan Context
  property_count: 29
  slug: atlan-context
layout: provider
modified: '2026-06-13'
name: Atlan
nav: Providers
network: true
overview: 'Atlan publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Data Catalog, Metadata Management, Data Governance, Data Lineage, and GraphQL.


  The Atlan catalog on APIs.io includes 1 JSON-LD context.


  Atlan''s developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Atlan Plans Pricing
  plan_count: 3
  slug: atlan-plans-pricing
random_paper: 64
rate_limits:
- limit_count: 0
  name: Atlan Rate Limits
  slug: atlan-rate-limits
score:
  band: thin
  composite: 36.5
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 56.8
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 36.5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/atlan/refs/heads/main/screenshots/atlan-2026-06-20T172523.png
security:
- kind: domain-security
  name: Atlan Domain Security
  slug: atlan-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Atlan Vulnerability Disclosure
  slug: atlan-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: atlan
tags:
- Data Catalog
- Metadata Management
- Data Governance
- Data Lineage
- GraphQL
- REST
- AI
- Analytics
website: https://atlan.com/
---
