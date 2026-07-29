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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Govly Agentic Access
  operation_count: 32
  slug: govly-agentic-access
  summary_line: 32 operations · 16 acting
api_count: 11
apis:
- description: Search and inspect awarded government contracts.
  name: Govly Awards API
  slug: govly-awards-api
- description: Read document representations and request temporary original-file downloads.
  name: Govly Documents API
  slug: govly-documents-api
- description: Follow opportunities and related workspace activity.
  name: Govly Follows API
  slug: govly-follows-api
- description: Read and triage the authenticated user's matched inbox items.
  name: Govly Inbox API
  slug: govly-inbox-api
- description: Search, fetch, and inspect Govly opportunity records.
  name: Govly Opportunities API
  slug: govly-opportunities-api
- description: Inspect quote submission requirements, submit quotes, and poll submission status.
  name: Govly Quote Submissions API
  slug: govly-quote-submissions-api
- description: List saved opportunity searches and cached matches.
  name: Govly Saved Searches API
  slug: govly-saved-searches-api
- description: List and upload workspace attachments.
  name: Govly Workspace Attachments API
  slug: govly-workspace-attachments-api
- description: Post comments to workspaces.
  name: Govly Workspace Comments API
  slug: govly-workspace-comments-api
- description: Add users and teams to workspaces.
  name: Govly Workspace Members API
  slug: govly-workspace-members-api
- description: Create, update, and inspect opportunity workspaces.
  name: Govly Workspaces API
  slug: govly-workspaces-api
artifact_total: 17
asyncapis:
- description: ''
  name: Govly Webhooks
  slug: govly-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/govly-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/govly-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/govly-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.govly.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.govly.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.govly.com/getting-started/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.govly.com/api-reference/tools-v1/opportunities/search-opportunities
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.govly.com/getting-started/introduction
- group: company
  title: ''
  type: Blog
  url: https://www.govly.com/blog
- group: operate
  title: ''
  type: Support
  url: https://intercom.help/govly/en
- group: commercial
  title: ''
  type: Pricing
  url: https://www.govly.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.govly.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.govly.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.govly.com
- group: auth
  title: ''
  type: TrustCenter
  url: https://security.govly.com
- group: auth
  title: ''
  type: Compliance
  url: https://docs.govly.com/enterprise/security
- group: agent
  title: ''
  type: MCPServer
  url: mcp/govly-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/govly-llms.txt
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/govly-tools-v1-openapi-original.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/govly-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/govly-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/govly-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/govly-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/govly-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/govly-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/govly-tools-v1-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Govly is an AI-powered market network for government contractors — primes, OEMs, VARs, and distributors — that ingests, parses, and analyzes federal and SLED (state, local, education) procurement data to surface RFQ/RFI opportunities and contract awards across 40+ federal contract vehicles and state/local procurement portals. The platform provides pipeline building, award tracking, competitor intelligence, AI matching agents, shared opportunity workspaces, and quote submission automation. Govly exposes an enterprise Tools API (agent- and automation-oriented, REST/JSON over HTTPS with API-key auth), a hosted MCP server for AI clients, webhooks for real-time opportunity and workspace events, and CRM integrations (Salesforce, HubSpot). Govly is SOC 2 Type I and CMMC compliant, hosted on AWS in the USA, and backed by Insight Partners.
image: https://cdn.prod.website-files.com/65f9f755792648d187d6d0dd/69e7b31d3d986500bd367ba0_webclip-256.png
layout: provider
mcp_servers:
- description: ''
  name: govly-mcp.yml
  slug: govly-mcpyml
modified: '2026-07-19'
name: Govly
nav: Providers
network: true
overview: 'Govly publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Awards API, Documents API, Follows API, and 8 more. Tagged areas include Company, Government, Public Sector, Procurement, and Government Contracting.


  The Govly catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Govly''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, support, pricing, and 20 more developer resources.'
random_paper: 8
score:
  band: developing
  composite: 52.5
  delta: -1.4
  facets:
    commercial_clarity: 47.4
    contract_quality: 64.9
    developer_ergonomics: 62.5
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 23.7
  previous_composite: 53.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 55.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/govly/refs/heads/main/screenshots/govly-2026-07-25T220138.png
security:
- kind: authentication
  name: Govly Authentication
  slug: govly-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Govly Domain Security
  slug: govly-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Govly Trust Center
  slug: govly-trust-center
  summary_line: SOC 2 Type I, CMMC Level 1, CMMC Level 2
slug: govly
tags:
- Company
- Government
- Public Sector
- Procurement
- Government Contracting
- GovTech
- Market Intelligence
- Awards
- Opportunities
- Agents
website: https://www.govly.com/
---
