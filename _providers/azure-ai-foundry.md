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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Azure Ai Foundry Agentic Access
  operation_count: 7
  slug: azure-ai-foundry-agentic-access
  summary_line: 7 operations · 6 acting
api_count: 6
apis:
- description: REST API for managing Foundry projects, hubs, model deployments, agents, threads, runs, and evaluations. Authentication uses Microsoft Entra ID OAuth 2.0 bearer tokens (or API keys for inference endpo
  name: Azure AI Foundry REST API
  slug: foundry-api
- description: Chat-formatted text generation
  name: Microsoft Azure AI Foundry Chat Completions API
  slug: azure-ai-foundry-chat-completions-api
- description: Plain text completions
  name: Microsoft Azure AI Foundry Completions API
  slug: azure-ai-foundry-completions-api
- description: Vector embeddings for text
  name: Microsoft Azure AI Foundry Embeddings API
  slug: azure-ai-foundry-embeddings-api
- description: Image generation
  name: Microsoft Azure AI Foundry Images API
  slug: azure-ai-foundry-images-api
- description: Model and deployment metadata
  name: Microsoft Azure AI Foundry Models API
  slug: azure-ai-foundry-models-api
artifact_total: 12
collections:
- collection_type: open
  name: Azure AI Foundry Model Inference REST API
  slug: open-azure-ai-foundry
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/azure-ai-foundry-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/azure-ai-foundry-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/azure-ai-foundry-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/azure-ai-foundry-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/azure-ai-foundry-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/azure-ai-foundry
- group: company
  title: ''
  type: Website
  url: https://azure.microsoft.com/en-us/products/ai-foundry/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/ai-foundry/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/ai-foundry/
- group: start
  title: ''
  type: Signup
  url: https://azure.microsoft.com/en-us/free/
- group: agent
  title: ''
  type: LlmsText
  url: https://ai.azure.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/feed/atom/
created: '2026-05-11'
description: Microsoft Azure AI Foundry (formerly Azure AI Studio) is an end-to-end platform for building, optimizing, evaluating, and governing AI applications and agents at scale. It provides access to Foundry Models (including Azure OpenAI and open-source models), the Foundry Agent Service, content safety, observability, and responsible AI tooling. The Foundry REST APIs and Azure SDKs use Microsoft Entra ID OAuth 2.0 bearer tokens or API keys for authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/azure-ai-foundry.png
layout: provider
modified: '2026-05-11'
name: Microsoft Azure AI Foundry
nav: Providers
network: true
overview: 'Microsoft Azure AI Foundry publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Chat Completions API, Completions API, Embeddings API, and 2 more. Tagged areas include Artificial Intelligence, Generative AI, AI Agents, Foundation Models, and Machine Learning.


  Microsoft Azure AI Foundry''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 7 more developer resources.'
random_paper: 110
scopes:
- name: Azure Ai Foundry Scopes
  scope_count: 1
  slug: azure-ai-foundry-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: thin
  composite: 28.9
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 57.4
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 28.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/azure-ai-foundry/refs/heads/main/screenshots/azure-ai-foundry-2026-06-20T172847.png
security:
- kind: authentication
  name: Azure Ai Foundry Authentication
  slug: azure-ai-foundry-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Azure Ai Foundry Domain Security
  slug: azure-ai-foundry-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Azure Ai Foundry Vulnerability Disclosure
  slug: azure-ai-foundry-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: azure-ai-foundry
tags:
- Artificial Intelligence
- Generative AI
- AI Agents
- Foundation Models
- Machine Learning
- Cloud
- Azure
website: https://azure.microsoft.com/en-us/products/ai-foundry/
---
