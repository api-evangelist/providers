---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.4
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Cortex Agentic Access
  operation_count: 28
  slug: cortex-agentic-access
  summary_line: 28 operations · 16 acting
api_count: 4
apis:
- description: Cortex exposes a Model Context Protocol (MCP) server that lets AI coding assistants and IDE agents query the service catalog, look up ownership, check scorecard scores, and run workflows directly from
  name: Cortex MCP Server
  slug: cortex-mcp
- description: The Catalog API from Cortex — 8 operation(s) for catalog.
  name: Cortex Catalog API
  slug: cortex-catalog-api
- description: The Scorecards API from Cortex — 7 operation(s) for scorecards.
  name: Cortex Scorecards API
  slug: cortex-scorecards-api
- description: The Teams API from Cortex — 5 operation(s) for teams.
  name: Cortex Teams API
  slug: cortex-teams-api
artifact_total: 12
collections:
- collection_type: open
  name: Cortex REST API
  slug: open-cortex
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cortex-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cortex-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cortex-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.cortex.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cortex.io/
- group: other
  title: ''
  type: Product
  url: https://www.cortex.io/product
- group: other
  title: ''
  type: ServiceCatalog
  url: https://www.cortex.io/product/service-catalog
- group: other
  title: ''
  type: Scorecards
  url: https://www.cortex.io/product/scorecards
- group: design
  title: ''
  type: Workflow
  url: https://www.cortex.io/product/workflows
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cortex.io/pricing
- group: other
  title: ''
  type: Customers
  url: https://www.cortex.io/customers
- group: company
  title: ''
  type: Blog
  url: https://www.cortex.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cortexapps
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.cortex.io/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cortex.io/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cortexapp/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/cortexapp
- group: operate
  title: ''
  type: Contact
  url: https://www.cortex.io/contact
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/cortexapps/cortex-mcp
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.cortex.io/llms.txt
created: '2026-03-16'
description: Cortex is an Engineering Operations (EngOps) platform and internal developer portal that helps engineering teams catalog services, enforce production readiness with scorecards, automate self-service workflows, and surface engineering intelligence across their organization. Cortex centralizes data from observability, CI/CD, source control, on-call, and SaaS tooling and exposes it through a REST API used to integrate the catalog with platform engineering and SRE workflows.
finops:
- name: Cortex Finops
  service_category: API
  slug: cortex-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cortex.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Cortex
nav: Providers
network: true
overview: 'Cortex publishes 3 APIs on the [APIs.io](https://apis.io/) network: Catalog API, Scorecards API, and Teams API. Tagged areas include Catalog, Custom Data, Dependencies, Deploys, and Developer Experience.


  Cortex''s developer surface includes authentication, documentation, pricing, engineering blog, changelog, and 15 more developer resources.'
plans:
- name: Cortex Plans Pricing
  plan_count: 3
  slug: cortex-plans-pricing
random_paper: 91
rate_limits:
- limit_count: 5
  name: Cortex Rate Limits
  slug: cortex-rate-limits
score:
  band: developing
  composite: 44.3
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 51.2
    developer_ergonomics: 30.4
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 68.4
  previous_composite: 44.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cortex/refs/heads/main/screenshots/cortex-2026-06-20T175126.png
security:
- kind: authentication
  name: Cortex Authentication
  slug: cortex-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cortex Domain Security
  slug: cortex-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cortex
tags:
- Catalog
- Custom Data
- Dependencies
- Deploys
- Developer Experience
- EngOps
- Engineering Intelligence
- Initiatives
- Internal Developer Portal
- On-call
- Platform Engineering
- Scorecards
- Service Catalog
- SRE
- Workflows
website: https://www.cortex.io/
---
