---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.7
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: RESTful API for programmatic access to Intellectible projects - list and run workflows synchronously, and manage Library files (create signed upload URLs, upload bytes, finalize, retrieve, list, and d
  name: Intellectible Public API
  slug: intellectible-public-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://intellectible.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.intellectible.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.intellectible.com/docs/guides/overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.intellectible.com/docs/api-reference/intro
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.intellectible.com/docs/editor-tutorials/tutorial-0-get-started
- group: company
  title: ''
  type: Blog
  url: https://intellectible.com/blog/
- group: start
  title: ''
  type: Login
  url: https://app.intellectible.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/intellectible-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/intellectible-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/intellectible-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/intellectible-conventions.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/intellectible-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/intellectible-domain-security.yml
created: '2026-07-17'
description: Intellectible is an AI build platform for enterprise service providers - federal and state government contractors (GovCon), professional services firms, and economic development organizations - that turns portals, emails, CRM data, and market signals into structured opportunity, proposal, pricing, and knowledge workflows. Its horizontal build environment (project workspaces, visual workflows, document libraries, PostgreSQL databases, applications, pages, jobs, and queues) is exposed programmatically through the Intellectible Public API and a Code Execution SDK, letting teams run workflows synchronously, manage Library files, and query project databases directly from code.
image: https://intellectible.com/
layout: provider
mcp_servers:
- description: ''
  name: intellectible-mcp.yml
  slug: intellectible-mcpyml
modified: '2026-07-19'
name: Intellectible
nav: Providers
network: true
overview: 'Intellectible publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Government, GovCon, and Proposals.


  Intellectible''s developer surface includes documentation, API reference, getting-started guide, engineering blog, authentication, and 8 more developer resources.'
random_paper: 46
score:
  band: emerging
  composite: 21.6
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 0.0
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 21.6
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 22.2
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/intellectible/refs/heads/main/screenshots/intellectible-2026-07-25T222643.png
security:
- kind: authentication
  name: Intellectible Authentication
  slug: intellectible-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Intellectible Domain Security
  slug: intellectible-domain-security
  summary_line: TLSv1.2 · HSTS
slug: intellectible
tags:
- Company
- Artificial Intelligence
- Government
- GovCon
- Proposals
- CRM
- Workflow Automation
- Pricing
- Knowledge Management
- Enterprise Software
- Professional Services
website: https://intellectible.com/
---
