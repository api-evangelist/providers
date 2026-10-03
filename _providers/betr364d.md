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
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: API documentation for Betr platform
  name: Betr API
  slug: betr-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/betr364d/refs/heads/main/llms/betr364d-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/betr364d-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/betr364d/refs/heads/main/well-known/betr364d-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/betr364d-help-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/betr364d/refs/heads/main/well-known/betr364d-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/betr364d-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/betr364d/refs/heads/main/hosts/betr364d-hosts.yml
  title: ''
  type: Hosts
  url: hosts/betr364d-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/betr364d/refs/heads/main/vendors/betr364d-vendors.yml
  title: ''
  type: Vendors
  url: vendors/betr364d-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/betr364d/refs/heads/main/security/betr364d-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/betr364d-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.betr.app
- group: docs
  title: ''
  type: Documentation
  url: https://help.betr.app/en/
- group: operate
  title: ''
  type: Support
  url: https://help.betr.app/en/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.betr.app/terms-and-conditions/betr-privacy-policy
coverage:
  checked: '2026-09-28'
  detail: Documentation is available at https://help.betr.app/en/ but no machine‑readable OpenAPI, GraphQL, AsyncAPI or other contract was found.
  evidence:
  - status: 200
    url: https://help.betr.app/en/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-28'
description: Betr is the world’s first real money gaming super app, offering daily fantasy, social sportsbook, social casino, and arcade experiences. Users can download the app to participate in real‑money gaming across a variety of sports and games, with high‑payout potential and a social community. The platform emphasizes responsible gaming and provides extensive help resources.
image: https://cdn.prod.website-files.com/62ed9b0abe9f7f955b2c20a8/62f1150838e3e464b61bde40_betr%20OG%20Image.jpg
layout: provider
modified: '2026-09-28'
name: Betr364d
nav: Providers
network: true
overview: 'Betr364d publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Gaming, Sports, Social, Betting, and App.


  Betr364d''s developer surface includes documentation, support, and 8 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 10.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 64.3
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
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Betr364D Domain Security
  slug: betr364d-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: betr364d
tags:
- Gaming
- Sports
- Social
- Betting
- App
- Company
website: https://www.betr.app
---
