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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Microsoft Azure Container Instances Agentic Access
  operation_count: 7
  slug: microsoft-azure-container-instances-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 2
apis:
- description: Container Groups operations
  name: microsoft-azure-container-instances Container Groups API
  slug: microsoft-azure-container-instances-container-groups-api
- description: Operations operations
  name: microsoft-azure-container-instances Operations API
  slug: microsoft-azure-container-instances-operations-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Azure Container Instances REST Container Groups API
  slug: open-microsoft-azure-container-instances-container-groups-api
- collection_type: open
  name: Azure Container Instances REST Container Groups Operations API
  slug: open-microsoft-azure-container-instances-operations-api
- collection_type: open
  name: Azure Container Instances REST API
  slug: open-microsoft-azure-container-instances
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-container-instances-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-container-instances-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-container-instances-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-container-instances-scopes.yml
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
- group: agent
  title: ''
  type: LlmsText
  url: https://portal.azure.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/feed/
description: Azure Container Instances offers the fastest and simplest way to run containers in Azure without managing virtual machines or higher-level orchestrators. This collection captures the REST API surface for creating container groups, configuring networking and storage, and operating serverless containers on demand.
finops:
- name: Microsoft Azure Container Instances Finops
  service_category: API
  slug: microsoft-azure-container-instances-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-container-instances.png
layout: provider
modified: '2026-05-19'
name: microsoft-azure-container-instances
nav: Providers
network: true
overview: 'microsoft-azure-container-instances publishes 2 APIs on the [APIs.io](https://apis.io/) network: Container Groups API and Operations API.


  microsoft-azure-container-instances'' developer surface includes authentication, developer portal, pricing, support, engineering blog, and 7 more developer resources.'
plans:
- name: Microsoft Azure Container Instances Plans Pricing
  plan_count: 3
  slug: microsoft-azure-container-instances-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Microsoft Azure Container Instances Rate Limits
  slug: microsoft-azure-container-instances-rate-limits
scopes:
- name: Microsoft Azure Container Instances Scopes
  scope_count: 1
  slug: microsoft-azure-container-instances-scopes
  summary_line: 1 scope · implicit
score:
  band: thin
  composite: 35.1
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 50.3
    developer_ergonomics: 28.6
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 35.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: false
    note: provider carries no tags; regime could not be determined
    undetermined: true
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-container-instances/refs/heads/main/screenshots/microsoft-azure-container-instances-2026-06-20T185406.png
security:
- kind: authentication
  name: Microsoft Azure Container Instances Authentication
  slug: microsoft-azure-container-instances-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Container Instances Domain Security
  slug: microsoft-azure-container-instances-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-container-instances
website: https://portal.azure.com/
---
