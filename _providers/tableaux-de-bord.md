---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
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
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Tableaux De Bord Agentic Access
  operation_count: 19
  slug: tableaux-de-bord-agentic-access
  summary_line: 19 operations · 9 acting
api_count: 1
apis:
- description: 'The Metabase REST API enables automation of business intelligence workflows including creating and managing dashboards, running questions (queries), managing users and groups, and embedding analytics '
  name: Metabase API
  slug: metabase
- baseURL: https://your-grafana-instance.com
  baseurl_source: declared
  description: Manage Grafana alerting rules
  name: Tableaux De Bord Alerting API
  slug: tableaux-de-bord-alerting-api
- baseURL: https://your-grafana-instance.com
  baseurl_source: declared
  description: Manage dashboard annotations
  name: Tableaux De Bord Annotations API
  slug: tableaux-de-bord-annotations-api
- baseURL: https://your-grafana-instance.com
  baseurl_source: declared
  description: Create and manage Grafana dashboards
  name: Tableaux De Bord Dashboards API
  slug: tableaux-de-bord-dashboards-api
- baseURL: https://your-grafana-instance.com
  baseurl_source: declared
  description: Manage data source connections
  name: Tableaux De Bord Datasources API
  slug: tableaux-de-bord-datasources-api
- baseURL: https://your-grafana-instance.com
  baseurl_source: declared
  description: Organize dashboards in folders
  name: Tableaux De Bord Folders API
  slug: tableaux-de-bord-folders-api
- baseURL: https://your-grafana-instance.com
  baseurl_source: declared
  description: Manage Grafana organizations
  name: Tableaux De Bord Organizations API
  slug: tableaux-de-bord-organizations-api
- baseURL: https://your-grafana-instance.com
  baseurl_source: declared
  description: Manage teams and memberships
  name: Tableaux De Bord Teams API
  slug: tableaux-de-bord-teams-api
- baseURL: https://your-grafana-instance.com
  baseurl_source: declared
  description: Manage Grafana users
  name: Tableaux De Bord Users API
  slug: tableaux-de-bord-users-api
artifact_total: 32
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Grafana Dashboard API
  slug: open-grafana-dashboard
- collection_type: open
  name: Grafana Dashboard Alerting API
  slug: open-tableaux-de-bord-alerting-api
- collection_type: open
  name: Grafana Dashboard Alerting Annotations API
  slug: open-tableaux-de-bord-annotations-api
- collection_type: open
  name: Grafana Dashboard Alerting Dashboards API
  slug: open-tableaux-de-bord-dashboards-api
- collection_type: open
  name: Grafana Dashboard Alerting Datasources API
  slug: open-tableaux-de-bord-datasources-api
- collection_type: open
  name: Grafana Dashboard Alerting Folders API
  slug: open-tableaux-de-bord-folders-api
- collection_type: open
  name: Grafana Dashboard Alerting Organizations API
  slug: open-tableaux-de-bord-organizations-api
- collection_type: open
  name: Grafana Dashboard Alerting Teams API
  slug: open-tableaux-de-bord-teams-api
- collection_type: open
  name: Grafana Dashboard Alerting Users API
  slug: open-tableaux-de-bord-users-api
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
random_paper: 14
rate_limits:
- limit_count: 5
  name: Tableaux De Bord Rate Limits
  slug: tableaux-de-bord-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Tableaux De Bord API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: tableaux-de-bord-jsonschema-spectral-rules
score:
  band: thin
  composite: 35.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 62.3
    catalog_earned_first_party: 0.0
    catalog_gap: 52.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 25.0
    contract_quality: 57.7
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 13.2
  previous_composite: 35.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
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
