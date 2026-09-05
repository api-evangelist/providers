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
  band: human-only
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/upsmith-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/upsmith-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.upsmith.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.upsmith.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.upsmith.com/terms
- group: operate
  title: ''
  type: Support
  url: mailto:support@upsmith.com
- group: other
  title: ''
  type: Marketplace
  url: https://marketplace.servicetitan.com/partner/upsmith
created: '2026-07-17'
description: UpSmith is a Dallas, Texas-based company backed by a16z that builds AI agents for home services and skilled trades businesses (HVAC, plumbing, electrical). Its platform texts customers to confirm appointments, follows up on cold estimates, responds to inbound leads around the clock, and reactivates dormant customers, syncing customer records, job details, and booking data with ServiceTitan through ServiceTitan's official APIs. UpSmith consumes partner APIs (a native ServiceTitan marketplace integration) but does not publish a public developer API of its own.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/upsmith.png
layout: provider
modified: '2026-07-21'
name: UpSmith
nav: Providers
network: true
overview: 'UpSmith is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Home Services, Skilled Trades, AI Agents, and SMS.


  UpSmith''s developer surface includes support and 6 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 9.4
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 19.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/upsmith/refs/heads/main/screenshots/upsmith-2026-09-02T165110.png
security:
- kind: domain-security
  name: Upsmith Domain Security
  slug: upsmith-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: upsmith
tags:
- Company
- Home Services
- Skilled Trades
- AI Agents
- SMS
- HVAC
- Plumbing
- Field Service
website: https://www.upsmith.com/
---
