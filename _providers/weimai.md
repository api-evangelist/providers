---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 12.9
  scored_at: '2026-09-04'
api_count: 1
apis:
- baseURL: https://openapi.myweimai.com
  baseurl_source: declared
  description: The WeiMai Open Platform (微脉开发平台API) is a partner-facing API surface hosted at openapi.myweimai.com. It publishes a live Swagger 2.0 document, but the public specification exposes no operations withou
  name: WeiMai Open Platform API
  slug: weimai-open-platform-api
artifact_total: 3
collections:
- collection_type: open
  name: 微脉开发平台API
  slug: open-weimai-openplatform
common:
- group: company
  title: ''
  type: Website
  url: https://myweimai.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://openapi.myweimai.com
- group: agent
  title: ''
  type: WellKnown
  url: well-known/weimai-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/weimai-domain-security.yml
created: '2026-07-17'
description: WeiMai (微脉) is a Chinese healthcare technology company operated by Choice Technology Inc. and headquartered in Hangzhou. It runs an internet-based medical services marketplace and licensed internet hospitals (including Hainan WeiMai Internet Hospital) that connect patients with doctors for online consultation, pharmaceutical products, medical devices, and health-management service packages, delivered primarily through the WeiMai consumer mobile app. WeiMai also operates a partner-facing Open Platform (微脉开发平台) at openapi.myweimai.com that exposes a Swagger 2.0 API surface for approved integrators; the public specification is a minimal stub with no operations exposed without partner credentials. The company is backed by IDG Capital and was added to the API Evangelist network as a healthcare portfolio company.
image: https://raw.githubusercontent.com/api-evangelist/weimai/refs/heads/main/apis.yml
layout: provider
modified: '2026-07-21'
name: WeiMai
nav: Providers
network: true
overview: 'WeiMai publishes 1 API on the [APIs.io](https://apis.io/) network: Open Platform API. Tagged areas include Company, Healthcare, Digital Health, Internet Hospital, and Telemedicine.'
random_paper: 6
score:
  band: emerging
  composite: 11.9
  coverage:
    artifact_dirs: 5
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
    contract_quality: 23.1
    developer_ergonomics: 4.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/weimai/refs/heads/main/screenshots/weimai-2026-09-02T170606.png
security:
- kind: domain-security
  name: Weimai Domain Security
  slug: weimai-domain-security
  summary_line: TLSv1.2 · HSTS
slug: weimai
tags:
- Company
- Healthcare
- Digital Health
- Internet Hospital
- Telemedicine
- Medical Services
- China
- Open Platform
website: https://myweimai.com
---
