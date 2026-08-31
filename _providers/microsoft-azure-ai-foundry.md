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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.2
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Microsoft Azure Ai Foundry Agentic Access
  operation_count: 7
  slug: microsoft-azure-ai-foundry-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 2
apis:
- description: Operations operations
  name: Microsoft Azure AI Foundry Operations API
  slug: microsoft-azure-ai-foundry-operations-api
- description: Workspaces operations
  name: Microsoft Azure AI Foundry Workspaces API
  slug: microsoft-azure-ai-foundry-workspaces-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Azure Machine Learning REST Operations API
  slug: open-microsoft-azure-ai-foundry-operations-api
- collection_type: open
  name: Azure Machine Learning REST Operations Workspaces API
  slug: open-microsoft-azure-ai-foundry-workspaces-api
- collection_type: open
  name: Azure Machine Learning REST API
  slug: open-microsoft-azure-ai-foundry
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-ai-foundry-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-ai-foundry-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-ai-foundry-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-ai-foundry-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/ai-foundry/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/
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
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/Azure/ai-foundry-isv-mcp-agent
- group: agent
  title: ''
  type: LlmsText
  url: https://portal.azure.com/llms.txt
created: '2026-03-13'
description: Microsoft Azure AI Foundry is a unified platform for building, evaluating, and deploying generative AI applications. It provides a model catalog, prompt engineering tools, fine-tuning capabilities, retrieval augmented generation (RAG) patterns, and responsible AI evaluation across a comprehensive set of management and data plane APIs.
finops:
- name: Microsoft Azure Ai Foundry Finops
  service_category: API
  slug: microsoft-azure-ai-foundry-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-ai-foundry.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Microsoft Azure AI Foundry
nav: Providers
network: true
overview: 'Microsoft Azure AI Foundry publishes 2 APIs on the [APIs.io](https://apis.io/) network: Operations API and Workspaces API. Tagged areas include Artificial Intelligence, AI Services, Generative AI, Microsoft Azure, and Model Catalog.


  Microsoft Azure AI Foundry''s developer surface includes authentication, developer portal, documentation, pricing, support, and 9 more developer resources.'
plans:
- name: Microsoft Azure Ai Foundry Plans Pricing
  plan_count: 3
  slug: microsoft-azure-ai-foundry-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Microsoft Azure Ai Foundry Rate Limits
  slug: microsoft-azure-ai-foundry-rate-limits
scopes:
- name: Microsoft Azure Ai Foundry Scopes
  scope_count: 1
  slug: microsoft-azure-ai-foundry-scopes
  summary_line: 1 scope · implicit
score:
  band: developing
  composite: 42.7
  coverage:
    artifact_dirs: 11
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 49.0
    developer_ergonomics: 50.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 42.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-ai-foundry/refs/heads/main/screenshots/microsoft-azure-ai-foundry-2026-06-20T185353.png
security:
- kind: authentication
  name: Microsoft Azure Ai Foundry Authentication
  slug: microsoft-azure-ai-foundry-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Ai Foundry Domain Security
  slug: microsoft-azure-ai-foundry-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-ai-foundry
tags:
- Artificial Intelligence
- AI Services
- Generative AI
- Microsoft Azure
- Model Catalog
website: https://portal.azure.com/
---
