---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 101
  human_in_the_loop: 0
  name: Vantage Sh Agentic Access
  operation_count: 193
  slug: vantage-sh-agentic-access
  summary_line: 193 operations · 101 acting
api_count: 44
apis:
- description: Operations about AccessGrants
  name: Vantage AccessGrants API
  slug: vantage-sh-accessgrants-api
- description: Operations about AnomalyAlerts
  name: Vantage AnomalyAlerts API
  slug: vantage-sh-anomalyalerts-api
- description: Operations about AnomalyNotifications
  name: Vantage AnomalyNotifications API
  slug: vantage-sh-anomalynotifications-api
- description: Operations about AuditLogs
  name: Vantage AuditLogs API
  slug: vantage-sh-auditlogs-api
- description: Operations about BillingProfiles
  name: Vantage BillingProfiles API
  slug: vantage-sh-billingprofiles-api
- description: Operations about BillingRules
  name: Vantage BillingRules API
  slug: vantage-sh-billingrules-api
- description: Operations about BudgetAlerts
  name: Vantage BudgetAlerts API
  slug: vantage-sh-budgetalerts-api
- description: Operations about Budgets
  name: Vantage Budgets API
  slug: vantage-sh-budgets-api
- description: Operations about BusinessMetrics
  name: Vantage BusinessMetrics API
  slug: vantage-sh-businessmetrics-api
- description: Operations about Canvases
  name: Vantage Canvases API
  slug: vantage-sh-canvases-api
- description: Operations about CostAlertEvents
  name: Vantage CostAlertEvents API
  slug: vantage-sh-costalertevents-api
- description: Operations about CostAlerts
  name: Vantage CostAlerts API
  slug: vantage-sh-costalerts-api
- description: Operations about CostProviders
  name: Vantage CostProvider API
  slug: vantage-sh-costprovider-api
- description: Operations about CostProviderAccounts
  name: Vantage CostProviderAccounts API
  slug: vantage-sh-costprovideraccounts-api
- description: Operations about Costs
  name: Vantage Costs API
  slug: vantage-sh-costs-api
- description: Operations about CostServices
  name: Vantage CostService API
  slug: vantage-sh-costservice-api
- description: Operations about Dashboards
  name: Vantage Dashboards API
  slug: vantage-sh-dashboards-api
- description: Operations about DataExports
  name: Vantage DataExports API
  slug: vantage-sh-dataexports-api
- description: Operations about ExchangeRates
  name: Vantage ExchangeRates API
  slug: vantage-sh-exchangerates-api
- description: Operations about FinancialCommitmentReports
  name: Vantage FinancialCommitmentReports API
  slug: vantage-sh-financialcommitmentreports-api
- description: Operations about FinancialCommitments
  name: Vantage FinancialCommitments API
  slug: vantage-sh-financialcommitments-api
- description: Operations about Folders
  name: Vantage Folders API
  slug: vantage-sh-folders-api
- description: Operations about Integrations
  name: Vantage Integrations API
  slug: vantage-sh-integrations-api
- description: Operations about Invoices
  name: Vantage Invoices API
  slug: vantage-sh-invoices-api
- description: Operations about KubernetesEfficiencyReports
  name: Vantage KubernetesEfficiencyReports API
  slug: vantage-sh-kubernetesefficiencyreports-api
- description: Operations about ManagedAccounts
  name: Vantage ManagedAccounts API
  slug: vantage-sh-managedaccounts-api
- description: Operations about Mes
  name: Vantage Me API
  slug: vantage-sh-me-api
- description: Operations about NetworkFlowReports
  name: Vantage NetworkFlowReports API
  slug: vantage-sh-networkflowreports-api
- description: Operations about Pings
  name: Vantage Ping API
  slug: vantage-sh-ping-api
- description: Operations about Prices
  name: Vantage Prices API
  slug: vantage-sh-prices-api
- description: Operations about Recommendations
  name: Vantage Recommendations API
  slug: vantage-sh-recommendations-api
- description: Operations about RecommendationViews
  name: Vantage RecommendationViews API
  slug: vantage-sh-recommendationviews-api
- description: Operations about ReportNotifications
  name: Vantage ReportNotifications API
  slug: vantage-sh-reportnotifications-api
- description: Operations about ResourceReports
  name: Vantage ResourceReports API
  slug: vantage-sh-resourcereports-api
- description: Operations about Resources
  name: Vantage Resources API
  slug: vantage-sh-resources-api
- description: Operations about SavedFilters
  name: Vantage SavedFilters API
  slug: vantage-sh-savedfilters-api
- description: Operations about Segments
  name: Vantage Segments API
  slug: vantage-sh-segments-api
- description: Operations about Tags
  name: Vantage Tags API
  slug: vantage-sh-tags-api
- description: Operations about Teams
  name: Vantage Teams API
  slug: vantage-sh-teams-api
- description: Operations about UnitCosts
  name: Vantage UnitCosts API
  slug: vantage-sh-unitcosts-api
- description: Operations about UserFeedbacks
  name: Vantage UserFeedback API
  slug: vantage-sh-userfeedback-api
- description: Operations about Users
  name: Vantage Users API
  slug: vantage-sh-users-api
- description: Operations about VirtualTags
  name: Vantage VirtualTags API
  slug: vantage-sh-virtualtags-api
- description: Operations about Workspaces
  name: Vantage Workspaces API
  slug: vantage-sh-workspaces-api
artifact_total: 51
collections:
- collection_type: open
  name: Vantage API
  slug: open-vantage-sh
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vantage-sh-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vantage-sh-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vantage-sh-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vantage-sh
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vantage-sh
- group: company
  title: ''
  type: Website
  url: https://www.vantage.sh
- group: docs
  title: ''
  type: Documentation
  url: https://docs.vantage.sh/api
- group: commercial
  title: ''
  type: Plans
  url: plans/vantage-sh-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vantage-sh-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/vantage-sh-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.vantage.sh/blog
created: '2026-07-11'
description: Vantage is a cloud cost management and FinOps platform that gives engineering and finance teams visibility into and control over cloud spend across AWS, Azure, GCP, Kubernetes, Datadog, Snowflake, MongoDB, and other providers. Its public REST API (base https://api.vantage.sh/v2) exposes Costs and Cost Reports, Resources, Recommendations, Budgets, Cost and Anomaly Alerts, Segments, Dashboards, Financial Commitments, and more, so teams can query normalized cost data, automate cost reporting, and wire cloud optimization into their own tooling. Vantage publishes a full OpenAPI specification and authenticates with OAuth2 (client-credentials bearer tokens) scoped for read and write.
finops:
- name: Vantage Sh Finops
  service_category: Cloud Cost Management and FinOps
  slug: vantage-sh-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vantage-sh.png
layout: provider
modified: '2026-07-11'
name: Vantage
nav: Providers
network: true
overview: 'Vantage publishes 44 APIs on the [APIs.io](https://apis.io/) network, including AccessGrants API, AnomalyAlerts API, AnomalyNotifications API, and 41 more. Tagged areas include Cloud Cost, FinOps, Cost Management, Cloud Optimization, and Cost Visibility.


  Vantage''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Vantage Sh Plans Pricing
  plan_count: 5
  slug: vantage-sh-plans-pricing
random_paper: 46
rate_limits:
- limit_count: 3
  name: Vantage Sh Rate Limits
  slug: vantage-sh-rate-limits
score:
  band: thin
  composite: 39.8
  delta: -2.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 61.5
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 42.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 44
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Vantage Sh Authentication
  slug: vantage-sh-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Vantage Sh Domain Security
  slug: vantage-sh-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vantage-sh
tags:
- Cloud Cost
- FinOps
- Cost Management
- Cloud Optimization
- Cost Visibility
- Cloud Spend
- Multi-Cloud
website: https://www.vantage.sh
---
