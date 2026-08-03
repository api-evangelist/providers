---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
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
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 114
  human_in_the_loop: 0
  name: Cloudquery Agentic Access
  operation_count: 236
  slug: cloudquery-agentic-access
  summary_line: 236 operations · 114 acting
api_count: 26
apis:
- description: REST API for managing CloudQuery Platform multi-tenant accounts, syncs, sources, destinations, and API keys. Authentication uses API keys generated from the CloudQuery Platform UI.
  name: CloudQuery Platform API
  slug: platform-api
- description: The admin API from CloudQuery — 7 operation(s) for admin.
  name: CloudQuery admin API
  slug: cloudquery-admin-api
- description: The alerts API from CloudQuery — 10 operation(s) for alerts.
  name: CloudQuery alerts API
  slug: cloudquery-alerts-api
- description: The api-keys API from CloudQuery — 2 operation(s) for api-keys.
  name: CloudQuery api-keys API
  slug: cloudquery-api-keys-api
- description: The apps API from CloudQuery — 1 operation(s) for apps.
  name: CloudQuery apps API
  slug: cloudquery-apps-api
- description: The audit-logs API from CloudQuery — 2 operation(s) for audit-logs.
  name: CloudQuery audit-logs API
  slug: cloudquery-audit-logs-api
- description: The chat API from CloudQuery — 7 operation(s) for chat.
  name: CloudQuery chat API
  slug: cloudquery-chat-api
- description: The custom-columns API from CloudQuery — 2 operation(s) for custom-columns.
  name: CloudQuery custom-columns API
  slug: cloudquery-custom-columns-api
- description: The filters API from CloudQuery — 7 operation(s) for filters.
  name: CloudQuery filters API
  slug: cloudquery-filters-api
- description: The healthcheck API from CloudQuery — 2 operation(s) for healthcheck.
  name: CloudQuery healthcheck API
  slug: cloudquery-healthcheck-api
- description: The insights API from CloudQuery — 8 operation(s) for insights.
  name: CloudQuery insights API
  slug: cloudquery-insights-api
- description: The notifications API from CloudQuery — 1 operation(s) for notifications.
  name: CloudQuery notifications API
  slug: cloudquery-notifications-api
- description: The onboardings API from CloudQuery — 21 operation(s) for onboardings.
  name: CloudQuery onboardings API
  slug: cloudquery-onboardings-api
- description: The Openapi.json API from CloudQuery — 1 operation(s) for openapi.json.
  name: CloudQuery Openapi.json API
  slug: cloudquery-openapi-json-api
- description: The platform API from CloudQuery — 2 operation(s) for platform.
  name: CloudQuery platform API
  slug: cloudquery-platform-api
- description: The plugins API from CloudQuery — 8 operation(s) for plugins.
  name: CloudQuery plugins API
  slug: cloudquery-plugins-api
- description: The policies API from CloudQuery — 10 operation(s) for policies.
  name: CloudQuery policies API
  slug: cloudquery-policies-api
- description: The queries API from CloudQuery — 11 operation(s) for queries.
  name: CloudQuery queries API
  slug: cloudquery-queries-api
- description: The rbac API from CloudQuery — 4 operation(s) for rbac.
  name: CloudQuery rbac API
  slug: cloudquery-rbac-api
- description: The reports API from CloudQuery — 4 operation(s) for reports.
  name: CloudQuery reports API
  slug: cloudquery-reports-api
- description: The sync-integrations API from CloudQuery — 1 operation(s) for sync-integrations.
  name: CloudQuery sync-integrations API
  slug: cloudquery-sync-integrations-api
- description: The syncs API from CloudQuery — 37 operation(s) for syncs.
  name: CloudQuery syncs API
  slug: cloudquery-syncs-api
- description: The tables API from CloudQuery — 12 operation(s) for tables.
  name: CloudQuery tables API
  slug: cloudquery-tables-api
- description: The teams API from CloudQuery — 1 operation(s) for teams.
  name: CloudQuery teams API
  slug: cloudquery-teams-api
- description: The usage API from CloudQuery — 2 operation(s) for usage.
  name: CloudQuery usage API
  slug: cloudquery-usage-api
- description: The users API from CloudQuery — 11 operation(s) for users.
  name: CloudQuery users API
  slug: cloudquery-users-api
artifact_total: 32
collections:
- collection_type: open
  name: CloudQuery Platform OpenAPI Spec
  slug: open-cloudquery
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cloudquery-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cloudquery-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cloudquery-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloudquery-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cloudquery-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cloudquery
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cloudqueryio
- group: company
  title: ''
  type: Website
  url: https://www.cloudquery.io
- group: docs
  title: ''
  type: Documentation
  url: https://www.cloudquery.io/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cloudquery.io/pricing
- group: start
  title: ''
  type: Signup
  url: https://www.cloudquery.io/docs/platform/quickstart/creating-a-new-account
- group: company
  title: ''
  type: Blog
  url: https://www.cloudquery.io/blog
created: '2026-05-11'
description: CloudQuery is a cloud infrastructure data platform that gives platform engineering and cloud operations teams a queryable SQL data layer for visibility, governance, and automation. It syncs configuration data from AWS, GCP, Azure, and 70+ SaaS sources into normalized tables, powering cloud asset inventory, security and compliance monitoring, and FinOps use cases. CloudQuery exposes Platform REST APIs for managing tenants, syncs, destinations, and API keys, authenticated via API key.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloudquery.png
layout: provider
modified: '2026-05-11'
name: CloudQuery
nav: Providers
network: true
overview: 'CloudQuery publishes 25 APIs on the [APIs.io](https://apis.io/) network, including admin API, alerts API, api-keys API, and 22 more. Tagged areas include Cloud Infrastructure, Cloud Asset Inventory, CSPM, Cloud Governance, and FinOps.


  CloudQuery''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 7 more developer resources.'
random_paper: 56
score:
  band: thin
  composite: 29.8
  delta: 0.0
  facets:
    commercial_clarity: 18.4
    contract_quality: 54.6
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 29.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 25
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cloudquery/refs/heads/main/screenshots/cloudquery-2026-06-20T174617.png
security:
- kind: authentication
  name: Cloudquery Authentication
  slug: cloudquery-authentication
  summary_line: http · 3 schemes
- kind: domain-security
  name: Cloudquery Domain Security
  slug: cloudquery-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cloudquery Vulnerability Disclosure
  slug: cloudquery-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Cloudquery Trust Center
  slug: cloudquery-trust-center
  summary_line: SOC 2, ISO 27001
slug: cloudquery
tags:
- Cloud Infrastructure
- Cloud Asset Inventory
- CSPM
- Cloud Governance
- FinOps
- Data Integration
- Platform Engineering
website: https://www.cloudquery.io
---
