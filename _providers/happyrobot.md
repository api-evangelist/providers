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
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 104
  human_in_the_loop: 0
  name: Happyrobot Agentic Access
  operation_count: 215
  slug: happyrobot-agentic-access
  summary_line: 215 operations · 104 acting
api_count: 2
apis:
- description: Happyrobot's first-party remote MCP server for building and governing workflows — 26 published tools plus 5 MCP prompts, served over Streamable HTTP and protected by OAuth 2.0 (scope mcp:full, RFC 972
  name: Happyrobot Workflows MCP Server
  slug: happyrobot-workflows-mcp-server
- description: 'First-party remote MCP server over the customer''s Twin database — 9 published tools covering schema introspection, paginated reads, table creation, row insert/update/delete, table drop, and arbitrary '
  name: Happyrobot Twin MCP Server
  slug: happyrobot-twin-mcp-server
- description: A hosted documentation-search MCP server on the docs host, discovered via RFC 9728 protected-resource metadata at https://docs.happyrobot.ai/.well-known/oauth-protected-resource. It advertises a singl
  name: Happyrobot Docs MCP Server
  slug: happyrobot-docs-mcp-server
- description: The Adversarial Suites API from Happyrobot — 8 operation(s) for adversarial suites.
  name: Happyrobot Adversarial Suites API
  slug: happyrobot-adversarial-suites-api
- description: The Adversarial Tests API from Happyrobot — 8 operation(s) for adversarial tests.
  name: Happyrobot Adversarial Tests API
  slug: happyrobot-adversarial-tests-api
- description: The API Keys API from Happyrobot — 1 operation(s) for api keys.
  name: Happyrobot API Keys API
  slug: happyrobot-api-keys-api
- description: The Apps API from Happyrobot — 1 operation(s) for apps.
  name: Happyrobot Apps API
  slug: happyrobot-apps-api
- description: The Artifacts API from Happyrobot — 1 operation(s) for artifacts.
  name: Happyrobot Artifacts API
  slug: happyrobot-artifacts-api
- description: The Audits API from Happyrobot — 8 operation(s) for audits.
  name: Happyrobot Audits API
  slug: happyrobot-audits-api
- description: The Billing API from Happyrobot — 4 operation(s) for billing.
  name: Happyrobot Billing API
  slug: happyrobot-billing-api
- description: The Chat API from Happyrobot — 7 operation(s) for chat.
  name: Happyrobot Chat API
  slug: happyrobot-chat-api
- description: The Contacts API from Happyrobot — 5 operation(s) for contacts.
  name: Happyrobot Contacts API
  slug: happyrobot-contacts-api
- description: The Custom Evals API from Happyrobot — 8 operation(s) for custom evals.
  name: Happyrobot Custom Evals API
  slug: happyrobot-custom-evals-api
- description: The Events API from Happyrobot — 1 operation(s) for events.
  name: Happyrobot Events API
  slug: happyrobot-events-api
- description: The Integration Resources API from Happyrobot — 15 operation(s) for integration resources.
  name: Happyrobot Integration Resources API
  slug: happyrobot-integration-resources-api
- description: The Integrations API from Happyrobot — 4 operation(s) for integrations.
  name: Happyrobot Integrations API
  slug: happyrobot-integrations-api
- description: The Issues API from Happyrobot — 3 operation(s) for issues.
  name: Happyrobot Issues API
  slug: happyrobot-issues-api
- description: The Knowledge Bases API from Happyrobot — 6 operation(s) for knowledge bases.
  name: Happyrobot Knowledge Bases API
  slug: happyrobot-knowledge-bases-api
- description: The MCP Servers API from Happyrobot — 3 operation(s) for mcp servers.
  name: Happyrobot MCP Servers API
  slug: happyrobot-mcp-servers-api
- description: The Messages API from Happyrobot — 1 operation(s) for messages.
  name: Happyrobot Messages API
  slug: happyrobot-messages-api
- description: The Northstars API from Happyrobot — 9 operation(s) for northstars.
  name: Happyrobot Northstars API
  slug: happyrobot-northstars-api
- description: The Organization API from Happyrobot — 2 operation(s) for organization.
  name: Happyrobot Organization API
  slug: happyrobot-organization-api
- description: The Phone Numbers API from Happyrobot — 10 operation(s) for phone numbers.
  name: Happyrobot Phone Numbers API
  slug: happyrobot-phone-numbers-api
- description: The Realtime API from Happyrobot — 1 operation(s) for realtime.
  name: Happyrobot Realtime API
  slug: happyrobot-realtime-api
- description: The Runs API from Happyrobot — 12 operation(s) for runs.
  name: Happyrobot Runs API
  slug: happyrobot-runs-api
- description: The Sessions API from Happyrobot — 4 operation(s) for sessions.
  name: Happyrobot Sessions API
  slug: happyrobot-sessions-api
- description: The Signals API from Happyrobot — 4 operation(s) for signals.
  name: Happyrobot Signals API
  slug: happyrobot-signals-api
- description: The SIP Trunks API from Happyrobot — 4 operation(s) for sip trunks.
  name: Happyrobot SIP Trunks API
  slug: happyrobot-sip-trunks-api
- description: The Twin API from Happyrobot — 6 operation(s) for twin.
  name: Happyrobot Twin API
  slug: happyrobot-twin-api
- description: The Use Cases API from Happyrobot — 1 operation(s) for use cases.
  name: Happyrobot Use Cases API
  slug: happyrobot-use-cases-api
- description: The UseCases API from Happyrobot — 2 operation(s) for usecases.
  name: Happyrobot Use Cases API
  slug: happyrobot-usecases-api
- description: The Versions API from Happyrobot — 16 operation(s) for versions.
  name: Happyrobot Versions API
  slug: happyrobot-versions-api
- description: The Voice API from Happyrobot — 1 operation(s) for voice.
  name: Happyrobot Voice API
  slug: happyrobot-voice-api
- description: The Workflow Folders API from Happyrobot — 2 operation(s) for workflow folders.
  name: Happyrobot Workflow Folders API
  slug: happyrobot-workflow-folders-api
- description: The Workflow Variables API from Happyrobot — 2 operation(s) for workflow variables.
  name: Happyrobot Workflow Variables API
  slug: happyrobot-workflow-variables-api
- description: The Workflows API from Happyrobot — 10 operation(s) for workflows.
  name: Happyrobot Workflows API
  slug: happyrobot-workflows-api
artifact_total: 48
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
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/happyrobot-capability-edges.yml
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
overview: 'Happyrobot publishes 33 APIs on the [APIs.io](https://apis.io/) network, including Adversarial Suites API, Adversarial Tests API, API Keys API, and 30 more. Tagged areas include AI Agents, Agent Orchestration, Voice AI, Conversational AI, and Logistics.


  The Happyrobot catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Happyrobot''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, engineering blog, support, and 36 more developer resources.'
random_paper: 4
scopes:
- name: Happyrobot Scopes
  scope_count: 8
  slug: happyrobot-scopes
  summary_line: 8 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 39.4
  coverage:
    artifact_dirs: 23
    catalog_gap: 91.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 55.3
    developer_ergonomics: 35.1
    discoverability: 51.9
    governance: 18.2
    operational_transparency: 31.6
  previous_composite: 39.4
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
