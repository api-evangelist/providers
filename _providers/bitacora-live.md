---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Bitácora design platform, documented at the developer portal.
  name: Bitácora API
  slug: bit-cora-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/bitacora-live/plans/bitacora-live-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bitacora-live-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/bitacora-live/llms/bitacora-live-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bitacora-live-llms.txt
- group: agent
  href: https://artifacts.apis.io/bitacora-live/well-known/bitacora-live-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bitacora-live-well-known.yml
- group: other
  href: https://artifacts.apis.io/bitacora-live/hosts/bitacora-live-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bitacora-live-hosts.yml
- group: other
  href: https://artifacts.apis.io/bitacora-live/vendors/bitacora-live-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bitacora-live-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bitacora.live/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bitacora.live/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://bitacora.live/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://help.bitacora.live/topics/getting-started
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.bitacora.live/for/developers
- group: docs
  title: ''
  type: Documentation
  url: https://help.bitacora.live/
- group: auth
  href: https://artifacts.apis.io/bitacora-live/security/bitacora-live-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bitacora-live-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bitacora.live/
coverage:
  checked: '2026-11-02'
  detail: Developer portal provides guides but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec.
  evidence:
  - status: 200
    url: https://help.bitacora.live/for/developers
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Bitácora is a web-based design platform that enables teams to create, review, and hand off interface designs directly in code. Users can dictate changes on screens, collaborate with clients through a portal, and generate production-ready assets. The service offers a free tier and multiple paid plans, catering to freelancers, agencies, and enterprises seeking streamlined design handoff workflows.
image: https://bitacora.live/media/og/bitacora.png
layout: provider
modified: '2026-11-02'
name: Bitácora
nav: Providers
network: true
overview: 'Bitácora is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Design, Collaboration, UI/UX, Software-as-a-Service, and Free Tier.


  Bitácora''s developer surface includes pricing, getting-started guide, documentation, and 10 more developer resources.'
plans:
- name: Bitacora Live Plans Pricing
  plan_count: 5
  slug: bitacora-live-plans-pricing
random_paper: 18
score:
  band: emerging
  composite: 18.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 15.5
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bitacora Live Domain Security
  slug: bitacora-live-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bitacora-live
tags:
- Design
- Collaboration
- UI/UX
- Software-as-a-Service
- Free Tier
website: https://bitacora.live/
---
