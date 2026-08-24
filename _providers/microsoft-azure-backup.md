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
  name: Microsoft Azure Backup Agentic Access
  operation_count: 7
  slug: microsoft-azure-backup-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 2
apis:
- description: Operations operations
  name: Azure Backup Operations API
  slug: microsoft-azure-backup-operations-api
- description: Vaults operations
  name: Azure Backup Vaults API
  slug: microsoft-azure-backup-vaults-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Azure Backup REST Operations API
  slug: open-microsoft-azure-backup-operations-api
- collection_type: open
  name: Azure Backup REST Operations Vaults API
  slug: open-microsoft-azure-backup-vaults-api
- collection_type: open
  name: Azure Backup REST API
  slug: open-microsoft-azure-backup
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-backup-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-backup-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-backup-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-backup-scopes.yml
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
created: '2026-03-13'
description: Learn how Azure Backup contributes to your business continuity and disaster recovery (BCDR) strategy by backing up data to the Azure clouds.
finops:
- name: Microsoft Azure Backup Finops
  service_category: API
  slug: microsoft-azure-backup-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-backup.png
layout: provider
modified: '2026-05-19'
name: Azure Backup
nav: Providers
network: true
overview: 'Azure Backup publishes 2 APIs on the [APIs.io](https://apis.io/) network: Operations API and Vaults API. Tagged areas include Backup, Data Protection, Disaster Recovery, and Recovery Services.


  Azure Backup''s developer surface includes authentication, developer portal, pricing, support, engineering blog, and 7 more developer resources.'
plans:
- name: Microsoft Azure Backup Plans Pricing
  plan_count: 3
  slug: microsoft-azure-backup-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Microsoft Azure Backup Rate Limits
  slug: microsoft-azure-backup-rate-limits
scopes:
- name: Microsoft Azure Backup Scopes
  scope_count: 1
  slug: microsoft-azure-backup-scopes
  summary_line: 1 scope · implicit
score:
  band: thin
  composite: 34.1
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 50.3
    developer_ergonomics: 28.6
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 34.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-backup/refs/heads/main/screenshots/microsoft-azure-backup-2026-06-20T185400.png
security:
- kind: authentication
  name: Microsoft Azure Backup Authentication
  slug: microsoft-azure-backup-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Backup Domain Security
  slug: microsoft-azure-backup-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-backup
tags:
- Backup
- Data Protection
- Disaster Recovery
- Recovery Services
website: https://portal.azure.com/
---
