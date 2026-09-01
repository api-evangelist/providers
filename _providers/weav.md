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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 2.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: REST API for the Weav.ai Decisioning Platform, exposing document, folder, form, agent, workflow, action, and chat services used to build agentic insurance decisioning flows. Authenticated with a Beare
  name: Weav.ai Decisioning Platform API
  slug: weavai-decisioning-platform-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://weav.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://weav-ai.github.io/
- group: docs
  title: ''
  type: Documentation
  url: https://weav-ai.github.io/
- group: docs
  title: ''
  type: APIReference
  url: https://weav-ai.github.io/docs/platform/intro
- group: company
  title: ''
  type: Blog
  url: https://weav.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/weav-ai
- group: operate
  title: ''
  type: Support
  url: https://weav.ai/contact-us
- group: build
  title: ''
  type: Packages
  url: packages/weav-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/weav-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/weav-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/weav-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/weav-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/weav-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/weav-domain-security.yml
created: '2026-07-17'
description: Weav.ai is an AI-native decisioning platform for property & casualty (P&C) insurance, applying agentic AI and document intelligence across underwriting, premium audit, and claims. The platform pairs pre-configured, line-of-business knowledge graphs and scorecards with an agentic decision engine and human-in-the-loop review, delivered through an API-first, no-code architecture that integrates with existing insurance systems. Developers integrate via a documented REST surface (documents, folders, forms, agents, workflows, actions, and chat services) and a first-party Python developer library (weavaidev) published through the weav-ai GitHub organization, authenticated with a Bearer token against a per-tenant environment host. Weav.ai is backed by Sierra Ventures and is a member of the Guidewire Insurtech Vanguards program.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/weav.png
layout: provider
mcp_servers:
- description: ''
  name: Weav MCP Server
  slug: weav-mcp-server
modified: '2026-07-21'
name: Weav
nav: Providers
network: true
overview: 'Weav publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Insurance, Insurtech, and Underwriting.


  Weav''s developer surface includes documentation, API reference, engineering blog, support, authentication, and 9 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 16.1
  coverage:
    artifact_dirs: 8
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 16.1
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 18.2
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Weav Authentication
  slug: weav-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Weav Domain Security
  slug: weav-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: weav
tags:
- Company
- Artificial Intelligence
- Insurance
- Insurtech
- Underwriting
- Premium Audit
- Claims
- Document AI
- Property and Casualty
- Decisioning
website: https://weav.ai/
---
