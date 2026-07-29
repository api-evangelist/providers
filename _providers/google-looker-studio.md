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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Google Looker Studio Agentic Access
  operation_count: 1
  slug: google-looker-studio-agentic-access
  summary_line: 1 operation
api_count: 2
apis:
- description: API for embedding Looker Studio reports in external applications.
  name: Google Looker Studio Embedding API
  slug: google-looker-studio-embedding-api
- description: The Assets:search API from Google Looker Studio — 1 operation(s) for assets:search.
  name: Google Looker Studio Assets:search API
  slug: google-looker-studio-assets-search-api
artifact_total: 10
collections:
- collection_type: open
  name: Google Looker Studio API
  slug: open-google-looker-studio
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-looker-studio-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-looker-studio-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-looker-studio-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-looker-studio-scopes.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://support.google.com/looker-studio/answer/6283323
- group: operate
  title: ''
  type: Support
  url: https://support.google.com/looker-studio
- group: operate
  title: ''
  type: Community
  url: https://www.en.advertisercommunity.com/t5/Looker-Studio/ct-p/looker-studio
- group: company
  title: ''
  type: Blog
  url: https://cloud.google.com/blog/products/data-analytics
- group: operate
  title: ''
  type: StatusPage
  url: https://www.google.com/appsstatus/dashboard
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://support.google.com/looker-studio/answer/11521624
- group: other
  title: ''
  type: Templates
  url: https://lookerstudio.google.com/gallery
- group: other
  title: ''
  type: Data Connectors
  url: https://lookerstudio.google.com/data
- group: company
  title: ''
  type: Partner Program
  url: https://developers.google.com/looker-studio/partner
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googledatastudio
created: '2024-01-01'
description: A collection of APIs and resources for Google Looker Studio (formerly Google Data Studio), Google's free business intelligence and data visualization platform.
finops:
- name: Google Looker Studio Finops
  service_category: API
  slug: google-looker-studio-finops
image: https://www.gstatic.com/analytics-suite/header/suite/v2/ic_data_studio.svg
layout: provider
modified: '2026-04-28'
name: Google Looker Studio
nav: Providers
network: true
overview: 'Google Looker Studio publishes 1 API on the [APIs.io](https://apis.io/) network: Assets:search API. Tagged areas include Analytics, Business Intelligence, Dashboards, Data Visualization, and Google.


  Google Looker Studio''s developer surface includes authentication, getting-started guide, support, engineering blog, release notes, and 9 more developer resources.'
plans:
- name: Google Looker Studio Plans Pricing
  plan_count: 3
  slug: google-looker-studio-plans-pricing
random_paper: 68
rate_limits:
- limit_count: 5
  name: Google Looker Studio Rate Limits
  slug: google-looker-studio-rate-limits
scopes:
- name: Google Looker Studio Scopes
  scope_count: 3
  slug: google-looker-studio-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: thin
  composite: 41.0
  delta: -0.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 55.1
    developer_ergonomics: 28.3
    discoverability: 48.1
    governance: 0.0
    operational_transparency: 68.4
  previous_composite: 41.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-looker-studio/refs/heads/main/screenshots/google-looker-studio-2026-06-20T182212.png
security:
- kind: authentication
  name: Google Looker Studio Authentication
  slug: google-looker-studio-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Looker Studio Domain Security
  slug: google-looker-studio-domain-security
  summary_line: TLSv1.3 · DMARC
slug: google-looker-studio
tags:
- Analytics
- Business Intelligence
- Dashboards
- Data Visualization
- Google
- Looker
- Reporting
website: https://lookerstudio.google.com
---
