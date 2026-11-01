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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/fluzo/well-known/fluzo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fluzo-well-known.yml
- group: other
  href: https://artifacts.apis.io/fluzo/hosts/fluzo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fluzo-hosts.yml
- group: other
  href: https://artifacts.apis.io/fluzo/vendors/fluzo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fluzo-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fluzo.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fluzo.com/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://fluzo.com/resources/blog/
- group: auth
  href: https://artifacts.apis.io/fluzo/security/fluzo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fluzo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fluzo.com
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://dashboard.fluzo.com/mcp
  - status: 401
    url: https://desk.fluzo.com/mcp
  - status: 200
    url: https://fluzo.com
  reason: partner-login
  state: gated
created: '2026-10-21'
description: Fluzo provides a cross‑media measurement platform that captures real exposure across TV, CTV, YouTube, audio, OOH and digital channels. It delivers deduplicated reach and frequency data, brand‑lift, digital behaviour and footfall insights for advertisers, agencies and media platforms, enabling them to assess ROI and optimise media spend.
image: https://fluzo.com/cms-assets/image-e807cffb8a1a72aa7d00fbf0711b6589de31078e-1200x630-png&w=1200&q=85.webp
layout: provider
modified: '2026-10-21'
name: Fluzo
nav: Providers
network: true
overview: 'Fluzo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Advertising Measurement, Media Analytics, Brand Lift, and Reach & Frequency.


  Fluzo''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 39.3
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Fluzo Domain Security
  slug: fluzo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: fluzo
tags:
- Advertising Measurement
- Media Analytics
- Brand Lift
- Reach & Frequency
website: https://fluzo.com
---
