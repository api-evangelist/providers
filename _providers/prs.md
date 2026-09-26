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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.1
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/prs/refs/heads/main/well-known/prs-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/prs-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/prs/refs/heads/main/hosts/prs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/prs-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/prs/refs/heads/main/vendors/prs-vendors.yml
  title: ''
  type: Vendors
  url: vendors/prs-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.prsformusic.com/legal-policy-hub/terms-conditions-prize-draw
- group: operate
  title: ''
  type: Support
  url: https://help.prsformusic.com/s/
- group: start
  title: ''
  type: SignUp
  url: https://www.prsformusic.com/music-and-royalties/register-and-manage-music
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.prsformusic.com/legal-policy-hub/privacy-notice
- group: company
  title: ''
  type: Newsroom
  url: https://www.prsformusic.com/news-and-insights/press
- group: docs
  title: ''
  type: Documentation
  url: https://help.prsformusic.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/prs/refs/heads/main/security/prs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/prs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://prsformusic.com/
coverage:
  checked: 2026-09-23
  detail: Documentation is served as a JavaScript-rendered help portal with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://help.prsformusic.com/s/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-23'
description: PRS for Music is the UK’s leading performing rights organisation representing songwriters, composers and music publishers. It collects royalties on behalf of its members when music is used across broadcast, streaming, live performance and public venues, ensuring creators are fairly compensated. The organisation also provides licensing solutions for businesses and supports a wide range of music-related services and initiatives.
layout: provider
modified: '2026-09-23'
name: PRS for Music
nav: Providers
network: true
overview: 'PRS for Music is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Music, Royalties, Licensing, and Rights.


  PRS for Music''s developer surface includes support, signup flow, documentation, and 8 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 14.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.6
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 46.4
    operational_transparency: 0.0
  previous_composite: 14.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Prs Domain Security
  slug: prs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: prs
tags:
- Company
- Music
- Royalties
- Licensing
- Rights
website: https://prsformusic.com/
---
