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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.1
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'The Spyne Unified API accepts vehicle images and video (by SKU / VIN / stock number) and returns AI-transformed studio images, background replacement, 360-degree spins, and feature videos, plus image '
  name: Spyne Unified API
  slug: spyne-unified-api
artifact_total: 5
asyncapis:
- description: ''
  name: Spyne Webhooks
  slug: spyne-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.spyne.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.spyne.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.spyne.ai/docs/overview-3
- group: docs
  title: ''
  type: APIReference
  url: https://docs.spyne.ai/reference/unified-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.spyne.ai/docs/transform-your-first-vehicle-1
- group: auth
  title: ''
  type: Authentication
  url: authentication/spyne-authentication.yml
- group: build
  title: ''
  type: SDKs
  url: packages/spyne-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/spyne-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/spyne-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/spyne-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/spyne-llms.txt
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/spyne-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/spyne-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/spyne-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/spyne-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/spyne-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spyne-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.spyne.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.spyne.ai/blogs/
- group: operate
  title: ''
  type: Support
  url: https://www.spyne.ai/contact-us
- group: commercial
  title: ''
  type: Pricing
  url: https://www.spyne.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://console.spyne.ai/
- group: start
  title: ''
  type: Login
  url: https://console.spyne.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.spyne.ai/terms-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.spyne.ai/privacy
created: '2026-07-17'
description: Spyne is an AI platform for automotive retail that helps car dealerships and marketplaces produce studio-grade vehicle visuals and merchandising at scale. Its Unified API and mobile SDKs let developers submit raw vehicle images and video and receive AI-transformed studio images, background replacement, 360-degree spins, feature videos, and automated image classification and QC. Processing is asynchronous - jobs are submitted per SKU/VIN and results are delivered via polling endpoints or signed webhook callbacks. Spyne also offers conversational AI agents for dealership sourcing, listing, marketing, and selling vehicles faster.
image: https://d20uiuzezo3er4.cloudfront.net/AI-tools/ai-tools-landing-360/logo+spyne.webp
layout: provider
mcp_servers:
- description: ''
  name: spyne-mcp.yml
  slug: spyne-mcpyml
modified: '2026-07-21'
name: Spyne
nav: Providers
network: true
overview: 'Spyne publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai, Automotive, Images, and Video.


  The Spyne catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Spyne''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, support, pricing, and 19 more developer resources.'
random_paper: 20
score:
  band: developing
  composite: 46.0
  delta: 4.8
  facets:
    commercial_clarity: 52.6
    contract_quality: 51.6
    developer_ergonomics: 62.5
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 7.9
  previous_composite: 41.2
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Spyne Authentication
  slug: spyne-authentication
  summary_line: http/apiKey · 2 schemes
- kind: domain-security
  name: Spyne Domain Security
  slug: spyne-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: spyne
tags:
- Company
- Ai
- Automotive
- Images
- Video
- Computer Vision
- Machine Learning
- Dealerships
- Media Processing
- Webhooks
website: https://www.spyne.ai/
---
