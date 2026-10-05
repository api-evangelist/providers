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
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/alphaeon-credit/refs/heads/main/well-known/alphaeon-credit-clarity-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/alphaeon-credit-clarity-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/alphaeon-credit/refs/heads/main/well-known/alphaeon-credit-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/alphaeon-credit-well-known.yml
- group: auth
  title: ''
  type: Security
  url: https://clarity.com/vdp
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/alphaeon-credit/refs/heads/main/hosts/alphaeon-credit-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alphaeon-credit-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/alphaeon-credit/refs/heads/main/vendors/alphaeon-credit-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alphaeon-credit-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://goalphaeon.com/login
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/alphaeon-credit/refs/heads/main/security/alphaeon-credit-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/alphaeon-credit-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/alphaeon-credit/refs/heads/main/security/alphaeon-credit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alphaeon-credit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://goalphaeon.com
created: '2026-09-24'
description: Alphaeon Credit provides a credit card that allows patients to finance medical procedures such as dental work, plastic surgery, ophthalmology and dermatology treatments. The card offers special financing options for purchases over $250 with credit lines up to $25,000 and uses a soft inquiry that does not affect credit scores. Credit plans require minimum payments and are issued by Comenity Capital Bank, with approval subject to credit review.
image: http://static1.squarespace.com/static/583ef043f5e2313f41d80cf0/t/662045a77eeddd5bef18e610/1713391015741/Alphaeon_Credit_logo_registered_RGB.png?format=1500w
layout: provider
modified: '2026-09-24'
name: Alphaeon Credit
nav: Providers
network: true
overview: Alphaeon Credit is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Credit Cards, Medical Financing, Dental, and Plastic Surgery.
random_paper: 2
score:
  band: minimal
  composite: 7.5
  coverage:
    artifact_dirs: 4
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 39.3
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 9.4
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Alphaeon Credit Domain Security
  slug: alphaeon-credit-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Alphaeon Credit Vulnerability Disclosure
  slug: alphaeon-credit-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: alphaeon-credit
tags:
- Credit Cards
- Medical Financing
- Dental
- Plastic Surgery
website: https://goalphaeon.com
---
