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
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Microsoft Azure Batch Agentic Access
  operation_count: 8
  slug: microsoft-azure-batch-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 3
apis:
- baseURL: https://batch.core.windows.net/
  baseurl_source: declared
  description: The Jobs API from microsoft-azure-batch — 1 operation(s) for jobs.
  name: microsoft-azure-batch Jobs API
  slug: microsoft-azure-batch-jobs-api
- baseURL: https://batch.core.windows.net/
  baseurl_source: declared
  description: The Pools API from microsoft-azure-batch — 2 operation(s) for pools.
  name: microsoft-azure-batch Pools API
  slug: microsoft-azure-batch-pools-api
- baseURL: https://batch.core.windows.net/
  baseurl_source: declared
  description: The Tasks API from microsoft-azure-batch — 1 operation(s) for tasks.
  name: microsoft-azure-batch Tasks API
  slug: microsoft-azure-batch-tasks-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Azure Batch Service REST Jobs API
  slug: open-microsoft-azure-batch-jobs-api
- collection_type: open
  name: Azure Batch Service REST Jobs Pools API
  slug: open-microsoft-azure-batch-pools-api
- collection_type: open
  name: Azure Batch Service REST Jobs Tasks API
  slug: open-microsoft-azure-batch-tasks-api
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
name: Microsoft Azure Batch
nav: Providers
network: true
overview: 'Microsoft Azure Batch publishes 3 APIs on the [APIs.io](https://apis.io/) network: microsoft-azure-batch Jobs API, microsoft-azure-batch Pools API, and microsoft-azure-batch Tasks API.


  Microsoft Azure Batch''s developer surface includes authentication, developer portal, pricing, support, engineering blog, and 6 more developer resources.'
plans:
- name: Microsoft Azure Batch Plans Pricing
  plan_count: 3
  slug: microsoft-azure-batch-plans-pricing
random_paper: 16
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
  band: thin
  composite: 36.3
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.0
    catalog_earned_first_party: 0.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 49.0
    developer_ergonomics: 38.1
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 36.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    note: provider declares no identity tags; regime could not be determined
    undetermined: true
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
