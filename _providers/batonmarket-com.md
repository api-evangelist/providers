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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/batonmarket-com/vendors/batonmarket-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/batonmarket-com-vendors.yml
- group: agent
  href: https://artifacts.apis.io/batonmarket-com/well-known/batonmarket-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/batonmarket-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/batonmarket-com/hosts/batonmarket-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/batonmarket-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.baton.com:443/terms-of-use
- group: operate
  title: ''
  type: StatusPage
  url: https://status.batonmarket.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.baton.com:443/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.baton.com:443/press
- group: auth
  href: https://artifacts.apis.io/batonmarket-com/security/batonmarket-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/batonmarket-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.batonmarket.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.batonmarket.com/
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: 'Baton Market is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by bloomberg-beta, obvious-ventures) and added to the network as a stub for full-pipeline profiling.'
image: https://images.ctfassets.net/p2zgtwwed5ac/1ydIwQBucbvoBW6yfMt02r/5e572dcdf3e364285c522dedf73f9efd/Social_Thumb.webp
layout: provider
modified: '2026-10-21'
name: Baton Market
nav: Providers
network: true
overview: Baton Market is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Business Buying and Business Valuation.
random_paper: 4
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 5
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 41.1
    operational_transparency: 15.8
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
  name: Batonmarket Com Domain Security
  slug: batonmarket-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: batonmarket-com
tags:
- Business Buying
- Business Valuation
website: https://www.batonmarket.com/
---
