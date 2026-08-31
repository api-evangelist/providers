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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Microsoft Azure Advisor Agentic Access
  operation_count: 7
  slug: microsoft-azure-advisor-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 2
apis:
- description: Operations operations
  name: Microsoft Azure Advisor Operations API
  slug: microsoft-azure-advisor-operations-api
- description: Recommendations operations
  name: Microsoft Azure Advisor Recommendations API
  slug: microsoft-azure-advisor-recommendations-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Azure Advisor REST Operations API
  slug: open-microsoft-azure-advisor-operations-api
- collection_type: open
  name: Azure Advisor REST Operations Recommendations API
  slug: open-microsoft-azure-advisor-recommendations-api
- collection_type: open
  name: Azure Advisor REST API
  slug: open-microsoft-azure-advisor
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-advisor-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-advisor-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-advisor-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-advisor-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/advisor/
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
  type: LlmsText
  url: https://portal.azure.com/llms.txt
created: '2026-03-13'
description: Microsoft Azure Advisor is a personalized cloud consultant that helps you follow best practices to optimize your Azure deployments. It analyzes your resource configuration and usage telemetry, then recommends solutions to improve the cost effectiveness, performance, reliability, security, and operational excellence of your Azure resources.
finops:
- name: Microsoft Azure Advisor Finops
  service_category: API
  slug: microsoft-azure-advisor-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-advisor.png
layout: provider
modified: '2026-05-19'
name: Microsoft Azure Advisor
nav: Providers
network: true
overview: 'Microsoft Azure Advisor publishes 2 APIs on the [APIs.io](https://apis.io/) network: Operations API and Recommendations API. Tagged areas include Advisor, Best Practices, Cost Optimization, Microsoft Azure, and Optimization.


  Microsoft Azure Advisor''s developer surface includes authentication, developer portal, documentation, pricing, support, and 8 more developer resources.'
plans:
- name: Microsoft Azure Advisor Plans Pricing
  plan_count: 3
  slug: microsoft-azure-advisor-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Microsoft Azure Advisor Rate Limits
  slug: microsoft-azure-advisor-rate-limits
scopes:
- name: Microsoft Azure Advisor Scopes
  scope_count: 1
  slug: microsoft-azure-advisor-scopes
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
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-advisor/refs/heads/main/screenshots/microsoft-azure-advisor-2026-06-20T185354.png
security:
- kind: authentication
  name: Microsoft Azure Advisor Authentication
  slug: microsoft-azure-advisor-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Advisor Domain Security
  slug: microsoft-azure-advisor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-advisor
tags:
- Advisor
- Best Practices
- Cost Optimization
- Microsoft Azure
- Optimization
- Recommendations
website: https://portal.azure.com/
---
