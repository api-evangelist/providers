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
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/buzz360/refs/heads/main/well-known/buzz360-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/buzz360-help-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/buzz360/refs/heads/main/well-known/buzz360-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/buzz360-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/buzz360/refs/heads/main/hosts/buzz360-hosts.yml
  title: ''
  type: Hosts
  url: hosts/buzz360-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/buzz360/refs/heads/main/vendors/buzz360-vendors.yml
  title: ''
  type: Vendors
  url: vendors/buzz360-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.buzz360.co/en/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.buzz360.co/pricing.html
- group: start
  title: ''
  type: GettingStarted
  url: https://help.buzz360.co/en/collections/10329593-quick-start
- group: docs
  title: ''
  type: Documentation
  url: https://help.buzz360.co/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/buzz360/refs/heads/main/security/buzz360-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/buzz360-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.buzz360.co/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.buzz360.co/
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-10-06'
description: Buzz360 is an all‑in‑one political campaign software platform based in Minneapolis, United States. Founded in 2011, it provides tools for voter contact, relational organizing, SMS, email, fundraising, event management, and ballot chase, targeting conservative campaigns and small organizations. The platform unifies data, door‑knocking, messaging, and analytics into a single system for fast, high‑stakes election work.
layout: provider
modified: '2026-10-06'
name: Buzz360
nav: Providers
network: true
overview: 'Buzz360 is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Political, CampaignSoftware, VoterEngagement, CRM, and Conservative.


  Buzz360''s developer surface includes support, pricing, getting-started guide, documentation, and 6 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Buzz360 Domain Security
  slug: buzz360-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: buzz360
tags:
- Political
- CampaignSoftware
- VoterEngagement
- CRM
- Conservative
website: https://www.buzz360.co/
---
