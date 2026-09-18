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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.7
  scored_at: '2026-09-17'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Azure Ai Foundry Agentic Access
  operation_count: 7
  slug: azure-ai-foundry-agentic-access
  summary_line: 7 operations · 6 acting
api_count: 1
apis:
- description: REST API for managing Foundry projects, hubs, model deployments, agents, threads, runs, and evaluations. Authentication uses Microsoft Entra ID OAuth 2.0 bearer tokens (or API keys for inference endpo
  name: Azure AI Foundry REST API
  slug: foundry-api
- baseURL: https://{your-resource-name}.services.ai.azure.com
  baseurl_source: declared
  description: Chat-formatted text generation
  name: Microsoft Azure AI Foundry Chat Completions API
  slug: azure-ai-foundry-chat-completions-api
- baseURL: https://{your-resource-name}.services.ai.azure.com
  baseurl_source: declared
  description: Plain text completions
  name: Microsoft Azure AI Foundry Completions API
  slug: azure-ai-foundry-completions-api
- baseURL: https://{your-resource-name}.services.ai.azure.com
  baseurl_source: declared
  description: Vector embeddings for text
  name: Microsoft Azure AI Foundry Embeddings API
  slug: azure-ai-foundry-embeddings-api
- baseURL: https://{your-resource-name}.services.ai.azure.com
  baseurl_source: declared
  description: Image generation
  name: Microsoft Azure AI Foundry Images API
  slug: azure-ai-foundry-images-api
- baseURL: https://{your-resource-name}.services.ai.azure.com
  baseurl_source: declared
  description: Model and deployment metadata
  name: Microsoft Azure AI Foundry Models API
  slug: azure-ai-foundry-models-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Operations operations
  name: Microsoft Azure AI Foundry Operations API
  slug: microsoft-azure-ai-foundry-operations-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Workspaces operations
  name: Microsoft Azure AI Foundry Workspaces API
  slug: microsoft-azure-ai-foundry-workspaces-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Azure AI Foundry Model Inference REST Chat Completions API
  slug: open-azure-ai-foundry-chat-completions-api
- collection_type: open
  name: Azure AI Foundry Model Inference REST Chat Completions API
  slug: open-azure-ai-foundry-completions-api
- collection_type: open
  name: Azure AI Foundry Model Inference REST Chat Completions Embeddings API
  slug: open-azure-ai-foundry-embeddings-api
- collection_type: open
  name: Azure AI Foundry Model Inference REST Chat Completions Images API
  slug: open-azure-ai-foundry-images-api
- collection_type: open
  name: Azure AI Foundry Model Inference REST Chat Completions Models API
  slug: open-azure-ai-foundry-models-api
- collection_type: open
  name: Azure AI Foundry Model Inference REST API
  slug: open-azure-ai-foundry
common:
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.azure.com/
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/Azure/ai-foundry-isv-mcp-agent
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/azure-ai-foundry/refs/heads/main/agentic-access/azure-ai-foundry-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/azure-ai-foundry-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/azure-ai-foundry/refs/heads/main/security/azure-ai-foundry-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/azure-ai-foundry-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/azure-ai-foundry/refs/heads/main/security/azure-ai-foundry-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/azure-ai-foundry-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/azure-ai-foundry/refs/heads/main/authentication/azure-ai-foundry-authentication.yml
  title: ''
  type: Authentication
  url: authentication/azure-ai-foundry-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/azure-ai-foundry/refs/heads/main/scopes/azure-ai-foundry-scopes.yml
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
mcp_servers:
- description: ''
  name: Microsoft Azure AI Foundry MCP Server
  slug: microsoft-azure-ai-foundry-mcp-server
modified: '2026-05-11'
name: Microsoft Azure AI Foundry
nav: Providers
network: true
overview: 'Microsoft Azure AI Foundry publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Chat Completions API, Completions API, Embeddings API, and 4 more. Tagged areas include Artificial Intelligence, Generative AI, AI Agents, Foundation Models, and Machine-Learning.


  Microsoft Azure AI Foundry''s developer surface includes developer portal, support, authentication, documentation, pricing, signup flow, engineering blog, and 11 more developer resources.'
random_paper: 12
scopes:
- name: Azure Ai Foundry Scopes
  scope_count: 1
  slug: azure-ai-foundry-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: developing
  composite: 44.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 50.0
    developer_ergonomics: 52.4
    discoverability: 83.3
    operational_transparency: 18.4
  previous_composite: 44.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: flat
  upsert:
    applies: true
    score: 22.2
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
- Machine-Learning
- Cloud
- Azure
website: https://azure.microsoft.com/en-us/products/ai-foundry/
---
