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
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Microsoft Azure Arc Agentic Access
  operation_count: 7
  slug: microsoft-azure-arc-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 2
apis:
- description: Machines operations
  name: Azure Arc Machines API
  slug: microsoft-azure-arc-machines-api
- description: Operations operations
  name: Azure Arc Operations API
  slug: microsoft-azure-arc-operations-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Azure Arc Hybrid Compute REST Machines API
  slug: open-microsoft-azure-arc-machines-api
- collection_type: open
  name: Azure Arc Hybrid Compute REST Machines Operations API
  slug: open-microsoft-azure-arc-operations-api
- collection_type: open
  name: Azure Arc Hybrid Compute REST API
  slug: open-microsoft-azure-arc
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-arc-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-arc-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-arc-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-arc-scopes.yml
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
description: Operation groups for the Hybrid Compute REST API.
finops:
- name: Microsoft Azure Arc Finops
  service_category: API
  slug: microsoft-azure-arc-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-arc.png
layout: provider
modified: '2026-05-19'
name: Azure Arc
nav: Providers
network: true
overview: 'Azure Arc publishes 2 APIs on the [APIs.io](https://apis.io/) network: Machines API and Operations API. Tagged areas include Arc, Hybrid Cloud, Kubernetes, Multi-Cloud, and Server Management.


  Azure Arc''s developer surface includes authentication, developer portal, pricing, support, engineering blog, and 7 more developer resources.'
plans:
- name: Microsoft Azure Arc Plans Pricing
  plan_count: 3
  slug: microsoft-azure-arc-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Microsoft Azure Arc Rate Limits
  slug: microsoft-azure-arc-rate-limits
scopes:
- name: Microsoft Azure Arc Scopes
  scope_count: 1
  slug: microsoft-azure-arc-scopes
  summary_line: 1 scope · implicit
score:
  band: thin
  composite: 37.4
  coverage:
    artifact_dirs: 12
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 49.0
    developer_ergonomics: 38.1
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 37.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-arc/refs/heads/main/screenshots/microsoft-azure-arc-2026-06-20T185355.png
security:
- kind: authentication
  name: Microsoft Azure Arc Authentication
  slug: microsoft-azure-arc-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Arc Domain Security
  slug: microsoft-azure-arc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-arc
tags:
- Arc
- Hybrid Cloud
- Kubernetes
- Multi-Cloud
- Server Management
website: https://portal.azure.com/
---
