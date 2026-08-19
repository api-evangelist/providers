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
    agent_skills: derived
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.4
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: Trellis property contracts generated from Hono/Zod schemas.
  name: Trellis properties API
  slug: trellistech-properties-api
- description: Trellis task contracts generated from Hono/Zod schemas.
  name: Trellis tasks API
  slug: trellistech-tasks-api
artifact_total: 8
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Trellis Public API v1 properties API
  slug: open-trellistech-properties-api
- collection_type: open
  name: Trellis Public API v1 properties tasks API
  slug: open-trellistech-tasks-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/trellistech-public-api-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/trellistech-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/trellistech-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/trellistech-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/trellistech-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/trellistech-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/trellistech-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.trellistech.com
- group: agent
  title: ''
  type: WellKnown
  url: well-known/trellistech-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trellistech-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.trellistech.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.trellistech.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.trellistech.com/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.trellistech.com/quickstart
- group: company
  title: ''
  type: Blog
  url: https://www.trellistech.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trellis-tech
- group: start
  title: ''
  type: SignUp
  url: https://app.trellistech.com
- group: operate
  title: ''
  type: Support
  url: mailto:support@trellistech.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.trellistech.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.trellistech.com/privacy
- group: company
  title: ''
  type: Website
  url: https://www.trellistech.com
created: '2026-07-17'
description: Trellis (Trellistech) is a Y Combinator-backed, AI-powered property operations platform for short-term and vacation rental operators. Trellis deploys AI agents across an operator's entire business - handling guest communications, coordinating field teams, and running day-to-day operations such as tasks, workforce scheduling, accounting, reviews, and the guest portal. For developers, Trellis publishes a versioned public REST API for CRUD access to tasks and properties, an official hosted MCP server (@trellistech/mcp-server) that exposes operational read and gated write tools to any MCP-compatible AI client, and connectors for property and finance systems including Guesty, Hostaway, Breezeway, Calry, Krossbooking, and Ramp.
image: https://www.trellistech.com/trellis-icon.svg
layout: provider
mcp_servers:
- description: ''
  name: trellistech-mcp.yml
  slug: trellistech-mcpyml
modified: '2026-07-21'
name: Trellis
nav: Providers
network: true
overview: 'Trellis publishes 2 APIs on the [APIs.io](https://apis.io/) network: properties API and tasks API. Tagged areas include Company, Property Management, Vacation Rentals, Short-Term Rentals, and AI Agents.


  Trellis'' developer surface includes CLI, changelog, documentation, API reference, getting-started guide, engineering blog, signup flow, and 15 more developer resources.'
random_paper: 144
score:
  band: developing
  composite: 42.0
  delta: -3.5
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 16.7
    contract_quality: 51.7
    developer_ergonomics: 54.2
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 34.2
  previous_composite: 45.5
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trellistech/refs/heads/main/screenshots/trellistech-2026-08-17T082435.png
security:
- kind: authentication
  name: Trellistech Authentication
  slug: trellistech-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Trellistech Domain Security
  slug: trellistech-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: trellistech
tags:
- Company
- Property Management
- Vacation Rentals
- Short-Term Rentals
- AI Agents
- Operations
- Hospitality
- Task Management
- Model Context Protocol
website: https://www.trellistech.com
---
