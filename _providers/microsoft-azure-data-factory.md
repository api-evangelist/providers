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
- acting_count: 3
  human_in_the_loop: 0
  name: Microsoft Azure Data Factory Agentic Access
  operation_count: 7
  slug: microsoft-azure-data-factory-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 2
apis:
- description: Factories operations
  name: microsoft-azure-data-factory Factories API
  slug: microsoft-azure-data-factory-factories-api
- description: Operations operations
  name: microsoft-azure-data-factory Operations API
  slug: microsoft-azure-data-factory-operations-api
artifact_total: 10
collections:
- collection_type: open
  name: Azure Data Factory REST API
  slug: open-microsoft-azure-data-factory
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-data-factory-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-data-factory-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-data-factory-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-data-factory-scopes.yml
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
description: 'Azure Data Factory is a cloud-based data integration service that orchestrates and automates the movement and transformation of data. This collection documents the REST APIs for managing pipelines, datasets, linked services, triggers, and data flows across ETL and ELT workloads spanning cloud and on-premises stores. - url: https://azure.microsoft.com/en-us/blog/azure-data-factory-announcing-new-capabilities-in-public-preview/ type: Blog'
finops:
- name: Microsoft Azure Data Factory Finops
  service_category: API
  slug: microsoft-azure-data-factory-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-data-factory.png
layout: provider
modified: '2026-05-19'
name: microsoft-azure-data-factory
nav: Providers
network: true
overview: 'microsoft-azure-data-factory publishes 2 APIs on the [APIs.io](https://apis.io/) network: Factories API and Operations API.


  microsoft-azure-data-factory''s developer surface includes authentication, developer portal, pricing, support, and 7 more developer resources.'
plans:
- name: Microsoft Azure Data Factory Plans Pricing
  plan_count: 3
  slug: microsoft-azure-data-factory-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Microsoft Azure Data Factory Rate Limits
  slug: microsoft-azure-data-factory-rate-limits
scopes:
- name: Microsoft Azure Data Factory Scopes
  scope_count: 1
  slug: microsoft-azure-data-factory-scopes
  summary_line: 1 scope · implicit
score:
  band: developing
  composite: 43.5
  delta: -1.6
  facets:
    commercial_clarity: 71.1
    contract_quality: 55.1
    developer_ergonomics: 23.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 45.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-data-factory/refs/heads/main/screenshots/microsoft-azure-data-factory-2026-06-20T185409.png
security:
- kind: authentication
  name: Microsoft Azure Data Factory Authentication
  slug: microsoft-azure-data-factory-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Data Factory Domain Security
  slug: microsoft-azure-data-factory-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-data-factory
website: https://portal.azure.com/
---
