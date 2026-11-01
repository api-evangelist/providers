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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/ecamm/plans/ecamm-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ecamm-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/ecamm/llms/ecamm-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ecamm-llms.txt
- group: auth
  href: https://artifacts.apis.io/ecamm/well-known/ecamm-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ecamm-support-security.txt
- group: auth
  href: https://artifacts.apis.io/ecamm/well-known/ecamm-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ecamm-status-security.txt
- group: agent
  href: https://artifacts.apis.io/ecamm/well-known/ecamm-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ecamm-well-known.yml
- group: other
  href: https://artifacts.apis.io/ecamm/hosts/ecamm-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ecamm-hosts.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ecamm.com
- group: company
  title: ''
  type: Newsroom
  url: https://www.ecamm.com/press/
- group: auth
  href: https://artifacts.apis.io/ecamm/security/ecamm-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ecamm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ecamm.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.ecamm.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.ecamm.com/mac/ecammlive/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.ecamm.com/mac/ecammlive/download.html
- group: operate
  title: ''
  type: Support
  url: https://support.ecamm.com
- group: company
  title: ''
  type: Blog
  url: https://www.ecamm.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ecamm.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ecamm.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ecamm.com/terms/privacy.html
coverage:
  checked: '2026-10-28'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found on the provider's hosts.
  evidence:
  - status: 404
    url: https://api.ecamm.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Ecamm provides powerful live streaming and video production software for macOS, enabling creators to stream, record, and present with professional features such as multi-camera support, scene composition, green screen effects, and integration with platforms like Stream Deck. Their flagship product, Ecamm Live, offers a user-friendly interface for live broadcasting, podcasting, and video creation, targeting both individual creators and businesses seeking high-quality video content.
image: https://www.ecamm.com/images/2026og.png
layout: provider
modified: '2026-10-28'
name: Ecamm
nav: Providers
network: true
overview: 'Ecamm is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Live Streaming, Video Production, Multistreaming, Virtual Camera, and Screen Capture.


  Ecamm''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Ecamm Plans Pricing
  plan_count: 2
  slug: ecamm-plans-pricing
random_paper: 11
score:
  band: thin
  composite: 26.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 50.0
    operational_transparency: 26.3
  provenance:
    mcp: unknown
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
  name: Ecamm Domain Security
  slug: ecamm-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: ecamm
tags:
- Live Streaming
- Video Production
- Multistreaming
- Virtual Camera
- Screen Capture
- Guest Video
website: https://ecamm.com/
---
