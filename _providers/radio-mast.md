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
  score: 22.9
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Radio Mast Agentic Access
  operation_count: 8
  slug: radio-mast-agentic-access
  summary_line: 8 operations
api_count: 1
apis:
- baseURL: https://api.radiomast.io/v1
  baseurl_source: declared
  description: The Analytics API from Radio Mast — 3 operation(s) for analytics.
  name: Radio Mast Analytics API
  slug: radio-mast-analytics-api
- baseURL: https://api.radiomast.io/v1
  baseurl_source: declared
  description: The Listener Pools API from Radio Mast — 1 operation(s) for listener pools.
  name: Radio Mast Listener Pools API
  slug: radio-mast-listener-pools-api
- baseURL: https://api.radiomast.io/v1
  baseurl_source: declared
  description: The Radio Mast API API from Radio Mast — 1 operation(s) for radio mast api.
  name: Radio Mast Radio Mast API API
  slug: radio-mast-radio-mast-api-api
- baseURL: https://api.radiomast.io/v1
  baseurl_source: declared
  description: The Radio Stations API from Radio Mast — 1 operation(s) for radio stations.
  name: Radio Mast Radio Stations API
  slug: radio-mast-radio-stations-api
- baseURL: https://api.radiomast.io/v1
  baseurl_source: declared
  description: The Radio Streams API from Radio Mast — 2 operation(s) for radio streams.
  name: Radio Mast Radio Streams API
  slug: radio-mast-radio-streams-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Radio Mast Analytics API
  slug: open-radio-mast-analytics-api
- collection_type: open
  name: Radio Mast Analytics Listener Pools API
  slug: open-radio-mast-listener-pools-api
- collection_type: open
  name: Radio Mast Analytics Radio Mast API API
  slug: open-radio-mast-radio-mast-api-api
- collection_type: open
  name: Radio Mast Analytics Radio Stations API
  slug: open-radio-mast-radio-stations-api
- collection_type: open
  name: Radio Mast Analytics Radio Streams API
  slug: open-radio-mast-radio-streams-api
- collection_type: open
  name: Radio Mast API
  slug: open-radio-mast
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/radio-mast-capability-edges.yml
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


  Radio Mast''s developer surface includes authentication, engineering blog, and 5 more developer resources.'
plans:
- name: Radio Mast Plans Pricing
  plan_count: 3
  slug: radio-mast-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Radio Mast Rate Limits
  slug: radio-mast-rate-limits
score:
  band: thin
  composite: 26.8
  coverage:
    artifact_dirs: 11
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 46.3
    developer_ergonomics: 23.8
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 26.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
