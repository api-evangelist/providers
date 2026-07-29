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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 60.4
  scored_at: '2026-07-28'
api_count: 6
apis:
- description: The Bridges API from Starbridge — 4 operation(s) for bridges.
  name: Starbridge Bridges API
  slug: starbridge-bridges-api
- description: The Buyer API from Starbridge — 4 operation(s) for buyer.
  name: Starbridge Buyer API
  slug: starbridge-buyer-api
- description: The Columns API from Starbridge — 1 operation(s) for columns.
  name: Starbridge Columns API
  slug: starbridge-columns-api
- description: The External API API from Starbridge — 11 operation(s) for external api.
  name: Starbridge External API API
  slug: starbridge-external-api-api
- description: The External MCP API from Starbridge — 11 operation(s) for external mcp.
  name: Starbridge External MCP API
  slug: starbridge-external-mcp-api
- description: The Signal API from Starbridge — 2 operation(s) for signal.
  name: Starbridge Signal API
  slug: starbridge-signal-api
artifact_total: 10
asyncapis:
- description: ''
  name: Starbridge Webhooks
  slug: starbridge-webhooks
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/starbridge-openapi.json
- group: agent
  title: ''
  type: MCPServer
  url: mcp/starbridge-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/starbridge-llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/starbridge-webhooks.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/starbridge-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/starbridge-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/starbridge-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/starbridge-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/starbridge-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: lifecycle/starbridge-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/starbridge-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/starbridge-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/starbridge-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/starbridge-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/starbridge-domain-security.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/starbridge-openapi-overlay.yaml
- group: docs
  title: ''
  type: Documentation
  url: https://hc.starbridge.ai
- group: docs
  title: ''
  type: APIReference
  url: https://hc.starbridge.ai/api-reference/rest/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://hc.starbridge.ai/api-reference/rest/generating-an-api-key
- group: operate
  title: ''
  type: HelpCenter
  url: https://hc.starbridge.ai
- group: company
  title: ''
  type: Blog
  url: https://starbridge.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/starbridge-ai
- group: start
  title: ''
  type: SignUp
  url: https://auth.starbridge.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://starbridge.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://starbridge.ai/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://starbridge.ai
created: '2026-07-17'
description: Starbridge is an AI-powered go-to-market and sales-intelligence platform for vendors selling to the public sector and education — government agencies, K-12 school districts, and higher-education institutions. It surfaces early buying signals (RFPs, board meetings, purchases, conferences, contact and job changes), scores and enriches target accounts, and drafts personalized outbound and RFP responses. Starbridge exposes an external REST API (Bearer API keys), Ed25519-signed webhooks, and a hosted OAuth MCP server, plus published Agent Skills, so buyer intelligence can be pulled into CRMs (Salesforce, HubSpot), Slack, Zapier, and AI agents. Backed by Craft Ventures.
image: https://cdn.prod.website-files.com/68a834f29776727eae1bc0f6/694fa319b9cd6a197c7be433_1_Starbridge%20Homepage%20OpenGraph.webp
layout: provider
mcp_servers:
- description: ''
  name: starbridge-mcp.yml
  slug: starbridge-mcpyml
modified: '2026-07-21'
name: Starbridge
nav: Providers
network: true
overview: 'Starbridge publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Bridges API, Buyer API, Columns API, and 3 more. Tagged areas include Company, Ai, Sales Intelligence, Go To Market, and Public Sector.


  The Starbridge catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Starbridge''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, engineering blog, signup flow, and 20 more developer resources.'
random_paper: 36
score:
  band: developing
  composite: 51.4
  delta: -0.8
  facets:
    commercial_clarity: 34.2
    contract_quality: 68.9
    developer_ergonomics: 58.7
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 44.7
  previous_composite: 52.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 46.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Starbridge Authentication
  slug: starbridge-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Starbridge Domain Security
  slug: starbridge-domain-security
  summary_line: TLSv1.3 · DMARC
slug: starbridge
tags:
- Company
- Ai
- Sales Intelligence
- Go To Market
- Public Sector
- Education
- Government
- Procurement
- Buyer Intelligence
- MCP
website: https://starbridge.ai
---
