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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.3
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Microsoft Power Platform Agentic Access
  operation_count: 8
  slug: microsoft-power-platform-agentic-access
  summary_line: 8 operations · 3 acting
api_count: 5
apis:
- description: The Microsoft Dataverse Web API provides OData v4 RESTful access to the Dataverse data platform that underpins Power Platform. Developers can perform CRUD operations on tables, execute actions and fun
  name: Microsoft Dataverse Web API
  slug: dataverse-api
- description: The Power Platform Admin API enables programmatic management of Power Platform environments, connectors, data loss prevention policies, and tenant settings. Administrators can create and manage enviro
  name: Power Platform Admin API
  slug: admin-api
- description: Power Platform Connectors provide pre-built integrations with hundreds of external services and enable developers to create custom connectors using OpenAPI definitions. Connectors abstract API authent
  name: Power Platform Connectors
  slug: connectors-api
- baseURL: https://{org}.api.crm.dynamics.com/api/data/v9.2/
  baseurl_source: declared
  description: The Metadata API from Microsoft Power Platform — 3 operation(s) for metadata.
  name: Microsoft Power Platform Metadata API
  slug: microsoft-power-platform-metadata-api
- baseURL: https://{org}.api.crm.dynamics.com/api/data/v9.2/
  baseurl_source: declared
  description: The Records API from Microsoft Power Platform — 2 operation(s) for records.
  name: Microsoft Power Platform Records API
  slug: microsoft-power-platform-records-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Microsoft Dataverse Web Metadata API
  slug: open-microsoft-power-platform-metadata-api
- collection_type: open
  name: Microsoft Dataverse Web Metadata Records API
  slug: open-microsoft-power-platform-records-api
- collection_type: open
  name: Microsoft Dataverse Web API
  slug: open-microsoft-power-platform
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-power-platform-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-power-platform-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-power-platform-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-power-platform-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/microsoft-power-platform
- group: start
  title: ''
  type: Portal
  url: https://make.powerapps.com/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/power-platform/
- group: commercial
  title: ''
  type: Pricing
  url: https://powerapps.microsoft.com/en-us/pricing/
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/power-platform/admin/programmability-authentication-v2
- group: company
  title: ''
  type: Blog
  url: https://powerplatform.microsoft.com/en-us/blog/
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
- group: operate
  title: ''
  type: StatusPage
  url: https://status.powerplatform.microsoft.com/
created: '2024-01-01'
description: Microsoft Power Platform is a suite of low-code development tools including Power Apps, Power Automate, Power BI, and Power Virtual Agents. It provides APIs for accessing Dataverse, managing environments, and integrating with external services through connectors.
finops:
- name: Microsoft Power Platform Finops
  service_category: API
  slug: microsoft-power-platform-finops
image: /assets/icons/microsoft-power-platform.png
layout: provider
modified: '2026-04-19'
name: Microsoft Power Platform
nav: Providers
network: true
overview: 'Microsoft Power Platform publishes 2 APIs on the [APIs.io](https://apis.io/) network: Metadata API and Records API. Tagged areas include Dataverse, Low-Code, Microsoft, Power Apps, and Power Automate.


  Microsoft Power Platform''s developer surface includes authentication, developer portal, documentation, pricing, engineering blog, support, and 9 more developer resources.'
plans:
- name: Microsoft Power Platform Plans Pricing
  plan_count: 3
  slug: microsoft-power-platform-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Microsoft Power Platform Rate Limits
  slug: microsoft-power-platform-rate-limits
scopes:
- name: Microsoft Power Platform Scopes
  scope_count: 1
  slug: microsoft-power-platform-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 43.5
  coverage:
    artifact_dirs: 11
    catalog_gap: 71.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 50.6
    developer_ergonomics: 50.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 43.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 50.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-power-platform/refs/heads/main/screenshots/microsoft-power-platform-2026-06-20T185525.png
security:
- kind: authentication
  name: Microsoft Power Platform Authentication
  slug: microsoft-power-platform-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Power Platform Domain Security
  slug: microsoft-power-platform-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-power-platform
tags:
- Dataverse
- Low-Code
- Microsoft
- Power Apps
- Power Automate
- Power BI
website: https://make.powerapps.com/
---
