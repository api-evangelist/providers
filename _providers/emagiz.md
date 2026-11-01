---
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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/emagiz/plans/emagiz-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/emagiz-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/emagiz/llms/emagiz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/emagiz-llms.txt
- group: agent
  href: https://artifacts.apis.io/emagiz/well-known/emagiz-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/emagiz-well-known.yml
- group: other
  href: https://artifacts.apis.io/emagiz/hosts/emagiz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/emagiz-hosts.yml
- group: other
  href: https://artifacts.apis.io/emagiz/vendors/emagiz-vendors.yml
  title: ''
  type: Vendors
  url: vendors/emagiz-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.emagiz.com/
- group: auth
  href: https://artifacts.apis.io/emagiz/security/emagiz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/emagiz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://emagiz.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://emagiz.com/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://emagiz.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://emagiz.com/contact/
- group: start
  title: ''
  type: GettingStarted
  url: https://emagiz.com/demo/
created: '2026-10-20'
description: eMagiz provides an integration Platform as a Service (iPaaS) enabling lifecycle management, integration landscape management, messaging, API gateway, event streaming, and state generation. The Dutch‑based company offers a unified platform for connecting applications, handling asynchronous message exchange, and supporting community resources, partners, and demos. It targets enterprises seeking seamless integration and API management across cloud and on‑premise environments.
image: https://emagiz.com/wp-content/uploads/2025/07/emagiz-ipaas-landscape-management-mob.webp
layout: provider
modified: '2026-10-20'
name: eMagiz
nav: Providers
network: true
overview: 'eMagiz is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include iPaaS, Integration, Messaging, API-Gateway, and Event-Streaming.


  eMagiz''s developer surface includes documentation, pricing, support, getting-started guide, and 8 more developer resources.'
plans:
- name: Emagiz Plans Pricing
  plan_count: 4
  slug: emagiz-plans-pricing
random_paper: 13
score:
  band: emerging
  composite: 20.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 48.2
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Emagiz Domain Security
  slug: emagiz-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: emagiz
tags:
- iPaaS
- Integration
- Messaging
- API-Gateway
- Event-Streaming
website: https://emagiz.com/
---
