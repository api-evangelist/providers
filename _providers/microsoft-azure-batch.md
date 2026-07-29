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
  name: Microsoft Azure Batch Agentic Access
  operation_count: 8
  slug: microsoft-azure-batch-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 3
apis:
- description: The Jobs API from microsoft-azure-batch — 1 operation(s) for jobs.
  name: microsoft-azure-batch Jobs API
  slug: microsoft-azure-batch-jobs-api
- description: The Pools API from microsoft-azure-batch — 2 operation(s) for pools.
  name: microsoft-azure-batch Pools API
  slug: microsoft-azure-batch-pools-api
- description: The Tasks API from microsoft-azure-batch — 1 operation(s) for tasks.
  name: microsoft-azure-batch Tasks API
  slug: microsoft-azure-batch-tasks-api
artifact_total: 11
collections:
- collection_type: open
  name: Azure Batch Service REST API
  slug: open-microsoft-azure-batch
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-batch-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-batch-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-batch-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-batch-scopes.yml
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
- group: company
  title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/feed/
created: '2026-03-13'
description: Learn how to use the Azure Batch API to schedule and run large scale computational workloads.
finops:
- name: Microsoft Azure Batch Finops
  service_category: API
  slug: microsoft-azure-batch-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-batch.png
layout: provider
modified: '2026-05-19'
name: microsoft-azure-batch
nav: Providers
network: true
overview: 'microsoft-azure-batch publishes 3 APIs on the [APIs.io](https://apis.io/) network: Jobs API, Pools API, and Tasks API.


  microsoft-azure-batch''s developer surface includes authentication, developer portal, pricing, support, engineering blog, and 6 more developer resources.'
plans:
- name: Microsoft Azure Batch Plans Pricing
  plan_count: 3
  slug: microsoft-azure-batch-plans-pricing
random_paper: 57
rate_limits:
- limit_count: 5
  name: Microsoft Azure Batch Rate Limits
  slug: microsoft-azure-batch-rate-limits
scopes:
- name: Microsoft Azure Batch Scopes
  scope_count: 1
  slug: microsoft-azure-batch-scopes
  summary_line: 1 scope · implicit
score:
  band: developing
  composite: 43.6
  delta: -1.4
  facets:
    commercial_clarity: 71.1
    contract_quality: 55.1
    developer_ergonomics: 26.1
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 45.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-batch/refs/heads/main/screenshots/microsoft-azure-batch-2026-06-20T185401.png
security:
- kind: authentication
  name: Microsoft Azure Batch Authentication
  slug: microsoft-azure-batch-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Batch Domain Security
  slug: microsoft-azure-batch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-batch
website: https://portal.azure.com/
---
