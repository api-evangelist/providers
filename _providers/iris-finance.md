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
api_count: 1
apis:
- description: Decentralized finance platform API documented at the developer portal.
  name: Iris Finance API
  slug: iris-finance-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/iris-finance/vendors/iris-finance-vendors.yml
  title: ''
  type: Vendors
  url: vendors/iris-finance-vendors.yml
- group: agent
  href: https://artifacts.apis.io/iris-finance/well-known/iris-finance-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/iris-finance-well-known.yml
- group: other
  href: https://artifacts.apis.io/iris-finance/hosts/iris-finance-hosts.yml
  title: ''
  type: Hosts
  url: hosts/iris-finance-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.irisfinance.co/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.irisfinance.co/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.irisfinance.co/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.irisfinance.co/blog
- group: auth
  href: https://artifacts.apis.io/iris-finance/security/iris-finance-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/iris-finance-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.irisfinance.co/
coverage:
  checked: '2026-10-24'
  detail: Docs site beta.iris.finance returns only JavaScript-rendered pages with no machine‑readable spec.
  evidence:
  - status: 302
    url: https://beta.iris.finance
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-24'
description: Iris Finance is a decentralized finance platform offering a suite of financial services including lending, borrowing, and yield farming. It leverages blockchain technology to provide transparent, permissionless access to financial instruments, targeting both retail and institutional users. The platform emphasizes security, composability, and user-friendly interfaces, aiming to democratize access to sophisticated financial products while maintaining regulatory compliance where applicable.
image: https://framerusercontent.com/images/U3blwl0bbVn1nKVMgS37VeavFk.jpg
layout: provider
modified: '2026-10-24'
name: Iris Finance
nav: Providers
network: true
overview: 'Iris Finance is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, DeFi, Finance, Blockchain, and Lending.


  Iris Finance''s developer surface includes pricing, engineering blog, and 7 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 13.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.1
    operational_transparency: 0.0
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
  name: Iris Finance Domain Security
  slug: iris-finance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: iris-finance
tags:
- Company
- DeFi
- Finance
- Blockchain
- Lending
- Borrowing
website: https://www.irisfinance.co/
---
