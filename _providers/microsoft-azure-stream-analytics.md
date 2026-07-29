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
- acting_count: 6
  human_in_the_loop: 1
  name: Microsoft Azure Stream Analytics Agentic Access
  operation_count: 14
  slug: microsoft-azure-stream-analytics-agentic-access
  summary_line: 14 operations · 6 acting · 1 human-in-the-loop
api_count: 6
apis:
- description: The Clusters API from Azure Stream Analytics — 1 operation(s) for clusters.
  name: Azure Stream Analytics Clusters API
  slug: microsoft-azure-stream-analytics-clusters-api
- description: The Functions API from Azure Stream Analytics — 1 operation(s) for functions.
  name: Azure Stream Analytics Functions API
  slug: microsoft-azure-stream-analytics-functions-api
- description: The Inputs API from Azure Stream Analytics — 1 operation(s) for inputs.
  name: Azure Stream Analytics Inputs API
  slug: microsoft-azure-stream-analytics-inputs-api
- description: The Outputs API from Azure Stream Analytics — 1 operation(s) for outputs.
  name: Azure Stream Analytics Outputs API
  slug: microsoft-azure-stream-analytics-outputs-api
- description: The StreamingJobs API from Azure Stream Analytics — 5 operation(s) for streamingjobs.
  name: Azure Stream Analytics StreamingJobs API
  slug: microsoft-azure-stream-analytics-streamingjobs-api
- description: The Transformations API from Azure Stream Analytics — 1 operation(s) for transformations.
  name: Azure Stream Analytics Transformations API
  slug: microsoft-azure-stream-analytics-transformations-api
artifact_total: 13
collections:
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
random_paper: 8
rate_limits:
- limit_count: 5
  name: Microsoft Azure Stream Analytics Rate Limits
  slug: microsoft-azure-stream-analytics-rate-limits
score:
  band: developing
  composite: 49.2
  delta: -1.7
  facets:
    commercial_clarity: 71.1
    contract_quality: 50.0
    developer_ergonomics: 45.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 50.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
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
