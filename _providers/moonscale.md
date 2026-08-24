---
access_model:
  confidence: high
  label: Contact sales
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.moonscale.com/
  - https://vidlab7-d7584a5d.mintlify.app/api-reference/endpoint/createApiKey
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.3
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Moonscale Agentic Access
  operation_count: 4
  slug: moonscale-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 1
apis:
- description: The Moonscale API covers two surfaces. The live-avatar surface creates single-participant meeting rooms hosted by a real-time AI sales avatar and returns the conversation transcript plus an AI-generat
  name: Moonscale API
  slug: moonscale-api
artifact_total: 7
asyncapis:
- description: ''
  name: Moonscale Webhooks
  slug: moonscale-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/moonscale-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/moonscale-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.moonscale.com/
- group: company
  title: ''
  type: Blog
  url: https://www.moonscale.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.moonscale.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.moonscale.com/legal/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.moonscale.com/legal/terms-and-conditions
- group: other
  title: ''
  type: Imprint
  url: https://www.moonscale.com/legal/imprint
- group: docs
  title: ''
  type: Documentation
  url: https://vidlab7-d7584a5d.mintlify.app/api-reference/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://vidlab7-d7584a5d.mintlify.app/api-reference/endpoint/liveAvatarsCreateRoom
- group: start
  title: ''
  type: GettingStarted
  url: https://vidlab7-d7584a5d.mintlify.app/api-reference/endpoint/createApiKey
- group: start
  title: ''
  type: Login
  url: https://app.moonscale.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/moonscale-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/moonscale-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/moonscale-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/moonscale-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/moonscale-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/moonscale-examples.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/moonscale-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/moonscale-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/moonscale-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/moonscale-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/moonscale-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/moonscale-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/moonscale-api-overlay.yaml
created: '2026-07-17'
description: 'Moonscale (formerly VidLab7) is a Munich-based AI sales advisor platform whose "Digital Sales Human" avatars automate top-of-funnel sales conversations — pitching products, qualifying inbound buyers, running interactive demos, handling objections, booking meetings and following up around the clock across websites, landing pages, emails and apps, with support for 130+ languages and CRM connections to Salesforce, HubSpot, Pipedrive, Slack and Clay. Moonscale does publish a real, machine-readable API: an OpenAPI 3.0.1 document titled "Moonscale API" served from its Mintlify documentation site, covering four operations across two surfaces — live-avatar meeting rooms with conversation transcripts and summaries (/api/v1/), and asynchronous studio-avatar video generation with a caller-registered completion webhook (/api/studio-avatar/). Requests authenticate with an x-api-key header against https://api-prd.moonscale.com; keys are issued from Moonscale Studio, but API access is feature-flagged
  per account and must be requested from support. There is no first-party SDK, MCP server, agent card, status page, changelog, published rate limit or published price. Backed by EQT Ventures.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/moonscale.png
layout: provider
modified: '2026-08-14'
name: Moonscale
nav: Providers
network: true
overview: 'Moonscale publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Sales, Sales Automation, and Lead Generation.


  The Moonscale catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Moonscale''s developer surface includes engineering blog, support, documentation, API reference, getting-started guide, authentication, code examples, and 19 more developer resources.'
plans:
- name: Moonscale Plans Pricing
  plan_count: 0
  slug: moonscale-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Moonscale Rate Limits
  slug: moonscale-rate-limits
score:
  band: developing
  composite: 40.7
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 16.7
    contract_quality: 58.7
    developer_ergonomics: 49.4
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 7.9
  previous_composite: 40.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/moonscale/refs/heads/main/screenshots/moonscale-2026-08-07T184246.png
security:
- kind: authentication
  name: Moonscale Authentication
  slug: moonscale-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Moonscale Domain Security
  slug: moonscale-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: moonscale
tags:
- Company
- Artificial Intelligence
- Sales
- Sales Automation
- Lead Generation
- AI Agents
- Conversational AI
- CRM
- Video Generation
- Avatars
- Speech
- Germany
website: https://www.moonscale.com/
---
