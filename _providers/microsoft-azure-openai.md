---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Microsoft Azure Openai Agentic Access
  operation_count: 4
  slug: microsoft-azure-openai-agentic-access
  summary_line: 4 operations · 4 acting
api_count: 4
apis:
- description: The Chat API from Azure OpenAI Service — 1 operation(s) for chat.
  name: Azure OpenAI Service Chat API
  slug: microsoft-azure-openai-chat-api
- description: The Completions API from Azure OpenAI Service — 1 operation(s) for completions.
  name: Azure OpenAI Service Completions API
  slug: microsoft-azure-openai-completions-api
- description: The Embeddings API from Azure OpenAI Service — 1 operation(s) for embeddings.
  name: Azure OpenAI Service Embeddings API
  slug: microsoft-azure-openai-embeddings-api
- description: The Images API from Azure OpenAI Service — 1 operation(s) for images.
  name: Azure OpenAI Service Images API
  slug: microsoft-azure-openai-images-api
artifact_total: 12
collections:
- collection_type: open
  name: Azure OpenAI Service REST API
  slug: open-microsoft-azure-openai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-openai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-openai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-openai-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-openai-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/cognitive-services/openai-service/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/ai-services/openai/
- group: company
  title: ''
  type: Website
  url: https://azure.microsoft.com/en-us/products/ai-services/openai-service
- group: start
  title: ''
  type: Signup
  url: https://azure.microsoft.com/en-us/free/
- group: start
  title: ''
  type: Login
  url: https://portal.azure.com/
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: agent
  title: ''
  type: LlmsText
  url: https://portal.azure.com/llms.txt
created: '2026-03-13'
description: Azure OpenAI Service provides REST API access to OpenAI large language models including GPT-4, GPT-4o, GPT-3.5 Turbo, DALL-E, and Whisper with enterprise-grade security, compliance, and regional availability.
finops:
- name: Microsoft Azure Openai Finops
  service_category: API
  slug: microsoft-azure-openai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-openai.png
layout: provider
modified: '2026-05-19'
name: Azure OpenAI Service
nav: Providers
network: true
overview: 'Azure OpenAI Service publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Chat API, Completions API, Embeddings API, and 1 more. Tagged areas include AI, Embeddings, GPT, Generative AI, and Large Language Models.


  Azure OpenAI Service''s developer surface includes authentication, developer portal, pricing, documentation, signup flow, support, and 9 more developer resources.'
plans:
- name: Microsoft Azure Openai Plans Pricing
  plan_count: 3
  slug: microsoft-azure-openai-plans-pricing
random_paper: 45
rate_limits:
- limit_count: 5
  name: Microsoft Azure Openai Rate Limits
  slug: microsoft-azure-openai-rate-limits
scopes:
- name: Microsoft Azure Openai Scopes
  scope_count: 1
  slug: microsoft-azure-openai-scopes
  summary_line: 1 scope · implicit
score:
  band: developing
  composite: 49.3
  delta: -2.1
  facets:
    commercial_clarity: 84.2
    contract_quality: 55.1
    developer_ergonomics: 32.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 51.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-openai/refs/heads/main/screenshots/microsoft-azure-openai-2026-06-20T185429.png
security:
- kind: authentication
  name: Microsoft Azure Openai Authentication
  slug: microsoft-azure-openai-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Microsoft Azure Openai Domain Security
  slug: microsoft-azure-openai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-openai
tags:
- AI
- Embeddings
- GPT
- Generative AI
- Large Language Models
- OpenAI
website: https://azure.microsoft.com/en-us/products/ai-services/openai-service
---
