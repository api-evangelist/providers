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
  name: Radio Mast Agentic Access
  operation_count: 8
  slug: radio-mast-agentic-access
  summary_line: 8 operations
api_count: 5
apis:
- description: The Analytics API from Radio Mast — 3 operation(s) for analytics.
  name: Radio Mast Analytics API
  slug: radio-mast-analytics-api
- description: The Listener Pools API from Radio Mast — 1 operation(s) for listener pools.
  name: Radio Mast Listener Pools API
  slug: radio-mast-listener-pools-api
- description: The Radio Mast API API from Radio Mast — 1 operation(s) for radio mast api.
  name: Radio Mast Radio Mast API API
  slug: radio-mast-radio-mast-api-api
- description: The Radio Stations API from Radio Mast — 1 operation(s) for radio stations.
  name: Radio Mast Radio Stations API
  slug: radio-mast-radio-stations-api
- description: The Radio Streams API from Radio Mast — 2 operation(s) for radio streams.
  name: Radio Mast Radio Streams API
  slug: radio-mast-radio-streams-api
artifact_total: 12
collections:
- collection_type: open
  name: Radio Mast API
  slug: open-radio-mast
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/radio-mast-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/radio-mast-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/radio-mast-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/radiomastinc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/radiomast
- group: company
  title: ''
  type: Blog
  url: https://www.radiomast.io/blog
created: '2025-02-12'
description: The Radio Mast API allows you to integrate Radio Mast functionality into your app or website, including streaming network management, stream monitoring, listener analytics, and encoder credentials.
finops:
- name: Radio Mast Finops
  service_category: API
  slug: radio-mast-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/radio-mast.png
layout: provider
modified: '2026-05-19'
name: Radio Mast
nav: Providers
network: true
overview: 'Radio Mast publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Listener Pools API, Radio Mast API API, and 2 more. Tagged areas include Radio, Streaming, Analytics, Audio, and Broadcasting.


  Radio Mast''s developer surface includes authentication, engineering blog, and 4 more developer resources.'
plans:
- name: Radio Mast Plans Pricing
  plan_count: 3
  slug: radio-mast-plans-pricing
random_paper: 25
rate_limits:
- limit_count: 5
  name: Radio Mast Rate Limits
  slug: radio-mast-rate-limits
score:
  band: thin
  composite: 33.8
  delta: -1.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 48.3
    developer_ergonomics: 13.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 35.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/radio-mast/refs/heads/main/screenshots/radio-mast-2026-06-20T192524.png
security:
- kind: authentication
  name: Radio Mast Authentication
  slug: radio-mast-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Radio Mast Domain Security
  slug: radio-mast-domain-security
  summary_line: TLSv1.2 · DNSSEC · DMARC
slug: radio-mast
tags:
- Radio
- Streaming
- Analytics
- Audio
- Broadcasting
---
