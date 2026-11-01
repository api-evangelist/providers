---
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/livecontrol/llms/livecontrol-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/livecontrol-llms.txt
- group: other
  href: https://artifacts.apis.io/livecontrol/hosts/livecontrol-hosts.yml
  title: ''
  type: Hosts
  url: hosts/livecontrol-hosts.yml
- group: other
  href: https://artifacts.apis.io/livecontrol/vendors/livecontrol-vendors.yml
  title: ''
  type: Vendors
  url: vendors/livecontrol-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.livecontrol.io/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.livecontrol.io/legal/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.livecontrol.io/pricing-plan/
- group: company
  title: ''
  type: Blog
  url: https://blog.livecontrol.io/
- group: auth
  href: https://artifacts.apis.io/livecontrol/security/livecontrol-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/livecontrol-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.livecontrol.io/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://dashboard.livecontrol.io/mcp
  - status: 200
    url: https://www.livecontrol.io/
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: LiveControl provides remote live video production services, enabling organizations to stream events such as worship services, conferences, education sessions, and funerals without on‑site crews. Their platform includes hardware encoders, remote videographers, multi‑camera switching, analytics, and a branded web player, supporting thousands of events annually across various industries.
image: https://storage.googleapis.com/livecontrol-quotes.firebasestorage.app/website/assets/images/61b09e0266c7327d9ad5104a_ogplc.webp
layout: provider
modified: '2026-10-25'
name: LiveControl
nav: Providers
network: true
overview: 'LiveControl is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Video, Streaming, RemoteProduction, LiveEvents, and SaaS.


  LiveControl''s developer surface includes pricing, engineering blog, and 7 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Livecontrol Domain Security
  slug: livecontrol-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: livecontrol
tags:
- Video
- Streaming
- RemoteProduction
- LiveEvents
- SaaS
website: https://www.livecontrol.io/
---
