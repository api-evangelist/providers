---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
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
  score: 21.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Openpanel Agentic Access
  operation_count: 80
  slug: openpanel-agentic-access
  summary_line: 80 operations · 15 acting
api_count: 7
apis:
- description: Legacy event ingestion (deprecated, use /track)
  name: OpenPanel Event API
  slug: openpanel-event-api
- description: Export data
  name: OpenPanel Export API
  slug: openpanel-export-api
- description: Import historical data
  name: OpenPanel Import API
  slug: openpanel-import-api
- description: Query analytics data
  name: OpenPanel Insights API
  slug: openpanel-insights-api
- description: Manage projects and clients
  name: OpenPanel Manage API
  slug: openpanel-manage-api
- description: Identify and update user profiles
  name: OpenPanel Profile API
  slug: openpanel-profile-api
- description: Track events and sessions
  name: OpenPanel Track API
  slug: openpanel-track-api
artifact_total: 14
collections:
- collection_type: open
  name: OpenPanel API
  slug: open-openpanel
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/openpanel-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/openpanel-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openpanel-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/openpanel
- group: company
  title: ''
  type: Website
  url: https://openpanel.dev
- group: docs
  title: ''
  type: Documentation
  url: https://openpanel.dev/docs
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Openpanel-dev/openpanel
- group: start
  title: ''
  type: GettingStarted
  url: https://openpanel.dev/docs/getting-started
- group: company
  title: ''
  type: Blog
  url: https://openpanel.dev/blog
- group: other
  title: ''
  type: SelfHosting
  url: https://openpanel.dev/docs/self-hosting
- group: start
  title: ''
  type: Login
  url: https://dashboard.openpanel.dev
- group: agent
  title: ''
  type: LlmsText
  url: https://openpanel.dev/llms.txt
created: '2026-03-26'
description: OpenPanel is an open source product analytics platform that provides event tracking, user journey analysis, real-time dashboards, and funnel analysis, offering a privacy-friendly alternative to tools like Mixpanel and Amplitude.
finops:
- name: Openpanel Finops
  service_category: API
  slug: openpanel-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openpanel.png
layout: provider
modified: '2026-05-19'
name: OpenPanel
nav: Providers
network: true
overview: 'OpenPanel publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Event API, Export API, Import API, and 4 more. Tagged areas include Event Tracking, Funnels, Open Source, Product Analytics, and Real-Time Analytics.


  OpenPanel''s developer surface includes documentation, GitHub presence, getting-started guide, engineering blog, and 8 more developer resources.'
plans:
- name: Openpanel Plans Pricing
  plan_count: 3
  slug: openpanel-plans-pricing
random_paper: 34
rate_limits:
- limit_count: 5
  name: Openpanel Rate Limits
  slug: openpanel-rate-limits
score:
  band: thin
  composite: 36.9
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 39.5
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 36.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openpanel/refs/heads/main/screenshots/openpanel-2026-06-20T191030.png
security:
- kind: domain-security
  name: Openpanel Domain Security
  slug: openpanel-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Openpanel Vulnerability Disclosure
  slug: openpanel-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: openpanel
tags:
- Event Tracking
- Funnels
- Open Source
- Product Analytics
- Real-Time Analytics
- User Analytics
website: https://openpanel.dev
---
