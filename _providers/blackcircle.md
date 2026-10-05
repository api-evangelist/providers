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
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blackcircle/refs/heads/main/hosts/blackcircle-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blackcircle-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blackcircle/refs/heads/main/vendors/blackcircle-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blackcircle-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blackcircle/refs/heads/main/security/blackcircle-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blackcircle-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://theblackcircle.com
- group: start
  title: ''
  type: GettingStarted
  url: https://theblackcircle.com/request-access
- group: start
  title: ''
  type: SignUp
  url: https://theblackcircle.com/request-access
- group: commercial
  title: ''
  type: TermsOfService
  url: https://theblackcircle.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://theblackcircle.com/privacy-policy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/theblackcircle/workspace
coverage:
  checked: '2026-09-29'
  detail: The Blackcircle website serves HTML pages rendered via JavaScript, providing no machine‑readable API specifications.
  evidence:
  - status: 404
    url: https://theblackcircle.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-29'
description: Blackcircle is a multi-jurisdictional private wealth management platform offering wealth planning, investment management, secondary market deals, and tailored solutions including gold and Bitcoin-backed financing. Operating across BVI, Cayman, and ADGM, it serves professional and institutional clients with a privacy‑first, concierge approach, regulated under relevant financial authorities.
image: https://theblackcircle.com/logo-2-line-white.png
layout: provider
modified: '2026-09-29'
name: Blackcircle
nav: Providers
network: true
overview: 'Blackcircle is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Wealth Management, Private Banking, Investment, and Multi-jurisdictional.


  Blackcircle''s developer surface includes getting-started guide, signup flow, and 7 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 13.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 11.0
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blackcircle Domain Security
  slug: blackcircle-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: blackcircle
tags:
- Company
- Wealth Management
- Private Banking
- Investment
- Multi-jurisdictional
website: https://theblackcircle.com
---
