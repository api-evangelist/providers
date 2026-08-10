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
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Metabase Agentic Access
  operation_count: 24
  slug: metabase-agentic-access
  summary_line: 24 operations · 11 acting
api_count: 10
apis:
- description: Saved questions used to power dashboards and embedded analytics.
  name: Metabase Cards API
  slug: metabase-cards-api
- description: Organize dashboards, questions, and pulses.
  name: Metabase Collections API
  slug: metabase-collections-api
- description: Build and manage interactive dashboards.
  name: Metabase Dashboards API
  slug: metabase-dashboards-api
- description: Manage data source connections and metadata.
  name: Metabase Databases API
  slug: metabase-databases-api
- description: Execute ad-hoc queries against connected databases.
  name: Metabase Datasets API
  slug: metabase-datasets-api
- description: Group and permission management.
  name: Metabase Permissions API
  slug: metabase-permissions-api
- description: Search across cards, dashboards, collections, and more.
  name: Metabase Search API
  slug: metabase-search-api
- description: Authentication and session management.
  name: Metabase Sessions API
  slug: metabase-sessions-api
- description: Global application settings.
  name: Metabase Settings API
  slug: metabase-settings-api
- description: User account management.
  name: Metabase Users API
  slug: metabase-users-api
artifact_total: 18
collections:
- collection_type: open
  name: Metabase API
  slug: open-metabase
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/metabase-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/metabase-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/metabase-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/metabase-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/metabase
- group: company
  title: ''
  type: Website
  url: https://www.metabase.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.metabase.com/docs/latest
- group: company
  title: ''
  type: Blog
  url: https://www.metabase.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.metabase.com/pricing
- group: build
  title: ''
  type: GitHub
  url: https://github.com/metabase/metabase
- group: start
  title: ''
  type: Login
  url: https://store.metabase.com/login
- group: start
  title: ''
  type: Signup
  url: https://www.metabase.com/start
- group: operate
  title: ''
  type: Support
  url: https://www.metabase.com/help
- group: other
  title: ''
  type: SelfHosting
  url: https://www.metabase.com/docs/latest/installation-and-operation/installing-metabase
- group: operate
  title: ''
  type: Community
  url: https://discourse.metabase.com
created: '2026-03-26'
description: Metabase is an open source business intelligence and analytics platform that enables teams to explore data, build interactive dashboards, and ask questions about their data without writing SQL.
finops:
- name: Metabase Finops
  service_category: API
  slug: metabase-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/metabase.png
layout: provider
modified: '2026-05-19'
name: Metabase
nav: Providers
network: true
overview: 'Metabase publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Cards API, Collections API, Dashboards API, and 7 more. Tagged areas include Analytics, Business Intelligence, Dashboards, Data Visualization, and Open Source.


  Metabase''s developer surface includes authentication, documentation, engineering blog, pricing, GitHub presence, signup flow, support, and 8 more developer resources.'
plans:
- name: Metabase Plans Pricing
  plan_count: 3
  slug: metabase-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 5
  name: Metabase Rate Limits
  slug: metabase-rate-limits
score:
  band: developing
  composite: 43.2
  delta: 0.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 53.5
    developer_ergonomics: 26.1
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 43.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/metabase/refs/heads/main/screenshots/metabase-2026-06-20T185245.png
security:
- kind: authentication
  name: Metabase Authentication
  slug: metabase-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Metabase Domain Security
  slug: metabase-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Metabase Trust Center
  slug: metabase-trust-center
  summary_line: SOC 2, GDPR
slug: metabase
tags:
- Analytics
- Business Intelligence
- Dashboards
- Data Visualization
- Open Source
- SQL
website: https://www.metabase.com
---
