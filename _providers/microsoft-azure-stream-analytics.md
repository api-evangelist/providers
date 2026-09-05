---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
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
- acting_count: 6
  human_in_the_loop: 1
  name: Microsoft Azure Stream Analytics Agentic Access
  operation_count: 14
  slug: microsoft-azure-stream-analytics-agentic-access
  summary_line: 14 operations · 6 acting · 1 human-in-the-loop
api_count: 6
apis:
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Clusters API from Azure Stream Analytics — 1 operation(s) for clusters.
  name: Azure Stream Analytics Clusters API
  slug: microsoft-azure-stream-analytics-clusters-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Functions API from Azure Stream Analytics — 1 operation(s) for functions.
  name: Azure Stream Analytics Functions API
  slug: microsoft-azure-stream-analytics-functions-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Inputs API from Azure Stream Analytics — 1 operation(s) for inputs.
  name: Azure Stream Analytics Inputs API
  slug: microsoft-azure-stream-analytics-inputs-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Outputs API from Azure Stream Analytics — 1 operation(s) for outputs.
  name: Azure Stream Analytics Outputs API
  slug: microsoft-azure-stream-analytics-outputs-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The StreamingJobs API from Azure Stream Analytics — 5 operation(s) for streamingjobs.
  name: Azure Stream Analytics StreamingJobs API
  slug: microsoft-azure-stream-analytics-streamingjobs-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Transformations API from Azure Stream Analytics — 1 operation(s) for transformations.
  name: Azure Stream Analytics Transformations API
  slug: microsoft-azure-stream-analytics-transformations-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Azure Stream Analytics REST Clusters API
  slug: open-microsoft-azure-stream-analytics-clusters-api
- collection_type: open
  name: Azure Stream Analytics REST Clusters Functions API
  slug: open-microsoft-azure-stream-analytics-functions-api
- collection_type: open
  name: Azure Stream Analytics REST Clusters Inputs API
  slug: open-microsoft-azure-stream-analytics-inputs-api
- collection_type: open
  name: Azure Stream Analytics REST Clusters Outputs API
  slug: open-microsoft-azure-stream-analytics-outputs-api
- collection_type: open
  name: Azure Stream Analytics REST Clusters StreamingJobs API
  slug: open-microsoft-azure-stream-analytics-streamingjobs-api
- collection_type: open
  name: Azure Stream Analytics REST Clusters Transformations API
  slug: open-microsoft-azure-stream-analytics-transformations-api
- collection_type: open
  name: Azure Stream Analytics REST API
  slug: open-microsoft-azure-stream-analytics
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-stream-analytics-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-stream-analytics-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-stream-analytics-authentication.yml
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
  url: https://azure.microsoft.com/en-us/pricing/details/stream-analytics/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/stream-analytics/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/stream-analytics/stream-analytics-quick-create-portal
- group: operate
  title: ''
  type: StatusPage
  url: https://azure.status.microsoft/en-us/status
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
  url: https://azure.microsoft.com/en-us/blog/product/stream-analytics/
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/azure-stream-analytics
- group: agent
  title: ''
  type: LlmsText
  url: https://portal.azure.com/llms.txt
created: '2026-03-13'
description: Azure Stream Analytics REST API provides management of real-time analytics jobs that process streaming data from IoT devices, Event Hubs, and blob storage. It supports creating streaming jobs, defining input sources, output destinations, and transformation queries using SQL-like syntax.
finops:
- name: Microsoft Azure Stream Analytics Finops
  service_category: API
  slug: microsoft-azure-stream-analytics-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-stream-analytics.png
layout: provider
modified: '2026-05-19'
name: Azure Stream Analytics
nav: Providers
network: true
overview: 'Azure Stream Analytics publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Clusters API, Functions API, Inputs API, and 3 more. Tagged areas include Stream Processing, Real-Time Analytics, IoT, and Event Processing.


  Azure Stream Analytics'' developer surface includes authentication, developer portal, pricing, documentation, getting-started guide, support, engineering blog, and 8 more developer resources.'
plans:
- name: Microsoft Azure Stream Analytics Plans Pricing
  plan_count: 3
  slug: microsoft-azure-stream-analytics-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Microsoft Azure Stream Analytics Rate Limits
  slug: microsoft-azure-stream-analytics-rate-limits
score:
  band: developing
  composite: 41.5
  coverage:
    artifact_dirs: 11
    catalog_earned: 44.0
    catalog_earned_first_party: 0.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 47.6
    developer_ergonomics: 47.6
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 41.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-stream-analytics/refs/heads/main/screenshots/microsoft-azure-stream-analytics-2026-06-20T185440.png
security:
- kind: authentication
  name: Microsoft Azure Stream Analytics Authentication
  slug: microsoft-azure-stream-analytics-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Microsoft Azure Stream Analytics Domain Security
  slug: microsoft-azure-stream-analytics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-stream-analytics
tags:
- Stream Processing
- Real-Time Analytics
- IoT
- Event Processing
website: https://portal.azure.com/
---
