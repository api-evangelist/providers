---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.5
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 104
  human_in_the_loop: 0
  name: Happyrobot Agentic Access
  operation_count: 215
  slug: happyrobot-agentic-access
  summary_line: 215 operations · 104 acting
api_count: 6
apis:
- description: The current Happyrobot Public API (v2) — 205 operations over 162 paths, described by a live OpenAPI 3.0.3 document served from the API host at /api/v2/docs/json. Covers workflows, workflow folders and
  name: Happyrobot Public API
  slug: happyrobot-public-api
- description: The legacy v1 read API, described by an OpenAPI 3.0.2 document at /api/v1/openapi.json. Ten read-only operations covering runs, run recordings, use cases, workflow versions, issues and organization us
  name: Happyrobot Platform API v1
  slug: happyrobot-platform-api-v1
- description: 'EU data-residency mirror of the Happyrobot Public API, serving an identical OpenAPI 3.0.3 document with its own OAuth authorization server and its own MCP hosts. Selected in the SDKs and MCP packages '
  name: Happyrobot Public API (EU cluster)
  slug: happyrobot-public-api-eu-cluster
- description: Happyrobot's first-party remote MCP server for building and governing workflows — 26 published tools plus 5 MCP prompts, served over Streamable HTTP and protected by OAuth 2.0 (scope mcp:full, RFC 972
  name: Happyrobot Workflows MCP Server
  slug: happyrobot-workflows-mcp-server
- description: 'First-party remote MCP server over the customer''s Twin database — 9 published tools covering schema introspection, paginated reads, table creation, row insert/update/delete, table drop, and arbitrary '
  name: Happyrobot Twin MCP Server
  slug: happyrobot-twin-mcp-server
- description: A hosted documentation-search MCP server on the docs host, discovered via RFC 9728 protected-resource metadata at https://docs.happyrobot.ai/.well-known/oauth-protected-resource. It advertises a singl
  name: Happyrobot Docs MCP Server
  slug: happyrobot-docs-mcp-server
artifact_total: 18
asyncapis:
- description: ''
  name: Happyrobot Events
  slug: happyrobot-events
collections:
- collection_type: open
  name: Happyrobot Platform API
  slug: open-happyrobot-platform-v1
- collection_type: open
  name: Happyrobot Public API
  slug: open-happyrobot-public-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.happyrobot.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.happyrobot.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.happyrobot.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.happyrobot.ai/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.happyrobot.ai/getting_started
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.happyrobot.ai/general/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.happyrobot.ai/signup
- group: start
  title: ''
  type: Login
  url: https://app.happyrobot.ai/login
- group: company
  title: ''
  type: Blog
  url: https://www.happyrobot.ai/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.happyrobot.ai/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.happyrobot.ai/legal/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.happyrobot.ai/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/happyrobot-ai
- group: operate
  title: ''
  type: StatusPage
  url: https://status.happyrobot.ai/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.happyrobot.ai/
- group: auth
  title: ''
  type: Compliance
  url: https://www.happyrobot.ai/product/security-and-reliability
- group: auth
  title: ''
  type: Security
  url: https://happyrobot.ai/.well-known/security.txt
- group: build
  title: ''
  type: Packages
  url: packages/happyrobot-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/happyrobot-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/happyrobot-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/happyrobot-security.txt
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/happyrobot-openid-configuration.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/happyrobot-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/happyrobot-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/happyrobot-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/happyrobot-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/happyrobot-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/happyrobot-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/happyrobot-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/happyrobot-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/happyrobot-trust-center.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/happyrobot-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/happyrobot-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/happyrobot-events.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/happyrobot-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/happyrobot-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/happyrobot-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/happyrobot-llms.txt
- group: design
  title: ''
  type: Components
  url: components/happyrobot-components.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/happyrobot-public-api-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: https://mcp.platform.happyrobot.ai/workflows/mcp
created: '2026-08-01'
description: HappyRobot is an AI orchestration platform — "the AI operating system for the real economy" — that lets enterprises build, govern and deploy AI agents ("AI workers") into operational workflows across logistics, freight brokerage, 3PL, utilities, airlines, finance, insurance, manufacturing, retail and telecom. Agents place and answer phone calls, send and receive email, SMS, WhatsApp and chat, read and write to TMS/ERP systems, and execute multi-step workflows built as node graphs in a visual builder. The Happyrobot Public API (v2) exposes 205 operations across 32 resource families — workflows, versions and nodes, runs, sessions and messages, contacts and memories, knowledge bases, phone numbers and SIP trunks, integrations, chat and voice tokens, signals, billing, plus a full agent-governance surface (audits, northstars, custom evals, adversarial tests and suites). Authentication is a bearer API key scoped to an organization and an environment; the platform additionally runs
  an Auth0 OIDC tenant for human sign-in and an OAuth 2.0 authorization server for its MCP surface.
image: https://happyrobot.b-cdn.net/HappyRobot_HeroLoop_v01%20(00184)%201-1200x630.png
layout: provider
mcp_servers:
- description: ''
  name: Happyrobot MCP Server
  slug: happyrobot-mcp-server
- description: ''
  name: Happyrobot MCP Server
  slug: happyrobot-mcp-server-2
- description: ''
  name: Happyrobot MCP Server
  slug: happyrobot-mcp-server-3
modified: '2026-08-01'
name: Happyrobot
nav: Providers
network: true
overview: 'Happyrobot publishes 3 APIs on the [APIs.io](https://apis.io/) network: Public API, Platform API v1, and Public API (EU cluster). Tagged areas include AI Agents, Agent Orchestration, Voice AI, Conversational AI, and Logistics.


  The Happyrobot catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Happyrobot''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, engineering blog, support, and 35 more developer resources.'
random_paper: 4
scopes:
- name: Happyrobot Scopes
  scope_count: 8
  slug: happyrobot-scopes
  summary_line: 8 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 43.5
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 30.3
    contract_quality: 52.5
    developer_ergonomics: 35.1
    discoverability: 85.2
    governance: 30.3
    operational_transparency: 31.6
  previous_composite: 43.5
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/happyrobot/refs/heads/main/screenshots/happyrobot-2026-08-07T165946.png
security:
- kind: authentication
  name: Happyrobot Authentication
  slug: happyrobot-authentication
  summary_line: http/apiKey/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Happyrobot Domain Security
  slug: happyrobot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Happyrobot Vulnerability Disclosure
  slug: happyrobot-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Happyrobot Trust Center
  slug: happyrobot-trust-center
  summary_line: SOC 2 Type II, GDPR, HIPAA, EU AI Act, NIST CSF, DORA
slug: happyrobot
tags:
- AI Agents
- Agent Orchestration
- Voice AI
- Conversational AI
- Logistics
- Freight
- Supply Chain
- Workflow-Automation
- Contact Center
- Telephony
- MCP
- agent-native
- Agent Governance
- Enterprise Automation
website: https://www.happyrobot.ai/
---
