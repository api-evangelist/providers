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
    well_known_catalog: false
  schema_version: '0.2'
  score: 10.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API platform for Q2 digital banking solutions offering various banking and fintech capabilities.
  name: Q2 Banking API
  slug: q2-banking-api
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/q2ebanking/well-known/q2ebanking-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/q2ebanking-www-security.txt
- group: auth
  href: https://artifacts.apis.io/q2ebanking/well-known/q2ebanking-developer-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/q2ebanking-developer-security.txt
- group: agent
  href: https://artifacts.apis.io/q2ebanking/well-known/q2ebanking-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/q2ebanking-well-known.yml
- group: other
  href: https://artifacts.apis.io/q2ebanking/hosts/q2ebanking-hosts.yml
  title: ''
  type: Hosts
  url: hosts/q2ebanking-hosts.yml
- group: other
  href: https://artifacts.apis.io/q2ebanking/vendors/q2ebanking-vendors.yml
  title: ''
  type: Vendors
  url: vendors/q2ebanking-vendors.yml
- group: build
  href: https://artifacts.apis.io/q2ebanking/packages/q2ebanking-packages.yml
  title: ''
  type: SDKs
  url: packages/q2ebanking-packages.yml
- group: build
  href: https://artifacts.apis.io/q2ebanking/packages/q2ebanking-packages.yml
  title: ''
  type: Packages
  url: packages/q2ebanking-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://www.q2.com/customer-experience/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.q2.com/privacy-policy?hsLang=en
- group: company
  title: ''
  type: Newsroom
  url: https://www.q2.com/company/news
- group: start
  title: ''
  type: GettingStarted
  url: https://www.q2.com/products/digital-onboarding/getting-started
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.q2.com/register
- group: company
  title: ''
  type: Blog
  url: https://www.q2.com/blog
- group: auth
  href: https://artifacts.apis.io/q2ebanking/security/q2ebanking-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/q2ebanking-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://q2ebanking.com/
created: '2026-10-21'
description: Q2 provides a single‑platform digital banking solution for financial institutions, including banks and credit unions. The platform offers consumer, small‑business, and commercial banking capabilities, along with fraud intelligence, risk management, and money‑movement services. Q2 also supports embedded finance products and AI‑driven tools for institutions seeking digital transformation.
layout: provider
modified: '2026-10-21'
name: Q2 Software
nav: Providers
network: true
overview: 'Q2 Software is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Digital Banking, Consumer Banking, Small Business Banking, Commercial Banking, and Fraud Intelligence.


  Q2 Software''s developer surface includes support, getting-started guide, engineering blog, and 12 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 11.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.0
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 22.6
    discoverability: 54.5
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 15.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 11.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/q2ebanking/q2ebanking-2026-11-03T141737.png
security:
- kind: domain-security
  name: Q2Ebanking Domain Security
  slug: q2ebanking-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: q2ebanking
tags:
- Digital Banking
- Consumer Banking
- Small Business Banking
- Commercial Banking
- Fraud Intelligence
- Risk & Fraud Management
- Embedded Finance
- Money Movement
website: https://q2ebanking.com/
---
