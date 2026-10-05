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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bepro11/refs/heads/main/hosts/bepro11-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bepro11-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://terms-of-use.bepro.ai/
- group: operate
  title: ''
  type: Support
  url: https://bepro.ai/help-center/intro
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bepro11/refs/heads/main/security/bepro11-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bepro11-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bepro.ai
coverage:
  checked: '2026-09-27'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found at the API host.
  evidence:
  - status: 404
    url: https://api.bepro.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-27'
description: Bepro11, operating under the brand BEPRO, provides analysis software, cameras, and data solutions for sports teams. Their platform enables recording, analysis, and collaboration on match footage, offering products such as fixed and portable sports cameras, data APIs, and bespoke data services. The company targets professional and amateur sports organizations seeking comprehensive performance analytics and video management tools.
image: https://framerusercontent.com/assets/EYkE3vvo8T376872mkjmJkD43E.png
layout: provider
modified: '2026-09-27'
name: Bepro11
nav: Providers
network: true
overview: 'Bepro11 is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Sports, Analytics, Video, Data, and Software.


  Bepro11''s developer surface includes support and 4 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 7.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bepro11 Domain Security
  slug: bepro11-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bepro11
tags:
- Sports
- Analytics
- Video
- Data
- Software
- Company
website: https://bepro.ai
---
