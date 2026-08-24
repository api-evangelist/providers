---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.9
  scored_at: '2026-08-24'
api_count: 2
apis:
- description: The Rokid Glass3 / Sprite Enterprise cloud API. Device registration lookup and real-time telemetry, message push to glasses, paged AI agent chat logs, RTC remote-collaboration meeting history and part
  name: Rokid Sprite Enterprise OpenAPI
  slug: rokid-sprite-enterprise-openapi
- description: Rokid's global storefront implements the Universal Commerce Protocol for agent-driven commerce, with a UCP merchant profile at /.well-known/ucp and a live MCP endpoint exposing catalog search, cart, c
  name: Rokid Store Agent Commerce API
  slug: rokid-store-agent-commerce-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rokid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.rokid.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://open.rokid.com/
- group: docs
  title: ''
  type: Documentation
  url: https://x-docs.rokid.com/docs/en/
- group: docs
  title: ''
  type: APIReference
  url: https://x-docs.rokid.com/docs/en/openapi/ApiKey.html
- group: start
  title: ''
  type: GettingStarted
  url: https://x-docs.rokid.com/docs/en/terminal-sdk/getting-started/%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B.html
- group: operate
  title: ''
  type: Support
  url: https://forum.rokid.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://global.rokid.com/pages/support
- group: company
  title: ''
  type: Blog
  url: https://global.rokid.com/blogs/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Rokid
- group: start
  title: ''
  type: Login
  url: https://global.rokid.com/account/login
- group: commercial
  title: ''
  type: Pricing
  url: https://global.rokid.com/collections/all
- group: commercial
  title: ''
  type: TermsOfService
  url: https://global.rokid.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://global.rokid.com/policies/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/rokid-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/rokid-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rokid-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/rokid-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rokid-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/rokid-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rokid-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/rokid-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/rokid-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/rokid-cli.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/rokid-protobuf.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/rokid-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rokid-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/rokid-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-05'
description: Rokid is a Chinese AR and AI wearables company that designs smart glasses and the operating system that runs on them. Its consumer line spans Rokid Glasses, Rokid AI Glasses Style, Rokid AR Spatial and Rokid Max 2, and its enterprise line is Rokid Glass3 / Sprite, backed by the YodaOS and YodaOS-Sprite operating systems. Rokid exposes three distinct developer surfaces. The Sprite Enterprise cloud OpenAPI at api.rokid.com covers device management, message push to glasses, AI agent chat logs, RTC remote-collaboration meeting history and AI work-assistant task records, authenticated with a bearer API key issued by sales. Terminal SDKs for the glasses and the companion phone are distributed from Rokid's own Maven repository at maven.rokid.com, with a dated release changelog and a provider-published Agent Skill package for AI coding tools. Separately, the global storefront implements the Universal Commerce Protocol with a live MCP endpoint, an llms.txt and an agents.md for buying
  agents.
image: https://static.rokidcdn.com/web_assets/site/og-image.jpg
layout: provider
mcp_servers:
- description: ''
  name: Rokid MCP Server
  slug: rokid-mcp-server
modified: '2026-08-05'
name: Rokid
nav: Providers
network: true
overview: 'Rokid publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Smart Glasses, Augmented Reality, Wearables, Artificial Intelligence, and Spatial Computing.


  Rokid''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, authentication, and 22 more developer resources.'
random_paper: 12
score:
  band: developing
  composite: 42.6
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 18.2
    contract_quality: 28.2
    developer_ergonomics: 78.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 42.6
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Rokid Authentication
  slug: rokid-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Rokid Domain Security
  slug: rokid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rokid
tags:
- Smart Glasses
- Augmented Reality
- Wearables
- Artificial Intelligence
- Spatial Computing
- Device Management
- Consumer Electronics
- Voice
- Enterprise
- Hardware
- Agents
website: https://www.rokid.com/
---
