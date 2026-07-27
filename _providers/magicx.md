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
  band: agent-aware
  dimensions:
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 33.7
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: Framework-agnostic HTTP API behind the AI Autocomplete SDKs. A single POST /api/suggest endpoint drives keystroke-by-keystroke guided autocomplete over a placeholder-based query model, with a POST /ap
  name: AI Autocomplete API
  slug: ai-autocomplete-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://magicx.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ai-autocomplete.com/
- group: docs
  title: ''
  type: Documentation
  url: https://ai-autocomplete.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://ai-autocomplete.com/docs/http/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://ai-autocomplete.com/docs/http/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://ai-autocomplete.com/other/pricing
- group: operate
  title: ''
  type: HelpCenter
  url: https://ai-autocomplete.com/other/faqs
- group: start
  title: ''
  type: Login
  url: https://ai-autocomplete.com/account/keys
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ai-autocomplete.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ai-autocomplete.com/legal/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://ai-autocomplete.com/other/enterprise
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/magicx-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/magicx-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/magicx-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/magicx-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/magicx-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/magicx-problem-types.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/magicx-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/magicx-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/magicx-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: MagicX Inc. builds software that lets people take actions instantly from any text box. Its flagship developer product, AI Autocomplete, is a drop-in SDK and HTTP API that turns a blank input into instant intent — guiding users on what to type with roughly 200ms suggestions, delivered as native SDKs for React, Angular, Vanilla JS and Swift or a framework-agnostic HTTP API. Auth uses public, secret, and short-lived access-token keys, and pricing is usage-based per prediction with a SOC 2 enterprise tier. MagicX also ships Hero Assistant, a consumer AI assistant. The company is backed by Forerunner Ventures.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/magicx.png
layout: provider
mcp_servers:
- description: ''
  name: magicx-mcp.yml
  slug: magicx-mcpyml
modified: '2026-07-20'
name: MagicX
nav: Providers
network: true
overview: 'MagicX publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Autocomplete, Developer Tools, and SDK.


  MagicX''s developer surface includes documentation, API reference, getting-started guide, pricing, authentication, and 16 more developer resources.'
random_paper: 21
score:
  band: thin
  composite: 34.1
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 0.0
    developer_ergonomics: 71.7
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 34.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/magicx/refs/heads/main/screenshots/magicx-2026-07-25T225856.png
security:
- kind: authentication
  name: Magicx Authentication
  slug: magicx-authentication
  summary_line: http · 3 schemes
- kind: domain-security
  name: Magicx Domain Security
  slug: magicx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: magicx
tags:
- Company
- AI
- Autocomplete
- Developer Tools
- SDK
- Natural Language
- Productivity
- Machine Learning
website: https://magicx.ai
---
