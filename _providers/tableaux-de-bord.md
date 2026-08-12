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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Tableaux De Bord Agentic Access
  operation_count: 19
  slug: tableaux-de-bord-agentic-access
  summary_line: 19 operations · 9 acting
api_count: 9
apis:
- description: 'The Metabase REST API enables automation of business intelligence workflows including creating and managing dashboards, running questions (queries), managing users and groups, and embedding analytics '
  name: Metabase API
  slug: metabase
- description: Manage Grafana alerting rules
  name: Tableaux De Bord Alerting API
  slug: tableaux-de-bord-alerting-api
- description: Manage dashboard annotations
  name: Tableaux De Bord Annotations API
  slug: tableaux-de-bord-annotations-api
- description: Create and manage Grafana dashboards
  name: Tableaux De Bord Dashboards API
  slug: tableaux-de-bord-dashboards-api
- description: Manage data source connections
  name: Tableaux De Bord Datasources API
  slug: tableaux-de-bord-datasources-api
- description: Organize dashboards in folders
  name: Tableaux De Bord Folders API
  slug: tableaux-de-bord-folders-api
- description: Manage Grafana organizations
  name: Tableaux De Bord Organizations API
  slug: tableaux-de-bord-organizations-api
- description: Manage teams and memberships
  name: Tableaux De Bord Teams API
  slug: tableaux-de-bord-teams-api
- description: Manage Grafana users
  name: Tableaux De Bord Users API
  slug: tableaux-de-bord-users-api
artifact_total: 23
collections:
- collection_type: open
  name: Grafana Dashboard API
  slug: open-grafana-dashboard
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tableaux-de-bord-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/tableaux-de-bord-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tableaux-de-bord-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tableaux-de-bord-authentication.yml
- group: company
  title: ''
  type: Grafana Website
  url: https://grafana.com/
- group: company
  title: ''
  type: Metabase Website
  url: https://www.metabase.com/
- group: docs
  title: ''
  type: Grafana Documentation
  url: https://grafana.com/docs/grafana/latest/developer-resources/api-reference/http-api/
- group: docs
  title: ''
  type: Metabase Documentation
  url: https://www.metabase.com/learn/metabase-basics/administration/administration-and-operation/metabase-api
- group: build
  title: ''
  type: Grafana GitHub
  url: https://github.com/grafana/grafana
- group: build
  title: ''
  type: Metabase GitHub
  url: https://github.com/metabase/metabase
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/tableaux-de-bord/refs/heads/main/vocabulary/tableaux-de-bord-vocabulary.yml
created: '2026-03-16'
description: Tableaux de Bord (French for "dashboards") is an API industry topic covering dashboard and data visualization APIs. The landscape includes open-source platforms such as Grafana (with its comprehensive HTTP API for dashboards, datasources, and alerting) and Metabase (with its REST API for questions, dashboards, and administration). These tools enable programmatic creation and management of business intelligence dashboards for monitoring, analytics, and operational visibility.
examples:
- key_count: 2
  name: Grafana Create Dashboard Example
  slug: grafana-create-dashboard-example
- key_count: 2
  name: Grafana Search Dashboards Example
  slug: grafana-search-dashboards-example
finops:
- name: Tableaux De Bord Finops
  service_category: API
  slug: tableaux-de-bord-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tableaux-de-bord.png
json_schemas:
- name: Dashboard
  property_count: 12
  slug: tableaux-de-bord-dashboard
json_structures:
- name: Tableaux De Bord Dashboard Structure
  property_count: 0
  slug: tableaux-de-bord-dashboard-structure
jsonld:
- class_count: 22
  name: Tableaux De Bord Context
  property_count: 0
  slug: tableaux-de-bord-context
layout: provider
modified: '2026-05-19'
name: Tableaux De Bord
nav: Providers
network: true
overview: 'Tableaux De Bord publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Alerting API, Annotations API, Dashboards API, and 5 more. Tagged areas include Dashboards, Business Intelligence, Analytics, Data Visualization, and Monitoring.


  The Tableaux De Bord catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Tableaux De Bord''s developer surface includes authentication and 10 more developer resources.'
plans:
- name: Tableaux De Bord Plans Pricing
  plan_count: 3
  slug: tableaux-de-bord-plans-pricing
random_paper: 60
rate_limits:
- limit_count: 5
  name: Tableaux De Bord Rate Limits
  slug: tableaux-de-bord-rate-limits
rules:
- name: Tableaux De Bord API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: tableaux-de-bord-jsonschema-spectral-rules
score:
  band: thin
  composite: 38.8
  delta: -8.4
  facets:
    commercial_clarity: 23.7
    contract_quality: 60.8
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 7.9
  previous_composite: 47.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/tableaux-de-bord/refs/heads/main/screenshots/tableaux-de-bord-2026-06-20T194915.png
security:
- kind: authentication
  name: Tableaux De Bord Authentication
  slug: tableaux-de-bord-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Tableaux De Bord Domain Security
  slug: tableaux-de-bord-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Tableaux De Bord Trust Center
  slug: tableaux-de-bord-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, FedRAMP, GDPR, CSA STAR
slug: tableaux-de-bord
tags:
- Dashboards
- Business Intelligence
- Analytics
- Data Visualization
- Monitoring
- Grafana
- Metabase
---
