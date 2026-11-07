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
    mcp_tool_quality: na
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
  scored_at: '2026-11-06'
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
overview: 'Sutton Bank is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Banking, Financial Services, Community Bank, Ohio, and Consumer Banking.


  Sutton Bank''s developer surface includes support and 6 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 4.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.9
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 49.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 6.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 6.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/sutton-bank/sutton-bank-2026-11-03T144120.png
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
- Consumer Banking
- Business Banking
website: https://suttonbank.com/
---
