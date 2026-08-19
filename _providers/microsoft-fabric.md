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
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Microsoft Fabric Agentic Access
  operation_count: 17
  slug: microsoft-fabric-agentic-access
  summary_line: 17 operations · 10 acting
api_count: 5
apis:
- description: 'Microsoft Fabric provides SQL connectivity to lakehouses and data warehouses through TDS endpoints. Developers can query Fabric data using standard SQL tools, JDBC/ODBC drivers, and client libraries, '
  name: Microsoft Fabric SQL Connection
  slug: sql-connection-api
- description: The Capacities API from Microsoft Fabric — 1 operation(s) for capacities.
  name: Microsoft Fabric Capacities API
  slug: microsoft-fabric-capacities-api
- description: The Connections API from Microsoft Fabric — 1 operation(s) for connections.
  name: Microsoft Fabric Connections API
  slug: microsoft-fabric-connections-api
- description: The Items API from Microsoft Fabric — 6 operation(s) for items.
  name: Microsoft Fabric Items API
  slug: microsoft-fabric-items-api
- description: The Workspaces API from Microsoft Fabric — 2 operation(s) for workspaces.
  name: Microsoft Fabric Workspaces API
  slug: microsoft-fabric-workspaces-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Microsoft Fabric REST API (Core) Capacities API
  slug: open-microsoft-fabric-capacities-api
- collection_type: open
  name: Microsoft Fabric REST API (Core) Capacities Connections API
  slug: open-microsoft-fabric-connections-api
- collection_type: open
  name: Microsoft Fabric REST API (Core) Capacities Items API
  slug: open-microsoft-fabric-items-api
- collection_type: open
  name: Microsoft Fabric REST API (Core) Capacities Workspaces API
  slug: open-microsoft-fabric-workspaces-api
- collection_type: open
  name: Microsoft Fabric REST API (Core)
  slug: open-microsoft-fabric
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-fabric-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-fabric-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-fabric-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-fabric-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/microsoftfabric
- group: start
  title: ''
  type: Portal
  url: https://app.fabric.microsoft.com/
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/en-us/microsoft-fabric
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/fabric/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/fabric/get-started/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/microsoft-fabric/
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/fabric/security/permission-model
- group: company
  title: ''
  type: Blog
  url: https://blog.fabric.microsoft.com/
- group: operate
  title: ''
  type: Community
  url: https://community.fabric.microsoft.com/
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
  url: https://status.fabric.microsoft.com/
created: '2024-01-01'
description: Microsoft Fabric is a unified analytics platform that brings together data engineering, data science, real-time analytics, and business intelligence. It provides REST APIs for managing workspaces, lakehouses, warehouses, data pipelines, notebooks, and other Fabric items.
finops:
- name: Microsoft Fabric Finops
  service_category: API
  slug: microsoft-fabric-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-fabric.png
layout: provider
modified: '2026-05-19'
name: Microsoft Fabric
nav: Providers
network: true
overview: 'Microsoft Fabric publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Capacities API, Connections API, Items API, and 1 more. Tagged areas include Data Analytics, Data Engineering, Data Platform, Lakehouse, and Microsoft.


  Microsoft Fabric''s developer surface includes authentication, developer portal, documentation, getting-started guide, pricing, engineering blog, support, and 11 more developer resources.'
plans:
- name: Microsoft Fabric Plans Pricing
  plan_count: 3
  slug: microsoft-fabric-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Microsoft Fabric Rate Limits
  slug: microsoft-fabric-rate-limits
score:
  band: developing
  composite: 42.4
  delta: -0.4
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 52.4
    developer_ergonomics: 50.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 42.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-fabric/refs/heads/main/screenshots/microsoft-fabric-2026-06-20T185503.png
security:
- kind: authentication
  name: Microsoft Fabric Authentication
  slug: microsoft-fabric-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Microsoft Fabric Domain Security
  slug: microsoft-fabric-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Fabric Vulnerability Disclosure
  slug: microsoft-fabric-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-fabric
tags:
- Data Analytics
- Data Engineering
- Data Platform
- Lakehouse
- Microsoft
website: https://www.microsoft.com/en-us/microsoft-fabric
---
