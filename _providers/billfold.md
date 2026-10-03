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
- description: API for Billfold point‑of‑sale platform
  name: Billfold API
  slug: billfold-api
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/billfold/refs/heads/main/plans/billfold-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/billfold-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/billfold/refs/heads/main/llms/billfold-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/billfold-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/billfold/refs/heads/main/well-known/billfold-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/billfold-help-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/billfold/refs/heads/main/well-known/billfold-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/billfold-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/billfold/refs/heads/main/hosts/billfold-hosts.yml
  title: ''
  type: Hosts
  url: hosts/billfold-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/billfold/refs/heads/main/vendors/billfold-vendors.yml
  title: ''
  type: Vendors
  url: vendors/billfold-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.billfold.tech/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.billfold.tech/privacy-policy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.billfold.tech/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/billfold/refs/heads/main/security/billfold-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/billfold-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.billfold.tech/
- group: docs
  title: ''
  type: Documentation
  url: https://help.billfoldpos.com/
- group: company
  title: ''
  type: Blog
  url: https://www.billfold.tech/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.billfold.tech/pricing
- group: operate
  title: ''
  type: Support
  url: https://help.billfoldpos.com/
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 403
    url: https://portal.billfold.tech/mcp
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-28'
description: Billfold provides a cashless and contactless point‑of‑sale operating system for live events. Built by operators for operators, it unifies payments, devices, POS terminals, and workflow data into a single platform, offering real‑time revenue control, streamlined reporting, and enhanced guest experiences across festivals, conferences, venues, and venues of all sizes. The solution supports RFID, NFC, and traditional card payments, delivering a flexible, scalable, and secure event‑payment ecosystem.
image: https://cdn.prod.website-files.com/625c9425341435b0290d74d6/62da651bcb63071d86513f26_Billfold-logotype-color-gradient-RGB.png
layout: provider
modified: '2026-09-28'
name: Billfold
nav: Providers
network: true
overview: 'Billfold publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Event, Point-of-Sale, RFID, and Cashless.


  Billfold''s developer surface includes documentation, engineering blog, pricing, support, and 11 more developer resources.'
plans:
- name: Billfold Plans Pricing
  plan_count: 17
  slug: billfold-plans-pricing
random_paper: 4
score:
  band: emerging
  composite: 23.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 64.3
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 12.5
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Billfold Domain Security
  slug: billfold-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: billfold
tags:
- Payments
- Event
- Point-of-Sale
- RFID
- Cashless
website: https://www.billfold.tech/
---
