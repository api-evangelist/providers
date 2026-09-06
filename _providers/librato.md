---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - '{''url'': ''https://www.librato.com'', ''status'': 301, ''note'': ''declared website redirects to https://documentation.solarwinds.com/en/success_center/observability/content/migrate-ao/ao-eol.htm — a different registrable domain (librato.com -> solarwinds.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: RETIRED. JSON REST API for submitting and retrieving time-series measurements and for managing metrics, metric attributes, spaces, charts, dashboards, instruments, annotations, alerts, notification se
  name: Librato Metrics API
  slug: metrics-api
artifact_total: 3
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/solarwinds/
- group: company
  title: ''
  type: Website
  url: https://www.librato.com
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/librato/api-docs
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/librato/api-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/librato/api-docs/blob/master/source/includes/_introduction.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/librato
- group: auth
  title: ''
  type: Authentication
  url: authentication/librato-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/librato-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/librato-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/librato-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/librato-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/librato-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/librato-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://documentation.solarwinds.com/en/success_center/observability/content/migrate-ao/ao-eol.htm
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/librato-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/librato-domain-security.yml
- group: other
  title: ''
  type: Parent Company
  url: https://www.solarwinds.com/
created: '2026-07-17'
description: 'Librato was a hosted metrics, monitoring and analytics service for operational data — time-series measurements, tagged metrics, dashboards ("spaces"), charts, annotations, alerts and notification services — delivered as a developer-first SaaS with a JSON REST API at metrics-api.librato.com/v1. Backed by Cowboy Ventures among others, the San Francisco company was acquired by SolarWinds in 2015 for a reported $40 million, and its metrics platform was folded into SolarWinds AppOptics — released in November 2017 — which has itself since reached end of life. The librato.com domain and every product subdomain (metrics., status., www.) now 301-redirect to the SolarWinds AppOptics end-of-life notice, the metrics-api.librato.com API host no longer resolves in DNS, and the github.com/librato organization was archived on 2024-01-02. This profile is retained as a historical record of a well-regarded developer API: the API reference source, the first-party Ruby, Python, Java and Node client
  libraries and the collection agents remain publicly archived and are catalogued here. The successor product is SolarWinds Observability SaaS.'
image: https://avatars.githubusercontent.com/u/146042?v=4
layout: provider
modified: '2026-07-19'
name: Librato
nav: Providers
network: true
overview: 'Librato publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Developer Tools, Monitoring, Metrics, and Observability.


  Librato''s developer surface includes API reference, documentation, getting-started guide, authentication, and 13 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 18.5
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 18.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/librato/refs/heads/main/screenshots/librato-2026-07-25T225027.png
security:
- kind: authentication
  name: Librato Authentication
  slug: librato-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Librato Domain Security
  slug: librato-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: librato
tags:
- Company
- Developer Tools
- Monitoring
- Metrics
- Observability
- Time Series
- Alerting
- Dashboards
- Analytics
- Retired
website: https://www.librato.com
---
