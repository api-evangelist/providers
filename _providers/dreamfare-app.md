---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/dreamfare-app/llms/dreamfare-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dreamfare-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/dreamfare-app/well-known/dreamfare-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dreamfare-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/dreamfare-app/hosts/dreamfare-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dreamfare-app-hosts.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.dreamfare.app/onboarding
- group: docs
  title: ''
  type: Documentation
  url: https://dev.dreamfare.app/
- group: auth
  href: https://artifacts.apis.io/dreamfare-app/security/dreamfare-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dreamfare-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dreamfare.app/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://api.dreamfare.app/mcp
  - status: null
    url: https://dreamfare.app/
  reason: no-developer-program
  state: none
created: '2026-11-05'
description: Dreamfare is an AI-native travel platform that turns travel inspiration into bookable trips. It helps users save Reddit and blog tips, discover places from videos, plan itineraries, and book stays and experiences with travel partners, offering a seamless AI-driven travel planning experience.
layout: provider
modified: '2026-11-05'
name: Dreamfare
nav: Providers
network: true
overview: 'Dreamfare is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Dreamfare''s developer surface includes getting-started guide, documentation, and 5 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 7.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 35.7
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dreamfare App Domain Security
  slug: dreamfare-app-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dreamfare-app
tags:
- Company
website: https://dreamfare.app/
---
