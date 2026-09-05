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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.7
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Google Looker Studio Agentic Access
  operation_count: 1
  slug: google-looker-studio-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: API for embedding Looker Studio reports in external applications.
  name: Google Looker Studio Embedding API
  slug: google-looker-studio-embedding-api
- baseURL: https://datastudio.googleapis.com
  baseurl_source: spec
  description: The Assets:search API from Google Looker Studio — 1 operation(s) for assets:search.
  name: Google Looker Studio Assets:search API
  slug: google-looker-studio-assets-search-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Looker Studio Assets:search API
  slug: open-google-looker-studio-assets-search-api
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
random_paper: 6
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
  composite: 33.4
  coverage:
    artifact_dirs: 11
    catalog_earned: 31.0
    catalog_earned_first_party: 0.0
    catalog_gap: 84.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 51.7
    developer_ergonomics: 14.3
    discoverability: 48.1
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 33.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
