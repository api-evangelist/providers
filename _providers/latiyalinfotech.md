---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: Read-only real-time cricket data API. 51 operations on the apiv5 tier (30 on apiv3), all reads, served from https://apicricketchampion.in/apiv{3|4|5}/ with an opaque API token as the final path segmen
  name: Cricket Live Line API
  slug: cricket-live-line-api
artifact_total: 7
collections:
- collection_type: postman
  name: 'API : Cricket Live Line V3'
  slug: postman-latiyalinfotech-cricket-live-line-v3
- collection_type: postman
  name: 'API : Cricket Live Line V4 & V5'
  slug: postman-latiyalinfotech-cricket-live-line-v4-v5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/latiyalinfotech-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/latiyalinfotech-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://latiyalinfotech.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://latiyalinfotech.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://latiyalinfotech.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://latiyalinfotech.com/terms-of-services/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://latiyalinfotech.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://latiyalinfotech.com/cricket-live-line-api-pricing/
created: '2026-08-31'
description: 'Latiyal Infotech Private Limited (CIN U72200RJ2022PTC084893) is a software development company in Kuchera, Rajasthan, India that builds mobile and web applications and sells one API product of its own: the Cricket Live Line API. The feed covers 108+ cricket leagues -- international, women''s, franchise league, domestic, T10 and local -- and returns ball-by-ball live match state, scorecards, commentary, playing XI and impact players, squads, points tables, over-by-over and probability history, player and team rankings, venue scoring patterns and cricket news. It is a read-only, poll-driven REST feed hosted at apicricketchampion.in and sold in four monthly INR tiers direct or in four USD tiers through RapidAPI. The published machine-readable contract is a pair of first-party Postman collections; there is no OpenAPI, no event surface and no agent surface.'
image: https://latiyalinfotech.com/wp-content/uploads/2023/06/cropped-favicon-270x270.png
layout: provider
modified: '2026-09-01'
name: Latiyal Infotech
nav: Providers
network: true
overview: 'Latiyal Infotech publishes 1 API on the [APIs.io](https://apis.io/) network: Cricket Live Line API. Tagged areas include Cricket, Sports, Live Scores, Sports Data, and Odds.


  Latiyal Infotech''s developer surface includes engineering blog, support, pricing, and 5 more developer resources.'
plans:
- name: Latiyalinfotech Plans Pricing
  plan_count: 8
  slug: latiyalinfotech-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 4
  name: Latiyalinfotech Rate Limits
  slug: latiyalinfotech-rate-limits
score:
  band: thin
  composite: 32.2
  coverage:
    artifact_dirs: 16
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 31.6
  previous_composite: 32.2
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/latiyalinfotech/refs/heads/main/screenshots/latiyalinfotech-2026-09-02T150217.png
security:
- kind: authentication
  name: Latiyalinfotech Authentication
  slug: latiyalinfotech-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Latiyalinfotech Domain Security
  slug: latiyalinfotech-domain-security
  summary_line: TLSv1.3
slug: latiyalinfotech
tags:
- Cricket
- Sports
- Live Scores
- Sports Data
- Odds
- Fantasy Sports
- Real-Time Data
- Cricket API
- India
- Postman
---
