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
  score: 10.8
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/instacart
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aldiusa/refs/heads/main/well-known/aldiusa-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aldiusa-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aldiusa/refs/heads/main/well-known/aldiusa-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aldiusa-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aldiusa/refs/heads/main/hosts/aldiusa-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aldiusa-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aldiusa/refs/heads/main/vendors/aldiusa-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aldiusa-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aldi.us/store/aldi/pages/terms-of-use
- group: commercial
  title: ''
  type: Pricing
  url: https://www.aldi.us/store/aldi/pages/price-drops
- group: company
  title: ''
  type: Newsroom
  url: https://corporate.aldi.us/newsroom/product-recalls/
- group: docs
  title: ''
  type: Documentation
  url: https://help.aldi.us/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aldiusa/refs/heads/main/security/aldiusa-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aldiusa-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aldiusa/refs/heads/main/security/aldiusa-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aldiusa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aldi.us
created: '2026-09-24'
description: Aldi USA operates a network of grocery stores across the United States, offering a limited‑assortment model focused on high‑quality private‑label products at everyday low prices. The company emphasizes simplicity, efficiency, and value, providing both in‑store shopping and online ordering for pickup and delivery through its website. Aldi USA is part of the global Aldi group, known for its cost‑effective retail approach and commitment to sustainability.
layout: provider
modified: '2026-09-24'
name: Aldiusa
nav: Providers
network: true
overview: 'Aldiusa is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Grocery, Retail, E-Commerce, Low‑price, and Sustainability.


  Aldiusa''s developer surface includes pricing, documentation, and 10 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 13.0
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.9
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 46.4
    operational_transparency: 10.5
  previous_composite: 12.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aldiusa Domain Security
  slug: aldiusa-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Aldiusa Vulnerability Disclosure
  slug: aldiusa-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: aldiusa
tags:
- Grocery
- Retail
- E-Commerce
- Low‑price
- Sustainability
website: https://www.aldi.us
---
