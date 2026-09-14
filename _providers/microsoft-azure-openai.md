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
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Microsoft Azure Openai Agentic Access
  operation_count: 4
  slug: microsoft-azure-openai-agentic-access
  summary_line: 4 operations · 4 acting
api_count: 9
apis:
- baseURL: https://{resource}.openai.azure.com/
  baseurl_source: declared
  description: The Chat API from Azure OpenAI Service — 1 operation(s) for chat.
  name: Azure OpenAI Service Chat API
  slug: microsoft-azure-openai-chat-api
- baseURL: https://{resource}.openai.azure.com/
  baseurl_source: declared
  description: The Completions API from Azure OpenAI Service — 1 operation(s) for completions.
  name: Azure OpenAI Service Completions API
  slug: microsoft-azure-openai-completions-api
- baseURL: https://{resource}.openai.azure.com/
  baseurl_source: declared
  description: The Embeddings API from Azure OpenAI Service — 1 operation(s) for embeddings.
  name: Azure OpenAI Service Embeddings API
  slug: microsoft-azure-openai-embeddings-api
- baseURL: https://{resource}.openai.azure.com/
  baseurl_source: declared
  description: The Images API from Azure OpenAI Service — 1 operation(s) for images.
  name: Azure OpenAI Service Images API
  slug: microsoft-azure-openai-images-api
- description: Data-plane REST API for running inference against deployed Azure OpenAI models, including chat completions, completions, embeddings, image generation, and audio transcription/translation. Authenticate
  name: Azure OpenAI Inference REST API
  slug: inference-api
- description: Stateful, agent-friendly API for building multi-turn AI experiences with tool use, file inputs, and conversation state managed on the service side.
  name: Azure OpenAI Responses API
  slug: responses-api
- description: Azure Resource Manager (ARM) REST API for creating and managing Azure OpenAI accounts, model deployments, network rules, and other resource configuration.
  name: Azure OpenAI Control Plane API
  slug: control-plane
- baseURL: https://{your-resource-name}.openai.azure.com/openai
  baseurl_source: declared
  description: Audio transcription and translation (Whisper)
  name: Azure OpenAI Service Audio API
  slug: azure-openai-audio-api
- baseURL: https://{your-resource-name}.openai.azure.com/openai
  baseurl_source: declared
  description: Chat-formatted text generation
  name: Azure OpenAI Service Chat Completions API
  slug: azure-openai-chat-completions-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Azure OpenAI Service REST Chat API
  slug: open-microsoft-azure-openai-chat-api
- collection_type: open
  name: Azure OpenAI Service REST Chat Completions API
  slug: open-microsoft-azure-openai-completions-api
- collection_type: open
  name: Azure OpenAI Service REST Chat Embeddings API
  slug: open-microsoft-azure-openai-embeddings-api
- collection_type: open
  name: Azure OpenAI Service REST Chat Images API
  slug: open-microsoft-azure-openai-images-api
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
graphqls:
- description: Azure OpenAI Service provides REST API access to OpenAI models (GPT-4, GPT-3.5, DALL-E, Whisper, Embeddings) with enterprise SLAs, private networking, and Azure identity. The API covers completions, c
  name: Azure OpenAI Service GraphQL API
  slug: azure-openai-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-openai.png
layout: provider
modified: '2026-05-19'
name: Azure OpenAI Service
nav: Providers
network: true
overview: 'Azure OpenAI Service publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Chat API, Completions API, Embeddings API, and 4 more. Tagged areas include Artificial Intelligence, Embeddings, GPT, Generative AI, and Large Language Models.


  Azure OpenAI Service''s developer surface includes authentication, developer portal, pricing, documentation, signup flow, support, and 9 more developer resources.'
plans:
- name: Microsoft Azure Openai Plans Pricing
  plan_count: 3
  slug: microsoft-azure-openai-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Microsoft Azure Openai Rate Limits
  slug: microsoft-azure-openai-rate-limits
scopes:
- name: Microsoft Azure Openai Scopes
  scope_count: 1
  slug: microsoft-azure-openai-scopes
  summary_line: 1 scope · implicit
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
- Artificial Intelligence
- Embeddings
- GPT
- Generative AI
- Large Language Models
- OpenAI
website: https://azure.microsoft.com/en-us/products/ai-services/openai-service
---
