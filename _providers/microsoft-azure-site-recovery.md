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
- acting_count: 10
  human_in_the_loop: 1
  name: Microsoft Azure Site Recovery Agentic Access
  operation_count: 15
  slug: microsoft-azure-site-recovery-agentic-access
  summary_line: 15 operations · 10 acting · 1 human-in-the-loop
api_count: 3
apis:
- description: Azure Site Recovery REST API provides management of disaster recovery for Azure VMs, on-premises VMs, and physical servers. It supports configuring replication, running test failovers, executing plann
  name: Azure Site Recovery REST API
  slug: rest-api
- description: Manage recovery plans for orchestrated failover
  name: Azure Site Recovery RecoveryPlans API
  slug: microsoft-azure-site-recovery-recoveryplans-api
- description: Manage replication protected items in a Recovery Services vault
  name: Azure Site Recovery ReplicationProtectedItems API
  slug: microsoft-azure-site-recovery-replicationprotecteditems-api
artifact_total: 11
collections:
- collection_type: open
  name: Azure Site Recovery REST API
  slug: open-microsoft-azure-site-recovery
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-site-recovery-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-site-recovery-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-site-recovery-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-site-recovery-scopes.yml
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
  url: https://azure.microsoft.com/en-us/pricing/details/site-recovery/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/site-recovery/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/site-recovery/azure-to-azure-quickstart
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
  url: https://azure.microsoft.com/en-us/blog/product/site-recovery/
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/azure-site-recovery
- group: agent
  title: ''
  type: LlmsText
  url: https://portal.azure.com/llms.txt
created: '2026-03-13'
description: Azure Site Recovery REST API provides management of disaster recovery for Azure VMs, on-premises VMs, and physical servers. It supports configuring replication, running test failovers, executing planned and unplanned failovers, and managing recovery plans.
finops:
- name: Microsoft Azure Site Recovery Finops
  service_category: API
  slug: microsoft-azure-site-recovery-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-site-recovery.png
layout: provider
modified: '2026-04-28'
name: Azure Site Recovery
nav: Providers
network: true
overview: 'Azure Site Recovery publishes 2 APIs on the [APIs.io](https://apis.io/) network: RecoveryPlans API and ReplicationProtectedItems API. Tagged areas include Disaster Recovery, Replication, Business Continuity, and Failover.


  Azure Site Recovery''s developer surface includes authentication, developer portal, pricing, documentation, getting-started guide, support, engineering blog, and 9 more developer resources.'
plans:
- name: Microsoft Azure Site Recovery Plans Pricing
  plan_count: 3
  slug: microsoft-azure-site-recovery-plans-pricing
random_paper: 68
rate_limits:
- limit_count: 5
  name: Microsoft Azure Site Recovery Rate Limits
  slug: microsoft-azure-site-recovery-rate-limits
scopes:
- name: Microsoft Azure Site Recovery Scopes
  scope_count: 1
  slug: microsoft-azure-site-recovery-scopes
  summary_line: 1 scope · implicit
score:
  band: developing
  composite: 50.0
  delta: -1.8
  facets:
    commercial_clarity: 71.1
    contract_quality: 53.4
    developer_ergonomics: 45.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 51.8
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
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-site-recovery/refs/heads/main/screenshots/microsoft-azure-site-recovery-2026-06-20T185437.png
security:
- kind: authentication
  name: Microsoft Azure Site Recovery Authentication
  slug: microsoft-azure-site-recovery-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Site Recovery Domain Security
  slug: microsoft-azure-site-recovery-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-site-recovery
tags:
- Disaster Recovery
- Replication
- Business Continuity
- Failover
website: https://portal.azure.com/
---
