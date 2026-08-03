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
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 40.8
  scored_at: '2026-08-03'
api_count: 4
apis:
- description: The Audit API from Siro — 1 operation(s) for audit.
  name: Siro Audit API
  slug: siro-audit-api
- description: The Core API from Siro — 23 operation(s) for core.
  name: Siro Core API
  slug: siro-core-api
- description: The Folders API from Siro — 2 operation(s) for folders.
  name: Siro Folders API
  slug: siro-folders-api
- description: The Integrations API from Siro — 21 operation(s) for integrations.
  name: Siro Integrations API
  slug: siro-integrations-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/siro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://siro.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.siro.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.siro.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.siro.ai/api-references/get-recordings
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.siro.ai/getting-started
- group: start
  title: ''
  type: Quickstart
  url: https://docs.siro.ai/phones-integration-getting-started
- group: operate
  title: ''
  type: Support
  url: https://docs.siro.ai/support
- group: company
  title: ''
  type: Blog
  url: https://www.siro.ai/insights
- group: start
  title: ''
  type: Login
  url: https://app.siro.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.siro.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.siro.ai/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.siro.ai/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/siro-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/siro-authentication.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/siro-webhooks.json
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/siro-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/siro-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/siro-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/siro-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/siro-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/siro-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/siro-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/siro-external-api-overlay.yaml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/siro-well-known.yml
created: '2026-07-17'
description: 'Siro is an AI sales coaching platform for in-person and field sales teams. Reps record their live sales conversations from the Siro mobile app, and Siro transcribes each conversation, surfaces coaching insights, generates scorecards and summaries, and extracts structured fields (budget, objections, decision makers, timelines) that are pushed back into the team''s CRM. Siro publishes a documented REST API and webhook surface that enables fully bidirectional, custom CRM integrations: syncing appointments/engagements, opportunities and accounts into Siro, matching recordings to CRM entities, and pulling recording details, summaries, entity extractions and coaching scorecards back out. The platform ships prebuilt integrations for Salesforce, HubSpot, Microsoft Dynamics, Pipedrive, Zoho, SalesRabbit, Leap SalesPro, Hatch, CompanyCam and a range of dealership DMS and home-services tools. Siro is backed by CRV and Index Ventures.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/siro.png
layout: provider
mcp_servers:
- description: ''
  name: siro-mcp.yml
  slug: siro-mcpyml
modified: '2026-07-21'
name: Siro
nav: Providers
network: true
overview: 'Siro publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Audit API, Core API, Folders API, and 1 more. Tagged areas include Company, Sales, Sales Coaching, Conversation Intelligence, and Field Sales.


  Siro''s developer surface includes documentation, API reference, getting-started guide, quickstart, support, engineering blog, authentication, and 19 more developer resources.'
random_paper: 65
rate_limits:
- limit_count: 1
  name: Siro Rate Limits
  slug: siro-rate-limits
score:
  band: developing
  composite: 47.8
  delta: 2.8
  facets:
    commercial_clarity: 42.1
    contract_quality: 55.0
    developer_ergonomics: 56.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 28.9
  previous_composite: 45.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Siro Authentication
  slug: siro-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Siro Domain Security
  slug: siro-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: siro
tags:
- Company
- Sales
- Sales Coaching
- Conversation Intelligence
- Field Sales
- CRM
- AI
- Speech to Text
- Webhooks
- Integrations
website: https://siro.ai/
---
