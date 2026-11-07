---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 13.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/alpine-bank/well-known/alpine-bank-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/alpine-bank-well-known.yml
- group: other
  href: https://artifacts.apis.io/alpine-bank/hosts/alpine-bank-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alpine-bank-hosts.yml
- group: other
  href: https://artifacts.apis.io/alpine-bank/vendors/alpine-bank-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alpine-bank-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.alpinebank.com/terms-of-use.html
- group: operate
  title: ''
  type: Support
  url: https://www.alpinebank.com/resources/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.alpinebank.com/privacy-policy.html
- group: start
  title: ''
  type: Login
  url: https://online.alpinebank.com/login
- group: company
  title: ''
  type: Blog
  url: https://blog.alpinebank.com/
- group: auth
  href: https://artifacts.apis.io/alpine-bank/security/alpine-bank-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alpine-bank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.alpinebank.com/
coverage:
  checked: '2026-10-27'
  detail: Alpine Bank website provides no developer portal or machine‑readable API specifications.
  evidence:
  - status: 200
    url: https://www.alpinebank.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: Alpine Bank is a Colorado‑based community‑focused financial institution offering personal and business banking services, including checking, savings, loans, mortgages, and digital banking. The bank emphasizes local engagement, transparent fees, and a range of online tools for customers.
layout: provider
modified: '2026-10-26'
name: Alpine Bank
nav: Providers
network: true
overview: 'Alpine Bank is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Banking, Financial Services, Colorado, and Community.


  Alpine Bank''s developer surface includes support, engineering blog, and 8 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 8.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.5
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 51.8
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 12.7
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 12.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/alpine-bank/alpine-bank-2026-11-03T120720.png
security:
- kind: domain-security
  name: Alpine Bank Domain Security
  slug: alpine-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: alpine-bank
tags:
- Company
- Banking
- Financial Services
- Colorado
- Community
website: https://www.alpinebank.com/
---
