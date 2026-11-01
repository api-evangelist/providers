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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/sutton-bank/hosts/sutton-bank-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sutton-bank-hosts.yml
- group: other
  href: https://artifacts.apis.io/sutton-bank/vendors/sutton-bank-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sutton-bank-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.suttonbank.com/resources/news
- group: auth
  href: https://artifacts.apis.io/sutton-bank/security/sutton-bank-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sutton-bank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://suttonbank.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.suttonbank.com/privacy-policy.html
- group: operate
  title: ''
  type: Support
  url: https://www.suttonbank.com/about-us/contact-us.html
coverage:
  checked: '2026-10-29'
  detail: The public website provides no machine‑readable API specifications despite probing common OpenAPI locations.
  evidence:
  - status: 404
    url: https://www.suttonbank.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Sutton Bank is a progressive, independent community bank headquartered in Attica, Ohio. Founded in 1878, it has been recognized as a top small business and agricultural lender in the state. The bank offers a full suite of personal and business banking services, including checking and savings accounts, mortgages, consumer and business loans, digital banking, credit cards, treasury management, and investment services through Ameriprise Financial. Sutton Bank focuses on serving the financial needs of individuals, families, and businesses in the communities it serves.
image: https://www.suttonbank.com/custom/4047/image/logo-white-2x.png
layout: provider
modified: '2026-10-28'
name: Sutton Bank
nav: Providers
network: true
overview: 'Sutton Bank is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Banking, Financial Services, Community Bank, Ohio, and Personal Banking.


  Sutton Bank''s developer surface includes support and 6 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 6.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Sutton Bank Domain Security
  slug: sutton-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sutton-bank
tags:
- Banking
- Financial Services
- Community Bank
- Ohio
- Personal Banking
- Business Banking
website: https://suttonbank.com/
---
