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
api_count: 1
apis:
- description: Developer portal for Zempler Bank APIs providing documentation and resources.
  name: Zempler Bank API
  slug: zempler-bank-api
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cashplus-bank/refs/heads/main/well-known/cashplus-bank-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cashplus-bank-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cashplus-bank/refs/heads/main/well-known/cashplus-bank-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cashplus-bank-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cashplus-bank/refs/heads/main/hosts/cashplus-bank-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cashplus-bank-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cashplus-bank/refs/heads/main/vendors/cashplus-bank-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cashplus-bank-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zemplerbank.com/terms-and-conditions/
- group: operate
  title: ''
  type: Support
  url: https://www.zemplerbank.com/help/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zemplerbank.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: http://www.zemplerbank.com/policies/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.zemplerbank.com/about/news/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.zemplerbank.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cashplus-bank/refs/heads/main/security/cashplus-bank-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cashplus-bank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.zemplerbank.com/
coverage:
  checked: '2026-10-07'
  detail: Developer portal page https://www.zemplerbank.com/api-developer/ returns HTML with no OpenAPI, GraphQL, or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://www.zemplerbank.com/api-developer/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-07'
description: Cashplus Bank, now operating as Zempler Bank, is a UK‑based challenger bank offering digital business and personal current accounts. It focuses on micro‑businesses, sole traders, freelancers and SMEs, providing features such as free business accounts, cashback, integrated accounting, and 24/7 online banking. The bank is authorised and FSCS‑protected, delivering a range of banking products through its web and mobile platforms.
image: https://www.zemplerbank.com/_gatsby/image/dacf860a84b0f4ef29fd63f50ce5c1d7/eddad12038f87d45051ed2170546e8a5/file.zempler-symbol-700x400.png
layout: provider
modified: '2026-10-07'
name: Cashplus Bank
nav: Providers
network: true
overview: 'Cashplus Bank is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Banking, ChallengerBank, United Kingdom, Digital Banking, and Small Business.


  Cashplus Bank''s developer surface includes support, documentation, and 10 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 13.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 58.9
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 11.0
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cashplus Bank Domain Security
  slug: cashplus-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cashplus-bank
tags:
- Banking
- ChallengerBank
- United Kingdom
- Digital Banking
- Small Business
website: https://www.zemplerbank.com/
---
