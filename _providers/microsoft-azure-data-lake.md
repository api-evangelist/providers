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
  scored_at: '2026-08-17'
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
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Azure Data Lake Storage Gen2 REST Filesystems API
  slug: open-microsoft-azure-data-lake-filesystems-api
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
random_paper: 107
rate_limits:
- limit_count: 5
  name: Microsoft Azure Data Lake Rate Limits
  slug: microsoft-azure-data-lake-rate-limits
score:
  band: thin
  composite: 35.5
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 54.5
    developer_ergonomics: 23.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 35.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.11.0
  scored_at: '2026-08-17'
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
