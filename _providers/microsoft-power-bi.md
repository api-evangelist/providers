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
    agent_skills: true
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
  score: 23.4
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Microsoft Power Bi Agentic Access
  operation_count: 25
  slug: microsoft-power-bi-agentic-access
  summary_line: 25 operations · 10 acting
api_count: 13
apis:
- description: Power BI Embedded enables developers to embed interactive Power BI reports, dashboards, and tiles into custom applications. It provides client-side JavaScript APIs for rendering and interacting with e
  name: Power BI Embedded API
  slug: embedded-api
- description: 'The Power BI Admin REST API provides tenant-level administrative capabilities for managing Power BI across an organization. It enables administrators to audit user activities, manage workspaces, scan '
  name: Power BI Admin REST API
  slug: admin-api
- description: The Power BI Push Datasets API enables real-time data streaming into Power BI datasets. Developers can push rows of data directly to streaming datasets for real-time dashboard visualizations, supporti
  name: Power BI Push Datasets API
  slug: push-datasets-api
- baseURL: https://api.powerbi.com/v1.0/myorg/
  baseurl_source: declared
  description: The Apps API from Microsoft Power BI — 1 operation(s) for apps.
  name: Microsoft Power BI Apps API
  slug: microsoft-power-bi-apps-api
- baseURL: https://api.powerbi.com/v1.0/myorg/
  baseurl_source: declared
  description: The Capacities API from Microsoft Power BI — 1 operation(s) for capacities.
  name: Microsoft Power BI Capacities API
  slug: microsoft-power-bi-capacities-api
- baseURL: https://api.powerbi.com/v1.0/myorg/
  baseurl_source: declared
  description: The Dashboards API from Microsoft Power BI — 2 operation(s) for dashboards.
  name: Microsoft Power BI Dashboards API
  slug: microsoft-power-bi-dashboards-api
- baseURL: https://api.powerbi.com/v1.0/myorg/
  baseurl_source: declared
  description: The Dataflows API from Microsoft Power BI — 1 operation(s) for dataflows.
  name: Microsoft Power BI Dataflows API
  slug: microsoft-power-bi-dataflows-api
- baseURL: https://api.powerbi.com/v1.0/myorg/
  baseurl_source: declared
  description: The Datasets API from Microsoft Power BI — 5 operation(s) for datasets.
  name: Microsoft Power BI Datasets API
  slug: microsoft-power-bi-datasets-api
- baseURL: https://api.powerbi.com/v1.0/myorg/
  baseurl_source: declared
  description: The EmbedToken API from Microsoft Power BI — 1 operation(s) for embedtoken.
  name: Microsoft Power BI EmbedToken API
  slug: microsoft-power-bi-embedtoken-api
- baseURL: https://api.powerbi.com/v1.0/myorg/
  baseurl_source: declared
  description: The Gateways API from Microsoft Power BI — 1 operation(s) for gateways.
  name: Microsoft Power BI Gateways API
  slug: microsoft-power-bi-gateways-api
- baseURL: https://api.powerbi.com/v1.0/myorg/
  baseurl_source: declared
  description: The Groups API from Microsoft Power BI — 2 operation(s) for groups.
  name: Microsoft Power BI Groups API
  slug: microsoft-power-bi-groups-api
- baseURL: https://api.powerbi.com/v1.0/myorg/
  baseurl_source: declared
  description: The Imports API from Microsoft Power BI — 1 operation(s) for imports.
  name: Microsoft Power BI Imports API
  slug: microsoft-power-bi-imports-api
- baseURL: https://api.powerbi.com/v1.0/myorg/
  baseurl_source: declared
  description: The Reports API from Microsoft Power BI — 5 operation(s) for reports.
  name: Microsoft Power BI Reports API
  slug: microsoft-power-bi-reports-api
artifact_total: 31
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Microsoft Power BI REST Apps API
  slug: open-microsoft-power-bi-apps-api
- collection_type: open
  name: Microsoft Power BI REST Apps Capacities API
  slug: open-microsoft-power-bi-capacities-api
- collection_type: open
  name: Microsoft Power BI REST Apps Dashboards API
  slug: open-microsoft-power-bi-dashboards-api
- collection_type: open
  name: Microsoft Power BI REST Apps Dataflows API
  slug: open-microsoft-power-bi-dataflows-api
- collection_type: open
  name: Microsoft Power BI REST Apps Datasets API
  slug: open-microsoft-power-bi-datasets-api
- collection_type: open
  name: Microsoft Power BI REST Apps EmbedToken API
  slug: open-microsoft-power-bi-embedtoken-api
- collection_type: open
  name: Microsoft Power BI REST Apps Gateways API
  slug: open-microsoft-power-bi-gateways-api
- collection_type: open
  name: Microsoft Power BI REST Apps Groups API
  slug: open-microsoft-power-bi-groups-api
- collection_type: open
  name: Microsoft Power BI REST Apps Imports API
  slug: open-microsoft-power-bi-imports-api
- collection_type: open
  name: Microsoft Power BI REST Apps Reports API
  slug: open-microsoft-power-bi-reports-api
- collection_type: open
  name: Microsoft Power BI REST API
  slug: open-microsoft-power-bi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-power-bi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-power-bi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-power-bi-authentication.yml
- group: agent
  title: ''
  type: AgentSkills
  url: https://community.fabric.microsoft.com/t5/Power-BI-Updates-Blog/AI-Powered-Power-BI-reporting-From-design-to-deployment-with/ba-p/5190703
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/microsoft-power-bi
- group: start
  title: ''
  type: Portal
  url: https://app.powerbi.com/
- group: company
  title: ''
  type: Website
  url: https://powerbi.microsoft.com/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/power-bi/
- group: commercial
  title: ''
  type: Pricing
  url: https://powerbi.microsoft.com/en-us/pricing/
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/power-bi/developer/embedded/get-azuread-access-token
- group: build
  title: ''
  type: SDKs
  url: https://learn.microsoft.com/en-us/power-bi/developer/embedded/
- group: operate
  title: ''
  type: Community
  url: https://community.fabric.microsoft.com/t5/Power-BI-forums/ct-p/pbi_english
- group: company
  title: ''
  type: Blog
  url: https://powerbi.microsoft.com/en-us/blog/
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
description: Microsoft Power BI is a business analytics service that delivers insights to enable fast, informed decisions. It provides REST APIs for accessing and managing Power BI resources including reports, dashboards, datasets, and workspaces programmatically.
finops:
- name: Microsoft Power Bi Finops
  service_category: API
  slug: microsoft-power-bi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-power-bi.png
layout: provider
modified: '2026-05-19'
name: Microsoft Power BI
nav: Providers
network: true
overview: 'Microsoft Power BI publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Apps API, Capacities API, Dashboards API, and 7 more. Tagged areas include Analytics, Business Intelligence, Dashboards, Microsoft, and Reports.


  Microsoft Power BI''s developer surface includes authentication, developer portal, documentation, pricing, engineering blog, support, and 12 more developer resources.'
plans:
- name: Microsoft Power Bi Plans Pricing
  plan_count: 3
  slug: microsoft-power-bi-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Microsoft Power Bi Rate Limits
  slug: microsoft-power-bi-rate-limits
score:
  band: developing
  composite: 43.1
  coverage:
    artifact_dirs: 10
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 47.6
    developer_ergonomics: 59.5
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 43.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-power-bi/refs/heads/main/screenshots/microsoft-power-bi-2026-06-20T185523.png
security:
- kind: authentication
  name: Microsoft Power Bi Authentication
  slug: microsoft-power-bi-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Microsoft Power Bi Domain Security
  slug: microsoft-power-bi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-power-bi
tags:
- Analytics
- Business Intelligence
- Dashboards
- Microsoft
- Reports
website: https://powerbi.microsoft.com/
---
