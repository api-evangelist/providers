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
artifact_total: 2
common:
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fyers.in/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fyers.in/privacy-policy
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/fyers/refs/heads/main/plans/fyers-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fyers-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fyers/refs/heads/main/llms/fyers-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fyers-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fyers/refs/heads/main/well-known/fyers-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/fyers-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fyers/refs/heads/main/well-known/fyers-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fyers-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fyers/refs/heads/main/hosts/fyers-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fyers-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fyers/refs/heads/main/vendors/fyers-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fyers-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fyers.in/
- group: company
  title: ''
  type: Newsroom
  url: https://fyers.in/media
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fyers/refs/heads/main/security/fyers-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fyers-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fyers.in
- group: docs
  title: ''
  type: APIReference
  url: https://fyers.in/api-docs
- group: operate
  title: ''
  type: Support
  url: https://fyers.in/contact-us
- group: company
  title: ''
  type: Blog
  url: https://fyers.in/whats-new
- group: commercial
  title: ''
  type: Pricing
  url: https://fyers.in/pricing
- group: start
  title: ''
  type: SignUp
  url: https://signup.fyers.in
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/fyers/workspace
created: '2026-10-14'
description: 'Fyers is a company surfaced via the API Evangelist harvest backlog (source: tag-qc) and added to the network as a stub for full-pipeline profiling.'
image: https://assets.fyers.in/Marcom_Avatar/images/meta-image/home.jpg
layout: provider
modified: '2026-10-14'
name: Fyers
nav: Providers
network: true
overview: 'Fyers is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Trading, Brokerage, and Fintech.


  Fyers'' developer surface includes API reference, support, engineering blog, pricing, signup flow, and 13 more developer resources.'
plans:
- name: Fyers Plans Pricing
  plan_count: 3
  slug: fyers-plans-pricing
random_paper: 3
score:
  band: emerging
  composite: 24.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 29.0
    catalog_earned_first_party: 12.0
    catalog_gap: 86.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 39.3
    operational_transparency: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 18.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Fyers Domain Security
  slug: fyers-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fyers
tags:
- Company
- Trading
- Brokerage
- Fintech
website: https://fyers.in
---
