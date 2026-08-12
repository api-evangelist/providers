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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Microsoft Azure Cost Management Agentic Access
  operation_count: 7
  slug: microsoft-azure-cost-management-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 2
apis:
- description: Exports operations
  name: microsoft-azure-cost-management Exports API
  slug: microsoft-azure-cost-management-exports-api
- description: Operations operations
  name: microsoft-azure-cost-management Operations API
  slug: microsoft-azure-cost-management-operations-api
artifact_total: 10
collections:
- collection_type: open
  name: Azure Cost Management REST API
  slug: open-microsoft-azure-cost-management
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-cost-management-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-cost-management-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-cost-management-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-cost-management-scopes.yml
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
description: 'Azure Cost Management provides programmatic access to cost analysis, budgets, exports, and recommendations across cloud spending. This collection documents the REST APIs that support multidimensional usage queries, budget alerts, scheduled cost exports, and FinOps optimization recommendations. - url: https://azure.microsoft.com/en-us/blog/azure-cost-management-2019-year-in-review/ type: Blog'
finops:
- name: Microsoft Azure Cost Management Finops
  service_category: API
  slug: microsoft-azure-cost-management-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-cost-management.png
layout: provider
modified: '2026-05-19'
name: microsoft-azure-cost-management
nav: Providers
network: true
overview: 'microsoft-azure-cost-management publishes 2 APIs on the [APIs.io](https://apis.io/) network: Exports API and Operations API.


  microsoft-azure-cost-management''s developer surface includes authentication, developer portal, pricing, support, and 7 more developer resources.'
plans:
- name: Microsoft Azure Cost Management Plans Pricing
  plan_count: 3
  slug: microsoft-azure-cost-management-plans-pricing
random_paper: 30
rate_limits:
- limit_count: 5
  name: Microsoft Azure Cost Management Rate Limits
  slug: microsoft-azure-cost-management-rate-limits
scopes:
- name: Microsoft Azure Cost Management Scopes
  scope_count: 1
  slug: microsoft-azure-cost-management-scopes
  summary_line: 1 scope · implicit
score:
  band: thin
  composite: 36.1
  delta: -7.6
  facets:
    commercial_clarity: 47.4
    contract_quality: 53.7
    developer_ergonomics: 23.9
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 43.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cost-management/refs/heads/main/screenshots/microsoft-azure-cost-management-2026-06-20T185407.png
security:
- kind: authentication
  name: Microsoft Azure Cost Management Authentication
  slug: microsoft-azure-cost-management-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Cost Management Domain Security
  slug: microsoft-azure-cost-management-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-cost-management
website: https://portal.azure.com/
---
