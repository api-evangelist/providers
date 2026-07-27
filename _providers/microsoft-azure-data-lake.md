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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Microsoft Azure Data Lake Agentic Access
  operation_count: 7
  slug: microsoft-azure-data-lake-agentic-access
  summary_line: 7 operations · 4 acting
api_count: 1
apis:
- description: Filesystems operations
  name: Azure Data Lake Storage Filesystems API
  slug: microsoft-azure-data-lake-filesystems-api
artifact_total: 8
collections:
- collection_type: open
  name: Azure Data Lake Storage Gen2 REST API
  slug: open-microsoft-azure-data-lake
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-data-lake-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-data-lake-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-data-lake-authentication.yml
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
created: '2024-01-01'
description: Azure Data Lake Storage Gen2 REST API provides a file system interface for big data analytics workloads on Azure Blob Storage. It supports creating file systems, managing directories and files with hierarchical namespace, setting ACLs, and integrating with analytics engines.
finops:
- name: Microsoft Azure Data Lake Finops
  service_category: API
  slug: microsoft-azure-data-lake-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-data-lake.png
layout: provider
modified: '2026-05-19'
name: Azure Data Lake Storage
nav: Providers
network: true
overview: 'Azure Data Lake Storage publishes 1 API on the [APIs.io](https://apis.io/) network: Filesystems API. Tagged areas include Analytics, Big Data, Data Lake, and Hierarchical Storage.


  Azure Data Lake Storage''s developer surface includes authentication, developer portal, pricing, support, and 5 more developer resources.'
plans:
- name: Microsoft Azure Data Lake Plans Pricing
  plan_count: 3
  slug: microsoft-azure-data-lake-plans-pricing
random_paper: 43
rate_limits:
- limit_count: 5
  name: Microsoft Azure Data Lake Rate Limits
  slug: microsoft-azure-data-lake-rate-limits
score:
  band: developing
  composite: 45.1
  delta: 3.3
  facets:
    commercial_clarity: 71.1
    contract_quality: 53.1
    developer_ergonomics: 23.9
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 41.8
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-data-lake/refs/heads/main/screenshots/microsoft-azure-data-lake-2026-06-20T185410.png
security:
- kind: authentication
  name: Microsoft Azure Data Lake Authentication
  slug: microsoft-azure-data-lake-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Microsoft Azure Data Lake Domain Security
  slug: microsoft-azure-data-lake-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-data-lake
tags:
- Analytics
- Big Data
- Data Lake
- Hierarchical Storage
website: https://portal.azure.com/
---
