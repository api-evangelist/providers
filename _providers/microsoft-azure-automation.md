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
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Microsoft Azure Automation Agentic Access
  operation_count: 7
  slug: microsoft-azure-automation-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 2
apis:
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Automation Accounts operations
  name: Azure Automation Automation Accounts API
  slug: microsoft-azure-automation-automation-accounts-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Operations operations
  name: Azure Automation Operations API
  slug: microsoft-azure-automation-operations-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Azure Automation REST Automation Accounts API
  slug: open-microsoft-azure-automation-automation-accounts-api
- collection_type: open
  name: Azure Automation REST Automation Accounts Operations API
  slug: open-microsoft-azure-automation-operations-api
- collection_type: open
  name: Azure Automation REST API
  slug: open-microsoft-azure-automation
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-automation-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-automation-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-automation-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-automation-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/azureautomation
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
description: Learn how the Azure Automation service provides a highly reliable and scalable workflow execution engine to automate frequently repeated management tasks.
finops:
- name: Microsoft Azure Automation Finops
  service_category: API
  slug: microsoft-azure-automation-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-automation.png
layout: provider
modified: '2026-05-19'
name: Azure Automation
nav: Providers
network: true
overview: 'Azure Automation publishes 2 APIs on the [APIs.io](https://apis.io/) network: Automation Accounts API and Operations API. Tagged areas include Automation, Configuration Management, Runbooks, and Update Management.


  Azure Automation''s developer surface includes authentication, developer portal, pricing, support, engineering blog, and 7 more developer resources.'
plans:
- name: Microsoft Azure Automation Plans Pricing
  plan_count: 3
  slug: microsoft-azure-automation-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Microsoft Azure Automation Rate Limits
  slug: microsoft-azure-automation-rate-limits
scopes:
- name: Microsoft Azure Automation Scopes
  scope_count: 1
  slug: microsoft-azure-automation-scopes
  summary_line: 1 scope · implicit
score:
  band: thin
  composite: 36.5
  coverage:
    artifact_dirs: 12
    catalog_gap: 79.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 49.0
    developer_ergonomics: 38.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 36.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-automation/refs/heads/main/screenshots/microsoft-azure-automation-2026-06-20T185358.png
security:
- kind: authentication
  name: Microsoft Azure Automation Authentication
  slug: microsoft-azure-automation-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Automation Domain Security
  slug: microsoft-azure-automation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-automation
tags:
- Automation
- Configuration Management
- Runbooks
- Update Management
website: https://portal.azure.com/
---
