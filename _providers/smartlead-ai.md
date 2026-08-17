---
access_model:
  confidence: high
  label: Paid · Free trial · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 59.9
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 54
  human_in_the_loop: 1
  name: Smartlead Ai Agentic Access
  operation_count: 112
  slug: smartlead-ai-agentic-access
  summary_line: 112 operations · 54 acting · 1 human-in-the-loop
api_count: 11
apis:
- description: The complete SmartLead REST API as published by SmartLead — OpenAPI 3.1.1, 85 paths and 98 operations across campaigns, sequences, leads and lead lists, email accounts and warmup, the master inbox, we
  name: SmartLead API
  slug: smartlead-api
- description: REST endpoints to create, list, fetch, update, schedule, pause, resume, and delete email campaigns, plus manage sequences, A/B variants, and sender account assignments inside a campaign.
  name: Smartlead Campaigns API
  slug: campaigns-api
- description: Endpoints to add leads to a campaign in bulk, fetch leads, update lead status (interested, replied, unsubscribed), search leads globally, and manage lead categories and lead lists.
  name: Smartlead Leads API
  slug: leads-api
- description: Endpoints to add, list, update, and remove sender mailboxes (SMTP, Gmail, Outlook), assign them to campaigns, and track per-account sending limits and warmup state.
  name: Smartlead Email Accounts API
  slug: email-accounts-api
- description: Endpoints for managing Smartlead's deliverability warmup engine — enabling warmup per mailbox, configuring ramp settings, and reading warmup reputation and stats.
  name: Smartlead Email Warmup API
  slug: email-warmup-api
- description: CRUD endpoints for user, client and campaign-scoped webhook subscriptions covering lead events (sent, opened, clicked, replied, bounced, unsubscribed) used to stream Smartlead activity to external sys
  name: Smartlead Webhooks API
  slug: webhooks-api
- description: Endpoints for campaign and account-level analytics — sent, open, click, reply, bounce, and unsubscribe metrics aggregated over time ranges.
  name: Smartlead Analytics API
  slug: analytics-api
- description: Endpoints for agency users to provision and manage white-labeled client accounts, mint and revoke per-client API keys, and meter usage across multiple end customers.
  name: Smartlead Client Management API
  slug: client-management-api
- description: Retrieve campaign performance metrics.
  name: Smartlead Campaign Statistics API
  slug: smartlead-ai-campaign-statistics-api
- description: Manage Smartlead email campaigns.
  name: Smartlead Campaigns API
  slug: smartlead-ai-campaigns-api
- description: 'SmartLead''s remote Model Context Protocol server. tools/list answers anonymously with three documentation tools (search, a read-only docs filesystem, feedback). It exposes the SmartLead documentation '
  name: SmartLead Documentation MCP Server
  slug: mcp-server
artifact_total: 23
asyncapis:
- description: ''
  name: Smartlead Ai Webhooks
  slug: smartlead-ai-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Smartlead Campaign Statistics API
  slug: open-smartlead-ai-campaign-statistics-api
- collection_type: open
  name: Smartlead Campaign Statistics Campaigns API
  slug: open-smartlead-ai-campaigns-api
- collection_type: open
  name: Smartlead API
  slug: open-smartlead-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/smartlead-ai-agentic-access.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/smartlead-ai-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/smartlead-ai-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/smartlead-ai-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/smartlead-ai-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/smartlead-ai-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/smartlead-ai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/smartlead-ai-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/smartlead-ai-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/smartlead-ai-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/smartlead-ai-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/smartlead-ai-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/smartlead-ai-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/smartlead-ai-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.smartlead.ai/dpa
- group: build
  title: ''
  type: Packages
  url: packages/smartlead-ai-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/smartlead-ai-cli.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/smartlead-ai-openapi-overlay.yaml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/smartlead-ai-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/smartlead-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.smartlead.ai
- group: other
  title: ''
  type: App
  url: https://app.smartlead.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.smartlead.ai/introduction
- group: docs
  title: ''
  type: Documentation
  url: https://api.smartlead.ai/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://api.smartlead.ai/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://api.smartlead.ai/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Smartlead-Public
- group: operate
  title: ''
  type: Roadmap
  url: https://roadmap.smartlead.ai
- group: commercial
  title: ''
  type: Pricing
  url: https://www.smartlead.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.smartlead.ai/blog
- group: start
  title: ''
  type: SignUp
  url: https://app.smartlead.ai/signup
- group: start
  title: ''
  type: Login
  url: https://app.smartlead.ai/login
- group: operate
  title: ''
  type: Support
  url: https://help.smartlead.ai
- group: operate
  title: ''
  type: Help
  url: https://help.smartlead.ai
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.smartlead.ai/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.smartlead.ai/new-terms-and-conditions
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/smartleadhq
- group: company
  title: ''
  type: Twitter
  url: https://x.com/smartlead_ai
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@smartlead
- group: agent
  title: ''
  type: LlmsText
  url: https://api.smartlead.ai/llms.txt
created: '2026-05-23'
description: Smartlead is cold email infrastructure for outbound sales and lead generation, focused on inbox deliverability through unlimited mailbox rotation, automated warmup, and a unified master inbox. Smartlead publishes an OpenAPI 3.1.1 contract with 98 operations at server.smartlead.ai/api/v1 covering campaigns, sequences, leads and lead lists, sender mailboxes and warmup, the master inbox, webhooks, analytics, Smart Delivery placement testing, Smart Senders and agency client management, authenticated with an API key passed as a query parameter. It also ships an unusually forward agent surface for its size — an A2A agent card, a published Agent Skill, a remote documentation MCP server, llms.txt, and a first-party CLI — alongside a 13-event signed webhook catalog.
finops:
- name: Smartlead Ai Finops
  service_category: API
  slug: smartlead-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/smartlead-ai.png
layout: provider
mcp_servers:
- description: ''
  name: smartlead-ai-mcp.yml
  slug: smartlead-ai-mcpyml
modified: '2026-08-13'
name: Smartlead
nav: Providers
network: true
overview: 'Smartlead publishes 3 APIs on the [APIs.io](https://apis.io/) network, including Campaign Statistics API, Campaigns API, and 1 more. Tagged areas include Cold Email, Outbound, Sales, Deliverability, and Email Warmup.


  The Smartlead catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Smartlead''s developer surface includes authentication, CLI, documentation, API reference, getting-started guide, pricing, engineering blog, and 34 more developer resources.'
plans:
- name: Smartlead Ai Plans Pricing
  plan_count: 4
  slug: smartlead-ai-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Smartlead Ai Rate Limits
  slug: smartlead-ai-rate-limits
score:
  band: exemplar
  composite: 68.0
  delta: 20.1
  facets:
    commercial_clarity: 92.1
    contract_quality: 70.5
    developer_ergonomics: 73.9
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 50.0
  previous_composite: 47.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/smartlead-ai/refs/heads/main/screenshots/smartlead-ai-2026-06-20T194043.png
security:
- kind: authentication
  name: Smartlead Ai Authentication
  slug: smartlead-ai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Smartlead Ai Domain Security
  slug: smartlead-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: smartlead-ai
tags:
- Cold Email
- Outbound
- Sales
- Deliverability
- Email Warmup
- Automation
- Sequences
website: https://www.smartlead.ai
---
