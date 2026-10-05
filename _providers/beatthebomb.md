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
api_count: 1
apis:
- description: Provides immersive team‑building experiences API (locations, missions, bookings).
  name: BeatTheBomb API
  slug: beatthebomb-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/beatthebomb/refs/heads/main/llms/beatthebomb-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/beatthebomb-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beatthebomb/refs/heads/main/hosts/beatthebomb-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beatthebomb-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.beatthebomb.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.beatthebomb.com/privacy-policy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beatthebomb/refs/heads/main/security/beatthebomb-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beatthebomb-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.beatthebomb.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.beatthebomb.com/api/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.beatthebomb.com/api/docs
- group: operate
  title: ''
  type: Support
  url: https://www.beatthebomb.com/contact-us
coverage:
  checked: '2026-09-27'
  detail: API documentation at https://www.beatthebomb.com/api/docs renders a Swagger UI with no raw OpenAPI file accessible.
  evidence:
  - status: 200
    url: https://www.beatthebomb.com/api/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-27'
description: Beat The Bomb provides immersive, team‑building experiences where participants suit up in hazmat gear and race to disarm paint, foam or slime bombs in themed rooms across multiple US cities. The company offers both in‑person locations—Atlanta, Brooklyn, Charlotte, DC, Denver, Houston, Philadelphia—and virtual experiences, combining puzzle solving, physical challenges and a competitive leaderboard to foster teamwork and fun.
image: https://www.beatthebomb.com/media/wf/65eb3080d0dc67be30dd0790_Brooklyn.avif
layout: provider
modified: '2026-09-27'
name: Beatthebomb
nav: Providers
network: true
overview: 'Beatthebomb publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Team Building, Immersive Experience, Entertainment, and US Locations.


  Beatthebomb''s developer surface includes documentation, API reference, support, and 6 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 14.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 64.3
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Beatthebomb Domain Security
  slug: beatthebomb-domain-security
  summary_line: TLSv1.3 · DMARC
slug: beatthebomb
tags:
- Company
- Team Building
- Immersive Experience
- Entertainment
- US Locations
website: https://www.beatthebomb.com
---
