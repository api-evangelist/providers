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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 115
  human_in_the_loop: 0
  name: Frontline Agentic Access
  operation_count: 188
  slug: frontline-agentic-access
  summary_line: 188 operations · 115 acting
api_count: 33
apis:
- description: Inspect the identity attached to the current API key
  name: Frontline Account API
  slug: frontline-account-api
- description: View and manage your AI agents across your account
  name: Frontline Agent Builder API
  slug: frontline-agent-builder-api
- description: 'Agent runtime data: conversations and transcripts'
  name: Frontline Agents API
  slug: frontline-agents-api
- description: Discover available AI models for agent configuration
  name: Frontline AI Models API
  slug: frontline-ai-models-api
- description: View billing plan details, credits, and renewal information
  name: Frontline Billing API
  slug: frontline-billing-api
- description: Manage variables scoped to an agent's flow
  name: Frontline Flow Variables API
  slug: frontline-flow-variables-api
- description: View and manage flows associated with your agents
  name: Frontline Flows API
  slug: frontline-flows-api
- description: Inbound HTTPS endpoints that external systems can post events to
  name: Frontline Incoming Webhooks API
  slug: frontline-incoming-webhooks-api
- description: Manage agent intents and training phrases
  name: Frontline Intents API
  slug: frontline-intents-api
- description: Manual activities (notes, calls, meetings, emails) attached to object rows
  name: Frontline Object activities API
  slug: frontline-object-activities-api
- description: Per-view aggregations on objects
  name: Frontline Object aggregations API
  slug: frontline-object-aggregations-api
- description: Export object data as XLSX or CSV
  name: Frontline Object export API
  slug: frontline-object-export-api
- description: Manage columns on an object
  name: Frontline Object fields API
  slug: frontline-object-fields-api
- description: Files attached to object rows
  name: Frontline Object files API
  slug: frontline-object-files-api
- description: Manage tag/select options on object fields
  name: Frontline Object options API
  slug: frontline-object-options-api
- description: Categorize records inside an object
  name: Frontline Object record types API
  slug: frontline-object-record-types-api
- description: Link and unlink records across objects
  name: Frontline Object relations API
  slug: frontline-object-relations-api
- description: Read and write object records
  name: Frontline Object rows API
  slug: frontline-object-rows-api
- description: Tasks attached to object rows
  name: Frontline Object tasks API
  slug: frontline-object-tasks-api
- description: Saved view configurations on an object
  name: Frontline Object views API
  slug: frontline-object-views-api
- description: Manage CRM objects (standard and custom)
  name: Frontline Objects API
  slug: frontline-objects-api
- description: Manual activities (notes, calls, meetings, emails) attached to table rows
  name: Frontline Table activities API
  slug: frontline-table-activities-api
- description: Per-view aggregations on tables
  name: Frontline Table aggregations API
  slug: frontline-table-aggregations-api
- description: Export table data as XLSX or CSV
  name: Frontline Table export API
  slug: frontline-table-export-api
- description: Manage columns on a table
  name: Frontline Table fields API
  slug: frontline-table-fields-api
- description: Files attached to table rows
  name: Frontline Table files API
  slug: frontline-table-files-api
- description: Manage tag/select options on table fields
  name: Frontline Table options API
  slug: frontline-table-options-api
- description: Read and write table rows
  name: Frontline Table rows API
  slug: frontline-table-rows-api
- description: Tasks attached to table rows
  name: Frontline Table tasks API
  slug: frontline-table-tasks-api
- description: Manage spreadsheet-style tables
  name: Frontline Tables API
  slug: frontline-tables-api
- description: Manage reusable HTTP integrations callable from flows and workflows
  name: Frontline Tools API
  slug: frontline-tools-api
- description: Manage variables scoped to an automation workflow
  name: Frontline Workflow Variables API
  slug: frontline-workflow-variables-api
- description: View and manage your workflows across your account
  name: Frontline Workflows API
  slug: frontline-workflows-api
artifact_total: 39
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/frontline-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/frontline-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/frontline-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/frontline-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/frontline-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/frontline-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.getfrontline.ai/
- group: auth
  title: ''
  type: TrustCenter
  url: security/frontline-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/frontline-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/frontline-agentic-access.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/frontline-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/frontline-llms.txt
- group: design
  title: ''
  type: DataModel
  url: data-model/frontline-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/frontline-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/frontline-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/frontline-cli.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.getfrontline.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://frontline-public-api.redocly.app/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.getfrontline.ai/docs/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getfrontline.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.getfrontline.ai
- group: operate
  title: ''
  type: Support
  url: https://www.getfrontline.ai/help
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getfrontline.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getfrontline.ai/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://getfrontline.ai
created: '2026-07-17'
description: Frontline is an AI-native CRM platform that builds and maintains itself. It unifies customer context from WhatsApp, email, and meetings, ships AI agents (Max) that draft replies, proposals, follow-ups and meeting notes, and a Studio for building an AI workforce for sales and support. The Frontline Public API exposes agents, agent-builder flows, automation workflows, CRM objects and rows, tables, tools, intents, AI models, incoming webhooks, account, and billing over REST at https://prod-api.getfrontline.ai/public/v1, authenticated with GENERAL (account) and USER Bearer API keys. Backed by 500 Global.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/frontline.png
layout: provider
mcp_servers:
- description: ''
  name: frontline-mcp.yml
  slug: frontline-mcpyml
modified: '2026-07-19'
name: Frontline
nav: Providers
network: true
overview: 'Frontline publishes 33 APIs on the [APIs.io](https://apis.io/) network, including Account API, Agent Builder API, Agents API, and 30 more. Tagged areas include Company, CRM, AI Agents, Sales Automation, and Customer Support.


  Frontline''s developer surface includes authentication, CLI, documentation, API reference, getting-started guide, pricing, signup flow, and 19 more developer resources.'
random_paper: 5
rate_limits:
- limit_count: 0
  name: Frontline Rate Limits
  slug: frontline-rate-limits
score:
  band: developing
  composite: 47.5
  delta: -1.5
  facets:
    commercial_clarity: 60.5
    contract_quality: 57.6
    developer_ergonomics: 51.6
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 49.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 33
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/frontline/refs/heads/main/screenshots/frontline-2026-07-25T215237.png
security:
- kind: authentication
  name: Frontline Authentication
  slug: frontline-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Frontline Domain Security
  slug: frontline-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Frontline Trust Center
  slug: frontline-trust-center
  summary_line: SOC 2, ISO 27001
slug: frontline
tags:
- Company
- CRM
- AI Agents
- Sales Automation
- Customer Support
- Workflows
- Conversational AI
website: https://getfrontline.ai
---
