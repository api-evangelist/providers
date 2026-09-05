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
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Dvids Api Agentic Access
  operation_count: 4
  slug: dvids-api-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- baseURL: https://api.dvidshub.net
  baseurl_source: declared
  description: Retrieve and relate individual assets
  name: DVIDS API Asset API
  slug: dvids-api-asset-api
- baseURL: https://api.dvidshub.net
  baseurl_source: declared
  description: Full-text search across DVIDS assets
  name: DVIDS API Search API
  slug: dvids-api-search-api
- baseURL: https://api.dvidshub.net
  baseurl_source: declared
  description: Search and retrieve military units
  name: DVIDS API Unit API
  slug: dvids-api-unit-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: DVIDS Asset API
  slug: open-dvids-api-asset-api
- collection_type: open
  name: DVIDS Asset Search API
  slug: open-dvids-api-search-api
- collection_type: open
  name: DVIDS Asset Unit API
  slug: open-dvids-api-unit-api
- collection_type: open
  name: DVIDS API
  slug: open-dvids-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dvids-api-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dvids-api-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dvids-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dvids-api-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.dvidshub.net
- group: docs
  title: ''
  type: Documentation
  url: https://api.dvidshub.net/docs
- group: company
  title: ''
  type: Blog
  url: https://www.dvidshub.net/rss/news
created: '2025-05-02'
description: The Defense Visual Information Distribution Service (DVIDS) API provides programmatic access to over 1.8 million U.S. military news, photos, video, audio, publications, and unit assets. The API is implemented as JSON over HTTP and integration is possible from any language that can make an HTTP request and parse JSON responses.
finops:
- name: Dvids Api Finops
  service_category: API
  slug: dvids-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dvids-api.png
layout: provider
modified: '2026-05-19'
name: DVIDS API
nav: Providers
network: true
overview: 'DVIDS API publishes 3 APIs on the [APIs.io](https://apis.io/) network: Asset API, Search API, and Unit API. Tagged areas include Media, Defense, Government, and Search.


  DVIDS API''s developer surface includes authentication, documentation, engineering blog, and 4 more developer resources.'
plans:
- name: Dvids Api Plans Pricing
  plan_count: 3
  slug: dvids-api-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Dvids Api Rate Limits
  slug: dvids-api-rate-limits
score:
  band: thin
  composite: 30.4
  coverage:
    artifact_dirs: 10
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
    contract_quality: 55.1
    developer_ergonomics: 23.8
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 30.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 33.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dvids-api/refs/heads/main/screenshots/dvids-api-2026-06-20T180330.png
security:
- kind: authentication
  name: Dvids Api Authentication
  slug: dvids-api-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Dvids Api Domain Security
  slug: dvids-api-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Dvids Api Vulnerability Disclosure
  slug: dvids-api-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: dvids-api
tags:
- Media
- Defense
- Government
- Search
website: https://www.dvidshub.net
---
