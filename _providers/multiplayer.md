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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/multiplayer/well-known/multiplayer-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/multiplayer-well-known.yml
- group: other
  href: https://artifacts.apis.io/multiplayer/hosts/multiplayer-hosts.yml
  title: ''
  type: Hosts
  url: hosts/multiplayer-hosts.yml
- group: other
  href: https://artifacts.apis.io/multiplayer/vendors/multiplayer-vendors.yml
  title: ''
  type: Vendors
  url: vendors/multiplayer-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.multiplayer.app/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.multiplayer.app/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.multiplayer.app/pricing/
- group: docs
  title: ''
  type: Documentation
  url: https://www.multiplayer.app/docs/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.multiplayer.app/docs/release-notes/release-notes-18-06-2026/
- group: company
  title: ''
  type: Blog
  url: https://www.multiplayer.app/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.multiplayer.app/docs
- group: auth
  href: https://artifacts.apis.io/multiplayer/security/multiplayer-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/multiplayer-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.multiplayer.app/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://sandbox.multiplayer.app/mcp
  - status: 200
    url: https://www.multiplayer.app/
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: 'Multiplayer is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by bowery-capital) and added to the network as a stub for full-pipeline profiling.'
image: https://www.multiplayer.app/og-image.jpg
layout: provider
modified: '2026-10-24'
name: Multiplayer
nav: Providers
network: true
overview: 'Multiplayer is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Debugging, Developer Tools, AI Coding Agents, Observability, and Production Debugging.


  Multiplayer''s developer surface includes pricing, documentation, changelog, engineering blog, getting-started guide, and 7 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 17.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 39.3
    operational_transparency: 15.8
  provenance:
    mcp: derived
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
  name: Multiplayer Domain Security
  slug: multiplayer-domain-security
  summary_line: TLSv1.3 · DMARC
slug: multiplayer
tags:
- Debugging
- Developer Tools
- AI Coding Agents
- Observability
- Production Debugging
website: https://www.multiplayer.app/
---
