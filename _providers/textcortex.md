---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Textcortex Agentic Access
  operation_count: 5
  slug: textcortex-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.textcortex.com/v1
  baseurl_source: declared
  description: Read API credit balance for the current API key.
  name: Textcortex Balance API
  slug: textcortex-balance-api
- baseURL: https://api.textcortex.com/v1
  baseurl_source: declared
  description: Generate chat completions with TextCortex models.
  name: Textcortex Chat Completions API
  slug: textcortex-chat-completions-api
- baseURL: https://api.textcortex.com/v1
  baseurl_source: declared
  description: Discover OpenAI-compatible TextCortex models.
  name: Textcortex Models API
  slug: textcortex-models-api
- baseURL: https://api.textcortex.com/v1
  baseurl_source: declared
  description: Generate responses with TextCortex models.
  name: Textcortex Responses API
  slug: textcortex-responses-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: TextCortex Balance API
  slug: open-textcortex-balance-api
- collection_type: open
  name: TextCortex Balance Chat Completions API
  slug: open-textcortex-chat-completions-api
- collection_type: open
  name: TextCortex Balance Models API
  slug: open-textcortex-models-api
- collection_type: open
  name: TextCortex Balance Responses API
  slug: open-textcortex-responses-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.textcortex.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/textcortex-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/textcortex-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/textcortex-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/textcortex-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/textcortex-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/textcortex-well-known.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/textcortex-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/textcortex-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/textcortex-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/textcortex-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/textcortex-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/textcortex-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.textcortex.com/
- group: design
  title: ''
  type: Conventions
  url: conventions/textcortex-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/textcortex-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.textcortex.com/
- group: operate
  title: ''
  type: Support
  url: https://help.textcortex.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/textcortex
- group: commercial
  title: ''
  type: Pricing
  url: https://textcortex.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://textcortex.com/terms-of-services
- group: start
  title: ''
  type: SignUp
  url: https://app.textcortex.com/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/textcortex/textcortex-text-generation-api/overview
created: '2026-07-17'
description: TextCortex is a Berlin-based AI writing and content-generation platform (ZenoChat assistant, knowledge bases, and a suite of writing tools) that also ships a public, OpenAI-compatible REST API. The API, served from https://api.textcortex.com/v1 with Bearer API-key authentication, exposes model discovery, chat completions, and an OpenAI Responses-compatible generation endpoint, plus an API-credit balance check. Streaming is supported over server-sent events and infrastructure is EU-hosted and GDPR-compliant. TextCortex is backed by Speedinvest and maintains first-party Python and JavaScript client libraries.
image: https://docs.textcortex.com/logo192.png
layout: provider
modified: '2026-07-21'
name: Textcortex
nav: Providers
network: true
overview: 'Textcortex publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Balance API, Chat Completions API, Models API, and 1 more. Tagged areas include Company, Artificial Intelligence, Text Generation, Large Language Models, and Chat Completions.


  Textcortex''s developer surface includes authentication, support, pricing, signup flow, and 20 more developer resources.'
random_paper: 1
screenshot: https://raw.githubusercontent.com/api-evangelist/textcortex/refs/heads/main/screenshots/textcortex-2026-08-17T082329.png
security:
- kind: authentication
  name: Textcortex Authentication
  slug: textcortex-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Textcortex Domain Security
  slug: textcortex-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: textcortex
tags:
- Company
- Artificial Intelligence
- Text Generation
- Large Language Models
- Chat Completions
- OpenAI-Compatible
- Content Generation
- Developer Tools
website: https://www.textcortex.com/
---
