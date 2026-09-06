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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 10
  human_in_the_loop: 1
  name: Microsoft Azure Site Recovery Agentic Access
  operation_count: 15
  slug: microsoft-azure-site-recovery-agentic-access
  summary_line: 15 operations · 10 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: Azure Site Recovery REST API provides management of disaster recovery for Azure VMs, on-premises VMs, and physical servers. It supports configuring replication, running test failovers, executing plann
  name: Azure Site Recovery REST API
  slug: rest-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Manage recovery plans for orchestrated failover
  name: Azure Site Recovery RecoveryPlans API
  slug: microsoft-azure-site-recovery-recoveryplans-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Manage replication protected items in a Recovery Services vault
  name: Azure Site Recovery ReplicationProtectedItems API
  slug: microsoft-azure-site-recovery-replicationprotecteditems-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Azure Site Recovery REST RecoveryPlans API
  slug: open-microsoft-azure-site-recovery-recoveryplans-api
- collection_type: open
  name: Azure Site Recovery REST RecoveryPlans ReplicationProtectedItems API
  slug: open-microsoft-azure-site-recovery-replicationprotecteditems-api
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
random_paper: 2
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
  composite: 41.0
  coverage:
    artifact_dirs: 12
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 47.6
    developer_ergonomics: 47.6
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 41.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
